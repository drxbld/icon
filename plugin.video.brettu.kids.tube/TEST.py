# -*- coding: utf-8 -*-
#------------------------------------------------------------
#  on YouTube by Biggy
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#
# Author: Biggy
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.brettu.kids.tube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')



YOUTUBE_CHANNEL_ID_1 = "PLI-nQtOHVKRu0erW8Khquk1pRvEHDpR7i"

YOUTUBE_CHANNEL_ID_2 = "PL4KpMgN0nsPrnQjDh23RG2KNlfgRKgfc9"

YOUTUBE_CHANNEL_ID_3 = "PL0qkhhDzibUc2_kMx-YcqZ8u9Oknu9xAq"

YOUTUBE_CHANNEL_ID_4 = "PLmdZ3yaBIVIW-OxGcVRCtD63thztEGK4_"

YOUTUBE_CHANNEL_ID_5 = "PLbcNlGLh0jHkA8PORhW_Cv1064VZnm4wZ"

YOUTUBE_CHANNEL_ID_6 = "PLI2i4PrLia3gAAYjMaVbAwdt1xrOsUaXS"

YOUTUBE_CHANNEL_ID_7 = "PLjzMO8jWPaAG3EZAZttX9zeezns7chUvV"

YOUTUBE_CHANNEL_ID_8 = "PLWV_3YPzfkGmsxdG17o-3kHSznuk4JA2H"

YOUTUBE_CHANNEL_ID_9 = "PLNsAcv8D6K154rUTBtTwa2nVIk0Au5_1f"

YOUTUBE_CHANNEL_ID_10 = "PLaPWTs1IOcfwBLH9uqaqTIRq5qj21W-rw"

YOUTUBE_CHANNEL_ID_11 = "PLsSFLraMjNq4hrmzAhEcY0XLT-sAXluQu"

YOUTUBE_CHANNEL_ID_12 = "PLn-mouasam6zXxoyjvncM4AKph8RNBLiz"

YOUTUBE_CHANNEL_ID_13 = "PLGkNyr63YU78ik95KVNB7hixSuPaSZP_z"

YOUTUBE_CHANNEL_ID_14 = "PLZZbX4vIH_0m1Fz493qxLrPkXkn_jsNx8"

YOUTUBE_CHANNEL_ID_15 = "PL1Oh5mKs0g1qVpmZkDzBLCP953d-AWkf0"

YOUTUBE_CHANNEL_ID_16 = "PL84GNxldnv4tIuFll-UBJMVgmnvY2gSCZ"

YOUTUBE_CHANNEL_ID_17 = "PLNUj2jg1L1S4ok-efWnbDgw6FGGOmn3gz"

YOUTUBE_CHANNEL_ID_18 = "PLEED6U9clBc2H8KpI1N73JpYWjg7O4eeQ"

YOUTUBE_CHANNEL_ID_19 = "PLU6jeEdYXZfOqwaU4_wwmGYfIYx7LYM3u"

YOUTUBE_CHANNEL_ID_20 = "PLKtrnoRier7-gHXgZK73a5LD05J_Pplvp"

YOUTUBE_CHANNEL_ID_21 = "PLpFXxE1AkTkNv5oazWZNIPghsVNijIsK7"

YOUTUBE_CHANNEL_ID_22 = "PLo0h8GefOALDxAN8SK7RDR2YhosM5b5Mp"

YOUTUBE_CHANNEL_ID_23 = "PL49595CC6EB8CDDDA"

YOUTUBE_CHANNEL_ID_24 = "PLJZ1Hn7gQL4_FM3BEoMQdTtj93bXmsISL"

YOUTUBE_CHANNEL_ID_25 = "PLqcNVz8UuCsJ0yJ5Td4bxbVHejncVncIj"

YOUTUBE_CHANNEL_ID_26 = "PLxNUaoVw4XbfTB0qrOtjSUF4UZowOfzKB"

YOUTUBE_CHANNEL_ID_27 = "PLNBods2kIOp1HVAbHlCw10jLaKKFkvC8V"

YOUTUBE_CHANNEL_ID_28 = "PLLOqGIRReFjdhESSQajbp3Vwim_6MokE-"

YOUTUBE_CHANNEL_ID_29 = "PLdU-LLwskmq98cWzl8yH5e8uPQw2SwBpE"

YOUTUBE_CHANNEL_ID_30 = "PLcrHHLADQ1n4SDRmeq23R3LGvNfUs6R4V"

YOUTUBE_CHANNEL_ID_31 = "PL6FytxeqgcEga0kEGnWZhqnuXypzYtovc"

