import sys
import requests
# import BeautifulSoup
import getopt
from lxml import html

url = sys.argv[1]
page = requests.get(url)
tree = html.fromstring(page.content)
text_array = tree.xpath('//div[@id="mw-content-text"]/p//text()[not(ancestor::sup)]')
text = "".join(text_array)
print text.encode("utf-8")

