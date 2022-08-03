import requests
from bs4 import BeautifulSoup
import pprint

#
# gamestop = requests.get("https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html")
# soup = BeautifulSoup(gamestop.text, "lxml")

bb = requests.get("https://www.target.com/p/playstation-5-console/-/A-81114595#lnk=sametab")
bbsoup = BeautifulSoup(bb.text, 'lxml')

pprint.pprint(bbsoup.body)
# bbtext = bbsoup.get_text()
#
# pprint.pprint(bbtext)
#
