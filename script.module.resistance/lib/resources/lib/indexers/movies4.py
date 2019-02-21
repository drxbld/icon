# -*- coding: utf-8 -*-




from resources.lib.modules import trakt
from resources.lib.modules import cleangenre
from resources.lib.modules import cleantitle
from resources.lib.modules import control
from resources.lib.modules import client
from resources.lib.modules import cache
from resources.lib.modules import metacache
from resources.lib.modules import playcount
from resources.lib.modules import workers
from resources.lib.modules import views
from resources.lib.modules import utils
from resources.lib.indexers import navigator

import os,sys,re,json,urllib,urlparse,datetime

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?',''))) if len(sys.argv) > 1 else dict()

action = params.get('action')


class movies:
    def __init__(self):
        self.list = []

        self.imdb_link = 'http://www.imdb.com'
        self.trakt_link = 'http://api.trakt.tv'
        self.datetime = (datetime.datetime.utcnow() - datetime.timedelta(hours = 5))
        self.systime = (self.datetime).strftime('%Y%m%d%H%M%S%f')
        self.trakt_user = control.setting('trakt.user').strip()
        self.imdb_user = control.setting('imdb.user').replace('ur', '')
        self.tm_user = control.setting('tm.user')
        self.fanart_tv_user = control.setting('fanart.tv.user')
        self.user = str(control.setting('fanart.tv.user')) + str(control.setting('tm.user'))
        self.lang = control.apiLanguage()['trakt']

        self.search_link = 'http://api.trakt.tv/search/movie?limit=20&page=1&query='
        self.fanart_tv_art_link = 'http://webservice.fanart.tv/v3/movies/%s'
        self.fanart_tv_level_link = 'http://webservice.fanart.tv/v3/level'
        self.tm_art_link = 'http://api.themoviedb.org/3/movie/%s/images?api_key=' + self.tm_user
        self.tm_img_link = 'https://image.tmdb.org/t/p/w%s%s'



        self.persons_link = 'http://www.imdb.com/search/name?count=100&name='
        self.personlist_link = 'http://www.imdb.com/search/name?count=100&gender=male,female'
        self.popular_link = 'http://www.imdb.com/search/title?title_type=feature&genres=horror&num_votes=1000,&production_status=released&groups=top_1000&sort=moviemeter,asc&count=40&start=1'
        self.views_link = 'http://www.imdb.com/search/title?title_type=feature&genres=horror&num_votes=1000,&production_status=released&sort=num_votes,desc&count=40&start=1'
        self.featured_link = 'http://www.imdb.com/search/title?title_type=feature&genres=horror&num_votes=1000,&production_status=released&release_date=date[365],date[60]&sort=moviemeter,asc&count=40&start=1'
        self.person_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie&production_status=released&role=%s&sort=year,desc&count=40&start=1'
        self.genre_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie,documentary&release_date=,date[0]&genres=horror,%s&sort=moviemeter,asc&count=40&start=1'
        self.keyword_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie,documentary&num_votes=100,&release_date=,date[0]&keywords=%s&sort=moviemeter,asc&count=40&start=1'
        self.language_link = 'http://www.imdb.com/search/title?title_type=feature&genres=horror&num_votes=100,&production_status=released&primary_language=%s&sort=moviemeter,asc&count=40&start=1'
        self.certification_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie&genres=horror&num_votes=100,&production_status=released&certificates=us:%s&sort=moviemeter,asc&count=40&start=1'
        self.year_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie&production_status=released&genres=horror&year=%s,%s&sort=moviemeter,asc&count=40&start=1'
        self.boxoffice_link = 'http://www.imdb.com/search/title?title_type=feature&genres=horror&production_status=released&sort=boxoffice_gross_us,desc&count=40&start=1'
        self.oscars_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie,documentary&genres=horror&groups=oscar_winner'
        self.theaters_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie,documentary&genres=horror&num_votes=1000,&release_date=date[365],date[0]&sort=release_date_us,desc&count=40&start=1'
        self.trending_link = 'http://api.trakt.tv/movies/trending?limit=40&page=1'
        self.popular2_link = 'http://api.trakt.tv/movies/popular?limit=40&page=1'
        self.anticipated_link = 'http://api.trakt.tv/movies/anticipated?limit=40&page=1'
        self.boxoffice2_link = 'http://api.trakt.tv/movies/boxoffice?limit=40&page=1'
        self.update_link = 'http://api.trakt.tv/movies/updates/%s?limit=40&page=1'
        self.played1_link = 'http://api.trakt.tv/movies/played/weekly?limit=40&page=1'
        self.played2_link = 'http://api.trakt.tv/movies/played/monthly?limit=40&page=1'
        self.played3_link = 'http://api.trakt.tv/movies/played/yearly?limit=40&page=1'
        self.played4_link = 'http://api.trakt.tv/movies/played/all?limit=40&page=1'
        self.collected1_link = 'http://api.trakt.tv/movies/collected/weekly?limit=40&page=1'
        self.collected2_link = 'http://api.trakt.tv/movies/collected/monthly?limit=40&page=1'
        self.collected3_link = 'http://api.trakt.tv/movies/collected/yearly?limit=40&page=1'
        self.collected4_link = 'http://api.trakt.tv/movies/collected/all?limit=40&page=1'
        self.watched1_link = 'http://api.trakt.tv/movies/watched/weekly?limit=40&page=1'
        self.watched2_link = 'http://api.trakt.tv/movies/watched/monthly?limit=40&page=1'
        self.watched3_link = 'http://api.trakt.tv/movies/watched/yearly?limit=40&page=1'
        self.watched4_link = 'http://api.trakt.tv/movies/watched/all?limit=40&page=1'
        self.genre2_link = 'http://api.trakt.tv/movies/genres/%s?limit=40&page=1'
        self.recommendations_link = 'http://api.trakt.tv/movies/recommendations/%s?limit=40&page=1'
        self.search2_link = 'http://api.trakt.tv/movies/search/%s?limit=40&page=1'

        self.ANightmareonElmStreet_link = 'http://www.imdb.com/list/ls009545233?sort=release_date,asc&st_dt=&mode=detail&page=1'
        self.HalloweenFranchise_link = 'http://www.imdb.com/list/ls020346099?sort=release_date,asc&st_dt=&mode=detail&page='
        self.FridaythethFranchise_link = 'http://www.imdb.com/list/ls020346637?sort=release_date,asc&st_dt=&mode=detail&page='
        self.ScreamFranchise_link = 'http://www.imdb.com/list/ls068935216?sort=release_date,asc&st_dt=&mode=detail&page='
        self.SawFranchise_link = 'http://www.imdb.com/list/ls066621524?sort=release_date,asc&st_dt=&mode=detail&page='
        self.AliensAndPredatorsFranchise_link = 'http://www.imdb.com/list/ls052409737?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TexasChainsawMassacreFranchise_link = 'http://www.imdb.com/list/ls055965689?sort=release_date,asc&st_dt=&mode=detail&page='
        self.EvilDeadFranchise_link = 'http://www.imdb.com/list/ls069785059?sort=release_date,asc&st_dt=&mode=detail&page='
        self.ChildsPlayFranchise_link = 'http://www.imdb.com/list/ls069414731?sort=release_date,asc&st_dt=&mode=detail&page='
        self.RomerosDeadZombieFranchise_link = 'http://www.imdb.com/list/ls020643549?sort=release_date,asc&st_dt=&mode=detail&page='
        self.FinalDestinationFranchise_link = 'http://www.imdb.com/list/ls033994527?sort=release_date,asc&st_dt=&mode=detail&page='
        self.JawsFranchise_link = 'http://www.imdb.com/list/ls033841457?sort=release_date,asc&st_dt=&mode=detail&page='
        self.JeepersCreepersFranchise_link = 'http://www.imdb.com/list/ls000699470?sort=release_date,asc&st_dt=&mode=detail&page='
        self.HellraiserFranchise_link = 'http://www.imdb.com/list/ls064593474?sort=release_date,asc&st_dt=&mode=detail&page='
        self.InsidiousFranchise_link = 'http://www.imdb.com/list/ls033805554?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TheExorcistFranchise_link = 'http://www.imdb.com/list/ls055967124?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TheHillsHaveEyesFranchise_link = 'http://www.imdb.com/list/ls033994174?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TheRingFranchise_link = 'http://www.imdb.com/list/ls079155258?sort=release_date,asc&st_dt=&mode=detail&page='
        self.JurassicParkFranchise_link = 'http://www.imdb.com/list/ls058618300?sort=release_date,asc&st_dt=&mode=detail&page='
        self.PoltergeistFranchise_link = 'http://www.imdb.com/list/ls074291923?sort=release_date,asc&st_dt=&mode=detail&page='
        self.PsychoFranchise_link = 'http://www.imdb.com/list/ls021735194?sort=release_date,asc&st_dt=&mode=detail&page='
        self.CandymanFranchise_link = 'http://www.imdb.com/list/ls021735630?sort=release_date,asc&st_dt=&mode=detail&page='
        self.ResidentEvilFranchise_link = 'http://www.imdb.com/list/ls056636896?sort=release_date,asc&st_dt=&mode=detail&page='
        self.AmityvilleFranchise_link = 'http://www.imdb.com/list/ls055967609?sort=release_date,asc&st_dt=&mode=detail&page='
        self.IKnowWhatYouDidLastSummerFranchise_link = 'http://www.imdb.com/list/ls021735266?sort=release_date,asc&st_dt=&mode=detail&page='
        self.ThePurgeFranchise_link = 'http://www.imdb.com/list/ls068935279?sort=release_date,asc&st_dt=&mode=detail&page='
        self.CreepshowFranchise_link = 'http://www.imdb.com/list/ls021735400?sort=release_date,asc&st_dt=&mode=detail&page='
        self.GremlinsFranchise_link = 'http://www.imdb.com/list/ls020139354?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TheOmenFranchise_link = 'http://www.imdb.com/list/ls055967692?sort=release_date,asc&st_dt=&mode=detail&page='
        self.SilentHillFranchise_link = 'http://www.imdb.com/list/ls000200809?sort=release_date,asc&st_dt=&mode=detail&page='
        self.WrongTurnFranchise_link = 'http://www.imdb.com/list/ls056439219?sort=release_date,asc&st_dt=&mode=detail&page='
        self.ChildrenoftheCornFranchise_link = 'http://www.imdb.com/list/ls055965933?sort=release_date,asc&st_dt=&mode=detail&page='
        self.BladeFranchise_link = 'http://www.imdb.com/list/ls033991401?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TheMummyFranchise_link = 'http://www.imdb.com/list/ls064437106?sort=release_date,asc&st_dt=&mode=detail&page='
        self.FromDusktillDawnFranchise_link = 'http://www.imdb.com/list/ls021735481?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TremorsFranchise_link = 'http://www.imdb.com/list/ls056439425?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TheConjuringFranchise_link = 'http://www.imdb.com/list/ls062340186?sort=release_date,asc&st_dt=&mode=detail&page='
        self.CubeFranchise_link = 'http://www.imdb.com/list/ls033993652?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TheThingFranchise_link = 'http://www.imdb.com/list/ls021735993?sort=release_date,asc&st_dt=&mode=detail&page='
        self.ParanormalActivityFranchise_link = 'http://www.imdb.com/list/ls034324170?sort=release_date,asc&st_dt=&mode=detail&page='
        self.PhantasmFranchise_link = 'http://www.imdb.com/list/ls071846231?sort=release_date,asc&st_dt=&mode=detail&page='
        self.ScaryMovieFranchise_link = 'http://www.imdb.com/list/ls057029693?sort=release_date,asc&st_dt=&mode=detail&page='
        self.ReturnoftheLivingDeadFranchise_link = 'http://www.imdb.com/list/ls021735826?sort=release_date,asc&st_dt=&mode=detail&page='
        self.CarrieFranchise_link = 'http://www.imdb.com/list/ls052742230?sort=release_date,asc&st_dt=&mode=detail&page='
        self.SinisterFranchise_link = 'http://www.imdb.com/list/ls021737007?sort=release_date,asc&st_dt=&mode=detail&page='
        self.UnderworldFranchise_link = 'http://www.imdb.com/list/ls062041689?sort=release_date,asc&st_dt=&mode=detail&page='
        self.TheGrudgeFranchise_link = 'http://www.imdb.com/list/ls074808311?sort=release_date,asc&st_dt=&mode=detail&page='
        self.imdbtest_link = 'http://www.imdb.com/list/ls079132902?sort=release_date,asc&st_dt=&mode=detail&page='
        self.JoyRideFranchise_link = 'http://www.imdb.com/list/ls021733838?sort=release_date,asc&st_dt=&mode=detail&page='
        self.GouliesFranchise_link = 'http://www.imdb.com/list/ls021733813?sort=release_date,asc&st_dt=&mode=detail&page='
        self.CrittersFranchise_link = 'http://www.imdb.com/list/ls021733870?sort=release_date,asc&st_dt=&mode=detail&page='
        self.WishmasterFranchise_link = 'http://www.imdb.com/list/ls000699486?sort=release_date,asc&st_dt=&mode=detail&page='
        self.screamq_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie&production_status=released&role=%s&sort=year,asc&count=40&start=1&genre=horror'
        self.HouseFranchise_link = 'http://www.imdb.com/list/ls021767689?sort=release_date,asc&st_dt=&mode=detail&page='
        self.DemonictoysFranchise_link = 'http://www.imdb.com/list/ls021761710?sort=release_date,asc&st_dt=&mode=detail&page='
        self.GateFranchise_link = 'http://www.imdb.com/list/ls021767978?sort=release_date,asc&st_dt=&mode=detail&page='
        self.CHUDFranchise_link = 'http://www.imdb.com/list/ls021767958?sort=release_date,asc&st_dt=&mode=detail&page='
        self.PumpkinheadFranchise_link = 'http://www.imdb.com/list/ls021761795?sort=release_date,asc&st_dt=&mode=detail&page='
        self.Facesofdeath_link = 'http://www.imdb.com/list/ls021722373?sort=release_date,asc&st_dt=&mode=detail&page='
        self.Hatchet_link = 'http://www.imdb.com/list/ls021722314?sort=release_date,asc&st_dt=&mode=detail&page='
        self.leprechaun_link = 'http://www.imdb.com/list/ls021722343?sort=release_date,asc&st_dt=&mode=detail&page='
        self.Alone_link = 'http://www.imdb.com/list/ls021742735?sort=release_date,asc&st_dt=&mode=detail&page='
        self.Anaconda_link = 'http://www.imdb.com/list/ls021742744?sort=release_date,asc&st_dt=&mode=detail&page='
        self.BlairWitch_link = 'http://www.imdb.com/list/ls021742170?sort=release_date,asc&st_dt=&mode=detail&page='
        self.PuppetMasterFranchise_link = 'http://www.imdb.com/list/ls021742139?sort=release_date,asc&st_dt=&mode=detail&page='


        self.horrordir_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie&production_status=released&role=%s&sort=year,asc&count=40&start=1&genre=horror'
        self.anime_link = 'http://www.imdb.com/search/title?title_type=feature,tv_movie,&genres=horror&keywords=anime&languages=en'		

        self.traktlists_link = 'http://api.trakt.tv/users/me/lists'
        self.traktlikedlists_link = 'http://api.trakt.tv/users/likes/lists?limit=1000000'
        self.traktlist_link = 'http://api.trakt.tv/users/%s/lists/%s/items'
        self.traktcollection_link = 'http://api.trakt.tv/users/me/collection/movies'
        self.traktwatchlist_link = 'http://api.trakt.tv/users/me/watchlist/movies'
        self.traktfeatured_link = 'http://api.trakt.tv/recommendations/movies?limit=40'
        self.trakthistory_link = 'http://api.trakt.tv/users/me/history/movies?limit=40&page=1'
        self.imdblists_link = 'http://www.imdb.com/user/ur%s/lists?tab=all&sort=mdfd&order=desc&filter=titles' % self.imdb_user
        self.imdblist_link = 'http://www.imdb.com/list/%s?view=detail&sort=alpha,asc&title_type=movie,tvMovie&start=1'
        self.imdblist2_link = 'http://www.imdb.com/list/%s?view=detail&sort=date_added,desc&title_type=movie,tvMovie&start=1'
        self.imdbwatchlist_link = 'http://www.imdb.com/user/ur%s/watchlist?sort=alpha,asc' % self.imdb_user
        self.imdbwatchlist2_link = 'http://www.imdb.com/user/ur%s/watchlist?sort=date_added,desc' % self.imdb_user







    def get(self, url, idx=True, create_directory=True):
        try:
            try: url = getattr(self, url + '_link')
            except: pass

            try: u = urlparse.urlparse(url).netloc.lower()
            except: pass


            if u in self.trakt_link and '/users/' in url:
                try:
                    if url == self.trakthistory_link: raise Exception()
                    if not '/users/me/' in url: raise Exception()
                    if trakt.getActivity() > cache.timeout(self.trakt_list, url, self.trakt_user): raise Exception()
                    self.list = cache.get(self.trakt_list, 720, url, self.trakt_user)
                except:
                    self.list = cache.get(self.trakt_list, 0, url, self.trakt_user)

                if '/users/me/' in url and '/collection/' in url:
                    self.list = sorted(self.list, key=lambda k: utils.title_key(k['title']))

                if idx == True: self.worker()

            elif u in self.trakt_link and self.search_link in url:
                self.list = cache.get(self.trakt_list, 1, url, self.trakt_user)
                if idx == True: self.worker(level=0)

            elif u in self.trakt_link:
                self.list = cache.get(self.trakt_list, 24, url, self.trakt_user)
                if idx == True: self.worker()


            elif u in self.imdb_link and ('/user/' in url or '/list/' in url):
                self.list = cache.get(self.imdb_list, 0, url)
                if idx == True: self.worker()

            elif u in self.imdb_link:
                self.list = cache.get(self.imdb_list, 24, url)
                if idx == True: self.worker()


            if idx == True and create_directory == True: self.movieDirectory(self.list)
            return self.list
        except:
            pass


    def widget(self):
        setting = control.setting('movie.widget')

        if setting == '2':
            self.get(self.trending_link)
        elif setting == '3':
            self.get(self.popular_link)
        elif setting == '4':
            self.get(self.theaters_link)
        else:
            self.get(self.featured_link)


    def search(self):
        try:
            control.idle()

            t = control.lang(32010).encode('utf-8')
            k = control.keyboard('', t) ; k.doModal()
            q = k.getText() if k.isConfirmed() else None

            if (q == None or q == ''): return

            url = self.search_link + urllib.quote_plus(q)
            url = '%s?action=moviePage&url=%s' % (sys.argv[0], urllib.quote_plus(url))
            control.execute('Container.Update(%s)' % url)
        except:
            return


    def person(self):
        try:
            control.idle()

            t = control.lang(32010).encode('utf-8')
            k = control.keyboard('', t) ; k.doModal()
            q = k.getText() if k.isConfirmed() else None

            if (q == None or q == ''): return

            url = self.persons_link + urllib.quote_plus(q)
            url = '%s?action=moviePersons&url=%s' % (sys.argv[0], urllib.quote_plus(url))
            control.execute('Container.Update(%s)' % url)
        except:
            return



    def screamq(self):
        genres = [
            ('Debbie Rochon', 'nm0004193', True),
            ('Brinke Stevens', 'nm0828288', True),
            ('Linnea Quigley', 'nm0001643', True),
            ('Tiffany Shepis', 'nm0791898', True),
            ('Tina Krause', 'nm0470268', True),
            ('Suzi Lorraine', 'nm1217063', True),
            ('Elissa Dowling', 'nm2233462', True),
            ('Erin Brown', 'nm0612691', True),
            ('Ruby Larocca', 'nm0217454', True),
            ('Felissa Rose', 'nm0741378', True),
            ('Julie Strain', 'nm0001781', True),
            ('Michelle Bauer', 'nm0000292', True),
            ('Ariauna Albright', 'nm0017001', True),
            ('Dee Wallace', 'nm0908914', True),
            ('Raine Brown', 'nm1102465', True),
            ('Shelley Cook', 'nm0177285', True),
            ('Alan Rowe Kelly', 'nm1342721', True),
            ('Rachel Grubb', 'nm2097751', True),
            ('Danielle Harris', 'nm0364583', True),
            ('Eileen Dietz', 'nm0226326', True),
            ('Monique Dupree', 'nm2374082', True),
            ('Heidi Honeycutt', 'nm1738579', True),
            ('Jasi Cotton Lanier', 'nm0584482', True),
            ('Eleanor James', 'nm1767850', True),
            ('Syn DeVil', 'nm1065060', True),
            ('Devanny Pinn', 'nm1922788', True),
            ('Elina Madison', 'nm0534965', True),
            ('Shannon Lark', 'nm2608690', True),
            ('Stephanie Beaton', 'nm0064116', True),
            ('Adrienne Barbeau', 'nm0000105', True),
            ('Maria Olsen', 'nm1864017', True),
            ('P.J. Soles', 'nm0001753', True),
            ('Amy Lynn Best', 'nm0078890', True),
            ('Sarah French', 'nm2720796', True),
            ('Christa Campbell', 'nm0132300', True),
            ('Leanna Chamish', 'nm1052270', True),
            ('Emmanuelle Vaugier', 'nm0891275', True),
            ('Katharine Isabelle', 'nm0410622', True),
            ('Lorielle New', 'nm0627581', True),
            ('Pamela Sutch', 'nm0839994', True),
            ('Deneen Melody', 'nm3069800', True),
            ('Jessica Cameron', 'nm2781723', True),
            ('Patty McCormack', 'nm0566478', True),
            ('Janet Tracy Keijser', 'nm0445044', True),
            ('Kerri Taylor', 'nm1423105', True),
            ('Lilith Stabs', 'nm0820931', True),
            ('Margot Kidder', 'nm0452288', True),
            ('Melantha Blackthorne', 'nm1520852', True),
            ('Rusty Apper', 'nm2488741', True),
            ('Crystal Lowe', 'nm0522909', True),
            ('Eileen Daly', 'nm0198432', True),
            ('Ingrid Pitt', 'nm0685839', True),
            ('Jodelle Ferland', 'nm0272706', True),
            ('Linda Blair', 'nm0000304', True),
            ('Monique Ganderton', 'nm1244650', True),
            ('Robyn Griggs', 'nm0341841', True),
            ('Susan Adriensen', 'nm2148045', True),
            ('Sybil Danning', 'nm0000356', True),
            ('Ashley Laurence', 'nm0491090', True),
            ('Brenda Cooney', 'nm1486239', True),
            ('Chelan Simmons', 'nm0799706', True),
            ('Dina Meyer', 'nm0000539', True),
            ('Elske McCain', 'nm2076518', True),
            ('GiGi Erneta', 'nm0259656', True),
            ('Julie Anne Prescott', 'nm2766218', True),
            ('Kayla Perkins', 'nm2765695', True),
            ('Leslie Easterbrook', 'nm0247579', True),
            ('Amy Lyndon', 'nm0004671', True),
            ('April Monique Burril', 'nm1486060', True),
            ('Daniella Evangelista', 'nm0006473', True),
            ('Emily Booth', 'nm0095696', True),
            ('Jace Anderson', 'nm0026829', True),
            ('M. Catherine Holseybrook Wynkoop', 'nm2045924', True),
            ('Maja Aro', 'nm2857057', True),
            ('Marysia Kay', 'nm1671380', True),
            ('Mircea Monroe', 'nm1597260', True),
            ('Nicola Fiore', 'nm2859629', True),
            ('Robin Sydney', 'nm1218053', True),
            ('Tara Cardinal', 'nm2286991', True),
            ('Vanelle', 'nm1457069', True),
            ('Victoria De Mare', 'nm1389064', True),
            ('Brenna Roth', 'nm2260940', True),
            ('Colleen Camp', 'nm0131974', True),
            ('Cyndi Crotts', 'nm1962680', True),
            ('Deborah Dutch', 'nm0244740', True),
            ('Debra Mayer', 'nm0562364', True),
            ('Eleni C. Krimitsos', 'nm1800320', True),
            ('Heather Langenkamp', 'nm0000486', True),
            ('Kaylee Williams', 'nm2545114', True),
            ('Kristi Boul', 'nm2877236', True),
            ('Melissa L. Nichols', 'nm0629659', True),
            ('Michelle Tomlinson', 'nm1009589', True),
            ('Priscilla Barnes', 'nm0055733', True),
            ('Stephanie Caleb', 'nm2554487', True),
            ('Traci Lords', 'nm0000183', True),
            ('Bianca Allaine', 'nm1440820', True),
            ('Brooke Lewis', 'nm0506989', True),
            ('Caia Coley', 'nm0171405', True),
            ('Eliza Swenson', 'nm1918942', True),
            ('Jamie Lee Curtis', 'nm0000130', True),
            ('parapsychology', 'parapsychology', True),
            ('Janet Leigh', 'nm0001463', True),
            ('Johnna Troxell', 'nm3133051', True),
            ('Kathleen Benner', 'nm1836808', True),
            ('Kim Little', 'nm0514605', True),
            ('Mary Elizabeth Winstead', 'nm0935541', True),
            ('Molly Celaschi', 'nm2104974', True),
            ('Nan Garcia-Wood', 'nm0305479', True),
            ('Natassia Malthe', 'nm0853573', True),
            ('Rachael Robbins', 'nm0730436', True),
            ('Rena Riffel', 'nm0726457', True),
            ('Sarah Lieving', 'nm1919727', True),
            ('Sarah Nicklin', 'nm2440492', True),
            ('Shawnee Smith', 'nm0809938', True),
            ('Tracy Scoggins', 'nm0001712', True),
            ('Alexandra Cipolla', 'nm2339778', True),
            ('Allison Kyler', 'nm1043358', True),
            ('Amanda Barton', 'nm0059088', True),
            ('April Wade', 'nm1696876', True),
            ('Betsy Russell', 'nm0751018', True),
            ('Clea DuVall', 'nm0245112', True),
            ('Denise Gossett', 'nm1011206', True),
            ('Ellie Cornell', 'nm0332081', True),
            ('Emily Haack', 'nm1092626', True),
            ('Eva Derrek', 'nm1564086', True),
            ('Glori-Anne Gilbert', 'nm0318061', True),
            ('Helene Udy', 'nm0879891', True),
            ('Junie Hoang', 'nm0387470', True),
            ('Lisa Langlois', 'nm0486590', True),
            ('Lisa Marie Caruk', 'nm0142250', True),
            ('Marilyn Burns', 'nm0122782', True),
            ('Nicole Kruex', 'nm2933947', True),
            ('Olivia Hussey', 'nm0001377', True),
            ('Phoebe Dollar', 'nm1085263', True),
            ('Sheri Moon Zombie', 'nm0600667', True),
            ('Stacey Dixon', 'nm3137199', True),
            ('Tanya Dempsey', 'nm0218770', True),
            ('Tarah Paige', 'nm1395985', True),
            ('Victoria Broom', 'nm2518469', True),
            ('Zenova Braeden', 'nm1247840', True),
            ('Zoe Hunter', 'nm1365273', True),
            ('Angela Bettis', 'nm0079374', True),
            ('Annmarie Lynn Gracey', 'nm1689836', True),
            ('Ashlie Rhey', 'nm0722269', True),
            ('Barbara Crampton', 'nm0186225', True),
            ('Carla Laemmle', 'nm0480675', True),
            ('Elizabeth Daily', 'nm0197354', True),
            ('Hannah Cowley', 'nm1157266', True),
            ('Jordan Ladd', 'nm0480465', True),
            ('Julie Benz', 'nm0004748', True),
            ('Kathleen Quinlan', 'nm0000599', True),
            ('Krista Grotte', 'nm1380166', True),
            ('Lauren Mary Kim', 'nm1830387', True),
            ('Lindy Booth', 'nm0095751', True),
            ('Lisa Wilcox', 'nm0928244', True),
            ('Lysette Anthony', 'nm0000771', True),
            ('Melissa George', 'nm0313534', True),
            ('MyAnna Buring', 'nm1769728', True),
            ('Neve Campbell', 'nm0000117', True),
            ('Patti Tindall', 'nm1197846', True),
            ('Siri Baruc', 'nm0059410', True),
            ('A.J. Cook', 'nm0176882', True),
            ('Athena Demos', 'nm0218664', True),
            ('Benita Ha', 'nm0351699', True),
            ('Bianca Lawson', 'nm0493161', True),
            ('Chloë Grace Moretz', 'nm1631269', True),
            ('Danielle Lozeau', 'nm1699451', True),
            ('DeeDee Bigelow', 'nm2397349', True),
            ('Eliza Dushku', 'nm0244630', True),
            ('Erika Smith', 'nm1653613', True),
            ('Julin', 'nm2734149', True),
            ('Katie Cassidy', 'nm1556320', True),
            ('Kelly Hu', 'nm0005026', True),
            ('Kristina Klebe', 'nm1640351', True),
            ('Lauren Lakis', 'nm3637755', True),
            ('Melissa R. Bacelar', 'nm0045279', True),
            ('Miranda Kwok', 'nm0477230', True),
            ('Rachel Miner', 'nm0001540', True),
            ('Samantha MacIvor', 'nm2210354', True),
            ('Sarah Carter', 'nm0141931', True),
            ('Stephanie Honoré', 'nm2576863', True),
            ('Thora Birch', 'nm0000301', True),
            ('Zelda Rubinstein', 'nm0748289', True),
            ('Allison Lange', 'nm0486068', True),
            ('America Olivo', 'nm1760388', True),
            ('Anna Paquin', 'nm0001593', True),
            ('Arielle Brachfeld', 'nm2290733', True),
            ('Barbara Nedeljakova', 'nm1319676', True),
            ('Brighid Fleming', 'nm2459787', True),
            ('Charisma Carpenter', 'nm0004806', True),
            ('Charlotte Sullivan', 'nm0838000', True),
            ('Christina Cole', 'nm1268047', True),
            ('Christina DeRosa', 'nm1981794', True),
            ('Christina Rosenberg', 'nm0479447', True),
            ('Claudia Christian', 'nm0160004', True),
            ('Danielle De Luca', 'nm2184630', True),
            ('Danielle Petty', 'nm0678776', True),
            ('Darcey Vanderhoef', 'nm1015793', True),
            ('Ellen Albertini Dow', 'nm0016687', True),
            ('Emily Perkins', 'nm0673932', True),
            ('Famke Janssen', 'nm0000463', True),

            ('Gina Valona', 'nm1680155', True),
            ('Heather Robb', 'nm1683366', True),
            ('Honor Blackman', 'nm0000303', True),
            ('Jackey Hall', 'nm2256392', True),
            ('Jacqui Holland', 'nm1194663', True),
            ('Jana Kramer', 'nm1325306', True),
            ('Jacquelyn Aurora', 'nm1989854', True),
            ('Jeanette OConnor', 'nm0640206', True),
            ('Jennifer Beals', 'nm0000884', True),
            ('Jessica Sonneborn', 'nm1939136', True),
            ('Katheryn Winnick', 'nm0935395', True),
            ('Kathleen Kinmont', 'nm0455681', True),
            ('Kelly Albano', 'nm2740786', True),
            ('Kitsie Duncan', 'nm4138267', True),
            ('Kristen Cloke', 'nm0167028', True),
            ('Lar Park-Lincoln', 'nm0661983', True),
            ('Laura Locascio', 'nm2017815', True),
            ('Lauren Francesca', 'nm3270989', True),
            ('Melanie Donihoo', 'nm1655670', True),
            ('Melanie Robel', 'nm3093027', True),
            ('Moksha McPherrin', 'nm1232826', True),
            ('Nora-Jane Noone', 'nm1172901', True),
            ('Rachelle Williams', 'nm1489995', True),
            ('Rebekah Brandes', 'nm1759942', True),
            ('Rebecca De Mornay', 'nm0000360', True),
            ('Rhoda Jordan', 'nm1128656', True),
            ('Rose McGowan', 'nm0000535', True),
            ('Sarah Lassez', 'nm0489857', True),
            ('Seregon O Dassey', 'nm1662562', True),
            ('Shannon Elizabeth', 'nm0002436', True),
            ('Sienna Guillory', 'nm0347149', True),
            ('Sigourney Weaver', 'nm0000244', True),
            ('Steffinnie Phrommany', 'nm2396859', True),
            ('Vera VanGuard', 'nm1475801', True),
            ('Virginia Bryant', 'nm0117249', True),
            ('Ali Larter', 'nm0005123', True),
            ('Alisa Robinson', 'nm1586857', True),
            ('Amy Irving', 'nm0001388', True),
            ('Amy Rene LaFavers', 'nm2536616', True),
            ('Angela Ware', 'nm2428362', True),
            ('Babs Chula', 'nm0161075', True),
            ('Brea Grant', 'nm2647420', True),
            ('Carrie Fisher', 'nm0000402', True),
            ('Cathy Baron', 'nm2199801', True),
            ('Cerina Vincent', 'nm0898597', True),
            ('Christina Ricci', 'nm0000207', True),
            ('Christine Lakin', 'nm0003115', True),
            ('Cindy Pickett', 'nm0681882', True),
            ('Courteney Cox', 'nm0001073', True),
            ('Cynthia LeBlanc', 'nm1897496', True),
            ('Danielle Donahue', 'nm2567761', True),
            ('Darlene Tygrett', 'nm1295267', True),
            ('Diora Baird', 'nm1401531', True),
            ('Drew Barrymore', 'nm0000106', True),
            ('Erica Leerhsen', 'nm0498713', True),
            ('Gillian Shure', 'nm0795926', True),
            ('Gina Philips', 'nm0005312', True),
            ('Heather Graham', 'nm0001287', True),
            ('J.C. Brandy', 'nm0105046', True),
            ('Jane Scarlett', 'nm1391524', True),
            ('Julian Berlin', 'nm1139554', True),
            ('Katherine Heigl', 'nm0001337', True),
            ('Krista Allen', 'nm0020739', True),
            ('Lara Grice', 'nm1305056', True),
            ('Lena Headey', 'nm0372176', True),
            ('Marley Shelton', 'nm0005420', True),
            ('Mercedes McNab', 'nm0573523', True),
            ('Mimi Michaels', 'nm1483657', True),
            ('Natasha Alam', 'nm1647994', True),
            ('Rebecca Torrellas', 'nm2267469', True),
            ('Sally Mullins', 'nm1559657', True),
            ('Sara Dee', 'nm0214223', True),
            ('Sara Downing', 'nm0236130', True),
            ('Sarah Christine Smith', 'nm0809882', True),
            ('Sarah Michelle Gellar', 'nm0001264', True),
            ('Scout Taylor-Compton', 'nm0174021', True),
            ('Sonya Salomaa', 'nm1176497', True),
            ('Sophia Disgrace', 'nm3802743', True),
            ('Tara Reid', 'nm0005346', True),
            ('Taryn Manning', 'nm0543383', True),
            ('Addy Miller', 'nm2900452', True),
            ('Agnes Bruckner', 'nm0115671', True),
            ('Alana Curry', 'nm1002979', True),
            ('Alexandra Holden', 'nm0005016', True),
            ('Alice Amter', 'nm0025364', True),
            ('Alisha Seaton', 'nm0780822', True),
            ('Amber Heard', 'nm1720028', True),
            ('Amy Paffrath', 'nm2625932', True),
            ('Andrea Bogart', 'nm0091553', True),
            ('Arielle Kebbel', 'nm0444223', True),
            ('Blythe Metz', 'nm1348416', True),
            ('Briana Evigan', 'nm0263759', True),
            ('Brianna Brown', 'nm0113158', True),
            ('Brianne Davis', 'nm1732403', True),
            ('Cooper Harris', 'nm2599630', True),
            ('Danica DeCosto', 'nm0002690', True),
            ('Daniella Alonso', 'nm0022161', True),
            ('Dominique Swain', 'nm0000663', True),
            ('Elisa Eliot', 'nm1799605', True),
            ('Erin Cahill', 'nm0128657', True),
            ('Gail O Grady', 'nm0641097', True),
            ('Gia Franzia', 'nm1018582', True),
            ('Ginger Lynn', 'nm0000259', True),
            ('Johanna Putnam', 'nm2033836', True),
            ('Heather Amos', 'nm2753218', True),
            ('Heather Darcy', 'nm3220669', True),
            ('Heather Donahue', 'nm0231946', True),
            ('Haley Mancini', 'nm2268818', True),
            ('Ingrid Bolsø Berdal', 'nm2070336', True),
            ('Jaime King', 'nm0454809', True),
            ('Jen Nikolaus', 'nm2946721', True),
            ('Jennifer Blanc-Biehn', 'nm0004760', True),
            ('Jennifer Field', 'nm3016499', True),
            ('Jennifer Holland', 'nm1684744', True),
            ('Jennifer Pfalzgraff', 'nm0679318', True),
            ('Jennifer Rouse', 'nm1488137', True),
            ('Jessica Lowndes', 'nm2057726', True),
            ('Jessica Stroup', 'nm1888211', True),
            ('Joanna Noyes', 'nm0637543', True),
            ('Julianna Guill', 'nm1566474', True),
            ('Juliette Lewis', 'nm0000496', True),
            ('Katherine Randolph', 'nm0939822', True),
            ('Kathleen Mackey', 'nm0533472', True),
            ('Kelly Stables', 'nm1261587', True),
            ('Kirsten Zien', 'nm0698977', True),
            ('Kristi Lynn', 'nm2240179', True),
            ('Kristin Pfeifer', 'nm0679388', True),
            ('Kristina Anapau', 'nm0002936', True),
            ('Kristina Plisko', 'nm3205313', True),
            ('Kristy Swanson', 'nm0001785', True),
            ('Kyle Richards', 'nm0724202', True),
            ('Laura Cayouette', 'nm0147312', True),
            ('Laura Ortiz', 'nm1925026', True),
            ('Laura Ramsey', 'nm1377561', True),
            ('Lauren Bushby', 'nm3893233', True),
            ('Leena Kurishingal', 'nm2116949', True),
            ('Leighton Meester', 'nm1015262', True),
            ('Liane Balaban', 'nm0049313', True),
            ('Lili Taylor', 'nm0000666', True),
            ('Linda Pine', 'nm0683981', True),
            ('Lindsey Riesen', 'nm3766020', True),
            ('Lisa Marie Kull', 'nm3326279', True),
            ('Lori Hallier', 'nm0356590', True),
            ('Lucy Lawless', 'nm0005128', True),
            ('Lunden De Leon', 'nm0212534', True),
            ('Mackenzie Firgens', 'nm0278673', True),
            ('Margo Harshman', 'nm0366106', True),
            ('Marta Zolynska', 'nm3548848', True),
            ('Masuimi Max', 'nm1110087', True),
            ('Meagan Good', 'nm0328709', True),
            ('Melissa Gruver', 'nm1955098', True),
            ('Mena Suvari', 'nm0002546', True),
            ('Michele Morrow', 'nm1310789', True),
            ('Michelle Borth', 'nm1218924', True),
            ('Michelle Lee', 'nm1685477', True),
            ('Michelle Romano', 'nm1995226', True),
            ('Mischa Barton', 'nm0059215', True),
            ('Molly Hagan', 'nm0353243', True),
            ('Moneca Delain', 'nm1340697', True),
            ('Monica Keena', 'nm0444621', True),
            ('Morgana Shaw', 'nm0789892', True),
            ('Nancy Lynn McDonald', 'nm4122496', True),
            ('Naomi Watts', 'nm0915208', True),
            ('Natalie Avital', 'nm1271176', True),
            ('Natasha Gregson Wagner', 'nm0906031', True),
            ('Natasha Lyonne', 'nm0005169', True),
            ('Nicole Blessing', 'nm1748299', True),
            ('Nicole Dionne', 'nm1000737', True),
            ('Nicole Rayburn', 'nm1190808', True),
            ('Ona Grauer', 'nm0336125', True),
            ('Paula Ficara', 'nm1092592', True),
            ('Penny Vital', 'nm1715297', True),
            ('Pia Pownall', 'nm1743094', True),
            ('Rachel Nichols', 'nm0629697', True),
            ('Rachel Wittman', 'nm1825093', True),
            ('Rainer Judd', 'nm0431864', True),
            ('Rita Ramnani', 'nm2645682', True),
            ('Riley Rose Critchlow', 'nm2587995', True),
            ('Sara Tomko', 'nm2896588', True),
            ('Sarah Agor', 'nm2706070', True),
            ('Selma Blair', 'nm0004757', True),
            ('Shirly Brener', 'nm0107197', True),
            ('Siobhan Flynn', 'nm0283627', True),
            ('Sita Young', 'nm1936986', True),
            ('Skye McCole Bartusiak', 'nm0566084', True),
            ('Sofiya Smirnova', 'nm2253395', True),
            ('Stephanie Skewes', 'nm2352148', True),
            ('Suziey Block', 'nm0088770', True),
            ('Tamara Frapasella', 'nm2159100', True),
            ('Tierza Scaccia', 'nm1964090', True),
            ('Vanessa Angel', 'nm0029502', True),
            ('Victoria Ullmann', 'nm1760608', True),
            ('Yankie Grant', 'nm0335702', True),
            ('Katie Featherston', 'nm2209370', True),
            ('Jennifer Day', 'nm2414230', True),
        ]

        for i in genres: self.list.append(
            {
                'name': cleangenre.lang(i[0], self.lang),
                'url': self.screamq_link % i[1] if i[2] else self.imdb_person_list % i[1],
                'image': 'queens.gif',
                'action': 'movies'
            })

        self.addDirectory(self.list)
        return self.list


    def namegenre(self):
        genres = [


            ('Tobe Hooper', 'nm0001361', True),
            ('John Carpenter', 'nm0000118', True),
            ('Dario Argento', 'nm0000783', True),
            ('George A. Romero', 'nm0001681', True),
            ('Alfred Hitchcock', 'nm0000033', True),
            ('Sam Raimi', 'nm0000600', True),
            ('Steve Miner', 'nm0591171', True),
            ('Tom Holland', 'nm0276169', True),
            ('Rob Zombie', 'nm0957772', True),
            ('Neil Marshall', 'nm0551076', True),
            ('Clive Barker', 'nm0000850', True),
            ('Tod Browning', 'nm0115218', True),
            ('Eli Roth', 'nm0744834', True),
            ('Stuart Gordon', 'nm0002340', True),
            ('James Whale', 'nm0001843', True),
            ('Hideo Nakata', 'nm0620378', True),
            ('Takashi Miike', 'nm0586281', True),
            ('Lamberto Bava', 'nm0000877', True),
            ('Wes Craven', 'nm0000127', True),
            ('John Landis', 'nm0000484', True),
            ('Darren Lynn Bousman', 'nm1135423', True),
            ('Don Coscarelli', 'nm0181741', True),
            ('Joe Dante', 'nm0001102', True),
            ('Guillermo del Toro', 'nm0868219', True),
            ('Peter Jackson', 'nm0001392', True),
            ('Jeff Burr', 'nm0123009', True),
            ('Christopher Smith', 'nm1247462', True),
            ('Lucio Fulci', 'nm0002086', True),
            ('James Wan', 'nm1490123', True),
            ('William Castle', 'nm0145336', True),
            ('Jack Arnold', 'nm0000791', True),
            ('Robert Rodriguez', 'nm0001675', True),
            ('Mick Garris', 'nm0308376', True),
            ('Kiyoshi Kurosawa', 'nm0475905', True),
            ('Roger Corman', 'nm0000339', True),
            ('Herschell Gordon Lewis', 'nm0504496', True),
            ('Jacques Tourneur', 'nm0869664', True),
            ('Terence Fisher', 'nm0279807', True),
            ('Mario Bava', 'nm0000878', True),
            ('David Cronenberg', 'nm0000343', True),
            ('David Lynch', 'nm0000186', True),
            ('Michael Haneke', 'nm0359734', True),
            ('Frank Darabont', 'nm0001104', True),
            ('Danny Boyle', 'nm0000965', True),
            ('Greg McLean', 'nm0572562', True),
            ('Stanley Kubrick', 'nm0000040', True),
            ('Mitchell Altieri', 'nm1243970', True),
            ('Lucky McKee', 'nm1031246', True),
            ('Brian De Palma', 'nm0000361', True),
            ('Larry Cohen', 'nm0169540', True),
        ]

        for i in genres: self.list.append(
            {
                'name': cleangenre.lang(i[0], self.lang),
                'url': self.horrordir_link % i[1] if i[2] else self.imdb_person_list % i[1],
                'image': 'dir.gif',
                'action': 'movies'
            })

        self.addDirectory(self.list)
        return self.list
		


    def genres(self):
        genres = [
            ('Horror Action', 'action', True),
            ('Horror Adventure', 'adventure', True),
            ('Horror Animation', 'animation', True),
            ('Horror Biography', 'biography', True),
            ('Horror Comedy', 'comedy', True),
            ('Horror Crime', 'crime', True),
            ('Horror Documentary', 'documentary', True),
            ('Horror Drama', 'drama', True),
            ('Horror Family', 'family', True),
            ('Horror Fantasy', 'fantasy', True),
            ('Horror History', 'history', True),
            ('Horror Music ', 'music', True),
            ('Horror Musical', 'musical', True),
            ('Horror Mystery', 'mystery', True),
            ('Horror Romance', 'romance', True),
            ('Horror Science Fiction', 'sci_fi', True),
            ('Horror Sport', 'sport', True),
            ('Horror Thriller', 'thriller', True),
            ('Horror War', 'war', True),
            ('Horror Western', 'western', True),
            ('b rated', 'b-rated', True),

        ]

        for i in genres: self.list.append(
            {
                'name': cleangenre.lang(i[0], self.lang),
                'url': self.genre_link % i[1] if i[2] else self.keyword_link % i[1],
                'image': 'genres.gif',
                'action': 'movies'
            })

        self.addDirectory(self.list)
        return self.list



    def languages(self):
        languages = [
            ('Arabic', 'ar'),
            ('Bulgarian', 'bg'),
            ('Chinese', 'zh'),
            ('Croatian', 'hr'),
            ('Dutch', 'nl'),
            ('English', 'en'),
            ('Finnish', 'fi'),
            ('French', 'fr'),
            ('German', 'de'),
            ('Greek', 'el'),
            ('Hebrew', 'he'),
            ('Hindi ', 'hi'),
            ('Hungarian', 'hu'),
            ('Icelandic', 'is'),
            ('Italian', 'it'),
            ('Japanese', 'ja'),
            ('Korean', 'ko'),
            ('Norwegian', 'no'),
            ('Persian', 'fa'),
            ('Polish', 'pl'),
            ('Portuguese', 'pt'),
            ('Punjabi', 'pa'),
            ('Romanian', 'ro'),
            ('Russian', 'ru'),
            ('Spanish', 'es'),
            ('Swedish', 'sv'),
            ('Turkish', 'tr'),
            ('Ukrainian', 'uk')
        ]

        for i in languages: self.list.append({'name': str(i[0]), 'url': self.language_link % i[1], 'image': 'languages.jpg', 'action': 'movies'})
        self.addDirectory(self.list)
        return self.list


    def certifications(self):
        certificates = ['G', 'PG', 'PG-13', 'R', 'NC-17']

        for i in certificates: self.list.append({'name': str(i), 'url': self.certification_link % str(i).replace('-', '_').lower(), 'image': 'certificates.jpg', 'action': 'movies'})
        self.addDirectory(self.list)
        return self.list


    def years(self):
        year = (self.datetime.strftime('%Y'))

        for i in range(int(year)-0, 1930, -1): self.list.append({'name': str(i), 'url': self.year_link % (str(i), str(i)), 'image': 'years.jpg', 'action': 'movies'})
        self.addDirectory(self.list)
        return self.list


    def persons(self, url):
        if url == None:
            self.list = cache.get(self.imdb_person_list, 24, self.personlist_link)
        else:
            self.list = cache.get(self.imdb_person_list, 1, url)

        for i in range(0, len(self.list)): self.list[i].update({'action': 'movies'})
        self.addDirectory(self.list)
        return self.list


    def userlists(self):
        try:
            userlists = []
            if trakt.getTraktCredentialsInfo() == False: raise Exception()
            activity = trakt.getActivity()
        except:
            pass

        try:
            if trakt.getTraktCredentialsInfo() == False: raise Exception()
            try:
                if activity > cache.timeout(self.trakt_user_list, self.traktlists_link, self.trakt_user): raise Exception()
                userlists += cache.get(self.trakt_user_list, 720, self.traktlists_link, self.trakt_user)
            except:
                userlists += cache.get(self.trakt_user_list, 0, self.traktlists_link, self.trakt_user)
        except:
            pass
        try:
            self.list = []
            if self.imdb_user == '': raise Exception()
            userlists += cache.get(self.imdb_user_list, 0, self.imdblists_link)
        except:
            pass
        try:
            self.list = []
            if trakt.getTraktCredentialsInfo() == False: raise Exception()
            try:
                if activity > cache.timeout(self.trakt_user_list, self.traktlikedlists_link, self.trakt_user): raise Exception()
                userlists += cache.get(self.trakt_user_list, 720, self.traktlikedlists_link, self.trakt_user)
            except:
                userlists += cache.get(self.trakt_user_list, 0, self.traktlikedlists_link, self.trakt_user)
        except:
            pass

        self.list = userlists
        for i in range(0, len(self.list)): self.list[i].update({'image': 'userlists.jpg', 'action': 'movies'})
        self.addDirectory(self.list, queue=True)
        return self.list


    def trakt_list(self, url, user):
        try:
            q = dict(urlparse.parse_qsl(urlparse.urlsplit(url).query))
            q.update({'extended': 'full'})
            q = (urllib.urlencode(q)).replace('%2C', ',')
            u = url.replace('?' + urlparse.urlparse(url).query, '') + '?' + q

            result = trakt.getTraktAsJson(u)

            items = []
            for i in result:
                try: items.append(i['movie'])
                except: pass
            if len(items) == 0:
                items = result
        except:
            return

        try:
            q = dict(urlparse.parse_qsl(urlparse.urlsplit(url).query))
            if not int(q['limit']) == len(items): raise Exception()
            q.update({'page': str(int(q['page']) + 1)})
            q = (urllib.urlencode(q)).replace('%2C', ',')
            next = url.replace('?' + urlparse.urlparse(url).query, '') + '?' + q
            next = next.encode('utf-8')
        except:
            next = ''

        for item in items:
            try:
                title = item['title']
                title = client.replaceHTMLCodes(title)

                year = item['year']
                year = re.sub('[^0-9]', '', str(year))

                if int(year) > int((self.datetime).strftime('%Y')): raise Exception()

                imdb = item['ids']['imdb']
                if imdb == None or imdb == '': raise Exception()
                imdb = 'tt' + re.sub('[^0-9]', '', str(imdb))

                tmdb = str(item.get('ids', {}).get('tmdb', 0))

                try: premiered = item['released']
                except: premiered = '0'
                try: premiered = re.compile('(\d{4}-\d{2}-\d{2})').findall(premiered)[0]
                except: premiered = '0'

                try: genre = item['genres']
                except: genre = '0'
                genre = [i.title() for i in genre]
                if genre == []: genre = '0'
                genre = ' / '.join(genre)

                try: duration = str(item['runtime'])
                except: duration = '0'
                if duration == None: duration = '0'

                try: rating = str(item['rating'])
                except: rating = '0'
                if rating == None or rating == '0.0': rating = '0'

                try: votes = str(item['votes'])
                except: votes = '0'
                try: votes = str(format(int(votes),',d'))
                except: pass
                if votes == None: votes = '0'

                try: mpaa = item['certification']
                except: mpaa = '0'
                if mpaa == None: mpaa = '0'

                try: plot = item['overview']
                except: plot = '0'
                if plot == None: plot = '0'
                plot = client.replaceHTMLCodes(plot)

                try: tagline = item['tagline']
                except: tagline = '0'
                if tagline == None: tagline = '0'
                tagline = client.replaceHTMLCodes(tagline)

                self.list.append({'title': title, 'originaltitle': title, 'year': year, 'premiered': premiered, 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'plot': plot, 'tagline': tagline, 'imdb': imdb, 'tmdb': tmdb, 'tvdb': '0', 'poster': '0', 'next': next})
            except:
                pass

        return self.list


    def trakt_user_list(self, url, user):
        try:
            items = trakt.getTraktAsJson(url)
        except:
            pass

        for item in items:
            try:
                try: name = item['list']['name']
                except: name = item['name']
                name = client.replaceHTMLCodes(name)

                try: url = (trakt.slug(item['list']['user']['username']), item['list']['ids']['slug'])
                except: url = ('me', item['ids']['slug'])
                url = self.traktlist_link % url
                url = url.encode('utf-8')

                self.list.append({'name': name, 'url': url, 'context': url})
            except:
                pass

        self.list = sorted(self.list, key=lambda k: utils.title_key(k['name']))
        return self.list


    def imdb_list(self, url):
        try:
            for i in re.findall('date\[(\d+)\]', url):
                url = url.replace('date[%s]' % i, (self.datetime - datetime.timedelta(days = int(i))).strftime('%Y-%m-%d'))

            def imdb_watchlist_id(url):
                return client.parseDOM(client.request(url), 'meta', ret='content', attrs = {'property': 'pageId'})[0]

            if url == self.imdbwatchlist_link:
                url = cache.get(imdb_watchlist_id, 8640, url)
                url = self.imdblist_link % url

            elif url == self.imdbwatchlist2_link:
                url = cache.get(imdb_watchlist_id, 8640, url)
                url = self.imdblist2_link % url

            result = client.request(url)

            result = result.replace('\n', ' ')

            items = client.parseDOM(result, 'div', attrs = {'class': 'lister-item .+?'})
            items += client.parseDOM(result, 'div', attrs = {'class': 'list_item.+?'})
        except:
            return

        try:
            next = client.parseDOM(result, 'a', ret='href', attrs = {'class': 'lister-page-next next-page'})

            if len(next) == 0:
                next = client.parseDOM(result, 'div', attrs = {'class': 'pagination'})[0]
                next = zip(client.parseDOM(next, 'a', ret='href'), client.parseDOM(next, 'a'))
                next = [i[0] for i in next if 'Next' in i[1]]

            next = url.replace(urlparse.urlparse(url).query, urlparse.urlparse(next[0]).query)
            next = client.replaceHTMLCodes(next)
            next = next.encode('utf-8')
        except:
            next = ''

        for item in items:
            try:
                title = client.parseDOM(item, 'a')[1]
                title = client.replaceHTMLCodes(title)
                title = title.encode('utf-8')

                year = client.parseDOM(item, 'span', attrs = {'class': 'lister-item-year.+?'})
                year += client.parseDOM(item, 'span', attrs = {'class': 'year_type'})
                try: year = re.compile('(\d{4})').findall(year)[0]
                except: year = '0'
                year = year.encode('utf-8')

                if int(year) > int((self.datetime).strftime('%Y')): raise Exception()

                imdb = client.parseDOM(item, 'a', ret='href')[0]
                imdb = re.findall('(tt\d*)', imdb)[0]
                imdb = imdb.encode('utf-8')

                try: poster = client.parseDOM(item, 'img', ret='loadlate')[0]
                except: poster = '0'
                if '/nopicture/' in poster: poster = '0'
                poster = re.sub('(?:_SX|_SY|_UX|_UY|_CR|_AL)(?:\d+|_).+?\.', '_SX500.', poster)
                poster = client.replaceHTMLCodes(poster)
                poster = poster.encode('utf-8')

                try: genre = client.parseDOM(item, 'span', attrs = {'class': 'genre'})[0]
                except: genre = '0'
                genre = ' / '.join([i.strip() for i in genre.split(',')])
                if genre == '': genre = '0'
                genre = client.replaceHTMLCodes(genre)
                genre = genre.encode('utf-8')

                try: duration = re.findall('(\d+?) min(?:s|)', item)[-1]
                except: duration = '0'
                duration = duration.encode('utf-8')

                rating = '0'
                try: rating = client.parseDOM(item, 'span', attrs = {'class': 'rating-rating'})[0]
                except: pass
                try: rating = client.parseDOM(rating, 'span', attrs = {'class': 'value'})[0]
                except: rating = '0'
                try: rating = client.parseDOM(item, 'div', ret='data-value', attrs = {'class': '.*?imdb-rating'})[0]
                except: pass
                if rating == '' or rating == '-': rating = '0'
                rating = client.replaceHTMLCodes(rating)
                rating = rating.encode('utf-8')

                try: votes = client.parseDOM(item, 'div', ret='title', attrs = {'class': '.*?rating-list'})[0]
                except: votes = '0'
                try: votes = re.findall('\((.+?) vote(?:s|)\)', votes)[0]
                except: votes = '0'
                if votes == '': votes = '0'
                votes = client.replaceHTMLCodes(votes)
                votes = votes.encode('utf-8')

                try: mpaa = client.parseDOM(item, 'span', attrs = {'class': 'certificate'})[0]
                except: mpaa = '0'
                if mpaa == '' or mpaa == 'NOT_RATED': mpaa = '0'
                mpaa = mpaa.replace('_', '-')
                mpaa = client.replaceHTMLCodes(mpaa)
                mpaa = mpaa.encode('utf-8')

                try: director = re.findall('Director(?:s|):(.+?)(?:\||</div>)', item)[0]
                except: director = '0'
                director = client.parseDOM(director, 'a')
                director = ' / '.join(director)
                if director == '': director = '0'
                director = client.replaceHTMLCodes(director)
                director = director.encode('utf-8')

                try: cast = re.findall('Stars(?:s|):(.+?)(?:\||</div>)', item)[0]
                except: cast = '0'
                cast = client.replaceHTMLCodes(cast)
                cast = cast.encode('utf-8')
                cast = client.parseDOM(cast, 'a')
                if cast == []: cast = '0'

                plot = '0'
                try: plot = client.parseDOM(item, 'p', attrs = {'class': 'text-muted'})[0]
                except: pass
                try: plot = client.parseDOM(item, 'div', attrs = {'class': 'item_description'})[0]
                except: pass
                plot = plot.rsplit('<span>', 1)[0].strip()
                plot = re.sub('<.+?>|</.+?>', '', plot)
                if plot == '': plot = '0'
                plot = client.replaceHTMLCodes(plot)
                plot = plot.encode('utf-8')

                self.list.append({'title': title, 'originaltitle': title, 'year': year, 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'director': director, 'cast': cast, 'plot': plot, 'tagline': '0', 'imdb': imdb, 'tmdb': '0', 'tvdb': '0', 'poster': poster, 'next': next})
            except:
                pass

        return self.list


    def imdb_person_list(self, url):
        try:
            result = client.request(url)
            items = client.parseDOM(result, 'div', attrs = {'class': '.+? mode-detail'})
        except:
            return

        for item in items:
            try:
                name = client.parseDOM(item, 'img', ret='alt')[0]
                name = client.replaceHTMLCodes(name)
                name = name.encode('utf-8')

                url = client.parseDOM(item, 'a', ret='href')[0]
                url = re.findall('(nm\d*)', url, re.I)[0]
                url = self.person_link % url
                url = client.replaceHTMLCodes(url)
                url = url.encode('utf-8')

                image = client.parseDOM(item, 'img', ret='src')[0]
                # if not ('._SX' in image or '._SY' in image): raise Exception()
                # image = re.sub('(?:_SX|_SY|_UX|_UY|_CR|_AL)(?:\d+|_).+?\.', '_SX500.', image)
                image = client.replaceHTMLCodes(image)
                image = image.encode('utf-8')

                self.list.append({'name': name, 'url': url, 'image': image})
            except:
                pass

        return self.list


    def imdb_user_list(self, url):
        try:
            result = client.request(url)
            items = client.parseDOM(result, 'li', attrs = {'class': 'ipl-zebra-list__item user-list'})
        except:
            pass

        for item in items:
            try:
                name = client.parseDOM(item, 'a')[0]
                name = client.replaceHTMLCodes(name)
                name = name.encode('utf-8')

                url = client.parseDOM(item, 'a', ret='href')[0]
                url = url.split('/list/', 1)[-1].strip('/')
                url = self.imdblist_link % url
                url = client.replaceHTMLCodes(url)
                url = url.encode('utf-8')

                self.list.append({'name': name, 'url': url, 'context': url})
            except:
                pass

        self.list = sorted(self.list, key=lambda k: utils.title_key(k['name']))
        return self.list


    def worker(self, level=1):
        self.meta = []
        total = len(self.list)

        self.fanart_tv_headers = {'api-key': 'NTI1MzI3N2U2MDQyOTQ5Y2U5NmYwNDI3NTMyNzM0MTY='.decode('base64')}
        if not self.fanart_tv_user == '':
            self.fanart_tv_headers.update({'client-key': self.fanart_tv_user})

        for i in range(0, total): self.list[i].update({'metacache': False})

        self.list = metacache.fetch(self.list, self.lang, self.user)

        for r in range(0, total, 40):
            threads = []
            for i in range(r, r+40):
                if i <= total: threads.append(workers.Thread(self.super_info, i))
            [i.start() for i in threads]
            [i.join() for i in threads]

            if self.meta: metacache.insert(self.meta)

        self.list = [i for i in self.list if not i['imdb'] == '0']

        self.list = metacache.local(self.list, self.tm_img_link, 'poster3', 'fanart2')

        if self.fanart_tv_user == '':
            for i in self.list: i.update({'clearlogo': '0', 'clearart': '0'})


    def super_info(self, i):
        try:
            if self.list[i]['metacache'] == True: raise Exception()

            imdb = self.list[i]['imdb']

            item = trakt.getMovieSummary(imdb)

            title = item.get('title')
            title = client.replaceHTMLCodes(title)

            originaltitle = title

            year = item.get('year', 0)
            year = re.sub('[^0-9]', '', str(year))

            imdb = item.get('ids', {}).get('imdb', '0')
            imdb = 'tt' + re.sub('[^0-9]', '', str(imdb))

            tmdb = str(item.get('ids', {}).get('tmdb', 0))

            premiered = item.get('released', '0')
            try: premiered = re.compile('(\d{4}-\d{2}-\d{2})').findall(premiered)[0]
            except: premiered = '0'

            genre = item.get('genres', [])
            genre = [x.title() for x in genre]
            genre = ' / '.join(genre).strip()
            if not genre: genre = '0'

            duration = str(item.get('Runtime', 0))

            rating = item.get('rating', '0')
            if not rating or rating == '0.0': rating = '0'

            votes = item.get('votes', '0')
            try: votes = str(format(int(votes), ',d'))
            except: pass

            mpaa = item.get('certification', '0')
            if not mpaa: mpaa = '0'

            tagline = item.get('tagline', '0')

            plot = item.get('overview', '0')

            people = trakt.getPeople(imdb, 'movies')

            director = writer = ''
            if 'crew' in people and 'directing' in people['crew']:
                director = ', '.join([director['person']['name'] for director in people['crew']['directing'] if director['job'].lower() == 'director'])
            if 'crew' in people and 'writing' in people['crew']:
                writer = ', '.join([writer['person']['name'] for writer in people['crew']['writing'] if writer['job'].lower() in ['writer', 'screenplay', 'author']])

            cast = []
            for person in people.get('cast', []):
                cast.append({'name': person['person']['name'], 'role': person['character']})
            cast = [(person['name'], person['role']) for person in cast]

            try:
                if self.lang == 'en' or self.lang not in item.get('available_translations', [self.lang]): raise Exception()

                trans_item = trakt.getMovieTranslation(imdb, self.lang, full=True)

                title = trans_item.get('title') or title
                tagline = trans_item.get('tagline') or tagline
                plot = trans_item.get('overview') or plot
            except:
                pass

            try:
                artmeta = True
                #if self.fanart_tv_user == '': raise Exception()
                art = client.request(self.fanart_tv_art_link % imdb, headers=self.fanart_tv_headers, timeout='10', error=True)
                try: art = json.loads(art)
                except: artmeta = False
            except:
                pass

            try:
                poster2 = art['movieposter']
                poster2 = [x for x in poster2 if x.get('lang') == self.lang][::-1] + [x for x in poster2 if x.get('lang') == 'en'][::-1] + [x for x in poster2 if x.get('lang') in ['00', '']][::-1]
                poster2 = poster2[0]['url'].encode('utf-8')
            except:
                poster2 = '0'

            try:
                if 'moviebackground' in art: fanart = art['moviebackground']
                else: fanart = art['moviethumb']
                fanart = [x for x in fanart  if x.get('lang') == self.lang][::-1] + [x for x in fanart if x.get('lang') == 'en'][::-1] + [x for x in fanart if x.get('lang') in ['00', '']][::-1]
                fanart = fanart[0]['url'].encode('utf-8')
            except:
                fanart = '0'

            try:
                banner = art['moviebanner']
                banner = [x for x in banner if x.get('lang') == self.lang][::-1] + [x for x in banner if x.get('lang') == 'en'][::-1] + [x for x in banner if x.get('lang') in ['00', '']][::-1]
                banner = banner[0]['url'].encode('utf-8')
            except:
                banner = '0'

            try:
                if 'hdmovielogo' in art: clearlogo = art['hdmovielogo']
                else: clearlogo = art['clearlogo']
                clearlogo = [x for x in clearlogo if x.get('lang') == self.lang][::-1] + [x for x in clearlogo if x.get('lang') == 'en'][::-1] + [x for x in clearlogo if x.get('lang') in ['00', '']][::-1]
                clearlogo = clearlogo[0]['url'].encode('utf-8')
            except:
                clearlogo = '0'

            try:
                if 'hdmovieclearart' in art: clearart = art['hdmovieclearart']
                else: clearart = art['clearart']
                clearart = [x for x in clearart if x.get('lang') == self.lang][::-1] + [x for x in clearart if x.get('lang') == 'en'][::-1] + [x for x in clearart if x.get('lang') in ['00', '']][::-1]
                clearart = clearart[0]['url'].encode('utf-8')
            except:
                clearart = '0'

            try:
                if self.tm_user == '': raise Exception()

                art2 = client.request(self.tm_art_link % imdb, timeout='10', error=True)
                art2 = json.loads(art2)
            except:
                pass

            try:
                poster3 = art2['posters']
                poster3 = [x for x in poster3 if x.get('iso_639_1') == self.lang] + [x for x in poster3 if x.get('iso_639_1') == 'en'] + [x for x in poster3 if not x.get('iso_639_1') not in [self.lang, 'en']]
                poster3 = [(x['width'], x['file_path']) for x in poster3]
                poster3 = [(x[0], x[1]) if x[0] < 300 else ('300', x[1]) for x in poster3]
                poster3 = self.tm_img_link % poster3[0]
                poster3 = poster3.encode('utf-8')
            except:
                poster3 = '0'

            try:
                fanart2 = art2['backdrops']
                fanart2 = [x for x in fanart2 if x.get('iso_639_1') == self.lang] + [x for x in fanart2 if x.get('iso_639_1') == 'en'] + [x for x in fanart2 if not x.get('iso_639_1') not in [self.lang, 'en']]
                fanart2 = [x for x in fanart2 if x.get('width') == 1920] + [x for x in fanart2 if x.get('width') < 1920]
                fanart2 = [(x['width'], x['file_path']) for x in fanart2]
                fanart2 = [(x[0], x[1]) if x[0] < 1280 else ('1280', x[1]) for x in fanart2]
                fanart2 = self.tm_img_link % fanart2[0]
                fanart2 = fanart2.encode('utf-8')
            except:
                fanart2 = '0'

            item = {'title': title, 'originaltitle': originaltitle, 'year': year, 'imdb': imdb, 'tmdb': tmdb, 'poster': '0', 'poster2': poster2, 'poster3': poster3, 'banner': banner, 'fanart': fanart, 'fanart2': fanart2, 'clearlogo': clearlogo, 'clearart': clearart, 'premiered': premiered, 'genre': genre, 'duration': duration, 'rating': rating, 'votes': votes, 'mpaa': mpaa, 'director': director, 'writer': writer, 'cast': cast, 'plot': plot, 'tagline': tagline}
            item = dict((k,v) for k, v in item.iteritems() if not v == '0')
            self.list[i].update(item)

            if artmeta == False: raise Exception()

            meta = {'imdb': imdb, 'tmdb': tmdb, 'tvdb': '0', 'lang': self.lang, 'user': self.user, 'item': item}
            self.meta.append(meta)
        except:
            pass


    def movieDirectory(self, items):
        if items == None or len(items) == 0: control.idle() ; sys.exit()

        sysaddon = sys.argv[0]

        syshandle = int(sys.argv[1])

        addonPoster, addonBanner = control.addonPoster(), control.addonBanner()

        addonFanart, settingFanart = control.addonFanart(), control.setting('fanart')

        traktCredentials = trakt.getTraktCredentialsInfo()

        try: isOld = False ; control.item().getArt('type')
        except: isOld = True

        isPlayable = 'true' if not 'plugin' in control.infoLabel('Container.PluginName') else 'false'

        indicators = playcount.getMovieIndicators(refresh=True) if action == 'movies' else playcount.getMovieIndicators()

        playbackMenu = control.lang(32063).encode('utf-8') if control.setting('hosts.mode') == '2' else control.lang(32064).encode('utf-8')

        watchedMenu = control.lang(32068).encode('utf-8') if trakt.getTraktIndicatorsInfo() == True else control.lang(32066).encode('utf-8')

        unwatchedMenu = control.lang(32069).encode('utf-8') if trakt.getTraktIndicatorsInfo() == True else control.lang(32067).encode('utf-8')

        queueMenu = control.lang(32065).encode('utf-8')

        traktManagerMenu = control.lang(32070).encode('utf-8')

        nextMenu = control.lang(32053).encode('utf-8')

        addToLibrary = control.lang(32551).encode('utf-8')

        for i in items:
            try:
                label = '%s (%s)' % (i['title'], i['year'])
                imdb, tmdb, title, year = i['imdb'], i['tmdb'], i['originaltitle'], i['year']
                sysname = urllib.quote_plus('%s (%s)' % (title, year))
                systitle = urllib.quote_plus(title)

                meta = dict((k,v) for k, v in i.iteritems() if not v == '0')
                meta.update({'code': imdb, 'imdbnumber': imdb, 'imdb_id': imdb})
                meta.update({'tmdb_id': tmdb})
                meta.update({'mediatype': 'movie'})
                meta.update({'trailer': '%s?action=trailer&name=%s' % (sysaddon, urllib.quote_plus(label))})
                #meta.update({'trailer': 'plugin://script.extendedinfo/?info=playtrailer&&id=%s' % imdb})
                if not 'duration' in i: meta.update({'duration': '120'})
                elif i['duration'] == '0': meta.update({'duration': '120'})
                try: meta.update({'duration': str(int(meta['duration']) * 60)})
                except: pass
                try: meta.update({'genre': cleangenre.lang(meta['genre'], self.lang)})
                except: pass

                poster = [i[x] for x in ['poster3', 'poster', 'poster2'] if i.get(x, '0') != '0']
                poster = poster[0] if poster else addonPoster
                meta.update({'poster': poster})

                sysmeta = urllib.quote_plus(json.dumps(meta))

                url = '%s?action=play1&title=%s&year=%s&imdb=%s&meta=%s&t=%s' % (sysaddon, systitle, year, imdb, sysmeta, self.systime)
                sysurl = urllib.quote_plus(url)

                path = '%s?action=play&title=%s&year=%s&imdb=%s' % (sysaddon, systitle, year, imdb)


                cm = []

                cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))

                try:
                    overlay = int(playcount.getMovieOverlay(indicators, imdb))
                    if overlay == 7:
                        cm.append((unwatchedMenu, 'RunPlugin(%s?action=moviePlaycount&imdb=%s&query=6)' % (sysaddon, imdb)))
                        meta.update({'playcount': 1, 'overlay': 7})
                    else:
                        cm.append((watchedMenu, 'RunPlugin(%s?action=moviePlaycount&imdb=%s&query=7)' % (sysaddon, imdb)))
                        meta.update({'playcount': 0, 'overlay': 6})
                except:
                    pass

                if traktCredentials == True:
                    cm.append((traktManagerMenu, 'RunPlugin(%s?action=traktManager&name=%s&imdb=%s&content=movie)' % (sysaddon, sysname, imdb)))

                cm.append((playbackMenu, 'RunPlugin(%s?action=alterSources&url=%s&meta=%s)' % (sysaddon, sysurl, sysmeta)))

                if isOld == True:
                    cm.append((control.lang2(19033).encode('utf-8'), 'Action(Info)'))

                cm.append((addToLibrary, 'RunPlugin(%s?action=movieToLibrary&name=%s&title=%s&year=%s&imdb=%s&tmdb=%s)' % (sysaddon, sysname, systitle, year, imdb, tmdb)))

                item = control.item(label=label)

                art = {}
                art.update({'icon': poster, 'thumb': poster, 'poster': poster})

                if 'banner' in i and not i['banner'] == '0':
                    art.update({'banner': i['banner']})
                else:
                    art.update({'banner': addonBanner})

                if 'clearlogo' in i and not i['clearlogo'] == '0':
                    art.update({'clearlogo': i['clearlogo']})

                if 'clearart' in i and not i['clearart'] == '0':
                    art.update({'clearart': i['clearart']})


                if settingFanart == 'true' and 'fanart2' in i and not i['fanart2'] == '0':
                    item.setProperty('Fanart_Image', i['fanart2'])
                elif settingFanart == 'true' and 'fanart' in i and not i['fanart'] == '0':
                    item.setProperty('Fanart_Image', i['fanart'])
                elif not addonFanart == None:
                    item.setProperty('Fanart_Image', addonFanart)

                item.setArt(art)
                item.addContextMenuItems(cm)
                item.setProperty('IsPlayable', isPlayable)
                item.setInfo(type='Video', infoLabels = meta)

                video_streaminfo = {'codec': 'h264'}
                item.addStreamInfo('video', video_streaminfo)

                control.addItem(handle=syshandle, url=url, listitem=item, isFolder=False)
            except:
                pass

        try:
            url = items[0]['next']
            if url == '': raise Exception()

            icon = control.addonNext()
            url = '%s?action=moviePage&url=%s' % (sysaddon, urllib.quote_plus(url))

            item = control.item(label=nextMenu)

            item.setArt({'icon': icon, 'thumb': icon, 'poster': icon, 'banner': icon})
            if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)

            control.addItem(handle=syshandle, url=url, listitem=item, isFolder=True)
        except:
            pass

        control.content(syshandle, 'movies')
        control.directory(syshandle, cacheToDisc=True)
        views.setView('movies', {'skin.estuary': 55, 'skin.confluence': 500})


    def addDirectory(self, items, queue=False):
        if items == None or len(items) == 0: control.idle() ; sys.exit()

        sysaddon = sys.argv[0]

        syshandle = int(sys.argv[1])

        addonFanart, addonThumb, artPath = control.addonFanart(), control.addonThumb(), control.artPath()

        queueMenu = control.lang(32065).encode('utf-8')

        playRandom = control.lang(32535).encode('utf-8')

        addToLibrary = control.lang(32551).encode('utf-8')

        for i in items:
            try:
                name = i['name']

                if i['image'].startswith('http'): thumb = i['image']
                elif not artPath == None: thumb = os.path.join(artPath, i['image'])
                else: thumb = addonThumb

                url = '%s?action=%s' % (sysaddon, i['action'])
                try: url += '&url=%s' % urllib.quote_plus(i['url'])
                except: pass

                cm = []

                cm.append((playRandom, 'RunPlugin(%s?action=random&rtype=movie&url=%s)' % (sysaddon, urllib.quote_plus(i['url']))))

                if queue == True:
                    cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))

                try: cm.append((addToLibrary, 'RunPlugin(%s?action=moviesToLibrary&url=%s)' % (sysaddon, urllib.quote_plus(i['context']))))
                except: pass

                item = control.item(label=name)

                item.setArt({'icon': thumb, 'thumb': thumb})
                if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)

                item.addContextMenuItems(cm)

                control.addItem(handle=syshandle, url=url, listitem=item, isFolder=True)
            except:
                pass

        control.content(syshandle, 'addons')
        control.directory(syshandle, cacheToDisc=True)
