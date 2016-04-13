class TrollBot():
	def __init__(self, name):
		self.name = name
	def reply_to(self, event):
		print "inspecting event of type '" + event["type"] + "'"
		if event["type"] == "message":
			# Skip the message if it's from a bot.
			if "subtype" in event and event["subtype"] == "bot_message":
				return None
			try:
				# Search the message for a keyword. If not found, throws ValueError.
				unicode.index(event["text"], "tuesday")
				# Return the response text!
				return "Someone said tuesday. Reminder: did anyone reserve the room?"
			except ValueError:
				pass
		return None
