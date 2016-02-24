import json
from os import path

anime_list = list()

def clear_list():
    anime_list = list()

def jdefault(o):
    return o.__dict__

def serialize_list():
    json_result = json.dumps(anime_list, indent=4, default=jdefault)
    caminho = path.dirname(path.abspath(__file__)) + '/dump_result.json'
    file = open(caminho, 'w')
    file.write(json_result)
    file.close()

def add_anime(anime):
    anime_list.append(anime)

def search_anime(name):
    return [anime for anime in anime_list if anime.name == name][0]

def contains(name):
    for anime in anime_list:
        if anime.name == name:
            return True
    return False

def iterate(show_episodes=False):
    for value in anime_list:
        print 'Name: %s' % value.name.encode('utf-8')
        if show_episodes == True:
            for episode in value.episode_list:
                print 'Episode: %s - Url:' % (episode.name.encode('utf-8'))

class Anime:
    def __init__(self, name, description, data_added, jwkey):
        self.name = name
        self.description = description
        self.data_added = data_added
        self.jwkey = jwkey
        self.episode_list = list()

    def add_episode(self, episode):
        self.episode_list.append(episode)

class Episode:
    def __init__(self, name, hd, sd):
        self.name = name
        self.hd = hd
        self.sd = sd

    def __init__(self, name):
        self.name = name
