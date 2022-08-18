import requests
from bs4 import BeautifulSoup
import pickle



sp_html = requests.get('https://board.portal2.sr/chambers/sp')
coop_html = requests.get('https://board.portal2.sr/chambers/coop')

sp_soup = BeautifulSoup(sp_html.text, 'lxml')
coop_soup = BeautifulSoup(coop_html.text, 'lxml')

map_dict = {}
sp_maps = sp_soup.find_all(class_='titlebg')
coop_maps = coop_soup.find_all(class_='titlebg')

for map in sp_maps:
    map_dict[map.text.lower()] = map.find('a').get('href')
for map in coop_maps:
    map_dict[map.text.lower()] = map.find('a').get('href')

filehandler = open('maps_list.pickle', 'wb')
pickle.dump(map_dict, filehandler)
filehandler.close()
pass