# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from requests import get
from os import path, makedirs
from urllib import urlretrieve
import sys
import re
import anime_list
import time


mother_of_urls = 'http://anitubebr.xpg.uol.com.br/categories/{penultimo}/{ultimo}'
jwp_config_url = 'http://anitubebr.xpg.uol.com.br/player/config.php?key={key}'

def get_total_pages(url):
    try:
        print 'Pegando o total de paginas do link: ' + url
        try:
            req = get(url)
        except Exception as er:
            print 'erro: ' + str(er)
            time.sleep(5)
            return get_total_pages(url)

        soup = BeautifulSoup(req.text, 'html.parser')
        ultimo = soup.select('#pagination-flickr > li')[-1].getText() # pega o útlimo elemento
        req.close()

        if ultimo == "Next": # se for next o ultimo elemento, pega o penultimo e percorre de novo
            possivel_ultimo = soup.select('#pagination-flickr > li')[-2].getText()
            soup.decompose()
            if 'page' in url:
                return int(get_total_pages(mother_of_urls.format(penultimo='page', ultimo=possivel_ultimo)))
            else:
                return int(get_total_pages(adjust_url(url, possivel_ultimo)))
        else:
            return int(ultimo)
    except Exception as e:
        print 'Exception: ' + str(e)
        time.sleep(5)
        get_total_pages(url)

def iterate_pages(url):
    try:
        total_pages = get_total_pages(url)
        url_splited_len = len(url.split('/'))
        print 'preparando para iterar pela url ' + url
        for value in range(1, total_pages + 1):
            print 'pagina %i de %i' % (value, total_pages)
            # pega todos elementos da pagina 'value'

            if 'page' in url:
                req = get(mother_of_urls.format(penultimo='page', ultimo=str(value)))
            else:
                req = get(adjust_url(url, str(value)))

            soup = BeautifulSoup(req.text, 'html.parser')
            print 'pegando os elementos da url ' + req.url
            page_elements = soup.findAll('div', { 'class': 'mainBox' })
            iterate_page_elements(page_elements, req.url)
            soup.decompose()
            req.close()
        anime_list.clear_list()
        anime_list.serialize_list()
    except Exception as e:
        print 'Exception: ' + str(e)
        time.sleep(5)
        iterate_pages(url)

def iterate_page_elements(page_elements, url):
    try:
        print 'iterando elementos do link ' + url
        if 'page' in url:
            for value in page_elements[0].findAll('div', { 'class': 'videoThumb' }):
                iterate_pages(value.find('a')['href'])
        else:
            print 'procurando dados do episódio'
            for value in page_elements[1].findAll('div', { 'class': 'videoThumb' }):
                search_episodes(value)
    except Exception as e:
        print 'Exception: ' + str(e)
        time.sleep(5)
        iterate_page_elements(page_elements, url)

def save_img(link, name):
    name = name.replace('/', ' ')
    img_path = path.dirname(path.abspath(__file__)) + '/imgs/'

    if not path.isfile(img_path + name + '.jpg'):
        print 'salvando imagem ' + name.encode('utf-8')
        urlretrieve(link, img_path + name + '.jpg')
    else:
        print 'imagem {img} ja existe'.format(img=name.encode('utf-8'))

def get_anime_name(div_container):
    detail_div = div_container.find('div', { 'class': 'viewVideoDetail' })
    if detail != None:
        return detail.find('img')['src'].encode('utf-8')

def search_episodes(page_elements):
    try:
        link = page_elements.find('a')['href']

        req = get(str(link.encode('utf-8')))
        soup = BeautifulSoup(req.text, 'html.parser')
        req.close()
        if soup.find('li', { 'class': 'videoDesc'}) != None:
            description = soup.find('li', { 'class': 'videoDesc'}).text
            date_added = soup.select('.viewVideoText > span')[0].getText()
            name = soup.select('.viewVideoTags > a')[-1].getText()
            name = name.replace('/', ' ') # ajusta o nome
            jwkey = soup.find('iframe')['src'].split('/')[len(soup.find('iframe')['src'].split('/')) -1] # pega só a key no final do link
            #soup.decompose()
            if anime_list.contains(name) == False:
                anime = anime_list.Anime(name, description, date_added, jwkey)
                anime_list.add_anime(anime)
            else:
                anime = anime_list.search_anime(name)

            req = get(jwp_config_url.format(key=anime.jwkey))

            episode_name = soup.find('h1', { 'class': 'mainBoxHeader' }).text
            url = None
            for line in req.text.splitlines():
                episode = anime_list.Episode(episode_name)
                if 'file' in line and 'mp4' in line:
                    url = str(re.findall('"([^"]*)"', line))
                if 'label' in line:
                    if 'HD' in line.upper():
                        episode.hd = url
                    else:
                        episode.sd = url
                        anime.add_episode(episode)
    except Exception as e:
        print 'Exception: ' + str(e)
        time.sleep(5)
        search_episodes(page_elements)

def adjust_url(url, possivel_ultimo):
    try:
        print 'ajustando url ' + url
        splited_url = url.split('/')
        if len(splited_url) == 6: #url n tem ainda a paginação no link
            new_url = mother_of_urls.format(penultimo=splited_url[-2], ultimo=possivel_ultimo + '/' + splited_url[-1])
        elif len(splited_url) == 7:
            new_url = mother_of_urls.format(penultimo=splited_url[-3], ultimo=possivel_ultimo + '/' + splited_url[-1])
        print 'url ajustada ' + new_url
        return new_url
    except Exception as e:
        print 'Exception: ' + str(e)
        time.sleep(5)
        adjust_url(url, possivel_ultimo)

print iterate_pages('http://anitubebr.xpg.uol.com.br/categories/page/1')
