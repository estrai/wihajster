#!/usr/bin/env python2.7

import httplib
import urllib2
import sys
from pprint import pprint

#from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
#from optparse import OptionParser

if len(sys.argv) < 2:
	print("Please provide a word to look for.")
	sys.exit(0)


def ling_pl(word):
	URL_TEMPLATE = 'http://m.ling.pl/m.php?word=%s'
	url = URL_TEMPLATE % word
	content = BeautifulSoup( urllib2.urlopen(url) )
	divs = content.find_all( 'div' )
	dictionary = []
	for div in divs:
		if not div.has_key('class'):
			continue
		if div['class'][0] == 'dictname':
			dictionary.append("\033[1m%s\033[0m" % div.contents[0])
		if div['class'][0] == 'dictword' or div['class'][0] == 'dictdef':
			dictionary.append(div.contents[0])
#	pprint(dictionary)
	return dictionary

answer = ling_pl(sys.argv[1])

for line in answer:
	print line
