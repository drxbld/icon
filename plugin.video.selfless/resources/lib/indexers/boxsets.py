# -*- coding: utf-8 -*-
################################################################################
# |                                                                            #
# |    Selfless Live                                                           #
# |    Copyright (C) 2018 Kodi Ghost                                           #
# |                                                                            #
# |    This program is free software: you can redistribute it and/or modify    #
# |    it under the terms of the GNU General Public License as published by    #
# |    the Free Software Foundation, either version 3 of the License, or       #
# |    (at your option) any later version.                                     #
# |                                                                            #
# |    This program is distributed in the hope that it will be useful,         #
# |    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
# |    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
# |    GNU General Public License for more details.                            #
# |                                                                            #
################################################################################
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
        if inprogress_db == 'true': self.addDirectoryItem("In Progress", 'movieProgress', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Action', 'actionNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Adventure', 'adventureNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Animation', 'animationNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Comedy', 'comedyNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Crime', 'crimeNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Drama', 'dramaNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Family', 'familyNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Fantasy', 'fantasyNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Horror', 'horrorNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mystery', 'mysteryNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Romance', 'romanceNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Sci-Fi', 'scifiNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Thriller', 'thrillerNavigator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem(32010, 'movieSearch', 'search.png', 'search.png')
        downloads = True if control.setting('downloads') == 'true' and (len(control.listDir(control.setting('movie.download.path'))[0]) > 0) else False
        if downloads == True: self.addDirectoryItem(32009, 'downloadNavigator', 'downloads.png', 'DefaultFolder.png')

        self.endDirectory()

	
    def action(self, lite=False):
        self.addDirectoryItem('12 Rounds', 'boxinfo&url=tmdbrounds', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('3 Ninjas', 'boxinfo&url=tmdb3nin', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('300', 'boxinfo&url=tmdb300', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Agent Cody Banks', 'boxinfo&url=tmdbagent', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('American Ninja', 'boxinfo&url=tmdbamninja', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Avengers', 'boxinfo&url=tmdbavengers', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('AVP', 'boxinfo&url=tmdbavp', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Bad Ass', 'boxinfo&url=tmdbbadass', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bad Boys', 'boxinfo&url=tmdbbb', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Batman', 'boxinfo&url=tmdbbatman', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Best Of The Best', 'boxinfo&url=tmdbbob', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Beverly Hills Cop', 'boxinfo&url=tmdbbeverly', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Big Mommas House', 'boxinfo&url=tmdbbig', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bloodsport', 'boxinfo&url=tmdbblood', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Blues Brother', 'boxinfo&url=tmdbblues', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Boondock Saints', 'boxinfo&url=tmdbboon', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Bourne', 'boxinfo&url=tmdbbourne', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Bruce Lee', 'boxinfo&url=tmdbbrucelee', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Captain America', 'boxinfo&url=tmdbcaptain', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cats & Dogs', 'boxinfo&url=tmdbcatsanddogs', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Crank', 'boxinfo&url=tmdbcrank', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Crow', 'boxinfo&url=tmdbcrow', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Die Hard', 'boxinfo&url=tmdbdie', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Dirty Harry', 'boxinfo&url=tmdbdirtyh', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Fast and Furious', 'boxinfo&url=tmdbfurious', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('G.I. Joe', 'boxinfo&url=tmdbgi', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ghost Rider', 'boxinfo&url=tmdbghost', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ghostbusters', 'boxinfo&url=tmdbghostbusters', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Highlander', 'boxinfo&url=tmdbhighlander', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hollow Man', 'boxinfo&url=tmdbhollow', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hoodwinked!', 'boxinfo&url=tmdbhoodwink', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Hot Shots', 'boxinfo&url=tmdbhot', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('How To Train Your Dragon', 'boxinfo&url=tmdbhow', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Huntsman', 'boxinfo&url=tmdbhuntsman', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Independence Day', 'boxinfo&url=tmdbindependence', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Indiana Jones', 'boxinfo&url=tmdbindiana', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Inspector Gadget', 'boxinfo&url=tmdbinspector', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Ip Man', 'boxinfo&url=tmdbipman', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Iron Fists', 'boxinfo&url=tmdbironfists', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Jackass', 'boxinfo&url=tmdbjackass', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('James Bond', 'boxinfo&url=tmdbjames', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Johnny English', 'boxinfo&url=tmdbjohnny', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Journey', 'boxinfo&url=tmdbjourney', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Judge Dredd', 'boxinfo&url=tmdbdredd', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Jump Street', 'boxinfo&url=tmdbjump', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Justice League', 'boxinfo&url=tmdbjusticeleague', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Karate Kid', 'boxinfo&url=tmdbkarate', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kick-Ass', 'boxinfo&url=tmdbkick', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kickboxer', 'boxinfo&url=tmdbkickboxer', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kill Bill', 'boxinfo&url=tmdbkill', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kung Fu Panda', 'boxinfo&url=tmdbkung', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Lethal Weapon', 'boxinfo&url=tmdblethal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Machete', 'boxinfo&url=tmdbmachete', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mad Max', 'boxinfo&url=tmdbmadmax', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Matrix', 'boxinfo&url=tmdbmatrix', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Maze Runner', 'boxinfo&url=tmdbmaze', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Mechanic', 'boxinfo&url=tmdbmechanic', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mission Impossible', 'boxinfo&url=tmdbmission', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Mummy', 'boxinfo&url=tmdbmummy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('National Treasure', 'boxinfo&url=tmdbnational', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Never Back Down', 'boxinfo&url=tmdbnever', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ninja', 'boxinfo&url=tmdbninja', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Olympus Has Fallen', 'boxinfo&url=tmdbolympus', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ong Bak', 'boxinfo&url=tmdbong', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Pirates of The Caribbean', 'boxinfo&url=tmdbpirates', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Power Rangers', 'boxinfo&url=tmdbpowerrangers', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Predator', 'boxinfo&url=tmdbpredator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Protector', 'boxinfo&url=tmdbprotector', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Punisher', 'boxinfo&url=tmdbpunisher', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Raid', 'boxinfo&url=tmdbraid', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rambo', 'boxinfo&url=tmdbrambo', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('R.E.D.', 'boxinfo&url=tmdbred', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Red Cliff', 'boxinfo&url=tmdbredcliff', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Resident Evil', 'boxinfo&url=tmdbresident', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Riddick', 'boxinfo&url=tmdbriddick', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ride Along', 'boxinfo&url=tmdbride', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Robocop', 'boxinfo&url=tmdbrobocop', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Romancing The Stone', 'boxinfo&url=tmdbromancing', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rush Hour', 'boxinfo&url=tmdbrush', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Sherlock Holmes', 'boxinfo&url=tmdbsherlock', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Smokey and The Bandit', 'boxinfo&url=tmdbsmokey', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Spy Kids', 'boxinfo&url=tmdbspy', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Star Trek', 'boxinfo&url=tmdbstartrek', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Star Wars', 'boxinfo&url=tmdbstarwars', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Starship Troopers', 'boxinfo&url=tmdbstarship', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Taken', 'boxinfo&url=tmdbtaken', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Teenage Mutant Ninja Turtles', 'boxinfo&url=tmdbteenage', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Terminator', 'boxinfo&url=tmdbterminator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Titans', 'boxinfo&url=tmdbtitans', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Transformers', 'boxinfo&url=tmdbtransformers', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Transporter', 'boxinfo&url=tmdbtransporter', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Tron', 'boxinfo&url=tmdbtron', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Under Siege', 'boxinfo&url=tmdbunder', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Underworld', 'boxinfo&url=tmdbunderworld', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Undisputed', 'boxinfo&url=tmdbundisputed', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Universal Soldier', 'boxinfo&url=tmdbuniversal', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('xXx', 'boxinfo&url=tmdbxxx', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Young Guns', 'boxinfo&url=tmdbyoung', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Zorro', 'boxinfo&url=tmdbzorro', 'boxsets.png', 'boxsets.png')


        self.endDirectory()

    def adventure(self, lite=False):
        self.addDirectoryItem('101 Dalmations', 'boxinfo&url=tmdbdal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Agent Cody Banks', 'boxinfo&url=tmdbagent', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Aladdin', 'boxinfo&url=tmdbaladdin', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Alice In Wonderland', 'boxinfo&url=tmdbalice', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('American Ninja', 'boxinfo&url=tmdbamninja', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Austin Powers', 'boxinfo&url=tmdbaustin', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Back To The Future', 'boxinfo&url=tmdbback', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Balto', 'boxinfo&url=tmdbbalto', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Batman', 'boxinfo&url=tmdbbatman', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bean', 'boxinfo&url=tmdbbean', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Brother Bear', 'boxinfo&url=tmdbbrotherbear', 'boxsets.png', 'boxsets.png')		

        self.addDirectoryItem('Captain America', 'boxinfo&url=tmdbcaptain', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Chronicles of Narnia', 'boxinfo&url=tmdbnarnia', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Cloudy With A Chance of Meatballs', 'boxinfo&url=tmdbcloudy', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Conan', 'boxinfo&url=tmdbconan', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Crocodile Dundee', 'boxinfo&url=tmdbcroc', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Curious George', 'boxinfo&url=tmdbcurious', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Despicable Me', 'boxinfo&url=tmdbdespicable', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Divergent', 'boxinfo&url=tmdbdivergent', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('FernGully', 'boxinfo&url=tmdbferngully', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Finding Nemo', 'boxinfo&url=tmdbfinding', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Fox and The Hound', 'boxinfo&url=tmdbfox', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Free Willy', 'boxinfo&url=tmdbfree', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('G.I. Joe', 'boxinfo&url=tmdbgi', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ghostbusters', 'boxinfo&url=tmdbghostbusters', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('A Goofy Movie', 'boxinfo&url=tmdbgoofy', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Harold and Kumar', 'boxinfo&url=tmdbharold', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Harry Potter', 'boxinfo&url=tmdbharry', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Herbie', 'boxinfo&url=tmdbherbie', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Highlander', 'boxinfo&url=tmdbhighlander', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Hobbit', 'boxinfo&url=tmdbhobbit', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Homeward Bound', 'boxinfo&url=tmdbhomeward', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Honey I Shrunk The Kids', 'boxinfo&url=tmdbhoney', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('How To Train Your Dragon', 'boxinfo&url=tmdbhow', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Hunger Games', 'boxinfo&url=tmdbhunger', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Huntsman', 'boxinfo&url=tmdbhuntsman', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ice Age', 'boxinfo&url=tmdbiceage', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Independence Day', 'boxinfo&url=tmdbindependence', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Indiana Jones', 'boxinfo&url=tmdbindiana', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Inspector Gadget', 'boxinfo&url=tmdbinspector', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('James Bond', 'boxinfo&url=tmdbjames', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Jaws', 'boxinfo&url=tmdbjaws', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Johnny English', 'boxinfo&url=tmdbjohnny', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Journey', 'boxinfo&url=tmdbjourney', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('The Jungle Book', 'boxinfo&url=tmdbjungle', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Jurassic Park', 'boxinfo&url=tmdbjurassic', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Justice League', 'boxinfo&url=tmdbjusticeleague', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kung Fu Panda', 'boxinfo&url=tmdbkung', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lady and The Tramp', 'boxinfo&url=tmdblady', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Land Before Time', 'boxinfo&url=tmdblbt', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lilo & Stitch', 'boxinfo&url=tmdblilo', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Lion King', 'boxinfo&url=tmdblion', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Lord of The Rings', 'boxinfo&url=tmdblord', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mad Max', 'boxinfo&url=tmdbmadmax', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Madagascar', 'boxinfo&url=tmdbmadagascar', 'boxsets.png', 'boxsets.png')		

        self.addDirectoryItem('Men in Black', 'boxinfo&url=tmdbmib', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mission Impossible', 'boxinfo&url=tmdbmission', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Monsters INC', 'boxinfo&url=tmdbmonster', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Monty Python', 'boxinfo&url=tmdbmonty', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mulan', 'boxinfo&url=tmdbmulan', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Mummy', 'boxinfo&url=tmdbmummy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Muppets', 'boxinfo&url=tmdbmuppets', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('National Treasure', 'boxinfo&url=tmdbnational', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('The Never Ending Story', 'boxinfo&url=tmdbnes', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('New Groove', 'boxinfo&url=tmdbnewgroove', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Night At The Museum', 'boxinfo&url=tmdbnatm', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Nims Island', 'boxinfo&url=tmdbnims', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Open Season', 'boxinfo&url=tmdbopen', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Percy Jackson', 'boxinfo&url=tmdbpercy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Peter Pan', 'boxinfo&url=tmdbpeter', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Pink Panther', 'boxinfo&url=tmdbpink', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Pirates of The Caribbean', 'boxinfo&url=tmdbpirates', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Planes', 'boxinfo&url=tmdbplanes', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Planet of The Apes', 'boxinfo&url=tmdbplanet', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Pocahontas', 'boxinfo&url=tmdbpoca', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Power Rangers', 'boxinfo&url=tmdbpowerrangers', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Rambo', 'boxinfo&url=tmdbrambo', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Red Cliff', 'boxinfo&url=tmdbredcliff', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Riddick', 'boxinfo&url=tmdbriddick', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rio', 'boxinfo&url=tmdbrio', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Romancing The Stone', 'boxinfo&url=tmdbromancing', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Sammys Adventures', 'boxinfo&url=tmdbsammy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Sherlock Holmes', 'boxinfo&url=tmdbsherlock', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Shrek', 'boxinfo&url=tmdbshrek', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Smurfs', 'boxinfo&url=tmdbsmurfs', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Space Chimps', 'boxinfo&url=tmdbspacechimps', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('SpongBob Squarepants', 'boxinfo&url=tmdbspongebob', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Spy Kids', 'boxinfo&url=tmdbspy', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Star Trek', 'boxinfo&url=tmdbstartrek', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Star Wars', 'boxinfo&url=tmdbstarwars', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Starship Troopers', 'boxinfo&url=tmdbstarship', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Stuart Little', 'boxinfo&url=tmdbstuart', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Tarzan', 'boxinfo&url=tmdbtarzan', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Teenage Mutant Ninja Turtles', 'boxinfo&url=tmdbteenage', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Tinker Bell', 'boxinfo&url=tmdbtinker', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Titans', 'boxinfo&url=tmdbtitans', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Transformers', 'boxinfo&url=tmdbtransformers', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Tron', 'boxinfo&url=tmdbtron', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Weekend at Bernies', 'boxinfo&url=tmdbweekend', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('xXx', 'boxinfo&url=tmdbxxx', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Zorro', 'boxinfo&url=tmdbzorro', 'boxsets.png', 'boxsets.png')


        self.endDirectory()
		
    def animation(self, lite=False):
        self.addDirectoryItem('101 Dalmations', 'boxinfo&url=tmdbdal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Aladdin', 'boxinfo&url=tmdbaladdin', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Alice In Wonderland', 'boxinfo&url=tmdbalice', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('All Dogs Go to Heaven', 'boxinfo&url=tmdballdogs', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Balto', 'boxinfo&url=tmdbbalto', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bambi', 'boxinfo&url=tmdbbambi', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Beauty and The Beast', 'boxinfo&url=tmdbbeauty', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Brother Bear', 'boxinfo&url=tmdbbrotherbear', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Cars', 'boxinfo&url=tmdbcars', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Charlottes Web', 'boxinfo&url=tmdbcharlottes', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cloudy With A Chance of Meatballs', 'boxinfo&url=tmdbcloudy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Curious George', 'boxinfo&url=tmdbcurious', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Despicable Me', 'boxinfo&url=tmdbdespicable', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Fantasia', 'boxinfo&url=tmdbfantasia', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('FernGully', 'boxinfo&url=tmdbferngully', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Finding Nemo', 'boxinfo&url=tmdbfinding', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Fox and The Hound', 'boxinfo&url=tmdbfox', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Garfield', 'boxinfo&url=tmdbgarfield', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('A Goofy Movie', 'boxinfo&url=tmdbgoofy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Happy Feet', 'boxinfo&url=tmdbhappy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hoodwinked!', 'boxinfo&url=tmdbhoodwink', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hotel Transylvania', 'boxinfo&url=tmdbhotel', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('How To Train Your Dragon', 'boxinfo&url=tmdbhow', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hunchback of Notre Dame', 'boxinfo&url=tmdbhunch', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ice Age', 'boxinfo&url=tmdbiceage', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Justice League', 'boxinfo&url=tmdbjusticeleague', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kung Fu Panda', 'boxinfo&url=tmdbkung', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lady and The Tramp', 'boxinfo&url=tmdblady', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Land Before Time', 'boxinfo&url=tmdblbt', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lego Star Wars', 'boxinfo&url=tmdblegostar', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lilo & Stitch', 'boxinfo&url=tmdblilo', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Lion King', 'boxinfo&url=tmdblion', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Little Mermaid', 'boxinfo&url=tmdbmermaid', 'boxsets.png', 'boxsets.png')	
        self.addDirectoryItem('Madagascar', 'boxinfo&url=tmdbmadagascar', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Monsters INC', 'boxinfo&url=tmdbmonster', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mulan', 'boxinfo&url=tmdbmulan', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('New Groove', 'boxinfo&url=tmdbnewgroove', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Open Season', 'boxinfo&url=tmdbopen', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Planes', 'boxinfo&url=tmdbplanes', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Pocahontas', 'boxinfo&url=tmdbpoca', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Reef', 'boxinfo&url=tmdbreef', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rio', 'boxinfo&url=tmdbrio', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Sammys Adventures', 'boxinfo&url=tmdbsammy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Shrek', 'boxinfo&url=tmdbshrek', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Smurfs', 'boxinfo&url=tmdbsmurfs', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Space Chimps', 'boxinfo&url=tmdbspacechimps', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('SpongBob Squarepants', 'boxinfo&url=tmdbspongebob', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Tarzan', 'boxinfo&url=tmdbtarzan', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Thomas & Friends', 'boxinfo&url=tmdbthomas', 'boxsets.png', 'boxsets.png')
		
        self.addDirectoryItem('Tinker Bell', 'boxinfo&url=tmdbtinker', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Wallace & Gromit', 'boxinfo&url=tmdbwallace', 'boxsets.png', 'boxsets.png')
		
		
		
		
		

        self.endDirectory()
		
    def comedy(self, lite=False):
        self.addDirectoryItem('101 Dalmations', 'boxinfo&url=tmdbdal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('3 Ninjas', 'boxinfo&url=tmdb3nin', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('A Haunted House', 'boxinfo&url=tmdbhaunted', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ace Ventura', 'boxinfo&url=tmdbace', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Adams Family', 'boxinfo&url=tmdbadams', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Agent Cody Banks', 'boxinfo&url=tmdbagent', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Aladdin', 'boxinfo&url=tmdbaladdin', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('All Dogs Go to Heaven', 'boxinfo&url=tmdballdogs', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('American Pie', 'boxinfo&url=tmdbampie', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Anchorman', 'boxinfo&url=tmdbanchor', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Austin Powers', 'boxinfo&url=tmdbaustin', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Babe', 'boxinfo&url=tmdbbabe', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Back To The Future', 'boxinfo&url=tmdbback', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bad Ass', 'boxinfo&url=tmdbbadass', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bad Boys', 'boxinfo&url=tmdbbb', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bad Neighbors', 'boxinfo&url=tmdbbn', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Barbershop', 'boxinfo&url=tmdbbarber', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bean', 'boxinfo&url=tmdbbean', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Best Exotic Marigold Hotel', 'boxinfo&url=tmdbbestexotic', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Beverly Hills Cop', 'boxinfo&url=tmdbbeverly', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Big Mommas House', 'boxinfo&url=tmdbbig', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Blues Brother', 'boxinfo&url=tmdbblues', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bridget Jones', 'boxinfo&url=tmdbbridget', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Brother Bear', 'boxinfo&url=tmdbbrotherbear', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Cars', 'boxinfo&url=tmdbcars', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Casper', 'boxinfo&url=tmdbcasper', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cats & Dogs', 'boxinfo&url=tmdbcatsanddogs', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('City Slickers', 'boxinfo&url=tmdbcity', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Clerks', 'boxinfo&url=tmdbclerks', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cloudy With A Chance of Meatballs', 'boxinfo&url=tmdbcloudy', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Crocodile Dundee', 'boxinfo&url=tmdbcroc', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Curious George', 'boxinfo&url=tmdbcurious', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Daddy Daycare', 'boxinfo&url=tmdbdaddy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Despicable Me', 'boxinfo&url=tmdbdespicable', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Diary of A Wimpy Kid', 'boxinfo&url=tmdbdiary', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Doctor Dolittle', 'boxinfo&url=tmdbdolittle', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Dumb and Dumber', 'boxinfo&url=tmdbdumb', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Finding Nemo', 'boxinfo&url=tmdbfinding', 'boxsets.png', 'boxsets.png')		

        self.addDirectoryItem('Friday', 'boxinfo&url=tmdbfriday', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Garfield', 'boxinfo&url=tmdbgarfield', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Ghostbusters', 'boxinfo&url=tmdbghostbusters', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('A Goofy Movie', 'boxinfo&url=tmdbgoofy', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Gremlins', 'boxinfo&url=tmdbgremlins', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Grown Ups', 'boxinfo&url=tmdbgrown', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Grumpy Old Men', 'boxinfo&url=tmdbgrumpy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Hangover', 'boxinfo&url=tmdbhangover', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Happy Feet', 'boxinfo&url=tmdbhappy', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Harold and Kumar', 'boxinfo&url=tmdbharold', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Herbie', 'boxinfo&url=tmdbherbie', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Home Alone', 'boxinfo&url=tmdbhome', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Homeward Bound', 'boxinfo&url=tmdbhomeward', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Honey I Shrunk The Kids', 'boxinfo&url=tmdbhoney', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hoodwinked!', 'boxinfo&url=tmdbhoodwink', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Horrible Bosses', 'boxinfo&url=tmdbhorrible', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hot Shots', 'boxinfo&url=tmdbhot', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Hot Tub Time Machine', 'boxinfo&url=tmdbhotub', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hotel Transylvania', 'boxinfo&url=tmdbhotel', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ice Age', 'boxinfo&url=tmdbiceage', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Inbetweeners', 'boxinfo&url=tmdbinbetweeners', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Inspector Gadget', 'boxinfo&url=tmdbinspector', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Jackass', 'boxinfo&url=tmdbjackass', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Johnny English', 'boxinfo&url=tmdbjohnny', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Jump Street', 'boxinfo&url=tmdbjump', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kick-Ass', 'boxinfo&url=tmdbkick', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Legally Blonde', 'boxinfo&url=tmdblegally', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Like Mike', 'boxinfo&url=tmdblikemike', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lilo & Stitch', 'boxinfo&url=tmdblilo', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Madagascar', 'boxinfo&url=tmdbmadagascar', 'boxsets.png', 'boxsets.png')		

        self.addDirectoryItem('Major League', 'boxinfo&url=tmdbmajor', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Meet The Parents', 'boxinfo&url=tmdbmeet', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Men in Black', 'boxinfo&url=tmdbmib', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Mighty Ducks', 'boxinfo&url=tmdbmighty', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Monsters INC', 'boxinfo&url=tmdbmonster', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Monty Python', 'boxinfo&url=tmdbmonty', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Muppets', 'boxinfo&url=tmdbmuppets', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('My Big Fat Greek Wedding', 'boxinfo&url=tmdbmbfgw', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Naked Gun', 'boxinfo&url=tmdbnaked', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('New Groove', 'boxinfo&url=tmdbnewgroove', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Night At The Museum', 'boxinfo&url=tmdbnatm', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Nims Island', 'boxinfo&url=tmdbnims', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Open Season', 'boxinfo&url=tmdbopen', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Pink Panther', 'boxinfo&url=tmdbpink', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Pitch Perfect', 'boxinfo&url=tmdbpitch', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Planes', 'boxinfo&url=tmdbplanes', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Police Academy', 'boxinfo&url=tmdbpolice', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Problem Child', 'boxinfo&url=tmdbproblem', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('R.E.D.', 'boxinfo&url=tmdbred', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ride Along', 'boxinfo&url=tmdbride', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rio', 'boxinfo&url=tmdbrio', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Romancing The Stone', 'boxinfo&url=tmdbromancing', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rush Hour', 'boxinfo&url=tmdbrush', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Sandlot', 'boxinfo&url=tmdbsandlot', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Scary Movie', 'boxinfo&url=tmdbscary', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Shrek', 'boxinfo&url=tmdbshrek', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Short Circuit', 'boxinfo&url=tmdbshort', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Smokey and The Bandit', 'boxinfo&url=tmdbsmokey', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('The Smurfs', 'boxinfo&url=tmdbsmurfs', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Space Chimps', 'boxinfo&url=tmdbspacechimps', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('SpongBob Squarepants', 'boxinfo&url=tmdbspongebob', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Spy Kids', 'boxinfo&url=tmdbspy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Stuart Little', 'boxinfo&url=tmdbstuart', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Ted', 'boxinfo&url=tmdbted', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Teenage Mutant Ninja Turtles', 'boxinfo&url=tmdbteenage', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Teen Wolf', 'boxinfo&url=tmdbteen', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Tooth Fairy', 'boxinfo&url=tmdbtooth', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Tremors', 'boxinfo&url=tmdbtremors', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Waynes World', 'boxinfo&url=tmdbwayne', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Weekend at Bernies', 'boxinfo&url=tmdbweekend', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Whole Nine Yards', 'boxinfo&url=tmdbwholenine', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Zoolander', 'boxinfo&url=tmdbzoo', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Zorro', 'boxinfo&url=tmdbzorro', 'boxsets.png', 'boxsets.png')


        self.endDirectory()
		
    def crime(self, lite=False):
        self.addDirectoryItem('12 Rounds', 'boxinfo&url=tmdbrounds', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bad Ass', 'boxinfo&url=tmdbbadass', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bad Boys', 'boxinfo&url=tmdbbb', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Beverly Hills Cop', 'boxinfo&url=tmdbbeverly', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Big Mommas House', 'boxinfo&url=tmdbbig', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Blues Brother', 'boxinfo&url=tmdbblues', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Boondock Saints', 'boxinfo&url=tmdbboon', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Crank', 'boxinfo&url=tmdbcrank', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Dirty Harry', 'boxinfo&url=tmdbdirtyh', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Dragon Tattoo', 'boxinfo&url=tmdbdragon', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Fast and Furious', 'boxinfo&url=tmdbfurious', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Godfather', 'boxinfo&url=tmdbgodfather', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Green Street Hooligans', 'boxinfo&url=tmdbgreen', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Hannibal Lecter', 'boxinfo&url=tmdbhannibal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Horrible Bosses', 'boxinfo&url=tmdbhorrible', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Infernal Affairs', 'boxinfo&url=tmdbinfernal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Judge Dredd', 'boxinfo&url=tmdbdredd', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Jump Street', 'boxinfo&url=tmdbjump', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kill Bill', 'boxinfo&url=tmdbkill', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lethal Weapon', 'boxinfo&url=tmdblethal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Machete', 'boxinfo&url=tmdbmachete', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Mechanic', 'boxinfo&url=tmdbmechanic', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Naked Gun', 'boxinfo&url=tmdbnaked', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ninja', 'boxinfo&url=tmdbninja', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Now You See Me', 'boxinfo&url=tmdbnysm', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Oceans', 'boxinfo&url=tmdboceans', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Once Were Warriors', 'boxinfo&url=tmdbonce', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Ong Bak', 'boxinfo&url=tmdbong', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Pink Panther', 'boxinfo&url=tmdbpink', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Protector', 'boxinfo&url=tmdbprotector', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Punisher', 'boxinfo&url=tmdbpunisher', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Raid', 'boxinfo&url=tmdbraid', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('R.E.D.', 'boxinfo&url=tmdbred', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ride Along', 'boxinfo&url=tmdbride', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rise of the Footsoldier', 'boxinfo&url=tmdbrise', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Robocop', 'boxinfo&url=tmdbrobocop', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rush Hour', 'boxinfo&url=tmdbrush', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Sherlock Holmes', 'boxinfo&url=tmdbsherlock', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Sin City', 'boxinfo&url=tmdbsin', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Step Up', 'boxinfo&url=tmdbstepup', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Transporter', 'boxinfo&url=tmdbtransporter', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Undisputed', 'boxinfo&url=tmdbundisputed', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Weekend at Bernies', 'boxinfo&url=tmdbweekend', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Whole Nine Yards', 'boxinfo&url=tmdbwholenine', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Young Guns', 'boxinfo&url=tmdbyoung', 'boxsets.png', 'boxsets.png')


        self.endDirectory()
		
    def drama(self, lite=False):
        self.addDirectoryItem('28 Days Later', 'boxinfo&url=tmdb28days', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('All Dogs Go to Heaven', 'boxinfo&url=tmdballdogs', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Babe', 'boxinfo&url=tmdbbabe', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Balto', 'boxinfo&url=tmdbbalto', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bambi', 'boxinfo&url=tmdbbambi', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Barbershop', 'boxinfo&url=tmdbbarber', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Before', 'boxinfo&url=tmdbbefore', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Best Exotic Marigold Hotel', 'boxinfo&url=tmdbbestexotic', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Best Of The Best', 'boxinfo&url=tmdbbob', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bloodsport', 'boxinfo&url=tmdbblood', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bruce Lee', 'boxinfo&url=tmdbbrucelee', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cinderella', 'boxinfo&url=tmdbcinderella', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Crow', 'boxinfo&url=tmdbcrow', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cube', 'boxinfo&url=tmdbcube', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Dirty Dancing', 'boxinfo&url=tmdbdirtyd', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Dolphin Tale', 'boxinfo&url=tmdbdolphin', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Dragon Tattoo', 'boxinfo&url=tmdbdragon', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Fly', 'boxinfo&url=tmdbfly', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Fox and The Hound', 'boxinfo&url=tmdbfox', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Free Willy', 'boxinfo&url=tmdbfree', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Friday', 'boxinfo&url=tmdbfriday', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Godfather', 'boxinfo&url=tmdbgodfather', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Green Street Hooligans', 'boxinfo&url=tmdbgreen', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Grumpy Old Men', 'boxinfo&url=tmdbgrumpy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hannibal Lecter', 'boxinfo&url=tmdbhannibal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Homeward Bound', 'boxinfo&url=tmdbhomeward', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hunchback of Notre Dame', 'boxinfo&url=tmdbhunch', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Huntsman', 'boxinfo&url=tmdbhuntsman', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Infernal Affairs', 'boxinfo&url=tmdbinfernal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ip Man', 'boxinfo&url=tmdbipman', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Jaws', 'boxinfo&url=tmdbjaws', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Jungle Book', 'boxinfo&url=tmdbjungle', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Karate Kid', 'boxinfo&url=tmdbkarate', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Land Before Time', 'boxinfo&url=tmdblbt', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Lion King', 'boxinfo&url=tmdblion', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Lord of The Rings', 'boxinfo&url=tmdblord', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Mighty Ducks', 'boxinfo&url=tmdbmighty', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('My Big Fat Greek Wedding', 'boxinfo&url=tmdbmbfgw', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Never Back Down', 'boxinfo&url=tmdbnever', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Never Ending Story', 'boxinfo&url=tmdbnes', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ninja', 'boxinfo&url=tmdbninja', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Nymphomaniac', 'boxinfo&url=tmdbnymph', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Once Were Warriors', 'boxinfo&url=tmdbonce', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Pocahontas', 'boxinfo&url=tmdbpoca', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Punisher', 'boxinfo&url=tmdbpunisher', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Red Cliff', 'boxinfo&url=tmdbredcliff', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rise of the Footsoldier', 'boxinfo&url=tmdbrise', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rocky', 'boxinfo&url=tmdbrocky', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Sandlot', 'boxinfo&url=tmdbsandlot', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Shanghai', 'boxinfo&url=tmdbshanghai', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Step Up', 'boxinfo&url=tmdbstepup', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Three Colors', 'boxinfo&url=tmdbthree', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Twilight', 'boxinfo&url=tmdbtwilight', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Undisputed', 'boxinfo&url=tmdbundisputed', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Woman in Black', 'boxinfo&url=tmdbwoman', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Young Guns', 'boxinfo&url=tmdbyoung', 'boxsets.png', 'boxsets.png')


        self.endDirectory()

    def family(self, lite=False):
        self.addDirectoryItem('3 Ninjas', 'boxinfo&url=tmdb3nin', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Alice In Wonderland', 'boxinfo&url=tmdbalice', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Babe', 'boxinfo&url=tmdbbabe', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bambi', 'boxinfo&url=tmdbbambi', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bean', 'boxinfo&url=tmdbbean', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Beauty and The Beast', 'boxinfo&url=tmdbbeauty', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cars', 'boxinfo&url=tmdbcars', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Casper', 'boxinfo&url=tmdbcasper', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cats & Dogs', 'boxinfo&url=tmdbcatsanddogs', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Charlottes Web', 'boxinfo&url=tmdbcharlottes', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Chronicles of Narnia', 'boxinfo&url=tmdbnarnia', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cinderella', 'boxinfo&url=tmdbcinderella', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Daddy Daycare', 'boxinfo&url=tmdbdaddy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Diary of A Wimpy Kid', 'boxinfo&url=tmdbdiary', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Doctor Dolittle', 'boxinfo&url=tmdbdolittle', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Dolphin Tale', 'boxinfo&url=tmdbdolphin', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Fantasia', 'boxinfo&url=tmdbfantasia', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('FernGully', 'boxinfo&url=tmdbferngully', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Flintstones', 'boxinfo&url=tmdbflintstones', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Free Willy', 'boxinfo&url=tmdbfree', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Garfield', 'boxinfo&url=tmdbgarfield', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Happy Feet', 'boxinfo&url=tmdbhappy', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Harry Potter', 'boxinfo&url=tmdbharry', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Herbie', 'boxinfo&url=tmdbherbie', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Home Alone', 'boxinfo&url=tmdbhome', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Honey I Shrunk The Kids', 'boxinfo&url=tmdbhoney', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hotel Transylvania', 'boxinfo&url=tmdbhotel', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Hunchback of Notre Dame', 'boxinfo&url=tmdbhunch', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Journey', 'boxinfo&url=tmdbjourney', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('The Jungle Book', 'boxinfo&url=tmdbjungle', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Karate Kid', 'boxinfo&url=tmdbkarate', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lego Star Wars', 'boxinfo&url=tmdblegostar', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Like Mike', 'boxinfo&url=tmdblikemike', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Little Mermaid', 'boxinfo&url=tmdbmermaid', 'boxsets.png', 'boxsets.png')	

        self.addDirectoryItem('Men in Black', 'boxinfo&url=tmdbmib', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('The Mighty Ducks', 'boxinfo&url=tmdbmighty', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mulan', 'boxinfo&url=tmdbmulan', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Muppets', 'boxinfo&url=tmdbmuppets', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('National Treasure', 'boxinfo&url=tmdbnational', 'boxsets.png', 'boxsets.png')		

        self.addDirectoryItem('The Never Ending Story', 'boxinfo&url=tmdbnes', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Night At The Museum', 'boxinfo&url=tmdbnatm', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Nims Island', 'boxinfo&url=tmdbnims', 'boxsets.png', 'boxsets.png')		

        self.addDirectoryItem('Percy Jackson', 'boxinfo&url=tmdbpercy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Peter Pan', 'boxinfo&url=tmdbpeter', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Power Rangers', 'boxinfo&url=tmdbpowerrangers', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Problem Child', 'boxinfo&url=tmdbproblem', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Reef', 'boxinfo&url=tmdbreef', 'boxsets.png', 'boxsets.png')
	
        self.addDirectoryItem('Sammys Adventures', 'boxinfo&url=tmdbsammy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Sandlot', 'boxinfo&url=tmdbsandlot', 'boxsets.png', 'boxsets.png')
	
        self.addDirectoryItem('Short Circuit', 'boxinfo&url=tmdbshort', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Stuart Little', 'boxinfo&url=tmdbstuart', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Tarzan', 'boxinfo&url=tmdbtarzan', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Thomas & Friends', 'boxinfo&url=tmdbthomas', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Tinker Bell', 'boxinfo&url=tmdbtinker', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Tooth Fairy', 'boxinfo&url=tmdbtooth', 'boxsets.png', 'boxsets.png')
		
	
        self.endDirectory()
		
    def fantasy(self, lite=False):
        self.addDirectoryItem('300', 'boxinfo&url=tmdb300', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('A Haunted House', 'boxinfo&url=tmdbhaunted', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Adams Family', 'boxinfo&url=tmdbadams', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Beauty and The Beast', 'boxinfo&url=tmdbbeauty', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Casper', 'boxinfo&url=tmdbcasper', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Chronicles of Narnia', 'boxinfo&url=tmdbnarnia', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cinderella', 'boxinfo&url=tmdbcinderella', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Conan', 'boxinfo&url=tmdbconan', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Crow', 'boxinfo&url=tmdbcrow', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Doctor Dolittle', 'boxinfo&url=tmdbdolittle', 'dolittle.jpg', 'boxsets.png')
        self.addDirectoryItem('Fantasia', 'boxinfo&url=tmdbfantasia', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Flintstones', 'boxinfo&url=tmdbflintstones', 'boxsets.png', 'boxsets.png')		

        self.addDirectoryItem('Ghost Rider', 'boxinfo&url=tmdbghost', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Gremlins', 'boxinfo&url=tmdbgremlins', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Harry Potter', 'boxinfo&url=tmdbharry', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Highlander', 'boxinfo&url=tmdbhighlander', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Hobbit', 'boxinfo&url=tmdbhobbit', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Indiana Jones', 'boxinfo&url=tmdbindiana', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lego Star Wars', 'boxinfo&url=tmdblegostar', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Like Mike', 'boxinfo&url=tmdblikemike', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Little Mermaid', 'boxinfo&url=tmdbmermaid', 'boxsets.png', 'boxsets.png')	

        self.addDirectoryItem('Lord of The Rings', 'boxinfo&url=tmdblord', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Monty Python', 'boxinfo&url=tmdbmonty', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Mummy', 'boxinfo&url=tmdbmummy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Percy Jackson', 'boxinfo&url=tmdbpercy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Peter Pan', 'boxinfo&url=tmdbpeter', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Pirates of The Caribbean', 'boxinfo&url=tmdbpirates', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Poltergeist', 'boxinfo&url=tmdbpolter', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Star Wars', 'boxinfo&url=tmdbstarwars', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ted', 'boxinfo&url=tmdbted', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Teen Wolf', 'boxinfo&url=tmdbteen', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Titans', 'boxinfo&url=tmdbtitans', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Tooth Fairy', 'boxinfo&url=tmdbtooth', 'boxsets.png', 'boxsets.png')

        self.addDirectoryItem('Twilight', 'boxinfo&url=tmdbtwilight', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Underworld', 'boxinfo&url=tmdbunderworld', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Woman in Black', 'boxinfo&url=tmdbwoman', 'boxsets.png', 'boxsets.png')


        self.endDirectory()
		
    def horror(self, lite=False):
        self.addDirectoryItem('28 Days Later', 'boxinfo&url=tmdb28days', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('A Nightmare on Elm Street', 'boxinfo&url=tmdbelmst', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Alien', 'boxinfo&url=tmdbalien', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('AVP', 'boxinfo&url=tmdbavp', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Childs Play', 'boxinfo&url=tmdbchilds', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Conjuring', 'boxinfo&url=tmdbconjuring', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Evil Dead', 'boxinfo&url=tmdbevil', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Exorcist', 'boxinfo&url=tmdbexorcist', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Final Destination', 'boxinfo&url=tmdbfinal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Fly', 'boxinfo&url=tmdbfly', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Friday The 13th', 'boxinfo&url=tmdbfriday13', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Gremlins', 'boxinfo&url=tmdbgremlins', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Grudge', 'boxinfo&url=tmdbgrudge', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Halloween', 'boxinfo&url=tmdbhalloween', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hellraiser', 'boxinfo&url=tmdbhell', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Hills Have Eyes', 'boxinfo&url=tmdbhills', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hollow Man', 'boxinfo&url=tmdbhollow', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hostel', 'boxinfo&url=tmdbhostel', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('The Human Centipede', 'boxinfo&url=tmdbhuman', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Insidious', 'boxinfo&url=tmdbinsidious', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Last Summer', 'boxinfo&url=tmdblast', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Omen', 'boxinfo&url=tmdbomen', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Paranormal Activity', 'boxinfo&url=tmdbparanormal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Poltergeist', 'boxinfo&url=tmdbpolter', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Psycho', 'boxinfo&url=tmdbpsycho', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Purge', 'boxinfo&url=tmdbpurge', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Quarantine', 'boxinfo&url=tmdbquarantine', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Resident Evil', 'boxinfo&url=tmdbresident', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Ring', 'boxinfo&url=tmdbring', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Saw', 'boxinfo&url=tmdbsaw', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Scream', 'boxinfo&url=tmdbscream', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Texas Chainsaw Massacre', 'boxinfo&url=tmdbtexas', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Tremors', 'boxinfo&url=tmdbtremors', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('VHS', 'boxinfo&url=tmdbvhs', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Woman in Black', 'boxinfo&url=tmdbwoman', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Wrong Turn', 'boxinfo&url=tmdbwrong', 'boxsets.png', 'boxsets.png')		


        self.endDirectory()
		
    def mystery(self, lite=False):
        self.addDirectoryItem('The Conjuring', 'boxinfo&url=tmdbconjuring', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Cube', 'boxinfo&url=tmdbcube', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Divergent', 'boxinfo&url=tmdbdivergent', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Dragon Tattoo', 'boxinfo&url=tmdbdragon', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Friday The 13th', 'boxinfo&url=tmdbfriday13', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Grudge', 'boxinfo&url=tmdbgrudge', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Infernal Affairs', 'boxinfo&url=tmdbinfernal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Insidious', 'boxinfo&url=tmdbinsidious', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Last Summer', 'boxinfo&url=tmdblast', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Now You See Me', 'boxinfo&url=tmdbnysm', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Paranormal Activity', 'boxinfo&url=tmdbparanormal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Psycho', 'boxinfo&url=tmdbpsycho', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Ring', 'boxinfo&url=tmdbring', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Saw', 'boxinfo&url=tmdbsaw', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Scream', 'boxinfo&url=tmdbscream', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Shanghai', 'boxinfo&url=tmdbshanghai', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Three Colors', 'boxinfo&url=tmdbthree', 'boxsets.png', 'boxsets.png')


        self.endDirectory()
		
    def romance(self, lite=False):
        self.addDirectoryItem('American Ninja', 'boxinfo&url=tmdbamninja', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Before', 'boxinfo&url=tmdbbefore', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Bridget Jones', 'boxinfo&url=tmdbbridget', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Dirty Dancing', 'boxinfo&url=tmdbdirtyd', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Grumpy Old Men', 'boxinfo&url=tmdbgrumpy', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Legally Blonde', 'boxinfo&url=tmdblegally', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Meet The Parents', 'boxinfo&url=tmdbmeet', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('My Big Fat Greek Wedding', 'boxinfo&url=tmdbmbfgw', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Shanghai', 'boxinfo&url=tmdbshanghai', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Think Like a Man', 'boxinfo&url=tmdbthink', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Three Colors', 'boxinfo&url=tmdbthree', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Twilight', 'boxinfo&url=tmdbtwilight', 'boxsets.png', 'boxsets.png')


        self.endDirectory()
		
    def scifi(self, lite=False):
        self.addDirectoryItem('28 Days Later', 'boxinfo&url=tmdb28days', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Alien', 'boxinfo&url=tmdbalien', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Avengers', 'boxinfo&url=tmdbavengers', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('AVP', 'boxinfo&url=tmdbavp', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Back To The Future', 'boxinfo&url=tmdbback', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Butterfly Effect', 'boxinfo&url=tmdbbutterfly', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Captain America', 'boxinfo&url=tmdbcaptain', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cocoon', 'boxinfo&url=tmdbcocoon', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Cube', 'boxinfo&url=tmdbcube', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Divergent', 'boxinfo&url=tmdbdivergent', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Fly', 'boxinfo&url=tmdbfly', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('G.I. Joe', 'boxinfo&url=tmdbgi', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hollow Man', 'boxinfo&url=tmdbhollow', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hot Tub Time Machine', 'boxinfo&url=tmdbhotub', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hunger Games', 'boxinfo&url=tmdbhunger', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Independence Day', 'boxinfo&url=tmdbindependence', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Judge Dredd', 'boxinfo&url=tmdbdredd', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Jurassic Park', 'boxinfo&url=tmdbjurassic', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mad Max', 'boxinfo&url=tmdbmadmax', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Matrix', 'boxinfo&url=tmdbmatrix', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Maze Runner', 'boxinfo&url=tmdbmaze', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Planet of The Apes', 'boxinfo&url=tmdbplanet', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Predator', 'boxinfo&url=tmdbpredator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Purge', 'boxinfo&url=tmdbpurge', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Quarantine', 'boxinfo&url=tmdbquarantine', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Resident Evil', 'boxinfo&url=tmdbresident', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Riddick', 'boxinfo&url=tmdbriddick', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Robocop', 'boxinfo&url=tmdbrobocop', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Short Circuit', 'boxinfo&url=tmdbshort', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Star Trek', 'boxinfo&url=tmdbstartrek', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Starship Troopers', 'boxinfo&url=tmdbstarship', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Terminator', 'boxinfo&url=tmdbterminator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Transformers', 'boxinfo&url=tmdbtransformers', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Tron', 'boxinfo&url=tmdbtron', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Universal Soldier', 'boxinfo&url=tmdbuniversal', 'boxsets.png', 'boxsets.png')		


        self.endDirectory()
		
    def thriller(self, lite=False):
        self.addDirectoryItem('12 Rounds', 'boxinfo&url=tmdbrounds', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Boondock Saints', 'boxinfo&url=tmdbboon', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Bourne', 'boxinfo&url=tmdbbourne', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('The Butterfly Effect', 'boxinfo&url=tmdbbutterfly', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Childs Play', 'boxinfo&url=tmdbchilds', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Conjuring', 'boxinfo&url=tmdbconjuring', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Crank', 'boxinfo&url=tmdbcrank', 'crank.jpg', 'boxsets.png')
        self.addDirectoryItem('Die Hard', 'boxinfo&url=tmdbdie', 'die.jpg', 'boxsets.png')
        self.addDirectoryItem('Dirty Harry', 'boxinfo&url=tmdbdirtyh', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Fast and Furious', 'boxinfo&url=tmdbfurious', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Friday The 13th', 'boxinfo&url=tmdbfriday13', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ghost Rider', 'boxinfo&url=tmdbghost', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Grudge', 'boxinfo&url=tmdbgrudge', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Halloween', 'boxinfo&url=tmdbhalloween', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hannibal Lecter', 'boxinfo&url=tmdbhannibal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hellraiser', 'boxinfo&url=tmdbhell', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Hills Have Eyes', 'boxinfo&url=tmdbhills', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Hunger Games', 'boxinfo&url=tmdbhunger', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Insidious', 'boxinfo&url=tmdbinsidious', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('James Bond', 'boxinfo&url=tmdbjames', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Jaws', 'boxinfo&url=tmdbjaws', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Jurassic Park', 'boxinfo&url=tmdbjurassic', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kickboxer', 'boxinfo&url=tmdbkickboxer', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Kill Bill', 'boxinfo&url=tmdbkill', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Last Summer', 'boxinfo&url=tmdblast', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Lethal Weapon', 'boxinfo&url=tmdblethal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Machete', 'boxinfo&url=tmdbmachete', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Maze Runner', 'boxinfo&url=tmdbmaze', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Mechanic', 'boxinfo&url=tmdbmechanic', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Mission Impossible', 'boxinfo&url=tmdbmission', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Now You See Me', 'boxinfo&url=tmdbnysm', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Oceans', 'boxinfo&url=tmdboceans', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Olympus Has Fallen', 'boxinfo&url=tmdbolympus', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Ong Bak', 'boxinfo&url=tmdbong', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Paranormal Activity', 'boxinfo&url=tmdbparanormal', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Poltergeist', 'boxinfo&url=tmdbpolter', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Predator', 'boxinfo&url=tmdbpredator', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Protector', 'boxinfo&url=tmdbprotector', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Psycho', 'boxinfo&url=tmdbpsycho', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Purge', 'boxinfo&url=tmdbpurge', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Quarantine', 'boxinfo&url=tmdbquarantine', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('The Raid', 'boxinfo&url=tmdbraid', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Rambo', 'boxinfo&url=tmdbrambo', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Saw', 'boxinfo&url=tmdbsaw', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Sin City', 'boxinfo&url=tmdbsin', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Taken', 'boxinfo&url=tmdbtaken', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('Transporter', 'boxinfo&url=tmdbtransporter', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Under Siege', 'boxinfo&url=tmdbunder', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Underworld', 'boxinfo&url=tmdbunderworld', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('Universal Soldier', 'boxinfo&url=tmdbuniversal', 'boxsets.png', 'boxsets.png')		
        self.addDirectoryItem('VHS', 'boxinfo&url=tmdbvhs', 'boxsets.png', 'boxsets.png')
        self.addDirectoryItem('xXx', 'boxinfo&url=tmdbxxx', 'boxsets.png', 'boxsets.png')		
        

        self.endDirectory()

        
        
		
    def tools(self):
        self.addDirectoryItem('[B]URL RESOLVER[/B]: Settings', 'resolversettings', 'boxsets.png', 'DefaultAddonProgram.png')

        self.addDirectoryItem(32043, 'openSettings&query=0.0', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32045, 'openSettings&query=1.0', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Accounts', 'openSettings&query=2.0', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32047, 'openSettings&query=3.0', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem(32046, 'openSettings&query=5.0', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Downloads', 'openSettings&query=4.0', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]SETTINGS[/B]: Watchlist', 'openSettings&query=6.0', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Views', 'viewsNavigator', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Providers', 'clearSources', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]Bone Crusher collections[/B]: Clear Cache', 'clearCache', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]BACKUP[/B]: Watchlist', 'backupwatchlist', 'boxsets.png', 'DefaultAddonProgram.png')
        self.addDirectoryItem('[B]RESTORE[/B]: Watchlist', 'restorewatchlist', 'boxsets.png', 'DefaultAddonProgram.png')

        self.endDirectory()


    def downloads(self):
        movie_downloads = control.setting('movie.download.path')

        if len(control.listDir(movie_downloads)[0]) > 0:
            self.addDirectoryItem(32001, movie_downloads, 'boxsets.png', 'boxsets.png', isAction=False)
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


