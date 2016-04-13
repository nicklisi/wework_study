import requests
from BeautifulSoup import BeautifulSoup
import sys
import argparse
parser = argparse.ArgumentParser(description='Count Words')
parser.add_argument('url', metavar='URL', type=str,
                    help='a URL')
args = parser.parse_args()
print args.url

#make the http request for the URL we supplied
response = requests.get(args.url)

#instantiate a beautifulsoup parser object using the content from the request we just made
soup = BeautifulSoup(response.content)

#look for the mw-content-text div on a wikipedia page
content = soup.find("div", { "id" : "mw-content-text" })

#getText the content object to get just the text without tags
content_text = content.getText(separator=u' ')

#getText returns a unicode encoded string which is difficult to work with, I was getting errors. attempting to encode it to ascii
content_text_string = content_text.encode('ascii', 'replace')

#content_text_string = repr(content_text) #another method I was trying for encoding

#write the output to a file called workfile so we can look at the entire output 
f = open('workfile', 'w+')
f.write(content_text.encode('utf-8'))

#also print to terminal
print (content_text_string)