YOUTUBE_CHANNEL_ID_32 = "PL0YGmUSvExR3pJvr-yGJjKgWzqwUXFCrX"

YOUTUBE_CHANNEL_ID_33 = "PL3_4ve-ZM3il4vz0kTKY8x6FqIOZ2vB0w"

YOUTUBE_CHANNEL_ID_34 = "PLZk7bahVu06gCmXdBOPs6WlfkLCB22u5K"

YOUTUBE_CHANNEL_ID_35 = "PLxIsIdKe598X87yIlqX2CtlmrgI8ZE7CO"

YOUTUBE_CHANNEL_ID_36 = "PL2F58A7E1B5F8F68E"

YOUTUBE_CHANNEL_ID_37 = "PLljZJGxpu56_vbSzBo8KEFeIE6IeNd6X2"

YOUTUBE_CHANNEL_ID_38 = "PLZs0gQed9tMQ7IS_r09pzwniRzW5hYMG8"

YOUTUBE_CHANNEL_ID_39 = "PLB3b1rGpgV7dT9CNlT8uEDWK9Oh1gG09R"

YOUTUBE_CHANNEL_ID_40 = "PLiEDYlIzEFFlktJgyLDlZqu57G_n9xCZS"

YOUTUBE_CHANNEL_ID_41 = "PLa1veDZhmjzAJGOW0PSS4I3-mpmyCzJqt"

YOUTUBE_CHANNEL_ID_42 = "PLj9VWzXzb8avJEdbLOPYdyybJ2EMOesgf"

YOUTUBE_CHANNEL_ID_43 = "PLuKw1oWzC2BOclAbo6NwpzJuPeZkiHGA2"

YOUTUBE_CHANNEL_ID_44 = "PLXPmGVFhPjW_1gzg5k8Xefrzwb25CamOK"

YOUTUBE_CHANNEL_ID_45 = "PLWCe2QugvDrWlnbmw8lgeeE7DPuNqDcK3"

YOUTUBE_CHANNEL_ID_46 = "PLMXmXFUEBWd0g_pOG81vqvFKVOxKNKEsp"

YOUTUBE_CHANNEL_ID_47 = "PLZs0gQed9tMSElYC30JlPa40L7oFWmQ_C"

YOUTUBE_CHANNEL_ID_48 = "PLgeJ6bGP6EDk6-qW9AflD-0riNB-Er-Mp"

YOUTUBE_CHANNEL_ID_49 = "PLJw-UqEB3j5kGdjWTqWBf7OS6dhF-2CgR"

YOUTUBE_CHANNEL_ID_50 = "PLIoK1f8rH9w0ROXfqEJhvHEWnTiHXWjVA"

YOUTUBE_CHANNEL_ID_51 = "PLHo-IIm0ajO2Tw2W-32OR8fqmgmi9xoc3"

YOUTUBE_CHANNEL_ID_52 = "PL_YBMMtPxA94Hkemk0E2StEMWM3L6IJW7"

YOUTUBE_CHANNEL_ID_53 = "PLWeCsq4nQ2V5E3OutZVcecu5eBlJd25PC"

YOUTUBE_CHANNEL_ID_54 = "PLIZ_JJxZwS5wVP_nvN07IVFM8BYfl8PkE"

YOUTUBE_CHANNEL_ID_55 = "PLsssbVJ2wz5Eshm4mSaasdTpNl97MFcLd"

YOUTUBE_CHANNEL_ID_56 = "PL36RfTuPBQ6u3M3dOmY4eUqHMCfkqMj3c"

YOUTUBE_CHANNEL_ID_57 = "PL_4hXCUn-FQCnjStEjFb2961a6Ff5xvvj"

YOUTUBE_CHANNEL_ID_58 = "PLtkjIm3lsICwPDQolU1z3KgZB4kvvsUBP"

YOUTUBE_CHANNEL_ID_59 = "PLLSc-pZBJUAsj913DZ0FPgQubXbZ84v1V"

YOUTUBE_CHANNEL_ID_60 = "PL0E88D514CD289C52"

YOUTUBE_CHANNEL_ID_61 = "PLj2156-l7FEzFtbUg0HSeU-VXAPKG2h4f"

YOUTUBE_CHANNEL_ID_62 = "PLK-g3awj_KCnpRqbwzSjWO_woK63mGDhF"

YOUTUBE_CHANNEL_ID_63 = "PLmf20YR5_3ib0UIOBsLjfh1x8On6GAX0q"

