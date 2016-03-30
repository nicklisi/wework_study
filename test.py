import requests
from BeautifulSoup import BeautifulSoup
import sys
import argparse
parser = argparse.ArgumentParser(description='Count Words')
parser.add_argument('url', metavar='URL', type=str,
                    help='a URL')
args = parser.parse_args()
print args.url
response = requests.get(args.url)
soup = BeautifulSoup(response.content)
content = soup.find("div", { "id" : "mw-content-text" })
content_text = content.getText()
content_text_string = content_text.encode('ascii', 'replace')
#content_text = repr(content_text) #convert the unicode to a string 
f = open('workfile', 'r+')
f.write(content_text_string)
print (content_text_string)