class Troll:
	def __init__(self, name):
		self.name = name

	def say_name(self):
		return "My name is " + self.name
	def reply_insincerely(self, comment):
		return "\"" + comment + "\", wowwww, soooo smart. I can tell you worked really hard on that comment"
		

Bob_troll = Troll("Bob")
print Bob_troll.reply_insincerely("I think this is an intelligent video")