YOUTUBE_CHANNEL_ID_64 = "PLIEbITAtGBeZP5k0rFk9JqeLBHwr8dKEA"




# Entry point
def run():
    plugintools.log("docu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("docu.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Mickey Mouse Club House",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_1+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/a5/8e/ca/a58ecacebad44ed0c8e32aa9a64727e1--mickey-mouse-wallpaper-watch-full-episodes.jpg",
        folder=True )	
	
    plugintools.add_item( 
        #action="", 
        title="Dora and Friends: Into the City! ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_2+"/",
        thumbnail="https://static-s.aa-cdn.net/img/gp/20600003629854/MvphB0SPX6R_xkarm1KgssWwPSZb49tJP_fV_OqYsmNld23DtCPzYd5v5814ReE8vfw=w300?v=1",
        folder=True )

    plugintools.add_item( 
        #action="", 
        title="Peppa Pig",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_3+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/1179475725/16ab89b20f7add7509e36aa7d757bcb2?v=1",
        folder=True )		
		
    plugintools.add_item( 
        #action="", 
        title="Teletubbies",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_4+"/",
        thumbnail="https://is3-ssl.mzstatic.com/image/thumb/Purple111/v4/ed/97/70/ed9770f7-aad5-ee42-7949-b2c0caa63d36/source/256x256bb.jpg",
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Danger Mouse",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_5+"/",
        thumbnail="https://is3-ssl.mzstatic.com/image/thumb/Purple117/v4/7f/4c/de/7f4cde3d-d18a-65ac-e617-c0e7e81ab2ef/source/256x256bb.jpg",
        folder=True )
  
    plugintools.add_item( 
        #action="", 
        title="Thomas and friends",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_6+"/",
        thumbnail="https://pbs.twimg.com/profile_images/2967350659/f2df9fbd585bbe6fd17d826b86684619.jpeg",
        folder=True )
  
    plugintools.add_item( 
        #action="", 
        title="Lazy Town",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_7+"/",
        thumbnail="https://c-sf.smule.com/sf/s34/arr/c2/13/ebefc994-310c-4cdc-b6dd-0d4e4b705dea.jpg",
        folder=True )		
  
    plugintools.add_item( 
        #action="", 
        title="Sesame Street Songs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_8+"/",
        thumbnail="https://c-sf.smule.com/sf/s24/arr/39/11/23d0cd79-d7d4-4397-8e56-59c285db5661.jpg",
        folder=True )
		 
    plugintools.add_item( 
        #action="", 
        title="Powerpuff Girls Z",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_9+"/",
        thumbnail="https://c-sf.smule.com/sf/s35/arr/ac/a9/bce7ac18-e560-4642-acda-028fa36d9681.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Winnie the Pooh ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_10+"/",
        thumbnail="http://static.wixstatic.com/media/0b1142_169bd577410745a89ed484ede4cfd6e4.jpg_256",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="The Queens Nose",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_11+"/",
        thumbnail="https://static.wixstatic.com/media/5aa587_a0970a72b9db4e478efc31ba7289c7cf~mv2.jpg_256",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="SuperTed",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_12+"/",
        thumbnail="https://lh6.googleusercontent.com/-JaD1FAaXQAo/AAAAAAAAAAI/AAAAAAAAChM/BXbAqJhUSgw/photo.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="The Fairly OddParents",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_13+"/",
        thumbnail="https://c-sf.smule.com/sf/s30/arr/d4/97/a329fb63-1956-4929-b065-a7ef8a65cd92.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="The Octonauts",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_14+"/",
        thumbnail="https://a.wattpad.com/useravatar/joecasey14.256.871174.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Barney & Friends",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_15+"/",
        thumbnail="https://pbs.twimg.com/profile_images/378800000302431426/fc1ef6c669d2e09de4695015a3538738.png",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Bananas in Pyjamas ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_16+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/484824236/17ec40c1713af258a4359fa880219fb2?v=1",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Rugrats ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_17+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/522987268/36879d9d3196f23c53e79b6d1dfead5f?v=1",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Animaniacs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_18+"/",
        thumbnail="https://c-sf.smule.com/sf/s41/arr/58/f0/9a13e324-ffc9-48cd-9c33-fd0acfde12f8.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="In the Night Garden",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_19+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/878619723/44032cd20627830fa6644c4277c9a030?v=1",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Rosie and Jim",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_20+"/",
        thumbnail="https://pbs.twimg.com/profile_images/2983640586/13059b95adbc494e18d814eefea0e5db.jpeg",
        folder=True )			
    plugintools.add_item( 
        #action="", 
        title="Postman Pat",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_21+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/458116091/fa724571ceef95f0c0efada5d064c00e?v=1",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Little Einsteins ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_22+"/",
        thumbnail="https://lh5.googleusercontent.com/-n1NWmOVKLGA/AAAAAAAAAAI/AAAAAAAAABA/Q6EtBsd-oUE/photo.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Woof",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_23+"/",
        thumbnail="https://is2-ssl.mzstatic.com/image/thumb/Purple122/v4/30/13/38/3013380d-6b47-863f-1d32-d38c289106d8/source/256x256bb.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Peg + Cat ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_24+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/945402023/68e9826760dc04a7404c0033c506febf",
        folder=True )			
    plugintools.add_item( 
        #action="", 
        title="Inspector Gadget",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_25+"/",
        thumbnail="https://pbs.twimg.com/profile_images/656209608164380676/GRengFhW.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Dexter's Laboratory ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_26+"/",
        thumbnail="http://files.igameu.com/app/1823/7ee81b906134c1be3e5a60b76168f906-256.png",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Bob the Builder",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_27+"/",
        thumbnail="https://pbs.twimg.com/profile_images/630942591333310464/4gyqQe_h.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Fireman Sam ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_28+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/606910110/c3163dd5f243e3c2e6afa0592e75b2ba?v=1",
        folder=True )			
    plugintools.add_item( 
        #action="", 
        title="Dinosaur Train ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_29+"/",
        thumbnail="https://is1-ssl.mzstatic.com/image/thumb/Purple122/v4/8b/62/c7/8b62c77d-9227-6dc9-5066-a2eacd235df7/source/256x256bb.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="The Magic School Bus ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_30+"/",
        thumbnail="https://is5-ssl.mzstatic.com/image/thumb/Purple71/v4/12/1f/3d/121f3d5e-f62e-13bb-9af4-00e81799e87d/source/256x256bb.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="DuckTales",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_31+"/",
        thumbnail="http://pm1.narvii.com/6260/095e2a8316c14ff980bed1e13244ec3ed0cc81ec_hq.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Clangers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_32+"/",
        thumbnail="https://is4-ssl.mzstatic.com/image/thumb/Purple6/v4/91/c9/cb/91c9cb92-0bad-2463-985e-f74087ca5b17/source/256x256bb.jpg",
        folder=True )			
    plugintools.add_item( 
        #action="", 
        title="Pingu",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_33+"/",
        thumbnail="https://pbs.twimg.com/profile_images/2845625946/cf319871ac781cbabb0bbbcb925fbd40.jpeg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Poddington Peas ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_34+"/",
        thumbnail="https://pbs.twimg.com/profile_images/680070536882450432/KhRBblrG.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Art Attack",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_35+"/",
        thumbnail="https://is5-ssl.mzstatic.com/image/thumb/Purple71/v4/d2/af/ba/d2afba0c-4b5e-9e1d-6673-a4eb8861e60a/source/256x256bb.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="The Busy World of Richard Scarry ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_36+"/",
        thumbnail="https://images-na.ssl-images-amazon.com/images/I/71L394-Xl3L._CR145,0,669,669_UX256.jpg",
        folder=True )			
    plugintools.add_item( 
        #action="", 
        title="Snoopy",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_37+"/",
        thumbnail="https://s-media-cache-ak0.pinimg.com/736x/e9/19/b8/e919b8839a262b919fce50ee3cb7ff9c--peanuts-cartoon-the-peanuts.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="THE WOMBLES",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_38+"/",
        thumbnail="https://d1dy244g59v5jo.cloudfront.net/artist-07/076f3802c7bb69ff4447db7837f53ef53a8f1bb12fe0ef440707af9450e039eab8df9119.jpg.256x256.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Woody Woodpecker",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_39+"/",
        thumbnail="https://pbs.twimg.com/profile_images/378800000493384102/b0e4c44787268be6fe15ddc8d67b69c4.jpeg",
        folder=True )			
    plugintools.add_item( 
        #action="", 
        title="Curious George ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_40+"/",
        thumbnail="https://superrepo.org/static/images/icons/original/xplugin.video.curiousgeorge.png.pagespeed.ic.aug_MF5sRz.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Goosebumps",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_41+"/",
        thumbnail="https://pbs.twimg.com/profile_images/378800000272859583/5f6bde83dc5274e3c35f95f9793584f4.jpeg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="The Amazing World Of Gumball ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_42+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/572508337/0391a34c5e7344e90675387c0d885c17?v=1",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Hannah Montana",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_43+"/",
        thumbnail="https://pbs.twimg.com/profile_images/3199743670/2e3e5d19b96f6713844fae5361754bfb.jpeg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="The Adventures of Jimmy Neutron",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_44+"/",
        thumbnail="https://c-sf.smule.com/sf/s38/arr/77/02/7f391819-03f0-4e8e-b5dc-415125fe0820.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Dennis the Menace and Gnasher",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_45+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/936735546/158a56148a15d187fd031dfc4975f973?v=1",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Fat Albert and the Cosby Kids ",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_46+"/",
        thumbnail="https://pbs.twimg.com/profile_images/731958253161172992/4Pbi1MzU.jpg",
        folder=True )			
    plugintools.add_item( 
        #action="", 
        title="SPIDER-MAN",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_47+"/",
        thumbnail="https://rkuykendall.github.io/wheretostartreading/spider-man/thumb-usm1.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="X-Men",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_48+"/",
        thumbnail="http://www.androidpolice.com/wp-content/uploads/2011/06/image154.png",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="TaleSpin",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_49+"/",
        thumbnail="https://c-sf.smule.com/sf/s24/arr/60/da/1693ba4c-e36d-483f-87f1-fcced1383ba0.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Martin Mystery",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_50+"/",
        thumbnail="https://pbs.twimg.com/profile_images/668478201790877696/nb17Bxju.png",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Scooby Doo",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_51+"/",
        thumbnail="https://c-sf.smule.com/sf/s24/arr/00/5e/f72e2103-a5ee-4be8-8507-cf909bef13a9.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Wizards Of Waverly Place",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_52+"/",
        thumbnail="https://a.wattpad.com/useravatar/Storywriter1786.256.872672.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Smurfs",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_53+"/",
        thumbnail="https://is2-ssl.mzstatic.com/image/thumb/Purple127/v4/80/98/55/80985578-6248-e00d-804b-b41f4dfe924d/source/256x256bb.jpg",
        folder=True )			
    plugintools.add_item( 
        #action="", 
        title="Garfield & Garfield and Friends",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_54+"/",
        thumbnail="https://static-s.aa-cdn.net/img/ios/1085405231/174178b211be7f7682f2e84cbfdbd28a",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Popeye",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_55+"/",
        thumbnail="https://is5-ssl.mzstatic.com/image/thumb/Purple71/v4/68/df/9b/68df9b38-5423-b65a-7093-7323acbceae3/source/256x256bb.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Justice League",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_56+"/",
        thumbnail="https://pbs.twimg.com/profile_images/689095300514971648/my8mLLL2.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="The Yogi Bear Show",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_57+"/",
        thumbnail="https://pbs.twimg.com/profile_images/635472091081367552/X_zHZEgc.png",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Pokémon",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_58+"/",
        thumbnail="http://pa1.narvii.com/6327/5ec6536a77b7b8e47fb66a0590b09a1289331dbd_hq.gif",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Thundercats",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_59+"/",
        thumbnail="https://c-sf.smule.com/sf/s24/arr/81/18/24b567fc-f813-4ac7-9ebc-004bf0dc3777.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Transformers",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_60+"/",
        thumbnail="https://is2-ssl.mzstatic.com/image/thumb/Purple117/v4/5d/67/6b/5d676b71-3c2f-2818-3229-dbbdbd54f1c4/source/256x256bb.jpg",
        folder=True )			
    plugintools.add_item( 
        #action="", 
        title="Invader Zim",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_61+"/",
        thumbnail="https://a.wattpad.com/useravatar/InvaderStupidInside.256.310827.jpg",
        folder=True )	
    plugintools.add_item( 
        #action="", 
        title="Rocky & Bullwinkle",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_62+"/",
        thumbnail="http://1.bp.blogspot.com/-vPChHG0QeGQ/TmgUu1ann0I/AAAAAAAAAGQ/6et5DNnIdU4/s320/bullwinkle.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="CatDog",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_63+"/",
        thumbnail="https://c-sf.smule.com/sf/s39/arr/cc/75/1eae2890-9dad-4af3-9ff5-35f61f3bf4c3.jpg",
        folder=True )		
    plugintools.add_item( 
        #action="", 
        title="Darkwing Duck",
        url="plugin://plugin.video.youtube/playlist/"+YOUTUBE_CHANNEL_ID_64+"/",
        thumbnail="https://c-sf.smule.com/sf/s24/arr/72/b0/d9a43b8c-5d15-4290-97fc-2b452d033adf.jpg",
        folder=True )		
run()
