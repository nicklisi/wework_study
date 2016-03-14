import requests
import BeautifulSoup
import sys
import getopt

print sys.argv[1]

url = sys.argv[1]
page = requests.get(url)

print page.content