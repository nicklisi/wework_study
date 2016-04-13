import config
import time
import json
import re

from slackclient import SlackClient
sc = SlackClient(config.web_token)

if sc.rtm_connect():
	sc_return = sc.api_call(
		"search.messages", query="http", channel="random"
	)
	
	f = open('workfile', 'w+')
	f.write(json.dumps(sc_return))
	#print sc_return['messages']['matches'][0]['text']
	for thing in sc_return['messages']['matches']:
		if(thing['username'] != "link archive bot"):
			matchObj = re.match( r'(.*)(\<http.*?\>)', thing['text'], re.M|re.I|re.S)
			if matchObj:
				link = matchObj.group(2)
				#sc.api_call(
				#	"chat.postMessage", channel="bot_testing", text=link,
				#	    username="Link Archive Bot", icon_emoji=':robot_face:'
				#)
				#time.sleep(1)
				print link;
			else:
				print "darn"
			#print thing['text'].encode('ascii')
			#f.write(thing['text'] + "\n")
		#print sc_return
else:
    print "Connection Failed, invalid token?"
