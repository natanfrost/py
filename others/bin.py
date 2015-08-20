# -*- coding: utf-8 -*-

from requests import get
from json import loads
#from io import open

path ='/home/diamond/Documents/py/others/bins.txt'
save_path = '/home/diamond/Documents/py/others/bins_verificados.txt'

def verifica_bins():
    f = open(path, 'r')
    count = 1
    new_file = open(save_path, 'w')
    for line in f:
        print count
        count += 1
        new_file.write(get_bank(line))
    new_file.close()
    f.close()
    print "Terminou."

def get_bank(bin):
    END_POINT = 'http://www.binlist.net/json/%s' % bin
    response = get(END_POINT, verify=False)
    retorno = ''
    if response.status_code != 404:
        banco = loads(response.content)['bank']
        if banco:
            retorno = banco
        else:
            retorno = 'NAO ENCONTRADO'
    else:
        retorno = 'NAO ENCONTRADO'
    return '%s\t%s\n' % (bin.rstrip(), retorno)
