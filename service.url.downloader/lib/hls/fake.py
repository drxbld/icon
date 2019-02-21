import urllib2


class FakeYDL(object):
    def _handleMessage(self, message, skip_eol=False):
        self.handleMessage('HLS: {0}'.format(message), skip_eol=skip_eol)

    def handleMessage(self, message, skip_eol=False):
        print message

    def to_screen(self, *args, **kargs):
        self.handleMessage('Message: {0}'.format(args[0]), skip_eol=kargs.get('skip_eol'))

    def to_stderr(self, message):
        self.handleMessage('StdError: {0}'.format(message))

    def to_console_title(self, message):
        pass

    def trouble(self, *args, **kargs):
        self.handleMessage('Trouble: {0} {1}'.format(args, kargs))

    def report_warning(self, *args, **kargs):
        self.handleMessage('Warning: {0} {1}'.format(args, kargs))

    def report_error(self, *args, **kargs):
        self.handleMessage('Error: {0} {1}'.format(args, kargs))

    def urlopen(self, *args, **kwargs):
        return urllib2.urlopen(*args, **kwargs)

    def shouldStop(self):
        return False