# -*- coding: utf-8 -*-




import os,sys,urlparse

from resources.lib.modules import control
from resources.lib.modules import trakt
inprogress_db = control.setting('inprogress_db')

sysaddon = sys.argv[0]

syshandle = int(sys.argv[1])

artPath = control.artPath()

addonFanart = control.addonFanart()

imdbCredentials = False if control.setting('imdb.user') == '' else True

traktCredentials = trakt.getTraktCredentialsInfo()

traktIndicators = trakt.getTraktIndicatorsInfo()

queueMenu = control.lang(32065).encode('utf-8')

	

class navigator:
    def root(self):
        if inprogress_db == 'true': self.addDirectoryItem("In Progress", 'movieProgress', 'bc.png', 'bc.png')
        self.addDirectoryItem('Action', 'actionNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Adventure', 'adventureNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Animation', 'animationNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Comedy', 'comedyNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Crime', 'crimeNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Drama', 'dramaNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Family', 'familyNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Fantasy', 'fantasyNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Horror', 'horrorNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mystery', 'mysteryNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Romance', 'romanceNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Sci-Fi', 'scifiNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Thriller', 'thrillerNavigator', 'bc.png', 'bc.png')
#        self.addDirectoryItem('War', 'warNavigator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Western', 'westernNavigator', 'bc.png', 'bc.png')
        #self.addDirectoryItem(32008, 'toolNavigator', 'bc.png', 'DefaultAddonProgram.png')
        #self.addDirectoryItem(32010, 'movieSearch', 'bc.png', 'bc.png')
        #downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0) else False
        #if downloads == True: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.endDirectory()

	
    def action(self, lite=False):
        self.addDirectoryItem('12 Rounds', 'movies2&url=tmdbrounds', 'bc.png', 'bc.png')
        self.addDirectoryItem('3 Ninjas', 'movies2&url=tmdb3nin', 'bc.png', 'bc.png')

        self.addDirectoryItem('300', 'movies2&url=tmdb300', 'bc.png', 'bc.png')
        self.addDirectoryItem('Agent Cody Banks', 'movies2&url=tmdbagent', 'bc.png', 'bc.png')

        self.addDirectoryItem('American Ninja', 'movies2&url=tmdbamninja', 'bc.png', 'bc.png')
        self.addDirectoryItem('Avengers', 'movies2&url=tmdbavengers', 'bc.png', 'bc.png')		
        self.addDirectoryItem('AVP', 'movies2&url=tmdbavp', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Bad Ass', 'movies2&url=tmdbbadass', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bad Boys', 'movies2&url=tmdbbb', 'bc.png', 'bc.png')
        self.addDirectoryItem('Batman', 'movies2&url=tmdbbatman', 'bc.png', 'bc.png')
        self.addDirectoryItem('Best Of The Best', 'movies2&url=tmdbbob', 'bc.png', 'bc.png')
        self.addDirectoryItem('Beverly Hills Cop', 'movies2&url=tmdbbeverly', 'bc.png', 'bc.png')
        self.addDirectoryItem('Big Mommas House', 'movies2&url=tmdbbig', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bloodsport', 'movies2&url=tmdbblood', 'bc.png', 'bc.png')
        self.addDirectoryItem('Blues Brother', 'movies2&url=tmdbblues', 'bc.png', 'bc.png')
        self.addDirectoryItem('Boondock Saints', 'movies2&url=tmdbboon', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Bourne', 'movies2&url=tmdbbourne', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Bruce Lee', 'movies2&url=tmdbbrucelee', 'bc.png', 'bc.png')
        self.addDirectoryItem('Captain America', 'movies2&url=tmdbcaptain', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cats & Dogs', 'movies2&url=tmdbcatsanddogs', 'bc.png', 'bc.png')

        self.addDirectoryItem('Crank', 'movies2&url=tmdbcrank', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Crow', 'movies2&url=tmdbcrow', 'bc.png', 'bc.png')
        self.addDirectoryItem('Die Hard', 'movies2&url=tmdbdie', 'bc.png', 'bc.png')
        self.addDirectoryItem('Dirty Harry', 'movies2&url=tmdbdirtyh', 'bc.png', 'bc.png')
        self.addDirectoryItem('Fast and Furious', 'movies2&url=tmdbfurious', 'bc.png', 'bc.png')
        self.addDirectoryItem('G.I. Joe', 'movies2&url=tmdbgi', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ghost Rider', 'movies2&url=tmdbghost', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ghostbusters', 'movies2&url=tmdbghostbusters', 'bc.png', 'bc.png')
        self.addDirectoryItem('Highlander', 'movies2&url=tmdbhighlander', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hollow Man', 'movies2&url=tmdbhollow', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hoodwinked!', 'movies2&url=tmdbhoodwink', 'bc.png', 'bc.png')

        self.addDirectoryItem('Hot Shots', 'movies2&url=tmdbhot', 'bc.png', 'bc.png')		
        self.addDirectoryItem('How To Train Your Dragon', 'movies2&url=tmdbhow', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Huntsman', 'movies2&url=tmdbhuntsman', 'bc.png', 'bc.png')
        self.addDirectoryItem('Independence Day', 'movies2&url=tmdbindependence', 'bc.png', 'bc.png')
        self.addDirectoryItem('Indiana Jones', 'movies2&url=tmdbindiana', 'bc.png', 'bc.png')
        self.addDirectoryItem('Inspector Gadget', 'movies2&url=tmdbinspector', 'bc.png', 'bc.png')

        self.addDirectoryItem('Ip Man', 'movies2&url=tmdbipman', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Iron Fists', 'movies2&url=tmdbironfists', 'bc.png', 'bc.png')
        self.addDirectoryItem('Jackass', 'movies2&url=tmdbjackass', 'bc.png', 'bc.png')
        self.addDirectoryItem('James Bond', 'movies2&url=tmdbjames', 'bc.png', 'bc.png')
        self.addDirectoryItem('Johnny English', 'movies2&url=tmdbjohnny', 'bc.png', 'bc.png')
        self.addDirectoryItem('Journey', 'movies2&url=tmdbjourney', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Judge Dredd', 'movies2&url=tmdbdredd', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Jump Street', 'movies2&url=tmdbjump', 'bc.png', 'bc.png')
        self.addDirectoryItem('Justice League', 'movies2&url=tmdbjusticeleague', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Karate Kid', 'movies2&url=tmdbkarate', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kick-Ass', 'movies2&url=tmdbkick', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kickboxer', 'movies2&url=tmdbkickboxer', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kill Bill', 'movies2&url=tmdbkill', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kung Fu Panda', 'movies2&url=tmdbkung', 'bc.png', 'bc.png')

        self.addDirectoryItem('Lethal Weapon', 'movies2&url=tmdblethal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Machete', 'movies2&url=tmdbmachete', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mad Max', 'movies2&url=tmdbmadmax', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Matrix', 'movies2&url=tmdbmatrix', 'bc.png', 'bc.png')
        self.addDirectoryItem('Maze Runner', 'movies2&url=tmdbmaze', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Mechanic', 'movies2&url=tmdbmechanic', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mission Impossible', 'movies2&url=tmdbmission', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Mummy', 'movies2&url=tmdbmummy', 'bc.png', 'bc.png')
        self.addDirectoryItem('National Treasure', 'movies2&url=tmdbnational', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Never Back Down', 'movies2&url=tmdbnever', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ninja', 'movies2&url=tmdbninja', 'bc.png', 'bc.png')
        self.addDirectoryItem('Olympus Has Fallen', 'movies2&url=tmdbolympus', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ong Bak', 'movies2&url=tmdbong', 'bc.png', 'bc.png')
        self.addDirectoryItem('Pirates of The Caribbean', 'movies2&url=tmdbpirates', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Power Rangers', 'movies2&url=tmdbpowerrangers', 'bc.png', 'bc.png')

        self.addDirectoryItem('Predator', 'movies2&url=tmdbpredator', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Protector', 'movies2&url=tmdbprotector', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Punisher', 'movies2&url=tmdbpunisher', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Raid', 'movies2&url=tmdbraid', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rambo', 'movies2&url=tmdbrambo', 'bc.png', 'bc.png')		
        self.addDirectoryItem('R.E.D.', 'movies2&url=tmdbred', 'bc.png', 'bc.png')
        self.addDirectoryItem('Red Cliff', 'movies2&url=tmdbredcliff', 'bc.png', 'bc.png')
        self.addDirectoryItem('Resident Evil', 'movies2&url=tmdbresident', 'bc.png', 'bc.png')
        self.addDirectoryItem('Riddick', 'movies2&url=tmdbriddick', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ride Along', 'movies2&url=tmdbride', 'bc.png', 'bc.png')
        self.addDirectoryItem('Robocop', 'movies2&url=tmdbrobocop', 'bc.png', 'bc.png')
        self.addDirectoryItem('Romancing The Stone', 'movies2&url=tmdbromancing', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rush Hour', 'movies2&url=tmdbrush', 'bc.png', 'bc.png')
        self.addDirectoryItem('Sherlock Holmes', 'movies2&url=tmdbsherlock', 'bc.png', 'bc.png')
        self.addDirectoryItem('Smokey and The Bandit', 'movies2&url=tmdbsmokey', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Spy Kids', 'movies2&url=tmdbspy', 'bc.png', 'bc.png')

        self.addDirectoryItem('Star Trek', 'movies2&url=tmdbstartrek', 'bc.png', 'bc.png')
        self.addDirectoryItem('Star Wars', 'movies2&url=tmdbstarwars', 'bc.png', 'bc.png')
        self.addDirectoryItem('Starship Troopers', 'movies2&url=tmdbstarship', 'bc.png', 'bc.png')
        self.addDirectoryItem('Taken', 'movies2&url=tmdbtaken', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Teenage Mutant Ninja Turtles', 'movies2&url=tmdbteenage', 'bc.png', 'bc.png')
        self.addDirectoryItem('Terminator', 'movies2&url=tmdbterminator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Titans', 'movies2&url=tmdbtitans', 'bc.png', 'bc.png')
        self.addDirectoryItem('Transformers', 'movies2&url=tmdbtransformers', 'bc.png', 'bc.png')
        self.addDirectoryItem('Transporter', 'movies2&url=tmdbtransporter', 'bc.png', 'bc.png')
        self.addDirectoryItem('Tron', 'movies2&url=tmdbtron', 'bc.png', 'bc.png')
        self.addDirectoryItem('Under Siege', 'movies2&url=tmdbunder', 'bc.png', 'bc.png')
        self.addDirectoryItem('Underworld', 'movies2&url=tmdbunderworld', 'bc.png', 'bc.png')
        self.addDirectoryItem('Undisputed', 'movies2&url=tmdbundisputed', 'bc.png', 'bc.png')
        self.addDirectoryItem('Universal Soldier', 'movies2&url=tmdbuniversal', 'bc.png', 'bc.png')		
        self.addDirectoryItem('xXx', 'movies2&url=tmdbxxx', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Young Guns', 'movies2&url=tmdbyoung', 'bc.png', 'bc.png')
        self.addDirectoryItem('Zorro', 'movies2&url=tmdbzorro', 'bc.png', 'bc.png')


        self.endDirectory()

    def adventure(self, lite=False):
        self.addDirectoryItem('101 Dalmations', 'movies2&url=tmdbdal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Agent Cody Banks', 'movies2&url=tmdbagent', 'bc.png', 'bc.png')
        self.addDirectoryItem('Aladdin', 'movies2&url=tmdbaladdin', 'bc.png', 'bc.png')
        self.addDirectoryItem('Alice In Wonderland', 'movies2&url=tmdbalice', 'bc.png', 'bc.png')

        self.addDirectoryItem('American Ninja', 'movies2&url=tmdbamninja', 'bc.png', 'bc.png')
        self.addDirectoryItem('Austin Powers', 'movies2&url=tmdbaustin', 'bc.png', 'bc.png')
        self.addDirectoryItem('Back To The Future', 'movies2&url=tmdbback', 'bc.png', 'bc.png')
        self.addDirectoryItem('Balto', 'movies2&url=tmdbbalto', 'bc.png', 'bc.png')

        self.addDirectoryItem('Batman', 'movies2&url=tmdbbatman', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bean', 'movies2&url=tmdbbean', 'bc.png', 'bc.png')
        self.addDirectoryItem('Brother Bear', 'movies2&url=tmdbbrotherbear', 'bc.png', 'bc.png')		

        self.addDirectoryItem('Captain America', 'movies2&url=tmdbcaptain', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Chronicles of Narnia', 'movies2&url=tmdbnarnia', 'bc.png', 'bc.png')

        self.addDirectoryItem('Cloudy With A Chance of Meatballs', 'movies2&url=tmdbcloudy', 'bc.png', 'bc.png')

        self.addDirectoryItem('Conan', 'movies2&url=tmdbconan', 'bc.png', 'bc.png')
        self.addDirectoryItem('Crocodile Dundee', 'movies2&url=tmdbcroc', 'bc.png', 'bc.png')
        self.addDirectoryItem('Curious George', 'movies2&url=tmdbcurious', 'bc.png', 'bc.png')
        self.addDirectoryItem('Despicable Me', 'movies2&url=tmdbdespicable', 'bc.png', 'bc.png')

        self.addDirectoryItem('Divergent', 'movies2&url=tmdbdivergent', 'bc.png', 'bc.png')
        self.addDirectoryItem('FernGully', 'movies2&url=tmdbferngully', 'bc.png', 'bc.png')
        self.addDirectoryItem('Finding Nemo', 'movies2&url=tmdbfinding', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Fox and The Hound', 'movies2&url=tmdbfox', 'bc.png', 'bc.png')
        self.addDirectoryItem('Free Willy', 'movies2&url=tmdbfree', 'bc.png', 'bc.png')

        self.addDirectoryItem('G.I. Joe', 'movies2&url=tmdbgi', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ghostbusters', 'movies2&url=tmdbghostbusters', 'bc.png', 'bc.png')
        self.addDirectoryItem('A Goofy Movie', 'movies2&url=tmdbgoofy', 'bc.png', 'bc.png')

        self.addDirectoryItem('Harold and Kumar', 'movies2&url=tmdbharold', 'bc.png', 'bc.png')
        self.addDirectoryItem('Harry Potter', 'movies2&url=tmdbharry', 'bc.png', 'bc.png')
        self.addDirectoryItem('Herbie', 'movies2&url=tmdbherbie', 'bc.png', 'bc.png')

        self.addDirectoryItem('Highlander', 'movies2&url=tmdbhighlander', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Hobbit', 'movies2&url=tmdbhobbit', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Homeward Bound', 'movies2&url=tmdbhomeward', 'bc.png', 'bc.png')
        self.addDirectoryItem('Honey I Shrunk The Kids', 'movies2&url=tmdbhoney', 'bc.png', 'bc.png')
        self.addDirectoryItem('How To Train Your Dragon', 'movies2&url=tmdbhow', 'bc.png', 'bc.png')

        self.addDirectoryItem('Hunger Games', 'movies2&url=tmdbhunger', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Huntsman', 'movies2&url=tmdbhuntsman', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ice Age', 'movies2&url=tmdbiceage', 'bc.png', 'bc.png')

        self.addDirectoryItem('Independence Day', 'movies2&url=tmdbindependence', 'bc.png', 'bc.png')
        self.addDirectoryItem('Indiana Jones', 'movies2&url=tmdbindiana', 'bc.png', 'bc.png')
        self.addDirectoryItem('Inspector Gadget', 'movies2&url=tmdbinspector', 'bc.png', 'bc.png')

        self.addDirectoryItem('James Bond', 'movies2&url=tmdbjames', 'bc.png', 'bc.png')
        self.addDirectoryItem('Jaws', 'movies2&url=tmdbjaws', 'bc.png', 'bc.png')
        self.addDirectoryItem('Johnny English', 'movies2&url=tmdbjohnny', 'bc.png', 'bc.png')
        self.addDirectoryItem('Journey', 'movies2&url=tmdbjourney', 'bc.png', 'bc.png')		
        self.addDirectoryItem('The Jungle Book', 'movies2&url=tmdbjungle', 'bc.png', 'bc.png')

        self.addDirectoryItem('Jurassic Park', 'movies2&url=tmdbjurassic', 'bc.png', 'bc.png')
        self.addDirectoryItem('Justice League', 'movies2&url=tmdbjusticeleague', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kung Fu Panda', 'movies2&url=tmdbkung', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lady and The Tramp', 'movies2&url=tmdblady', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Land Before Time', 'movies2&url=tmdblbt', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lilo & Stitch', 'movies2&url=tmdblilo', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Lion King', 'movies2&url=tmdblion', 'bc.png', 'bc.png')

        self.addDirectoryItem('Lord of The Rings', 'movies2&url=tmdblord', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mad Max', 'movies2&url=tmdbmadmax', 'bc.png', 'bc.png')
        self.addDirectoryItem('Madagascar', 'movies2&url=tmdbmadagascar', 'bc.png', 'bc.png')		

        self.addDirectoryItem('Men in Black', 'movies2&url=tmdbmib', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mission Impossible', 'movies2&url=tmdbmission', 'bc.png', 'bc.png')
        self.addDirectoryItem('Monsters INC', 'movies2&url=tmdbmonster', 'bc.png', 'bc.png')

        self.addDirectoryItem('Monty Python', 'movies2&url=tmdbmonty', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mulan', 'movies2&url=tmdbmulan', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Mummy', 'movies2&url=tmdbmummy', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Muppets', 'movies2&url=tmdbmuppets', 'bc.png', 'bc.png')

        self.addDirectoryItem('National Treasure', 'movies2&url=tmdbnational', 'bc.png', 'bc.png')		
        self.addDirectoryItem('The Never Ending Story', 'movies2&url=tmdbnes', 'bc.png', 'bc.png')
        self.addDirectoryItem('New Groove', 'movies2&url=tmdbnewgroove', 'bc.png', 'bc.png')

        self.addDirectoryItem('Night At The Museum', 'movies2&url=tmdbnatm', 'bc.png', 'bc.png')
        self.addDirectoryItem('Nims Island', 'movies2&url=tmdbnims', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Open Season', 'movies2&url=tmdbopen', 'bc.png', 'bc.png')

        self.addDirectoryItem('Percy Jackson', 'movies2&url=tmdbpercy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Peter Pan', 'movies2&url=tmdbpeter', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Pink Panther', 'movies2&url=tmdbpink', 'bc.png', 'bc.png')
        self.addDirectoryItem('Pirates of The Caribbean', 'movies2&url=tmdbpirates', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Planes', 'movies2&url=tmdbplanes', 'bc.png', 'bc.png')

        self.addDirectoryItem('Planet of The Apes', 'movies2&url=tmdbplanet', 'bc.png', 'bc.png')
        self.addDirectoryItem('Pocahontas', 'movies2&url=tmdbpoca', 'bc.png', 'bc.png')
        self.addDirectoryItem('Power Rangers', 'movies2&url=tmdbpowerrangers', 'bc.png', 'bc.png')

        self.addDirectoryItem('Rambo', 'movies2&url=tmdbrambo', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Red Cliff', 'movies2&url=tmdbredcliff', 'bc.png', 'bc.png')
        self.addDirectoryItem('Riddick', 'movies2&url=tmdbriddick', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rio', 'movies2&url=tmdbrio', 'bc.png', 'bc.png')

        self.addDirectoryItem('Romancing The Stone', 'movies2&url=tmdbromancing', 'bc.png', 'bc.png')
        self.addDirectoryItem('Sammys Adventures', 'movies2&url=tmdbsammy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Sherlock Holmes', 'movies2&url=tmdbsherlock', 'bc.png', 'bc.png')
        self.addDirectoryItem('Shrek', 'movies2&url=tmdbshrek', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Smurfs', 'movies2&url=tmdbsmurfs', 'bc.png', 'bc.png')
        self.addDirectoryItem('Space Chimps', 'movies2&url=tmdbspacechimps', 'bc.png', 'bc.png')
        self.addDirectoryItem('SpongBob Squarepants', 'movies2&url=tmdbspongebob', 'bc.png', 'bc.png')
        self.addDirectoryItem('Spy Kids', 'movies2&url=tmdbspy', 'bc.png', 'bc.png')

        self.addDirectoryItem('Star Trek', 'movies2&url=tmdbstartrek', 'bc.png', 'bc.png')
        self.addDirectoryItem('Star Wars', 'movies2&url=tmdbstarwars', 'bc.png', 'bc.png')
        self.addDirectoryItem('Starship Troopers', 'movies2&url=tmdbstarship', 'bc.png', 'bc.png')
        self.addDirectoryItem('Stuart Little', 'movies2&url=tmdbstuart', 'bc.png', 'bc.png')
        self.addDirectoryItem('Tarzan', 'movies2&url=tmdbtarzan', 'bc.png', 'bc.png')

        self.addDirectoryItem('Teenage Mutant Ninja Turtles', 'movies2&url=tmdbteenage', 'bc.png', 'bc.png')
        self.addDirectoryItem('Tinker Bell', 'movies2&url=tmdbtinker', 'bc.png', 'bc.png')
        self.addDirectoryItem('Titans', 'movies2&url=tmdbtitans', 'bc.png', 'bc.png')
        self.addDirectoryItem('Transformers', 'movies2&url=tmdbtransformers', 'bc.png', 'bc.png')
        self.addDirectoryItem('Tron', 'movies2&url=tmdbtron', 'bc.png', 'bc.png')
        self.addDirectoryItem('Weekend at Bernies', 'movies2&url=tmdbweekend', 'bc.png', 'bc.png')
        self.addDirectoryItem('xXx', 'movies2&url=tmdbxxx', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Zorro', 'movies2&url=tmdbzorro', 'bc.png', 'bc.png')


        self.endDirectory()
		
    def animation(self, lite=False):
        self.addDirectoryItem('101 Dalmations', 'movies2&url=tmdbdal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Aladdin', 'movies2&url=tmdbaladdin', 'bc.png', 'bc.png')
        self.addDirectoryItem('Alice In Wonderland', 'movies2&url=tmdbalice', 'bc.png', 'bc.png')
        self.addDirectoryItem('All Dogs Go to Heaven', 'movies2&url=tmdballdogs', 'bc.png', 'bc.png')
        self.addDirectoryItem('Balto', 'movies2&url=tmdbbalto', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bambi', 'movies2&url=tmdbbambi', 'bc.png', 'bc.png')
        self.addDirectoryItem('Beauty and The Beast', 'movies2&url=tmdbbeauty', 'bc.png', 'bc.png')
        self.addDirectoryItem('Brother Bear', 'movies2&url=tmdbbrotherbear', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Cars', 'movies2&url=tmdbcars', 'bc.png', 'bc.png')
        self.addDirectoryItem('Charlottes Web', 'movies2&url=tmdbcharlottes', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cloudy With A Chance of Meatballs', 'movies2&url=tmdbcloudy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Curious George', 'movies2&url=tmdbcurious', 'bc.png', 'bc.png')
        self.addDirectoryItem('Despicable Me', 'movies2&url=tmdbdespicable', 'bc.png', 'bc.png')
        self.addDirectoryItem('Fantasia', 'movies2&url=tmdbfantasia', 'bc.png', 'bc.png')
        self.addDirectoryItem('FernGully', 'movies2&url=tmdbferngully', 'bc.png', 'bc.png')
        self.addDirectoryItem('Finding Nemo', 'movies2&url=tmdbfinding', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Fox and The Hound', 'movies2&url=tmdbfox', 'bc.png', 'bc.png')
        self.addDirectoryItem('Garfield', 'movies2&url=tmdbgarfield', 'bc.png', 'bc.png')
        self.addDirectoryItem('A Goofy Movie', 'movies2&url=tmdbgoofy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Happy Feet', 'movies2&url=tmdbhappy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hoodwinked!', 'movies2&url=tmdbhoodwink', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hotel Transylvania', 'movies2&url=tmdbhotel', 'bc.png', 'bc.png')
        self.addDirectoryItem('How To Train Your Dragon', 'movies2&url=tmdbhow', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hunchback of Notre Dame', 'movies2&url=tmdbhunch', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ice Age', 'movies2&url=tmdbiceage', 'bc.png', 'bc.png')
        self.addDirectoryItem('Justice League', 'movies2&url=tmdbjusticeleague', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kung Fu Panda', 'movies2&url=tmdbkung', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lady and The Tramp', 'movies2&url=tmdblady', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Land Before Time', 'movies2&url=tmdblbt', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lego Star Wars', 'movies2&url=tmdblegostar', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lilo & Stitch', 'movies2&url=tmdblilo', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Lion King', 'movies2&url=tmdblion', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Little Mermaid', 'movies2&url=tmdbmermaid', 'bc.png', 'bc.png')	
        self.addDirectoryItem('Madagascar', 'movies2&url=tmdbmadagascar', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Monsters INC', 'movies2&url=tmdbmonster', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mulan', 'movies2&url=tmdbmulan', 'bc.png', 'bc.png')
        self.addDirectoryItem('New Groove', 'movies2&url=tmdbnewgroove', 'bc.png', 'bc.png')
        self.addDirectoryItem('Open Season', 'movies2&url=tmdbopen', 'bc.png', 'bc.png')
        self.addDirectoryItem('Planes', 'movies2&url=tmdbplanes', 'bc.png', 'bc.png')

        self.addDirectoryItem('Pocahontas', 'movies2&url=tmdbpoca', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Reef', 'movies2&url=tmdbreef', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rio', 'movies2&url=tmdbrio', 'bc.png', 'bc.png')

        self.addDirectoryItem('Sammys Adventures', 'movies2&url=tmdbsammy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Shrek', 'movies2&url=tmdbshrek', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Smurfs', 'movies2&url=tmdbsmurfs', 'bc.png', 'bc.png')
        self.addDirectoryItem('Space Chimps', 'movies2&url=tmdbspacechimps', 'bc.png', 'bc.png')
        self.addDirectoryItem('SpongBob Squarepants', 'movies2&url=tmdbspongebob', 'bc.png', 'bc.png')
        self.addDirectoryItem('Tarzan', 'movies2&url=tmdbtarzan', 'bc.png', 'bc.png')
        self.addDirectoryItem('Thomas & Friends', 'movies2&url=tmdbthomas', 'bc.png', 'bc.png')
		
        self.addDirectoryItem('Tinker Bell', 'movies2&url=tmdbtinker', 'bc.png', 'bc.png')
        self.addDirectoryItem('Wallace & Gromit', 'movies2&url=tmdbwallace', 'bc.png', 'bc.png')
		
		
		
		
		

        self.endDirectory()
		
    def comedy(self, lite=False):
        self.addDirectoryItem('101 Dalmations', 'movies2&url=tmdbdal', 'bc.png', 'bc.png')
        self.addDirectoryItem('3 Ninjas', 'movies2&url=tmdb3nin', 'bc.png', 'bc.png')

        self.addDirectoryItem('A Haunted House', 'movies2&url=tmdbhaunted', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ace Ventura', 'movies2&url=tmdbace', 'bc.png', 'bc.png')
        self.addDirectoryItem('Adams Family', 'movies2&url=tmdbadams', 'bc.png', 'bc.png')
        self.addDirectoryItem('Agent Cody Banks', 'movies2&url=tmdbagent', 'bc.png', 'bc.png')
        self.addDirectoryItem('Aladdin', 'movies2&url=tmdbaladdin', 'bc.png', 'bc.png')
        self.addDirectoryItem('All Dogs Go to Heaven', 'movies2&url=tmdballdogs', 'bc.png', 'bc.png')

        self.addDirectoryItem('American Pie', 'movies2&url=tmdbampie', 'bc.png', 'bc.png')
        self.addDirectoryItem('Anchorman', 'movies2&url=tmdbanchor', 'bc.png', 'bc.png')
        self.addDirectoryItem('Austin Powers', 'movies2&url=tmdbaustin', 'bc.png', 'bc.png')
        self.addDirectoryItem('Babe', 'movies2&url=tmdbbabe', 'bc.png', 'bc.png')

        self.addDirectoryItem('Back To The Future', 'movies2&url=tmdbback', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bad Ass', 'movies2&url=tmdbbadass', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bad Boys', 'movies2&url=tmdbbb', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bad Neighbors', 'movies2&url=tmdbbn', 'bc.png', 'bc.png')
        self.addDirectoryItem('Barbershop', 'movies2&url=tmdbbarber', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bean', 'movies2&url=tmdbbean', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Best Exotic Marigold Hotel', 'movies2&url=tmdbbestexotic', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Beverly Hills Cop', 'movies2&url=tmdbbeverly', 'bc.png', 'bc.png')
        self.addDirectoryItem('Big Mommas House', 'movies2&url=tmdbbig', 'bc.png', 'bc.png')
        self.addDirectoryItem('Blues Brother', 'movies2&url=tmdbblues', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bridget Jones', 'movies2&url=tmdbbridget', 'bc.png', 'bc.png')
        self.addDirectoryItem('Brother Bear', 'movies2&url=tmdbbrotherbear', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Cars', 'movies2&url=tmdbcars', 'bc.png', 'bc.png')
        self.addDirectoryItem('Casper', 'movies2&url=tmdbcasper', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cats & Dogs', 'movies2&url=tmdbcatsanddogs', 'bc.png', 'bc.png')

        self.addDirectoryItem('City Slickers', 'movies2&url=tmdbcity', 'bc.png', 'bc.png')
        self.addDirectoryItem('Clerks', 'movies2&url=tmdbclerks', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cloudy With A Chance of Meatballs', 'movies2&url=tmdbcloudy', 'bc.png', 'bc.png')

        self.addDirectoryItem('Crocodile Dundee', 'movies2&url=tmdbcroc', 'bc.png', 'bc.png')
        self.addDirectoryItem('Curious George', 'movies2&url=tmdbcurious', 'bc.png', 'bc.png')
        self.addDirectoryItem('Daddy Daycare', 'movies2&url=tmdbdaddy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Despicable Me', 'movies2&url=tmdbdespicable', 'bc.png', 'bc.png')

        self.addDirectoryItem('Diary of A Wimpy Kid', 'movies2&url=tmdbdiary', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Doctor Dolittle', 'movies2&url=tmdbdolittle', 'bc.png', 'bc.png')

        self.addDirectoryItem('Dumb and Dumber', 'movies2&url=tmdbdumb', 'bc.png', 'bc.png')
        self.addDirectoryItem('Finding Nemo', 'movies2&url=tmdbfinding', 'bc.png', 'bc.png')		

        self.addDirectoryItem('Friday', 'movies2&url=tmdbfriday', 'bc.png', 'bc.png')
        self.addDirectoryItem('Garfield', 'movies2&url=tmdbgarfield', 'bc.png', 'bc.png')

        self.addDirectoryItem('Ghostbusters', 'movies2&url=tmdbghostbusters', 'bc.png', 'bc.png')
        self.addDirectoryItem('A Goofy Movie', 'movies2&url=tmdbgoofy', 'bc.png', 'bc.png')

        self.addDirectoryItem('Gremlins', 'movies2&url=tmdbgremlins', 'bc.png', 'bc.png')
        self.addDirectoryItem('Grown Ups', 'movies2&url=tmdbgrown', 'bc.png', 'bc.png')
        self.addDirectoryItem('Grumpy Old Men', 'movies2&url=tmdbgrumpy', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Hangover', 'movies2&url=tmdbhangover', 'bc.png', 'bc.png')
        self.addDirectoryItem('Happy Feet', 'movies2&url=tmdbhappy', 'bc.png', 'bc.png')

        self.addDirectoryItem('Harold and Kumar', 'movies2&url=tmdbharold', 'bc.png', 'bc.png')
        self.addDirectoryItem('Herbie', 'movies2&url=tmdbherbie', 'bc.png', 'bc.png')

        self.addDirectoryItem('Home Alone', 'movies2&url=tmdbhome', 'bc.png', 'bc.png')
        self.addDirectoryItem('Homeward Bound', 'movies2&url=tmdbhomeward', 'bc.png', 'bc.png')
        self.addDirectoryItem('Honey I Shrunk The Kids', 'movies2&url=tmdbhoney', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hoodwinked!', 'movies2&url=tmdbhoodwink', 'bc.png', 'bc.png')

        self.addDirectoryItem('Horrible Bosses', 'movies2&url=tmdbhorrible', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hot Shots', 'movies2&url=tmdbhot', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Hot Tub Time Machine', 'movies2&url=tmdbhotub', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hotel Transylvania', 'movies2&url=tmdbhotel', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ice Age', 'movies2&url=tmdbiceage', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Inbetweeners', 'movies2&url=tmdbinbetweeners', 'bc.png', 'bc.png')
        self.addDirectoryItem('Inspector Gadget', 'movies2&url=tmdbinspector', 'bc.png', 'bc.png')

        self.addDirectoryItem('Jackass', 'movies2&url=tmdbjackass', 'bc.png', 'bc.png')
        self.addDirectoryItem('Johnny English', 'movies2&url=tmdbjohnny', 'bc.png', 'bc.png')
        self.addDirectoryItem('Jump Street', 'movies2&url=tmdbjump', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kick-Ass', 'movies2&url=tmdbkick', 'bc.png', 'bc.png')
        self.addDirectoryItem('Legally Blonde', 'movies2&url=tmdblegally', 'bc.png', 'bc.png')
        self.addDirectoryItem('Like Mike', 'movies2&url=tmdblikemike', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lilo & Stitch', 'movies2&url=tmdblilo', 'bc.png', 'bc.png')
        self.addDirectoryItem('Madagascar', 'movies2&url=tmdbmadagascar', 'bc.png', 'bc.png')		

        self.addDirectoryItem('Major League', 'movies2&url=tmdbmajor', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Meet The Parents', 'movies2&url=tmdbmeet', 'bc.png', 'bc.png')
        self.addDirectoryItem('Men in Black', 'movies2&url=tmdbmib', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Mighty Ducks', 'movies2&url=tmdbmighty', 'bc.png', 'bc.png')
        self.addDirectoryItem('Monsters INC', 'movies2&url=tmdbmonster', 'bc.png', 'bc.png')

        self.addDirectoryItem('Monty Python', 'movies2&url=tmdbmonty', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Muppets', 'movies2&url=tmdbmuppets', 'bc.png', 'bc.png')

        self.addDirectoryItem('My Big Fat Greek Wedding', 'movies2&url=tmdbmbfgw', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Naked Gun', 'movies2&url=tmdbnaked', 'bc.png', 'bc.png')
        self.addDirectoryItem('New Groove', 'movies2&url=tmdbnewgroove', 'bc.png', 'bc.png')

        self.addDirectoryItem('Night At The Museum', 'movies2&url=tmdbnatm', 'bc.png', 'bc.png')
        self.addDirectoryItem('Nims Island', 'movies2&url=tmdbnims', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Open Season', 'movies2&url=tmdbopen', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Pink Panther', 'movies2&url=tmdbpink', 'bc.png', 'bc.png')
        self.addDirectoryItem('Pitch Perfect', 'movies2&url=tmdbpitch', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Planes', 'movies2&url=tmdbplanes', 'bc.png', 'bc.png')

        self.addDirectoryItem('Police Academy', 'movies2&url=tmdbpolice', 'bc.png', 'bc.png')
        self.addDirectoryItem('Problem Child', 'movies2&url=tmdbproblem', 'bc.png', 'bc.png')
        self.addDirectoryItem('R.E.D.', 'movies2&url=tmdbred', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ride Along', 'movies2&url=tmdbride', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rio', 'movies2&url=tmdbrio', 'bc.png', 'bc.png')

        self.addDirectoryItem('Romancing The Stone', 'movies2&url=tmdbromancing', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rush Hour', 'movies2&url=tmdbrush', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Sandlot', 'movies2&url=tmdbsandlot', 'bc.png', 'bc.png')

        self.addDirectoryItem('Scary Movie', 'movies2&url=tmdbscary', 'bc.png', 'bc.png')
        self.addDirectoryItem('Shrek', 'movies2&url=tmdbshrek', 'bc.png', 'bc.png')

        self.addDirectoryItem('Short Circuit', 'movies2&url=tmdbshort', 'bc.png', 'bc.png')
        self.addDirectoryItem('Smokey and The Bandit', 'movies2&url=tmdbsmokey', 'bc.png', 'bc.png')		
        self.addDirectoryItem('The Smurfs', 'movies2&url=tmdbsmurfs', 'bc.png', 'bc.png')
        self.addDirectoryItem('Space Chimps', 'movies2&url=tmdbspacechimps', 'bc.png', 'bc.png')
        self.addDirectoryItem('SpongBob Squarepants', 'movies2&url=tmdbspongebob', 'bc.png', 'bc.png')
        self.addDirectoryItem('Spy Kids', 'movies2&url=tmdbspy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Stuart Little', 'movies2&url=tmdbstuart', 'bc.png', 'bc.png')

        self.addDirectoryItem('Ted', 'movies2&url=tmdbted', 'bc.png', 'bc.png')
        self.addDirectoryItem('Teenage Mutant Ninja Turtles', 'movies2&url=tmdbteenage', 'bc.png', 'bc.png')
        self.addDirectoryItem('Teen Wolf', 'movies2&url=tmdbteen', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Tooth Fairy', 'movies2&url=tmdbtooth', 'bc.png', 'bc.png')

        self.addDirectoryItem('Tremors', 'movies2&url=tmdbtremors', 'bc.png', 'bc.png')
        self.addDirectoryItem('Waynes World', 'movies2&url=tmdbwayne', 'bc.png', 'bc.png')
        self.addDirectoryItem('Weekend at Bernies', 'movies2&url=tmdbweekend', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Whole Nine Yards', 'movies2&url=tmdbwholenine', 'bc.png', 'bc.png')
        self.addDirectoryItem('Zoolander', 'movies2&url=tmdbzoo', 'bc.png', 'bc.png')
        self.addDirectoryItem('Zorro', 'movies2&url=tmdbzorro', 'bc.png', 'bc.png')


        self.endDirectory()
		
    def crime(self, lite=False):
        self.addDirectoryItem('12 Rounds', 'movies2&url=tmdbrounds', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bad Ass', 'movies2&url=tmdbbadass', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bad Boys', 'movies2&url=tmdbbb', 'bc.png', 'bc.png')
        self.addDirectoryItem('Beverly Hills Cop', 'movies2&url=tmdbbeverly', 'bc.png', 'bc.png')
        self.addDirectoryItem('Big Mommas House', 'movies2&url=tmdbbig', 'bc.png', 'bc.png')
        self.addDirectoryItem('Blues Brother', 'movies2&url=tmdbblues', 'bc.png', 'bc.png')
        self.addDirectoryItem('Boondock Saints', 'movies2&url=tmdbboon', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Crank', 'movies2&url=tmdbcrank', 'bc.png', 'bc.png')
        self.addDirectoryItem('Dirty Harry', 'movies2&url=tmdbdirtyh', 'bc.png', 'bc.png')
        self.addDirectoryItem('Dragon Tattoo', 'movies2&url=tmdbdragon', 'bc.png', 'bc.png')
        self.addDirectoryItem('Fast and Furious', 'movies2&url=tmdbfurious', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Godfather', 'movies2&url=tmdbgodfather', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Green Street Hooligans', 'movies2&url=tmdbgreen', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Hannibal Lecter', 'movies2&url=tmdbhannibal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Horrible Bosses', 'movies2&url=tmdbhorrible', 'bc.png', 'bc.png')
        self.addDirectoryItem('Infernal Affairs', 'movies2&url=tmdbinfernal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Judge Dredd', 'movies2&url=tmdbdredd', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Jump Street', 'movies2&url=tmdbjump', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kill Bill', 'movies2&url=tmdbkill', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lethal Weapon', 'movies2&url=tmdblethal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Machete', 'movies2&url=tmdbmachete', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Mechanic', 'movies2&url=tmdbmechanic', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Naked Gun', 'movies2&url=tmdbnaked', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ninja', 'movies2&url=tmdbninja', 'bc.png', 'bc.png')
        self.addDirectoryItem('Now You See Me', 'movies2&url=tmdbnysm', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Oceans', 'movies2&url=tmdboceans', 'bc.png', 'bc.png')
        self.addDirectoryItem('Once Were Warriors', 'movies2&url=tmdbonce', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Ong Bak', 'movies2&url=tmdbong', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Pink Panther', 'movies2&url=tmdbpink', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Protector', 'movies2&url=tmdbprotector', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Punisher', 'movies2&url=tmdbpunisher', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Raid', 'movies2&url=tmdbraid', 'bc.png', 'bc.png')
        self.addDirectoryItem('R.E.D.', 'movies2&url=tmdbred', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ride Along', 'movies2&url=tmdbride', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rise of the Footsoldier', 'movies2&url=tmdbrise', 'bc.png', 'bc.png')
        self.addDirectoryItem('Robocop', 'movies2&url=tmdbrobocop', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rush Hour', 'movies2&url=tmdbrush', 'bc.png', 'bc.png')
        self.addDirectoryItem('Sherlock Holmes', 'movies2&url=tmdbsherlock', 'bc.png', 'bc.png')
        self.addDirectoryItem('Sin City', 'movies2&url=tmdbsin', 'bc.png', 'bc.png')
        self.addDirectoryItem('Step Up', 'movies2&url=tmdbstepup', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Transporter', 'movies2&url=tmdbtransporter', 'bc.png', 'bc.png')
        self.addDirectoryItem('Undisputed', 'movies2&url=tmdbundisputed', 'bc.png', 'bc.png')
        self.addDirectoryItem('Weekend at Bernies', 'movies2&url=tmdbweekend', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Whole Nine Yards', 'movies2&url=tmdbwholenine', 'bc.png', 'bc.png')
        self.addDirectoryItem('Young Guns', 'movies2&url=tmdbyoung', 'bc.png', 'bc.png')


        self.endDirectory()
		
    def drama(self, lite=False):
        self.addDirectoryItem('28 Days Later', 'movies2&url=tmdb28days', 'bc.png', 'bc.png')
        self.addDirectoryItem('All Dogs Go to Heaven', 'movies2&url=tmdballdogs', 'bc.png', 'bc.png')
        self.addDirectoryItem('Babe', 'movies2&url=tmdbbabe', 'bc.png', 'bc.png')
        self.addDirectoryItem('Balto', 'movies2&url=tmdbbalto', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bambi', 'movies2&url=tmdbbambi', 'bc.png', 'bc.png')

        self.addDirectoryItem('Barbershop', 'movies2&url=tmdbbarber', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Before', 'movies2&url=tmdbbefore', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Best Exotic Marigold Hotel', 'movies2&url=tmdbbestexotic', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Best Of The Best', 'movies2&url=tmdbbob', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bloodsport', 'movies2&url=tmdbblood', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bruce Lee', 'movies2&url=tmdbbrucelee', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cinderella', 'movies2&url=tmdbcinderella', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Crow', 'movies2&url=tmdbcrow', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cube', 'movies2&url=tmdbcube', 'bc.png', 'bc.png')
        self.addDirectoryItem('Dirty Dancing', 'movies2&url=tmdbdirtyd', 'bc.png', 'bc.png')
        self.addDirectoryItem('Dolphin Tale', 'movies2&url=tmdbdolphin', 'bc.png', 'bc.png')

        self.addDirectoryItem('Dragon Tattoo', 'movies2&url=tmdbdragon', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Fly', 'movies2&url=tmdbfly', 'bc.png', 'bc.png')
        self.addDirectoryItem('Fox and The Hound', 'movies2&url=tmdbfox', 'bc.png', 'bc.png')
        self.addDirectoryItem('Free Willy', 'movies2&url=tmdbfree', 'bc.png', 'bc.png')

        self.addDirectoryItem('Friday', 'movies2&url=tmdbfriday', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Godfather', 'movies2&url=tmdbgodfather', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Green Street Hooligans', 'movies2&url=tmdbgreen', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Grumpy Old Men', 'movies2&url=tmdbgrumpy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hannibal Lecter', 'movies2&url=tmdbhannibal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Homeward Bound', 'movies2&url=tmdbhomeward', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hunchback of Notre Dame', 'movies2&url=tmdbhunch', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Huntsman', 'movies2&url=tmdbhuntsman', 'bc.png', 'bc.png')
        self.addDirectoryItem('Infernal Affairs', 'movies2&url=tmdbinfernal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ip Man', 'movies2&url=tmdbipman', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Jaws', 'movies2&url=tmdbjaws', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Jungle Book', 'movies2&url=tmdbjungle', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Karate Kid', 'movies2&url=tmdbkarate', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Land Before Time', 'movies2&url=tmdblbt', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Lion King', 'movies2&url=tmdblion', 'bc.png', 'bc.png')

        self.addDirectoryItem('Lord of The Rings', 'movies2&url=tmdblord', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Mighty Ducks', 'movies2&url=tmdbmighty', 'bc.png', 'bc.png')
        self.addDirectoryItem('My Big Fat Greek Wedding', 'movies2&url=tmdbmbfgw', 'bc.png', 'bc.png')
        self.addDirectoryItem('Never Back Down', 'movies2&url=tmdbnever', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Never Ending Story', 'movies2&url=tmdbnes', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ninja', 'movies2&url=tmdbninja', 'bc.png', 'bc.png')
        self.addDirectoryItem('Nymphomaniac', 'movies2&url=tmdbnymph', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Once Were Warriors', 'movies2&url=tmdbonce', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Pocahontas', 'movies2&url=tmdbpoca', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Punisher', 'movies2&url=tmdbpunisher', 'bc.png', 'bc.png')
        self.addDirectoryItem('Red Cliff', 'movies2&url=tmdbredcliff', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rise of the Footsoldier', 'movies2&url=tmdbrise', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rocky', 'movies2&url=tmdbrocky', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Sandlot', 'movies2&url=tmdbsandlot', 'bc.png', 'bc.png')

        self.addDirectoryItem('Shanghai', 'movies2&url=tmdbshanghai', 'bc.png', 'bc.png')
        self.addDirectoryItem('Step Up', 'movies2&url=tmdbstepup', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Three Colors', 'movies2&url=tmdbthree', 'bc.png', 'bc.png')
        self.addDirectoryItem('Twilight', 'movies2&url=tmdbtwilight', 'bc.png', 'bc.png')
        self.addDirectoryItem('Undisputed', 'movies2&url=tmdbundisputed', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Woman in Black', 'movies2&url=tmdbwoman', 'bc.png', 'bc.png')
        self.addDirectoryItem('Young Guns', 'movies2&url=tmdbyoung', 'bc.png', 'bc.png')


        self.endDirectory()

    def family(self, lite=False):
        self.addDirectoryItem('3 Ninjas', 'movies2&url=tmdb3nin', 'bc.png', 'bc.png')
        self.addDirectoryItem('Alice In Wonderland', 'movies2&url=tmdbalice', 'bc.png', 'bc.png')
        self.addDirectoryItem('Babe', 'movies2&url=tmdbbabe', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bambi', 'movies2&url=tmdbbambi', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bean', 'movies2&url=tmdbbean', 'bc.png', 'bc.png')
        self.addDirectoryItem('Beauty and The Beast', 'movies2&url=tmdbbeauty', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cars', 'movies2&url=tmdbcars', 'bc.png', 'bc.png')
        self.addDirectoryItem('Casper', 'movies2&url=tmdbcasper', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cats & Dogs', 'movies2&url=tmdbcatsanddogs', 'bc.png', 'bc.png')
        self.addDirectoryItem('Charlottes Web', 'movies2&url=tmdbcharlottes', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Chronicles of Narnia', 'movies2&url=tmdbnarnia', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cinderella', 'movies2&url=tmdbcinderella', 'bc.png', 'bc.png')
        self.addDirectoryItem('Daddy Daycare', 'movies2&url=tmdbdaddy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Diary of A Wimpy Kid', 'movies2&url=tmdbdiary', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Doctor Dolittle', 'movies2&url=tmdbdolittle', 'bc.png', 'bc.png')

        self.addDirectoryItem('Dolphin Tale', 'movies2&url=tmdbdolphin', 'bc.png', 'bc.png')
        self.addDirectoryItem('Fantasia', 'movies2&url=tmdbfantasia', 'bc.png', 'bc.png')
        self.addDirectoryItem('FernGully', 'movies2&url=tmdbferngully', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Flintstones', 'movies2&url=tmdbflintstones', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Free Willy', 'movies2&url=tmdbfree', 'bc.png', 'bc.png')
        self.addDirectoryItem('Garfield', 'movies2&url=tmdbgarfield', 'bc.png', 'bc.png')
        self.addDirectoryItem('Happy Feet', 'movies2&url=tmdbhappy', 'bc.png', 'bc.png')

        self.addDirectoryItem('Harry Potter', 'movies2&url=tmdbharry', 'bc.png', 'bc.png')
        self.addDirectoryItem('Herbie', 'movies2&url=tmdbherbie', 'bc.png', 'bc.png')

        self.addDirectoryItem('Home Alone', 'movies2&url=tmdbhome', 'bc.png', 'bc.png')

        self.addDirectoryItem('Honey I Shrunk The Kids', 'movies2&url=tmdbhoney', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hotel Transylvania', 'movies2&url=tmdbhotel', 'bc.png', 'bc.png')

        self.addDirectoryItem('Hunchback of Notre Dame', 'movies2&url=tmdbhunch', 'bc.png', 'bc.png')

        self.addDirectoryItem('Journey', 'movies2&url=tmdbjourney', 'bc.png', 'bc.png')		
        self.addDirectoryItem('The Jungle Book', 'movies2&url=tmdbjungle', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Karate Kid', 'movies2&url=tmdbkarate', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lego Star Wars', 'movies2&url=tmdblegostar', 'bc.png', 'bc.png')
        self.addDirectoryItem('Like Mike', 'movies2&url=tmdblikemike', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Little Mermaid', 'movies2&url=tmdbmermaid', 'bc.png', 'bc.png')	

        self.addDirectoryItem('Men in Black', 'movies2&url=tmdbmib', 'bc.png', 'bc.png')

        self.addDirectoryItem('The Mighty Ducks', 'movies2&url=tmdbmighty', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mulan', 'movies2&url=tmdbmulan', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Muppets', 'movies2&url=tmdbmuppets', 'bc.png', 'bc.png')

        self.addDirectoryItem('National Treasure', 'movies2&url=tmdbnational', 'bc.png', 'bc.png')		

        self.addDirectoryItem('The Never Ending Story', 'movies2&url=tmdbnes', 'bc.png', 'bc.png')
        self.addDirectoryItem('Night At The Museum', 'movies2&url=tmdbnatm', 'bc.png', 'bc.png')
        self.addDirectoryItem('Nims Island', 'movies2&url=tmdbnims', 'bc.png', 'bc.png')		

        self.addDirectoryItem('Percy Jackson', 'movies2&url=tmdbpercy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Peter Pan', 'movies2&url=tmdbpeter', 'bc.png', 'bc.png')
        self.addDirectoryItem('Power Rangers', 'movies2&url=tmdbpowerrangers', 'bc.png', 'bc.png')

        self.addDirectoryItem('Problem Child', 'movies2&url=tmdbproblem', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Reef', 'movies2&url=tmdbreef', 'bc.png', 'bc.png')
	
        self.addDirectoryItem('Sammys Adventures', 'movies2&url=tmdbsammy', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Sandlot', 'movies2&url=tmdbsandlot', 'bc.png', 'bc.png')
	
        self.addDirectoryItem('Short Circuit', 'movies2&url=tmdbshort', 'bc.png', 'bc.png')
        self.addDirectoryItem('Stuart Little', 'movies2&url=tmdbstuart', 'bc.png', 'bc.png')
        self.addDirectoryItem('Tarzan', 'movies2&url=tmdbtarzan', 'bc.png', 'bc.png')
        self.addDirectoryItem('Thomas & Friends', 'movies2&url=tmdbthomas', 'bc.png', 'bc.png')

        self.addDirectoryItem('Tinker Bell', 'movies2&url=tmdbtinker', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Tooth Fairy', 'movies2&url=tmdbtooth', 'bc.png', 'bc.png')
		
	
        self.endDirectory()
		
    def fantasy(self, lite=False):
        self.addDirectoryItem('300', 'movies2&url=tmdb300', 'bc.png', 'bc.png')
        self.addDirectoryItem('A Haunted House', 'movies2&url=tmdbhaunted', 'bc.png', 'bc.png')
        self.addDirectoryItem('Adams Family', 'movies2&url=tmdbadams', 'bc.png', 'bc.png')
        self.addDirectoryItem('Beauty and The Beast', 'movies2&url=tmdbbeauty', 'bc.png', 'bc.png')
        self.addDirectoryItem('Casper', 'movies2&url=tmdbcasper', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Chronicles of Narnia', 'movies2&url=tmdbnarnia', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cinderella', 'movies2&url=tmdbcinderella', 'bc.png', 'bc.png')
        self.addDirectoryItem('Conan', 'movies2&url=tmdbconan', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Crow', 'movies2&url=tmdbcrow', 'bc.png', 'bc.png')
        self.addDirectoryItem('Doctor Dolittle', 'movies2&url=tmdbdolittle', 'dolittle.jpg', 'bc.png')
        self.addDirectoryItem('Fantasia', 'movies2&url=tmdbfantasia', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Flintstones', 'movies2&url=tmdbflintstones', 'bc.png', 'bc.png')		

        self.addDirectoryItem('Ghost Rider', 'movies2&url=tmdbghost', 'bc.png', 'bc.png')
        self.addDirectoryItem('Gremlins', 'movies2&url=tmdbgremlins', 'bc.png', 'bc.png')
        self.addDirectoryItem('Harry Potter', 'movies2&url=tmdbharry', 'bc.png', 'bc.png')
        self.addDirectoryItem('Highlander', 'movies2&url=tmdbhighlander', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Hobbit', 'movies2&url=tmdbhobbit', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Indiana Jones', 'movies2&url=tmdbindiana', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lego Star Wars', 'movies2&url=tmdblegostar', 'bc.png', 'bc.png')
        self.addDirectoryItem('Like Mike', 'movies2&url=tmdblikemike', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Little Mermaid', 'movies2&url=tmdbmermaid', 'bc.png', 'bc.png')	

        self.addDirectoryItem('Lord of The Rings', 'movies2&url=tmdblord', 'bc.png', 'bc.png')
        self.addDirectoryItem('Monty Python', 'movies2&url=tmdbmonty', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Mummy', 'movies2&url=tmdbmummy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Percy Jackson', 'movies2&url=tmdbpercy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Peter Pan', 'movies2&url=tmdbpeter', 'bc.png', 'bc.png')

        self.addDirectoryItem('Pirates of The Caribbean', 'movies2&url=tmdbpirates', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Poltergeist', 'movies2&url=tmdbpolter', 'bc.png', 'bc.png')
        self.addDirectoryItem('Star Wars', 'movies2&url=tmdbstarwars', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ted', 'movies2&url=tmdbted', 'bc.png', 'bc.png')
        self.addDirectoryItem('Teen Wolf', 'movies2&url=tmdbteen', 'bc.png', 'bc.png')
        self.addDirectoryItem('Titans', 'movies2&url=tmdbtitans', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Tooth Fairy', 'movies2&url=tmdbtooth', 'bc.png', 'bc.png')

        self.addDirectoryItem('Twilight', 'movies2&url=tmdbtwilight', 'bc.png', 'bc.png')
        self.addDirectoryItem('Underworld', 'movies2&url=tmdbunderworld', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Woman in Black', 'movies2&url=tmdbwoman', 'bc.png', 'bc.png')


        self.endDirectory()
		
    def horror(self, lite=False):
        self.addDirectoryItem('28 Days Later', 'movies2&url=tmdb28days', 'bc.png', 'bc.png')
        self.addDirectoryItem('A Nightmare on Elm Street', 'movies2&url=tmdbelmst', 'bc.png', 'bc.png')
        self.addDirectoryItem('Alien', 'movies2&url=tmdbalien', 'bc.png', 'bc.png')
        self.addDirectoryItem('AVP', 'movies2&url=tmdbavp', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Childs Play', 'movies2&url=tmdbchilds', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Conjuring', 'movies2&url=tmdbconjuring', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Evil Dead', 'movies2&url=tmdbevil', 'bc.png', 'bc.png')
        self.addDirectoryItem('Exorcist', 'movies2&url=tmdbexorcist', 'bc.png', 'bc.png')
        self.addDirectoryItem('Final Destination', 'movies2&url=tmdbfinal', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Fly', 'movies2&url=tmdbfly', 'bc.png', 'bc.png')
        self.addDirectoryItem('Friday The 13th', 'movies2&url=tmdbfriday13', 'bc.png', 'bc.png')
        self.addDirectoryItem('Gremlins', 'movies2&url=tmdbgremlins', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Grudge', 'movies2&url=tmdbgrudge', 'bc.png', 'bc.png')
        self.addDirectoryItem('Halloween', 'movies2&url=tmdbhalloween', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hellraiser', 'movies2&url=tmdbhell', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Hills Have Eyes', 'movies2&url=tmdbhills', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hollow Man', 'movies2&url=tmdbhollow', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hostel', 'movies2&url=tmdbhostel', 'bc.png', 'bc.png')		
        self.addDirectoryItem('The Human Centipede', 'movies2&url=tmdbhuman', 'bc.png', 'bc.png')
        self.addDirectoryItem('Insidious', 'movies2&url=tmdbinsidious', 'bc.png', 'bc.png')
        self.addDirectoryItem('Last Summer', 'movies2&url=tmdblast', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Omen', 'movies2&url=tmdbomen', 'bc.png', 'bc.png')
        self.addDirectoryItem('Paranormal Activity', 'movies2&url=tmdbparanormal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Poltergeist', 'movies2&url=tmdbpolter', 'bc.png', 'bc.png')
        self.addDirectoryItem('Psycho', 'movies2&url=tmdbpsycho', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Purge', 'movies2&url=tmdbpurge', 'bc.png', 'bc.png')
        self.addDirectoryItem('Quarantine', 'movies2&url=tmdbquarantine', 'bc.png', 'bc.png')
        self.addDirectoryItem('Resident Evil', 'movies2&url=tmdbresident', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Ring', 'movies2&url=tmdbring', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Saw', 'movies2&url=tmdbsaw', 'bc.png', 'bc.png')
        self.addDirectoryItem('Scream', 'movies2&url=tmdbscream', 'bc.png', 'bc.png')
        self.addDirectoryItem('Texas Chainsaw Massacre', 'movies2&url=tmdbtexas', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Tremors', 'movies2&url=tmdbtremors', 'bc.png', 'bc.png')
        self.addDirectoryItem('VHS', 'movies2&url=tmdbvhs', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Woman in Black', 'movies2&url=tmdbwoman', 'bc.png', 'bc.png')
        self.addDirectoryItem('Wrong Turn', 'movies2&url=tmdbwrong', 'bc.png', 'bc.png')		


        self.endDirectory()
		
    def mystery(self, lite=False):
        self.addDirectoryItem('The Conjuring', 'movies2&url=tmdbconjuring', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Cube', 'movies2&url=tmdbcube', 'bc.png', 'bc.png')
        self.addDirectoryItem('Divergent', 'movies2&url=tmdbdivergent', 'bc.png', 'bc.png')
        self.addDirectoryItem('Dragon Tattoo', 'movies2&url=tmdbdragon', 'bc.png', 'bc.png')
        self.addDirectoryItem('Friday The 13th', 'movies2&url=tmdbfriday13', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Grudge', 'movies2&url=tmdbgrudge', 'bc.png', 'bc.png')
        self.addDirectoryItem('Infernal Affairs', 'movies2&url=tmdbinfernal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Insidious', 'movies2&url=tmdbinsidious', 'bc.png', 'bc.png')
        self.addDirectoryItem('Last Summer', 'movies2&url=tmdblast', 'bc.png', 'bc.png')
        self.addDirectoryItem('Now You See Me', 'movies2&url=tmdbnysm', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Paranormal Activity', 'movies2&url=tmdbparanormal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Psycho', 'movies2&url=tmdbpsycho', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Ring', 'movies2&url=tmdbring', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Saw', 'movies2&url=tmdbsaw', 'bc.png', 'bc.png')
        self.addDirectoryItem('Scream', 'movies2&url=tmdbscream', 'bc.png', 'bc.png')
        self.addDirectoryItem('Shanghai', 'movies2&url=tmdbshanghai', 'bc.png', 'bc.png')
        self.addDirectoryItem('Three Colors', 'movies2&url=tmdbthree', 'bc.png', 'bc.png')


        self.endDirectory()
		
    def romance(self, lite=False):
        self.addDirectoryItem('American Ninja', 'movies2&url=tmdbamninja', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Before', 'movies2&url=tmdbbefore', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bridget Jones', 'movies2&url=tmdbbridget', 'bc.png', 'bc.png')
        self.addDirectoryItem('Dirty Dancing', 'movies2&url=tmdbdirtyd', 'bc.png', 'bc.png')
        self.addDirectoryItem('Grumpy Old Men', 'movies2&url=tmdbgrumpy', 'bc.png', 'bc.png')
        self.addDirectoryItem('Legally Blonde', 'movies2&url=tmdblegally', 'bc.png', 'bc.png')
        self.addDirectoryItem('Meet The Parents', 'movies2&url=tmdbmeet', 'bc.png', 'bc.png')
        self.addDirectoryItem('My Big Fat Greek Wedding', 'movies2&url=tmdbmbfgw', 'bc.png', 'bc.png')
        self.addDirectoryItem('Shanghai', 'movies2&url=tmdbshanghai', 'bc.png', 'bc.png')
        self.addDirectoryItem('Think Like a Man', 'movies2&url=tmdbthink', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Three Colors', 'movies2&url=tmdbthree', 'bc.png', 'bc.png')
        self.addDirectoryItem('Twilight', 'movies2&url=tmdbtwilight', 'bc.png', 'bc.png')


        self.endDirectory()
		
    def scifi(self, lite=False):
        self.addDirectoryItem('28 Days Later', 'movies2&url=tmdb28days', 'bc.png', 'bc.png')
        self.addDirectoryItem('Alien', 'movies2&url=tmdbalien', 'bc.png', 'bc.png')
        self.addDirectoryItem('Avengers', 'movies2&url=tmdbavengers', 'bc.png', 'bc.png')		
        self.addDirectoryItem('AVP', 'movies2&url=tmdbavp', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Back To The Future', 'movies2&url=tmdbback', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Butterfly Effect', 'movies2&url=tmdbbutterfly', 'bc.png', 'bc.png')
        self.addDirectoryItem('Captain America', 'movies2&url=tmdbcaptain', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cocoon', 'movies2&url=tmdbcocoon', 'bc.png', 'bc.png')
        self.addDirectoryItem('Cube', 'movies2&url=tmdbcube', 'bc.png', 'bc.png')
        self.addDirectoryItem('Divergent', 'movies2&url=tmdbdivergent', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Fly', 'movies2&url=tmdbfly', 'bc.png', 'bc.png')
        self.addDirectoryItem('G.I. Joe', 'movies2&url=tmdbgi', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hollow Man', 'movies2&url=tmdbhollow', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hot Tub Time Machine', 'movies2&url=tmdbhotub', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hunger Games', 'movies2&url=tmdbhunger', 'bc.png', 'bc.png')
        self.addDirectoryItem('Independence Day', 'movies2&url=tmdbindependence', 'bc.png', 'bc.png')
        self.addDirectoryItem('Judge Dredd', 'movies2&url=tmdbdredd', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Jurassic Park', 'movies2&url=tmdbjurassic', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mad Max', 'movies2&url=tmdbmadmax', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Matrix', 'movies2&url=tmdbmatrix', 'bc.png', 'bc.png')
        self.addDirectoryItem('Maze Runner', 'movies2&url=tmdbmaze', 'bc.png', 'bc.png')
        self.addDirectoryItem('Planet of The Apes', 'movies2&url=tmdbplanet', 'bc.png', 'bc.png')
        self.addDirectoryItem('Predator', 'movies2&url=tmdbpredator', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Purge', 'movies2&url=tmdbpurge', 'bc.png', 'bc.png')
        self.addDirectoryItem('Quarantine', 'movies2&url=tmdbquarantine', 'bc.png', 'bc.png')
        self.addDirectoryItem('Resident Evil', 'movies2&url=tmdbresident', 'bc.png', 'bc.png')
        self.addDirectoryItem('Riddick', 'movies2&url=tmdbriddick', 'bc.png', 'bc.png')
        self.addDirectoryItem('Robocop', 'movies2&url=tmdbrobocop', 'bc.png', 'bc.png')
        self.addDirectoryItem('Short Circuit', 'movies2&url=tmdbshort', 'bc.png', 'bc.png')
        self.addDirectoryItem('Star Trek', 'movies2&url=tmdbstartrek', 'bc.png', 'bc.png')
        self.addDirectoryItem('Starship Troopers', 'movies2&url=tmdbstarship', 'bc.png', 'bc.png')
        self.addDirectoryItem('Terminator', 'movies2&url=tmdbterminator', 'bc.png', 'bc.png')
        self.addDirectoryItem('Transformers', 'movies2&url=tmdbtransformers', 'bc.png', 'bc.png')
        self.addDirectoryItem('Tron', 'movies2&url=tmdbtron', 'bc.png', 'bc.png')
        self.addDirectoryItem('Universal Soldier', 'movies2&url=tmdbuniversal', 'bc.png', 'bc.png')		


        self.endDirectory()
		
    def thriller(self, lite=False):
        self.addDirectoryItem('12 Rounds', 'movies2&url=tmdbrounds', 'bc.png', 'bc.png')
        self.addDirectoryItem('Boondock Saints', 'movies2&url=tmdbboon', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Bourne', 'movies2&url=tmdbbourne', 'bc.png', 'bc.png')		
        self.addDirectoryItem('The Butterfly Effect', 'movies2&url=tmdbbutterfly', 'bc.png', 'bc.png')
        self.addDirectoryItem('Childs Play', 'movies2&url=tmdbchilds', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Conjuring', 'movies2&url=tmdbconjuring', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Crank', 'movies2&url=tmdbcrank', 'crank.jpg', 'bc.png')
        self.addDirectoryItem('Die Hard', 'movies2&url=tmdbdie', 'die.jpg', 'bc.png')
        self.addDirectoryItem('Dirty Harry', 'movies2&url=tmdbdirtyh', 'bc.png', 'bc.png')
        self.addDirectoryItem('Fast and Furious', 'movies2&url=tmdbfurious', 'bc.png', 'bc.png')
        self.addDirectoryItem('Friday The 13th', 'movies2&url=tmdbfriday13', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ghost Rider', 'movies2&url=tmdbghost', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Grudge', 'movies2&url=tmdbgrudge', 'bc.png', 'bc.png')
        self.addDirectoryItem('Halloween', 'movies2&url=tmdbhalloween', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hannibal Lecter', 'movies2&url=tmdbhannibal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hellraiser', 'movies2&url=tmdbhell', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Hills Have Eyes', 'movies2&url=tmdbhills', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hunger Games', 'movies2&url=tmdbhunger', 'bc.png', 'bc.png')
        self.addDirectoryItem('Insidious', 'movies2&url=tmdbinsidious', 'bc.png', 'bc.png')
        self.addDirectoryItem('James Bond', 'movies2&url=tmdbjames', 'bc.png', 'bc.png')
        self.addDirectoryItem('Jaws', 'movies2&url=tmdbjaws', 'bc.png', 'bc.png')
        self.addDirectoryItem('Jurassic Park', 'movies2&url=tmdbjurassic', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kickboxer', 'movies2&url=tmdbkickboxer', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kill Bill', 'movies2&url=tmdbkill', 'bc.png', 'bc.png')
        self.addDirectoryItem('Last Summer', 'movies2&url=tmdblast', 'bc.png', 'bc.png')
        self.addDirectoryItem('Lethal Weapon', 'movies2&url=tmdblethal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Machete', 'movies2&url=tmdbmachete', 'bc.png', 'bc.png')
        self.addDirectoryItem('Maze Runner', 'movies2&url=tmdbmaze', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Mechanic', 'movies2&url=tmdbmechanic', 'bc.png', 'bc.png')
        self.addDirectoryItem('Mission Impossible', 'movies2&url=tmdbmission', 'bc.png', 'bc.png')
        self.addDirectoryItem('Now You See Me', 'movies2&url=tmdbnysm', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Oceans', 'movies2&url=tmdboceans', 'bc.png', 'bc.png')
        self.addDirectoryItem('Olympus Has Fallen', 'movies2&url=tmdbolympus', 'bc.png', 'bc.png')
        self.addDirectoryItem('Ong Bak', 'movies2&url=tmdbong', 'bc.png', 'bc.png')
        self.addDirectoryItem('Paranormal Activity', 'movies2&url=tmdbparanormal', 'bc.png', 'bc.png')
        self.addDirectoryItem('Poltergeist', 'movies2&url=tmdbpolter', 'bc.png', 'bc.png')
        self.addDirectoryItem('Predator', 'movies2&url=tmdbpredator', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Protector', 'movies2&url=tmdbprotector', 'bc.png', 'bc.png')
        self.addDirectoryItem('Psycho', 'movies2&url=tmdbpsycho', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Purge', 'movies2&url=tmdbpurge', 'bc.png', 'bc.png')
        self.addDirectoryItem('Quarantine', 'movies2&url=tmdbquarantine', 'bc.png', 'bc.png')
        self.addDirectoryItem('The Raid', 'movies2&url=tmdbraid', 'bc.png', 'bc.png')
        self.addDirectoryItem('Rambo', 'movies2&url=tmdbrambo', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Saw', 'movies2&url=tmdbsaw', 'bc.png', 'bc.png')
        self.addDirectoryItem('Sin City', 'movies2&url=tmdbsin', 'bc.png', 'bc.png')
        self.addDirectoryItem('Taken', 'movies2&url=tmdbtaken', 'bc.png', 'bc.png')		
        self.addDirectoryItem('Transporter', 'movies2&url=tmdbtransporter', 'bc.png', 'bc.png')
        self.addDirectoryItem('Under Siege', 'movies2&url=tmdbunder', 'bc.png', 'bc.png')
        self.addDirectoryItem('Underworld', 'movies2&url=tmdbunderworld', 'bc.png', 'bc.png')
        self.addDirectoryItem('Universal Soldier', 'movies2&url=tmdbuniversal', 'bc.png', 'bc.png')		
        self.addDirectoryItem('VHS', 'movies2&url=tmdbvhs', 'bc.png', 'bc.png')
        self.addDirectoryItem('xXx', 'movies2&url=tmdbxxx', 'bc.png', 'bc.png')		
        

        self.endDirectory()



    def Clts(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]More To Come[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('canada loves tv shows', 'tvshows&url=tmdbClts', 'bc.png', 'bc.png')
        self.addDirectoryItem('Canada loves movies', 'movies2&url=tmdbClm', 'bc.png', 'bc.png')


        self.endDirectory()

    def Urt(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('Users requests tv ', 'tvshows&url=tmdbUrt', 'bc.png', 'bc.png')
        self.addDirectoryItem('Users requests movies', 'movies2&url=tmdbUrm', 'bc.png', 'bc.png')



        self.endDirectory()


    def Tts(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('Toddler tv shows', 'tvshows&url=tmdbTts', 'bc.png', 'bc.png')
        self.addDirectoryItem('Toddler movies', 'movies2&url=tmdbTm', 'bc.png', 'bc.png')



        self.endDirectory()

    def Kzt(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kids zone tv', 'tvshows&url=tmdbKzt', 'bc.png', 'bc.png')
        self.addDirectoryItem('Kids Zone Movies', 'movies2&url=tmdbKzm', 'bc.png', 'bc.png')



        self.endDirectory()

    def Bftv(self, lite=False):
        self.addDirectoryItem('bone crushers fav tv shows', 'tvshows&url=tmdbBft', 'bc.png', 'bc.png')
        self.addDirectoryItem('bone crushers fav', 'movies2&url=tmdbbcfm', 'bc.png', 'bc.png')



        self.endDirectory()
		
    def Docstv(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('documentary tv', 'tvshows&url=tmdbDocstv', 'bc.png', 'bc.png')
        self.addDirectoryItem('documentary movies', 'movies2&url=tmdbDocs', 'bc.png', 'bc.png')



        self.endDirectory()
		
    def at(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('anime tv', 'tvshows&url=tmdbat', 'bc.png', 'bc.png')
        self.addDirectoryItem('Anime movies', 'movies2&url=tmdbam', 'bc.png', 'bc.png')


        self.endDirectory()
		
    def Tl(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('Tv legends', 'tvshows&url=tmdbTl', 'bc.png', 'bc.png')
        self.addDirectoryItem('Movie legends ', 'movies2&url=tmdbMl', 'bc.png', 'bc.png')



        self.endDirectory()
		
    def Sfts(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('Sci fi tv shows', 'tvshowstvshows&url=tmdbSfts', 'bc.png', 'bc.png')
        self.addDirectoryItem('Sci fi movies', 'movies2&url=tmdbSfim', 'bc.png', 'bc.png')


        self.endDirectory()

    def Paratv(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem(' paranormal tv', 'tvshows&url=tmdbParamtv', 'bc.png', 'bc.png')
        self.addDirectoryItem('paranormal Movies', 'movies2&url=tmdbParam', 'bc.png', 'bc.png')



        self.endDirectory()

    def Kfuleg(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('Bruce Lee', 'movies2&url=tmdbbrucelee', 'bc.png', 'bc.png')
        self.addDirectoryItem('Jet Li', 'movies2&url=tmdbjli', 'bc.png', 'bc.png')
        self.addDirectoryItem('Chuck Norris', 'movies2&url=tmdbchuck', 'bc.png', 'bc.png')
        self.addDirectoryItem('Jackie Chan', 'movies2&url=tmdbchan', 'bc.png', 'bc.png')
        self.addDirectoryItem('Jean Claude Van Damme', 'movies2&url=tmdbtmdbdam', 'bc.png', 'bc.png')
        self.addDirectoryItem('Steven Seagal', 'movies2&url=tmdbsegal', 'bc.png', 'bc.png')


        self.endDirectory()


		
    def Br(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('B rated', 'movies2&url=tmdbBr', 'bc.png', 'bc.png')


        self.endDirectory()
		
    def Mh(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('Morbid minded movies', 'movies2&url=tmdbMh', 'bc.png', 'bc.png')



        self.endDirectory()
		

    def ldmov(self, lite=False):
        self.addDirectoryItem('LockDown movies', 'movies2&url=tmdbldmov', 'lock.png', 'bc.png')
        self.addDirectoryItem('LockDown Tv Shows', 'tvshows&url=tmdbldtv', 'lock.png', 'bc.png')

        self.endDirectory()

    def Enforcermo(self, lite=False):
        self.addDirectoryItem('Enforcer movies', 'movies2&url=tmdbenmov', 'ENFORCER.png', 'bc.png')
        self.addDirectoryItem('Enforcer Tv Shows', 'tvshows&url=tmdbentv', 'ENFORCER.png', 'bc.png')

        self.endDirectory()

    def warhammermo(self, lite=False):
        self.addDirectoryItem('Warhammer movies', 'movies2&url=tmdbwarm', 'WAR.png', 'bc.png')
        self.addDirectoryItem('Warhammer Tv Shows', 'tvshows&url=tmdbwartv', 'WAR.png', 'bc.png')

        self.endDirectory()


    def katsmo(self, lite=False):
        self.addDirectoryItem('Kastastrophy movies', 'movies2&url=tmdbkatsmov', 'kat.png', 'bc.png')
        self.addDirectoryItem('Kastastrophy Tv Shows', 'tvshows&url=tmdbkatstv', 'kat.png', 'bc.png')

        self.endDirectory()

    def stalkermo(self, lite=False):
        self.addDirectoryItem('Stalkers movies', 'movies2&url=tmdbstalkermov', 'stalker.png', 'bc.png')
        self.addDirectoryItem('Stalkers Tv Shows', 'tvshows&url=tmdbstalkertv', 'stalker.png', 'bc.png')

        self.endDirectory()
    def Swm(self, lite=False):
        self.addDirectoryItem('[COLOR yellow]users requets accepted[/COLOR]', '', 'bc.png', 'bc.png')
        self.addDirectoryItem('Hockey movies', 'movies2&url=tmdbSwm', 'bc.png', 'bc.png')
        self.addDirectoryItem('Baseball movies', 'movies2&url=tmdbBaseball', 'bc.png', 'bc.png')  
        self.addDirectoryItem('Soccer movies', 'movies2&url=tmdbSoccer', 'bc.png', 'bc.png')
        self.addDirectoryItem('Football movies', 'movies2&url=tmdbFootball', 'bc.png', 'bc.png')
        self.addDirectoryItem('Basketball movies', 'movies2&url=tmdbBasketball', 'bc.png', 'bc.png')
        self.endDirectory()

    def western(self, lite=False):
        self.addDirectoryItem('The Man With No Name', 'movies2&url=tmdbnoman', 'bc.png', 'bc.png')		


        self.endDirectory()



        
        
		
    def tools(self):
        self.addDirectoryItem('[B]URL RESOLVER[/B]: Settings', 'Darknessresolversettings', 'bc.png', 'DefaultAddonProgram.png')

        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Accounts', 'openSettings&query=2.0', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=3.0', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=5.0', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Downloads', 'openSettings&query=4.0', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Watchlist', 'openSettings&query=6.0', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Views', 'viewsNavigator', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Providers', 'clearSources', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Cache', 'clearCache', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]BACKUP[/B]: Watchlist', 'backupwatchlist', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]RESTORE[/B]: Watchlist', 'restorewatchlist', 'bc.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Progress Database', 'clearProgress', 'bc.png', 'DefaultAddonProgram.png')

        self.endDirectory()


    def downloads(self):
        movie_downloads = control.setting('movie.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'bc.png', 'bc.png', isAction=False)
        self.endDirectory()



    def views(self):
        try:
            control.idle()

            items = [ (control.lang(32001).encode('utf-8'), 'movies'), (control.lang(32002).encode('utf-8'), 'tvshows'), (control.lang(32054).encode('utf-8'), 'seasons'), (control.lang(32038).encode('utf-8'), 'episodes') ]

            select = control.selectDialog([i[0] for i in items], control.lang(32049).encode('utf-8'))

            if select == -1: return

            content = items[select][1]

            title = control.lang(32059).encode('utf-8')
            url = '%s?action=addView&content=%s' % (sys.argv[0], content)

            poster, banner, fanart = control.addonPoster(), control.addonBanner(), control.addonFanart()

            item = control.item(label=title)
            item.setInfo(type='Video', infoLabels = {'title': title})
            item.setArt({'icon': poster, 'thumb': poster, 'poster': poster, 'tvshow.poster': poster, 'season.poster': poster, 'banner': banner, 'tvshow.banner': banner, 'season.banner': banner})
            item.setProperty('Fanart_Image', fanart)

            control.addItem(handle=int(sys.argv[1]), url=url, listitem=item, isFolder=False)
            control.content(int(sys.argv[1]), content)
            control.directory(int(sys.argv[1]), cacheToDisc=True)

            from resources.lib.modules import cache
            views.setView(content, {})
        except:
            return


    def accountCheck(self):
        if traktCredentials == False and imdbCredentials == False:
            control.idle()
            control.infoDialog(control.lang(32042).encode('utf-8'), sound=True, icon='WARNING')
            sys.exit()


    def clearCache(self):
        control.idle()
        yes = control.yesnoDialog(control.lang(32056).encode('utf-8'), '', '')
        if not yes: return
        from resources.lib.modules import cache
        cache.clear()
        control.infoDialog(control.lang(32057).encode('utf-8'), sound=True, icon='INFO')


    def addDirectoryItem(self, name, query, thumb, icon, queue=False, isAction=True, isFolder=True):
        try: name = control.lang(name).encode('utf-8')
        except: pass
        url = '%s?action=%s' % (sysaddon, query) if isAction == True else query
        thumb = os.path.join(artPath, thumb) if not artPath == None else icon
        cm = []
        if queue == True: cm.append((queueMenu, 'RunPlugin(%s?action=queueItem)' % sysaddon))
        item = control.item(label=name)
        item.addContextMenuItems(cm)
        item.setArt({'icon': thumb, 'thumb': thumb})
        if not addonFanart == None: item.setProperty('Fanart_Image', addonFanart)
        control.addItem(handle=syshandle, url=url, listitem=item, isFolder=isFolder)


    def endDirectory(self):
        control.directory(syshandle, cacheToDisc=True)


