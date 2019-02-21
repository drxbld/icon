from __future__ import unicode_literals

import os.path
import re
import binascii
import xbmc
try:
    from Crypto.Cipher import AES
    can_decrypt_frag = True
except ImportError:
    can_decrypt_frag = False

from fragment import FragmentFD

from compat import (
    compat_urlparse,
    compat_struct_pack,
)
from utils import (
    encodeFilename,
    sanitize_open,
    parse_m3u8_attributes,
)


class HlsFD(FragmentFD):
    """ A limited implementation that does not require ffmpeg """

    FD_NAME = 'hlsnative'

    @staticmethod
    def can_download(manifest):
        UNSUPPORTED_FEATURES = (
            r'#EXT-X-KEY:METHOD=(?!NONE|AES-128)',  # encrypted streams [1]
            r'#EXT-X-BYTERANGE',  # playlists composed of byte ranges of media files [2]

        )
        check_results = [not re.search(feature, manifest) for feature in UNSUPPORTED_FEATURES]
        check_results.append(can_decrypt_frag or '#EXT-X-KEY:METHOD=AES-128' not in manifest)
        return all(check_results)

    def real_download(self, filename, info_dict):
        man_url = info_dict['url']
        self.to_screen('[%s] Downloading m3u8 manifest' % self.FD_NAME)

        ctx = {
            'filename': filename,
            'total_frags': 0,
            'live': info_dict['is_live']
        }

        self._prepare_and_start_frag_download(ctx)


        prev_media_sequence = 0
        media_sequence = 0
        i = 0
        while not self.ydl.shouldStop():
            manifest = self.ydl.urlopen(man_url).read()

            s = manifest.decode('utf-8', 'ignore')

            if not self.can_download(s):
                return False

            total_frags = 0
            for line in s.splitlines():
                line = line.strip()
                if line and not line.startswith('#'):
                    total_frags += 1

            decrypt_info = {'METHOD': 'NONE'}
            frags_filenames = []
            exit = False
            for line in s.splitlines():
                if self.ydl.shouldStop():
                    exit = True
                    break

                line = line.strip()
                if line:
                    if not line.startswith('#'):
                        media_sequence += 1
                        if media_sequence <= prev_media_sequence:
                            continue

                        frag_url = (
                            line
                            if re.match(r'^https?://', line)
                            else compat_urlparse.urljoin(man_url, line))
                        frag_filename = '%s-Frag%d' % (ctx['tmpfilename'], media_sequence)
                        #xbmc.log("Start download...  " + frag_filename,2)
                        flag = 0
                        for i in [1,2,3]:
                            try:
                                success = ctx['dl'].download(frag_filename, {'url': frag_url})
                                #xbmc.log("Successful download...  " + frag_filename,2)
                                break
                            except Exception as e:
                                #xbmc.log("From hls try.... "+str(i)+" ... " + str(e),2)
                                xbmc.sleep(100)
                                flag = flag + 1

                        if flag > 2:
                            #xbmc.log("skipping url ... " + frag_url,2)
                            #xbmc.log("skipping file ... " + frag_filename,2)
                            continue

                        if not success:
                            return False
                            

                        down, frag_sanitized = sanitize_open(frag_filename, 'rb')
                        frag_content = down.read()
                        down.close()
    
                        if decrypt_info['METHOD'] == 'AES-128':
                            iv = decrypt_info.get('IV') or compat_struct_pack('>8xq', media_sequence)
                            frag_content = AES.new(
                                decrypt_info['KEY'], AES.MODE_CBC, iv).decrypt(frag_content)
                        ctx['dest_stream'].write(frag_content)
                        frags_filenames.append(frag_sanitized)
                        # We only download the first fragment during the test
                        if self.params.get('test', False):
                            break
                        i += 1

                    elif line.startswith('#EXT-X-KEY'):
                        decrypt_info = parse_m3u8_attributes(line[11:])
                        if decrypt_info['METHOD'] == 'AES-128':
                            if 'IV' in decrypt_info:
                                decrypt_info['IV'] = binascii.unhexlify(decrypt_info['IV'][2:])
                            if not re.match(r'^https?://', decrypt_info['URI']):
                                decrypt_info['URI'] = compat_urlparse.urljoin(
                                    man_url, decrypt_info['URI'])
                            decrypt_info['KEY'] = self.ydl.urlopen(decrypt_info['URI']).read()
                    elif line.startswith('#EXT-X-MEDIA-SEQUENCE'):
                        read_pre_media_sequence = int(line[22:]) - 1
                        if read_pre_media_sequence + total_frags < media_sequence:
                            self.report_warning('Failed to fetch new fragments: finishing')
                            exit = True
                            break

                        prev_media_sequence = max(read_pre_media_sequence, media_sequence)

                        media_sequence = read_pre_media_sequence

            prev_media_sequence = media_sequence

            for frag_file in frags_filenames:
                os.remove(encodeFilename(frag_file))

            if exit or not info_dict.get('is_live'):
                break

        self._finish_frag_download(ctx)


        return True
