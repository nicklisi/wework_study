import random 

class Troll:
  def __init__(self, name):
    self.name = name
  
  def say_name(self):
    return "Yo, Jerkface. I'm " + self.name + ", maybe."

  def reply_sincerely(self, stupid_comment):
  	foo = [
  		   ' <-- You are an idiot' ,
  		   ' <-- Your face is too round!' ,
  		   ' <-- You should really get a new name' ,
  		   ' <-- You are not even worthy of a mean comment' ,
  		   ' <-- Have you noticed that your nose is too big?',
  		   ' <--Who is the Troll now?!' ,
  		   ' <-- Are you sure about that...?'
  		   ]

  	return stupid_comment + random.choice(foo)

Bob_Troll = Troll("Bob")
print Bob_Troll.say_name()

Liz_Troll = Troll("Liz")
bobs_name = Bob_Troll.say_name()
print Liz_Troll.reply_sincerely(bobs_name)