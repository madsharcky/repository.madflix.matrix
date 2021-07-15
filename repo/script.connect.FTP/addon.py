import xbmcaddon
import xbmcgui
import xbmc
import argparse
import os.path
import xml.etree.ElementTree as ET
import sqlite3

#make location folder
addon = xbmcaddon.Addon()
addonid= addon.getAddonInfo('id')
KodiFolder = xbmc.translatePath("special://home")
savelocation = xbmc.translatePath("special://userdata")
getlocation =  KodiFolder+"/addons/"+addonid+"/resources"

# Launch a dialog box in kodi giving the user Input methods
dialog=xbmcgui.Dialog()
username = dialog.input("Please enter username: ", type=xbmcgui.INPUT_ALPHANUM)
pwd= dialog.input("Now enter your Passsword: ", type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.ALPHANUM_HIDE_INPUT)

#edit mediasources file 
mediasources = ET.parse(getlocation+"/mediasources.xml")
root = mediasources.getroot()
for elem in root.iter("location"):
    elem.text = "ftp://"+username+":"+pwd+"@4k6qpf10oygosoxr.myfritz.net:990/"
mediasources.write(savelocation+"/mediasources.xml")

#edit sources file
sources=ET.parse(getlocation+"/sources.xml")
root=sources.getroot()
video=root.find("video")
for source in video.findall("source"):
    name = source.find("name")
    path = source.find("path")
    path.text = "ftp://"+username+":"+pwd+"@4k6qpf10oygosoxr.myfritz.net:990/"+name.text
sources.write(savelocation+"/sources.xml")

#adding to Video Database
conn = sqlite3.connect(savelocation +"/Database/MyVideos119.db")
c=conn.cursor()
c.execute(""" DELETE FROM "main"."path" """)
c.execute(""" INSERT INTO "main"."path" ("idPath", "strPath", "strContent", "strScraper", "strHash", "scanRecursive", "useFolderNames", "strSettings", "noUpdate", "exclude", "allAudio", "dateAdded", "idParentPath") VALUES ('2', 'ftp://"""+username+":"+pwd+"""@4k6qpf10oygosoxr.myfritz.net:990/Deutsch/', 'movies', 'metadata.themoviedb.org.python', '', '2147483647', '1', '<settings version="2"><setting id="certprefix" default="true">Rated </setting><setting id="fanart">true</setting><setting id="imdbanyway" default="true">false</setting><setting id="keeporiginaltitle" default="true">false</setting><setting id="landscape" default="true">false</setting><setting id="language">de-DE</setting><setting id="RatingS">IMDb</setting><setting id="tmdbcertcountry" default="true">us</setting><setting id="trailer">true</setting></settings>', '0', '0', '0', '', ''); """)
c.execute(""" INSERT INTO "main"."path" ("idPath", "strPath", "strContent", "strScraper", "strHash", "scanRecursive", "useFolderNames", "strSettings", "noUpdate", "exclude", "allAudio", "dateAdded", "idParentPath") VALUES ('3', 'ftp://"""+username+":"+pwd+"""@4k6qpf10oygosoxr.myfritz.net:990/Nur English/', 'movies', 'metadata.themoviedb.org.python', '', '2147483647', '1', '<settings version="2"><setting id="certprefix" default="true">Rated </setting><setting id="fanart">true</setting><setting id="imdbanyway" default="true">false</setting><setting id="keeporiginaltitle" default="true">false</setting><setting id="landscape" default="true">false</setting><setting id="language" default="true">en</setting><setting id="RatingS">IMDb</setting><setting id="tmdbcertcountry" default="true">us</setting><setting id="trailer">true</setting></settings>', '0', '0', '0', '', '');""")
c.execute("""INSERT INTO "main"."path" ("idPath", "strPath", "strContent", "strScraper", "strHash", "scanRecursive", "useFolderNames", "strSettings", "noUpdate", "exclude", "allAudio", "dateAdded", "idParentPath") VALUES ('4', 'ftp://"""+username+":"+pwd+"""@4k6qpf10oygosoxr.myfritz.net:990/Serien/', 'tvshows', 'metadata.tvshows.themoviedb.org.python', '', '0', '0', '<settings version="2"><setting id="alsoimdb" default="true">false</setting><setting id="certprefix" default="true"></setting><setting id="fallback">true</setting><setting id="fanarttvart">true</setting><setting id="keeporiginaltitle" default="true">false</setting><setting id="language" default="true">en</setting><setting id="RatingS">IMDb</setting><setting id="titleprefix" default="true">Episode </setting><setting id="titlesuffix" default="true"></setting><setting id="tmdbart">true</setting><setting id="tmdbcertcountry" default="true">us</setting><setting id="tvdbwidebanners">true</setting></settings>', '0', '0', '0', '', '');""")
conn.commit()
conn.close()