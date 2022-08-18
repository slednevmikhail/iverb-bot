import re

import requests  # установи
import pickle  # дефолтная хуйня устанавливать не надо
from bs4 import BeautifulSoup  # установить

read_filehandler = open('players.pickle', 'rb')
player_id_list = pickle.load(read_filehandler)
read_filehandler.close()

map_filehandler = open('maps_list.pickle', 'rb')
map_dict = pickle.load(map_filehandler)
map_filehandler.close()

def load_players():
    read_filehandler = open('players.pickle', 'rb')
    player_id_list = pickle.load(read_filehandler)
    read_filehandler.close()


def add_player(iverb_id):  # для добавления игроков
    load_players()
    if not is_exists(iverb_id) or iverb_id in player_id_list:
        return False
    player_id_list.append(iverb_id)  # да, да. player_id это стим айди. мне похуй
    save_players()
    return True


def is_exists(iverb_id):
    player_page = requests.get(f'https://board.portal2.sr/profile/{iverb_id}')
    page_soup = BeautifulSoup(player_page.text, 'lxml')
    nickname = page_soup.find('div', class_='nickname')
    return nickname!= None and nickname.text != ''


def remove_player(player_id):
    load_players()
    player_id_list.remove(player_id)
    save_players()


class Player:
    def __init__(self, boardname, time, rank):
        self.rank = rank
        self.time = time
        self.name = boardname


def get_results(iverb_id, page_soup):  # это не суй в бота
    score_ref = page_soup.find(href=re.compile(iverb_id))
    if score_ref is None:
        return Player('', '999', '999')
    score_info = score_ref.parent.parent
    time = score_info.find('a', class_='score').text
    rank = score_info.find(class_='rank').text
    boardname = score_info.find(class_='boardname').text
    return Player(boardname, time, rank)

    pass


def save_players():  # это не суй в бота
    edit_fileholder = open('players.pickle', 'wb')
    pickle.dump(player_id_list, edit_fileholder)
    edit_fileholder.close()


def get_map_players(map_name):
    map_link = get_map_link(map_name)
    map_page = requests.get(f'https://board.portal2.sr{map_link}')
    page_soup = BeautifulSoup(map_page.text, 'lxml')
    result_list = []
    for player_id in player_id_list:
        player = get_results(player_id, page_soup)
        result_list.append(player)
    result_list.sort(key=lambda p: int(p.rank))
    return result_list
    pass


def get_map_link(map_name):
    return map_dict[map_name.lower()]
    pass



def Test(): #ИДИ НАХУЙ
    #print(is_exists('228123'))
    #print(is_exists('тюбик'))
    #print(is_exists('76561198015267733'))
    get_map_players('Core')