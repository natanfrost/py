#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from urllib2 import urlopen
from requests import get
from bs4 import BeautifulSoup
from os import system

from json import loads

script, lang, query = argv

def success(query):
	os.system("clear")
	print """
	\033[0;37m
	██████╗ ██╗   ██╗██╗    ██╗██╗██╗  ██╗██╗
	██╔══██╗╚██╗ ██╔╝██║    ██║██║██║ ██╔╝██║
	██████╔╝ ╚████╔╝ ██║ █╗ ██║██║█████╔╝ ██║
	██╔═══╝   ╚██╔╝  ██║███╗██║██║██╔═██╗ ██║
	██║        ██║   ╚███╔███╔╝██║██║  ██╗██║
	╚═╝        ╚═╝    ╚══╝╚══╝ ╚═╝╚═╝  ╚═╝╚═╝
    	Developed by \033[1;37mArsh Leak.\033[0;37m (github.com/4rsh)\033[0m
	"""

def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

def wiki_ok(lang, query):
	query_search = {'action': 'parse',
					'prop': 'text',
					'format': 'json',
					'section': '0',
					'page': query}
	search = get("https://%s.wikipedia.org/w/api.php?action=query" % lang, params=query_search, verify=False)

	if search.status_code != 200:
		print "\033[1;31mError in connection, or your search was not found.\033[0m\n"
	else:
		conn = BeautifulSoup(search.content)
		result = conn.findAll('p')[1] # get the first paragraph of page

		print '\033[1;31m%s\033[0m"' % result.text

def wiki_error():
	print "\n\033[1;37mSomething is wrong, you used:\033[0;37m\n$ python %s --yourtld Query ?\n\033[0m" % script

if "--" in lang:
	lang = lang.replace("--", "")
	wiki_ok(lang, query)

else:
	wiki_error()
