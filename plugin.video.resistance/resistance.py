# -*- coding: utf-8 -*-

'''
    resistance Add-on

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import urlparse,sys,urllib
from resources.lib.modules import control


import xbmcgui

params = dict(urlparse.parse_qsl(sys.argv[2].replace('?','')))

action = params.get('action')

name = params.get('name')

title = params.get('title')

year = params.get('year')

imdb = params.get('imdb')

tvdb = params.get('tvdb')

tmdb = params.get('tmdb')

season = params.get('season')

episode = params.get('episode')

tvshowtitle = params.get('tvshowtitle')

premiered = params.get('premiered')

url = params.get('url')

image = params.get('image')

meta = params.get('meta')

select = params.get('select')

query = params.get('query')

source = params.get('source')

content = params.get('content')

windowedtrailer = params.get('windowedtrailer')
windowedtrailer = int(windowedtrailer) if windowedtrailer in ("0","1") else 0

######################ZIM################################

if action == 'zimNavigator':
    from resources.lib.indexers import zim
    zim.navigator().root()

elif action == 'kidmovieNavigator':
    from resources.lib.indexers import zim
    zim.navigator().kidmovie()      

elif action == 'kidstvNavigator':
    from resources.lib.indexers import zim
    zim.navigator().kidstv()

elif action == 'animemovieNavigator':
    from resources.lib.indexers import zim
    zim.navigator().animemovie() 
    
elif action == 'animetvNavigator':
    from resources.lib.indexers import zim
    zim.navigator().animetv()  
    
elif action == 'toddlertvNavigator':
    from resources.lib.indexers import zim
    zim.navigator().toddlertv()

elif action == 'movies10':
    from resources.lib.indexers import movies10
    movies10.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies10
    movies10.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies10
    movies10.movies().widget()

elif action == 'moviePerson':
    from resources.lib.indexers import movies10
    movies10.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies10
    movies10.movies().genres()

elif action == 'animegenres':
    from resources.lib.indexers import movies10
    movies10.movies().animegenres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies10
    movies10.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies10
    movies10.movies().certifications()

elif action == 'movieanimecertifications':
    from resources.lib.indexers import movies10
    movies10.movies().animecertifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies10
    movies10.movies().years()

elif action == 'animemovyears':
    from resources.lib.indexers import movies10
    movies10.movies().animeyears()

elif action == 'moviePersons':
    from resources.lib.indexers import movies10
    movies10.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies10
    movies10.movies().userlists()

elif action == 'tvshows10':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().get(url)

elif action == 'animetvyears':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().animeyears()
    
elif action == 'tvPerson':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().genres()

elif action == 'animeGenres':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().animegenres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().certifications()

elif action == 'tvanimecertifications':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().animecertifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows10
    tvshows10.tvshows().userlists()              

######################DARKLOVE################################

if action == 'darkloveNavigator':
    from resources.lib.indexers import darklove
    darklove.navigator().root()

elif action == 'moviesromNavigator':
    from resources.lib.indexers import darklove
    darklove.navigator().moviesrom()      

elif action == 'moviesdramaNavigator':
    from resources.lib.indexers import darklove
    darklove.navigator().moviesdrama()

elif action == 'tvdramaNavigator':
    from resources.lib.indexers import darklove
    darklove.navigator().tvdrama()      

elif action == 'tvromNavigator':
    from resources.lib.indexers import darklove
    darklove.navigator().tvrom()

elif action == 'movieGenresdrama':
    from resources.lib.indexers import movies9
    movies9.movies().genresdrama()
    
elif action == 'movieGenresrom':
    from resources.lib.indexers import movies9
    movies9.movies().genresrom()

elif action == 'movieLanguagesdrama':
    from resources.lib.indexers import movies9
    movies9.movies().languagesdrama()

elif action == 'movieLanguagesrom':
    from resources.lib.indexers import movies9
    movies9.movies().languagesrom()

elif action == 'movieCertificatesdrama':
    from resources.lib.indexers import movies9
    movies9.movies().certificationsdrama()

elif action == 'movieCertificatesrom':
    from resources.lib.indexers import movies9
    movies9.movies().certificationsrom()

elif action == 'movieYearsdrama':
    from resources.lib.indexers import movies9
    movies9.movies().yearsdrama()

elif action == 'movieYearsrom':
    from resources.lib.indexers import movies9
    movies9.movies().yearsrom()  
    
elif action == 'tvYearsdrama':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().yearsdrama()

elif action == 'tvYearsrom':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().yearsrom()

elif action == 'tvGenresdrama':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().genresdrama()

elif action == 'tvGenresrom':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().genresrom()

elif action == 'tvLanguagesdrama':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().languagesdrama()

elif action == 'tvLanguagesrom':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().languagesrom()

elif action == 'tvCertificatesdrama':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().certificationsdrama()

elif action == 'tvCertificatesrom':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().certificationsrom()

elif action == 'movies9':
    from resources.lib.indexers import movies9
    movies9.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies9
    movies9.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies9
    movies9.movies().widget()

elif action == 'moviePerson':
    from resources.lib.indexers import movies9
    movies9.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies9
    movies9.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies9
    movies9.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies9
    movies9.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies9
    movies9.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies9
    movies9.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies9
    movies9.movies().userlists() 
    
elif action == 'tvshows9':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().get(url)
    
elif action == 'tvPerson':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows9
    tvshows9.tvshows().userlists()        

######################LAUGHINGHOUR################################

if action == 'laughNavigator':
    from resources.lib.indexers import laugh
    laugh.navigator().root()

elif action == 'laughmNavigator':
    from resources.lib.indexers import laugh
    laugh.navigator().laughm()      

elif action == 'laughtNavigator':
    from resources.lib.indexers import laugh
    laugh.navigator().laught()

elif action == 'movies8':
    from resources.lib.indexers import movies8
    movies8.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies8
    movies8.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies8
    movies8.movies().widget()

elif action == 'moviePerson':
    from resources.lib.indexers import movies8
    movies8.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies8
    movies8.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies8
    movies8.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies8
    movies8.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies8
    movies8.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies8
    movies8.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies8
    movies8.movies().userlists()

elif action == 'tvshows8':
    from resources.lib.indexers import tvshows8
    tvshows8.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows8
    tvshows8.tvshows().get(url)
    
elif action == 'tvPerson':
    from resources.lib.indexers import tvshows8
    tvshows8.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows8
    tvshows8.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows8
    tvshows8.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows8
    tvshows8.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows8
    tvshows8.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows8
    tvshows8.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows8
    tvshows8.tvshows().userlists()    

######################ASTROPLANE################################

if action == 'astroplaneNavigator':
    from resources.lib.indexers import astroplane
    astroplane.navigator().root()

elif action == 'astropmNavigator':
    from resources.lib.indexers import astroplane
    astroplane.navigator().astropm()      

elif action == 'astroptNavigator':
    from resources.lib.indexers import astroplane
    astroplane.navigator().astropt()

elif action == 'Franchise1Navigator':
    from resources.lib.indexers import astroplane
    astroplane.navigator().Franchise1()

elif action == 'Franchise2Navigator':
    from resources.lib.indexers import astroplane
    astroplane.navigator().Franchise2()

elif action == 'namegenre':
    from resources.lib.indexers import movies7
    movies7.movies().namegenre()

elif action == 'movies7':
    from resources.lib.indexers import movies7
    movies7.movies().get(url)

elif action == 'tvshows7':
    from resources.lib.indexers import tvshows7
    tvshows7.tvshows().get(url)    

elif action == 'moviePage':
    from resources.lib.indexers import movies7
    movies7.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies7
    movies7.movies().widget()

elif action == 'moviePerson':
    from resources.lib.indexers import movies7
    movies7.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies7
    movies7.movies().genres()


elif action == 'movieLanguages':
    from resources.lib.indexers import movies7
    movies7.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies7
    movies7.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies7
    movies7.movies().years()

elif action == 'tvYears':
    from resources.lib.indexers import tvshows7
    tvshows7.tvshows().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies7
    movies7.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies7
    movies7.movies().userlists()         

######################WILDWEST################################

if action == 'wildwestNavigator':
    from resources.lib.indexers import wildwest
    wildwest.navigator().root()

elif action == 'wildmovieNavigator':
    from resources.lib.indexers import wildwest
    wildwest.navigator().wildmovie()      

elif action == 'wildshowsNavigator':
    from resources.lib.indexers import wildwest
    wildwest.navigator().wildshows()

elif action == 'movies6':
    from resources.lib.indexers import movies6
    movies6.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies6
    movies6.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies6
    movies6.movies().widget()

elif action == 'moviePerson':
    from resources.lib.indexers import movies6
    movies6.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies6
    movies6.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies6
    movies6.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies6
    movies6.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies6
    movies6.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies6
    movies6.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies6
    movies6.movies().userlists()

elif action == 'tvshows6':
    from resources.lib.indexers import tvshows6
    tvshows6.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows6
    tvshows6.tvshows().get(url)
    
elif action == 'tvPerson':
    from resources.lib.indexers import tvshows6
    tvshows6.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows6
    tvshows6.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows6
    tvshows6.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows6
    tvshows6.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows6
    tvshows6.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows6
    tvshows6.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows6
    tvshows6.tvshows().userlists()    

######################ACTIONPACKED################################

if action == 'actionpNavigator':
    from resources.lib.indexers import actionp
    actionp.navigator().root()

elif action == 'moviesapNavigator':
    from resources.lib.indexers import actionp
    actionp.navigator().moviesap()      

elif action == 'tvshowsapNavigator':
    from resources.lib.indexers import actionp
    actionp.navigator().tvshowsap()

elif action == 'movies5':
    from resources.lib.indexers import movies5
    movies5.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies5
    movies5.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies5
    movies5.movies().widget()

elif action == 'moviePerson':
    from resources.lib.indexers import movies5
    movies5.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies5
    movies5.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies5
    movies5.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies5
    movies5.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies5
    movies5.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies5
    movies5.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies5
    movies5.movies().userlists()

elif action == 'tvshows5':
    from resources.lib.indexers import tvshows5
    tvshows5.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows5
    tvshows5.tvshows().get(url)
    
elif action == 'tvPerson':
    from resources.lib.indexers import tvshows5
    tvshows5.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows5
    tvshows5.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows5
    tvshows5.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows5
    tvshows5.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows5
    tvshows5.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows5
    tvshows5.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows5
    tvshows5.tvshows().userlists()

######################NIGHTMARE################################

if action == 'nightmareNavigator':
    from resources.lib.indexers import nightmare
    nightmare.navigator().root()

elif action == 'nightmaremovNavigator':
    from resources.lib.indexers import nightmare
    nightmare.navigator().nightmaremov()      

elif action == 'nightmaretvNavigator':
    from resources.lib.indexers import nightmare
    nightmare.navigator().nightmaretv()

elif action == 'FranchiseNavigator':
    from resources.lib.indexers import nightmare
    nightmare.navigator().Franchise()    

elif action == 'screamq':
    from resources.lib.indexers import movies4
    movies4.movies().screamq()

elif action == 'namegenre':
    from resources.lib.indexers import movies4
    movies4.movies().namegenre()

elif action == 'movies4':
    from resources.lib.indexers import movies4
    movies4.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies4
    movies4.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies4
    movies4.movies().widget()

elif action == 'moviePerson':
    from resources.lib.indexers import movies4
    movies4.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies4
    movies4.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies4
    movies4.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies4
    movies4.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies4
    movies4.movies().years()

elif action == 'tvYears':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies4
    movies4.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies4
    movies4.movies().userlists()

elif action == 'tvshows4':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().get(url)

elif action == 'tvPerson':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows4
    tvshows4.tvshows().userlists()

######################TOONTOWN#################################

if action == 'toontownNavigator':
    from resources.lib.indexers import toontown
    toontown.navigator().root()

elif action == 'toontownNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().toontown()      

elif action == 'toonmovieNavigator':
    from resources.lib.indexers import toontown
    toontown.navigator().toonsmov()

elif action == 'animemovieNavigator':
    from resources.lib.indexers import toontown
    toontown.navigator().animemov()

elif action == 'animetvNavigator':
    from resources.lib.indexers import toontown
    toontown.navigator().animetvshows()    

elif action == 'toonstvNavigator':
    from resources.lib.indexers import toontown
    toontown.navigator().toonstvshows()

elif action == 'movies3':
    from resources.lib.indexers import movies3
    movies3.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies3
    movies3.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies3
    movies3.movies().widget()

elif action == 'moviePerson':
    from resources.lib.indexers import movies3
    movies3.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies3
    movies3.movies().genres()

elif action == 'animegenres':
    from resources.lib.indexers import movies3
    movies3.movies().animegenres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies3
    movies3.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies3
    movies3.movies().certifications()

elif action == 'animemovyears':
    from resources.lib.indexers import movies3
    movies3.movies().animeyears()

elif action == 'animetvyears':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().animeyears()
    
elif action == 'tvanimecertifications':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().animecertifications()
    
elif action == 'movieanimecertifications':
    from resources.lib.indexers import movies3
    movies3.movies().animecertifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies3
    movies3.movies().years()

elif action == 'tvYears':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies3
    movies3.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies3
    movies3.movies().userlists()

elif action == 'tvshows3':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().get(url)

elif action == 'tvPerson':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().genres()

elif action == 'animeGenres':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().animegenres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows3
    tvshows3.tvshows().userlists()    

######################BONECRUSHER#################################

if action == 'docs2navNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().root()

if action == 'bioNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().bio()

if action == 'natutredocsNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().natutredocs()
    
if action == 'thebibleNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().bible()

if action == 'ConspiraciesNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().Conspiracies()
    
if action == 'mentalNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().mental()

if action == 'killersNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().killers()
    
if action == 'ufoNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().ufo()

if action == 'mythsNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().myths()
    
if action == 'addictionNavigator':
    from resources.lib.indexers import docs2nav
    docs2nav.navigator().addiction()

if action == 'kids2Navigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().root()
    
if action == 'toddlerNavigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().toddler()

if action == 'KidsNavigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().Kids()
    
if action == 'TeenNavigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().Teen()

    
if action == 'NatureNavigator':
    from resources.lib.indexers import kidsnav
    kidsnav.navigator().Nature()

if action == 'classicsNavigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().root()

if action == 'action2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().action()
    
if action == 'adventure2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().adventure()

if action == 'animation2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().animation()
    
if action == 'comedy2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().comedy()

if action == 'crime2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().crime()
    
if action == 'drama2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().drama()

if action == 'family2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().family()
    
if action == 'fantasy2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().fantasy()

if action == 'horror2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().horror()
    
if action == 'mystery2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().mystery()

if action == 'romance2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().romance()
    
if action == 'scifi2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().scifi()

if action == 'thriller2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().thriller()
    
if action == 'war2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().war()

if action == 'western2Navigator':
    from resources.lib.indexers import classicnav
    classicnav.navigator().western()
    
if action == 'boxsetsNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().root()

elif action == 'tvshows2':
    from resources.lib.indexers import tvshows2
    tvshows2.tvshows().get(url)    

elif action == 'bonecNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().bonec()    

elif action == 'movies2':
    from resources.lib.indexers import movies2
    movies2.movies().get(url)
    
elif action == 'actionNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().action()
    
elif action == 'actionliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().action(lite=True)

elif action == 'adventureNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().adventure()
    
elif action == 'adventureliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().adventure(lite=True)
    
elif action == 'animationNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().animation()
    
elif action == 'animationliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().animation(lite=True)
    
elif action == 'comedyNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().comedy()
    
elif action == 'comedyliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().comedy(lite=True)
    
elif action == 'crimeNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().crime()
    
elif action == 'crimeliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().crime(lite=True)
    
elif action == 'dramaNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().drama()
    
elif action == 'dramaliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().drama(lite=True)
    
elif action == 'familyNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().family()
    
elif action == 'familyliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().family(lite=True)
    
elif action == 'fantasyNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().fantasy()
    
elif action == 'fantasyliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().fantasy(lite=True)

elif action == 'horrorNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().horror()
    
elif action == 'horrorliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().horror(lite=True)
    
elif action == 'mysteryNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().mystery()
    
elif action == 'mysteryliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().mystery(lite=True)
    
elif action == 'romanceNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().romance()
    
elif action == 'romanceliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().romance(lite=True)
    
elif action == 'scifiNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().scifi()
    
elif action == 'scifiliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().scifi(lite=True)
    
elif action == 'thrillerNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().thriller()
    
elif action == 'thrillerliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().thriller(lite=True)
    
elif action == 'westernNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().western()
    
elif action == 'westernliteNavigator':
    from resources.lib.indexers import bxsets
    bxsets.navigator().western(lite=True)

elif action == 'teamNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().root()

elif action == 'ldmovNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().ldmov()

elif action == 'EnforcermoNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().Enforcermo()
    
elif action == 'warhammermoNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().warhammermo()

elif action == 'katsmoNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().katsmo()
    
elif action == 'stalkermoNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().stalkermo()

elif action == 'BftvNavigator':
    from resources.lib.indexers import teamnav
    teamnav.navigator().Bftv()

######################LISTS SCRAPER#################################

if action == 'lists':
    from resources.lib.indexers import lists
    lists.indexer().root()

elif action == 'resistdNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().resistd()    

elif action == 'directory':
    from resources.lib.indexers import lists
    lists.indexer().get(url)

elif action == 'qdirectory':
    from resources.lib.indexers import lists
    lists.indexer().getq(url)

elif action == 'xdirectory':
    from resources.lib.indexers import lists
    lists.indexer().getx(url)

elif action == 'developer':
    from resources.lib.indexers import lists
    lists.indexer().developer()

elif action == 'tvtuner':
    from resources.lib.indexers import lists
    lists.indexer().tvtuner(url)

elif 'youtube' in str(action):
    from resources.lib.indexers import lists
    lists.indexer().youtube(url, action)

elif action == 'play':
    from resources.lib.indexers import lists
    lists.player().play(url, content)

elif action == 'browser':
    from resources.lib.indexers import lists
    lists.resolver().browser(url)

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings()

elif action == 'urlresolverSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.urlresolver')

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'downloader':
    from resources.lib.modules import downloader
    downloader.downloader()

elif action == 'addDownload':
    from resources.lib.modules import downloader
    downloader.addDownload(name,url,image)

elif action == 'removeDownload':
    from resources.lib.modules import downloader
    downloader.removeDownload(url)

elif action == 'startDownload':
    from resources.lib.modules import downloader
    downloader.startDownload()

elif action == 'startDownloadThread':
    from resources.lib.modules import downloader
    downloader.startDownloadThread()

elif action == 'stopDownload':
    from resources.lib.modules import downloader
    downloader.stopDownload()

elif action == 'statusDownload':
    from resources.lib.modules import downloader
    downloader.statusDownload()

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name)

elif action == 'clearCache1':
    from resources.lib.modules import cache
    cache.clear()   

######################IMDB SCRAPER#################################

if action == None:
    from resources.lib.indexers import navigator
    from resources.lib.modules import cache
    cache.cache_version_check()
    navigator.navigator().root()

elif action == "furkNavigator":
    from resources.lib.indexers import navigator
    navigator.navigator().furk()

elif action == "furkMetaSearch":
    from resources.lib.indexers import furk
    furk.furk().furk_meta_search(url)

elif action == "furkSearch":
    from resources.lib.indexers import furk
    furk.furk().search()

elif action == "furkUserFiles":
    from resources.lib.indexers import furk
    furk.furk().user_files()

elif action == "furkSearchNew":
    from resources.lib.indexers import furk
    furk.furk().search_new()

elif action == 'ruSettings':
    from resources.lib.modules import control
    control.openSettings(id='script.module.resolveurl')    

elif action == 'movieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies()

elif action == 'movieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().movies(lite=True)

elif action == 'mymovieNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies()

elif action == 'mymovieliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mymovies(lite=True)

elif action == 'tvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows()

elif action == 'tvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tvshows(lite=True)

elif action == 'mytvNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows()

elif action == 'mytvliteNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().mytvshows(lite=True)

elif action == 'downloadNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().downloads()

elif action == 'paranormalNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().paranormal()

elif action == 'oneclickNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().oneclick()

elif action == 'oneclick2Navigator':
    from resources.lib.indexers import navigator
    navigator.navigator().oneclick2()            

elif action == 'libraryNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().library()

elif action == 'toolNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().tools()

elif action == 'searchNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().search()

elif action == 'viewsNavigator':
    from resources.lib.indexers import navigator
    navigator.navigator().views()

elif action == 'clearCache':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCache()

elif action == 'clearCacheSearch':
    from resources.lib.indexers import navigator
    navigator.navigator().clearCacheSearch()
    
elif action == 'infoCheck':
    from resources.lib.indexers import navigator
    navigator.navigator().infoCheck('')

elif action == 'movies':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'moviePage':
    from resources.lib.indexers import movies
    movies.movies().get(url)

elif action == 'movieWidget':
    from resources.lib.indexers import movies
    movies.movies().widget()

elif action == 'movieSearch':
    from resources.lib.indexers import movies
    movies.movies().search_new()

elif action == 'movieSearchnew':
    from resources.lib.indexers import movies
    movies.movies().search_new()

elif action == 'movieSearchterm':
    from resources.lib.indexers import movies
    movies.movies().search_term(name)

elif action == 'moviePerson':
    from resources.lib.indexers import movies
    movies.movies().person()

elif action == 'movieGenres':
    from resources.lib.indexers import movies
    movies.movies().genres()

elif action == 'movieLanguages':
    from resources.lib.indexers import movies
    movies.movies().languages()

elif action == 'movieCertificates':
    from resources.lib.indexers import movies
    movies.movies().certifications()

elif action == 'movieYears':
    from resources.lib.indexers import movies
    movies.movies().years()

elif action == 'moviePersons':
    from resources.lib.indexers import movies
    movies.movies().persons(url)

elif action == 'movieUserlists':
    from resources.lib.indexers import movies
    movies.movies().userlists()

elif action == 'channels':
    from resources.lib.indexers import channels
    channels.channels().get()

elif action == 'tvshows':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvshowPage':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().get(url)

elif action == 'tvSearch':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_new()

elif action == 'tvSearchnew':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_new()

elif action == 'tvSearchterm':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().search_term(name)
    
elif action == 'tvPerson':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().person()

elif action == 'tvGenres':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().genres()

elif action == 'tvNetworks':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().networks()

elif action == 'tvLanguages':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().languages()

elif action == 'tvCertificates':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().certifications()

elif action == 'tvPersons':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().persons(url)

elif action == 'tvUserlists':
    from resources.lib.indexers import tvshows
    tvshows.tvshows().userlists()

elif action == 'seasons':
    from resources.lib.indexers import episodes
    episodes.seasons().get(tvshowtitle, year, imdb, tvdb)

elif action == 'episodes':
    from resources.lib.indexers import episodes
    episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, episode)

elif action == 'calendar':
    from resources.lib.indexers import episodes
    episodes.episodes().calendar(url)

elif action == 'tvWidget':
    from resources.lib.indexers import episodes
    episodes.episodes().widget()

elif action == 'calendars':
    from resources.lib.indexers import episodes
    episodes.episodes().calendars()

elif action == 'episodeUserlists':
    from resources.lib.indexers import episodes
    episodes.episodes().userlists()

elif action == 'refresh':
    from resources.lib.modules import control
    control.refresh()

elif action == 'queueItem':
    from resources.lib.modules import control
    control.queueItem()

elif action == 'openSettings':
    from resources.lib.modules import control
    control.openSettings(query)

elif action == 'artwork':
    from resources.lib.modules import control
    control.artwork()

elif action == 'addView':
    from resources.lib.modules import views
    views.addView(content)

elif action == 'moviePlaycount':
    from resources.lib.modules import playcount
    playcount.movies(imdb, query)

elif action == 'episodePlaycount':
    from resources.lib.modules import playcount
    playcount.episodes(imdb, tvdb, season, episode, query)

elif action == 'tvPlaycount':
    from resources.lib.modules import playcount
    playcount.tvshows(name, imdb, tvdb, season, query)

elif action == 'trailer':
    from resources.lib.modules import trailer
    trailer.trailer().play(name, url, windowedtrailer)

elif action == 'traktManager':
    from resources.lib.modules import trakt
    trakt.manager(name, imdb, tvdb, content)

elif action == 'authTrakt':
    from resources.lib.modules import trakt
    trakt.authTrakt()

elif action == 'smuSettings':
    try: import resolveurl
    except: pass
    resolveurl.display_settings()

elif action == 'download':
    import json
    from resources.lib.modules import sources
    from resources.lib.modules import downloader
    try: downloader.download(name, image, sources.sources().sourcesResolve(json.loads(source)[0], True))
    except: pass

elif action == 'play1':
    from resources.lib.modules import sources
    sources.sources().play(title, year, imdb, tvdb, season, episode, tvshowtitle, premiered, meta, select)

elif action == 'addItem':
    from resources.lib.modules import sources
    sources.sources().addItem(title)

elif action == 'playItem':
    from resources.lib.modules import sources
    sources.sources().playItem(title, source)

elif action == 'alterSources':
    from resources.lib.modules import sources
    sources.sources().alterSources(url, meta)

elif action == 'clearSources':
    from resources.lib.modules import sources
    sources.sources().clearSources()

elif action == 'random':
    rtype = params.get('rtype')
    if rtype == 'movie':
        from resources.lib.indexers import movies
        rlist = movies.movies().get(url, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'episode':
        from resources.lib.indexers import episodes
        rlist = episodes.episodes().get(tvshowtitle, year, imdb, tvdb, season, create_directory=False)
        r = sys.argv[0]+"?action=play"
    elif rtype == 'season':
        from resources.lib.indexers import episodes
        rlist = episodes.seasons().get(tvshowtitle, year, imdb, tvdb, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=episode"
    elif rtype == 'show':
        from resources.lib.indexers import tvshows
        rlist = tvshows.tvshows().get(url, create_directory=False)
        r = sys.argv[0]+"?action=random&rtype=season"
    from resources.lib.modules import control
    from random import randint
    import json
    try:
        rand = randint(1,len(rlist))-1
        for p in ['title','year','imdb','tvdb','season','episode','tvshowtitle','premiered','select']:
            if rtype == "show" and p == "tvshowtitle":
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand]['title'])
                except: pass
            else:
                try: r += '&'+p+'='+urllib.quote_plus(rlist[rand][p])
                except: pass
        try: r += '&meta='+urllib.quote_plus(json.dumps(rlist[rand]))
        except: r += '&meta='+urllib.quote_plus("{}")
        if rtype == "movie":
            try: control.infoDialog(rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        elif rtype == "episode":
            try: control.infoDialog(rlist[rand]['tvshowtitle']+" - Season "+rlist[rand]['season']+" - "+rlist[rand]['title'], control.lang(32536).encode('utf-8'), time=30000)
            except: pass
        control.execute('RunPlugin(%s)' % r)
    except:
        control.infoDialog(control.lang(32537).encode('utf-8'), time=8000)

elif action == 'movieToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().add(name, title, year, imdb, tmdb)

elif action == 'moviesToLibrary':
    from resources.lib.modules import libtools
    libtools.libmovies().range(url)

elif action == 'moviesToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libmovies().silent(url)

elif action == 'tvshowToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().add(tvshowtitle, year, imdb, tvdb)

elif action == 'tvshowsToLibrary':
    from resources.lib.modules import libtools
    libtools.libtvshows().range(url)

elif action == 'tvshowsToLibrarySilent':
    from resources.lib.modules import libtools
    libtools.libtvshows().silent(url)

elif action == 'updateLibrary':
    from resources.lib.modules import libtools
    libtools.libepisodes().update(query)

elif action == 'service':
    from resources.lib.modules import libtools
    libtools.libepisodes().service()
