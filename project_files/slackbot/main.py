import config
import time

from trollbot import TrollBot
bot = TrollBot(config.name)

from slackclient import SlackClient
sc = SlackClient(config.web_token)

if sc.rtm_connect():
    while True:
		time.sleep(1)
		for event in sc.rtm_read():
			response = bot.reply_to(event)
			if response:
				sc.api_call(
				    "chat.postMessage", channel=config.channel, text=response,
				    username=config.name, icon_emoji=':robot_face:'
				)
else:
    print "Connection Failed, invalid token?"
