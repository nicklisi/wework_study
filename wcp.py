import sys
import requests
import BeautifulSoup
import getopt
from lxml import html

url = sys.argv[1]

print "pinging " + url

page = requests.get(url)

print page

stuff = html.fromstring(page.content)

print stuff
