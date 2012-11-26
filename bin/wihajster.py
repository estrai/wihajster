#!/usr/bin/env python

import http.client
import urllib.parse
import sys

#from optparse import OptionParser

if len(sys.argv) < 2:
	print("Please provide a word to look for.")
	sys.exit(0)

print(sys.argv[1])


def lingpl(word):
#	...

