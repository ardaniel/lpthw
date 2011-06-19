# Basic setup for Exercise 43's adventure game.
# Generating all my room setups first,
# then hacking on the engine and mapping....

from random import choice

class MainHub(object):

# Eventually I'd like the codeword to be randomly selected; not there yet

	def room_setup(self):
		room_desc = """
This is the main hub of the space station. There is a 
guide here.  He tells you to go north to the Diplomatic Office
and give the Chief Diplomat the codeword 'cookie.'"
"""
		print room_desc
		
		move = raw_input("> ")
		
		if "north" in move and "do not" not in move:
			print "The guide smiles and you head north."
			return 'DiplomatRoom'

		else:
			print "The guide looks at you and gestures north again."
			return 'MainHub'
			
class DiplomatRoom(object):
	def room_setup(self):
		room_desc = """This is the office of the station's chief diplomat.
She smiles and asks you for the codeword."""

		print room_desc
		codeguess = raw_input("> ")
		
		if "cookie" in codeguess:
			print "She hands you an envelope and points you to the door to the right."
			return 'AlienRoom'
			
		else:
			print 'She looks appalled and pushes a button on her desk. "Intruder!" she yells,'
			print "and you are sucked into a tube and vented into space, where you die."
			return 'death'
		
class AlienRoom(object):
	def room_setup(self):
		room_desc = """This room is hot, and a little damp, and contains the biggest,
leafiest alien you've ever seen.  It extends a tendril towards you inquiringly."""

		print room_desc
		offer_item = raw_input("> ")
		
		if "give" in offer_item and "envelope" in offer_item and "do not" not in offer_item:
			print "You think the alien looks pleased; it takes the envelope and"
			print "promptly digests it.  One of its vines points you back to the diplomat's office."
			print "(You think you hear a noise in there...)"
			return 'DiplomatOffice2'
			
		else:
			print "The alien shrugs and eats you, the faster to obtain the envelope."
			print "You might be pooped out in 500 years."
			return 'death'

class DiplomatOffice2(object):
	def room_setup(self):
		room_desc="""Back in the diplomat's office, you find that she's been replaced with a robot.
It levels a blaster at you and fires."""

		print room_desc
		evade = raw_input("> ")
		
		if ("dodge" or "move") and not ("don't" or "do not") in evade:
			print "You dodge expertly.  You spot a shiny plaque on the wall near your head."
			print "What are you going to do now? The robot prepares to fire again."
			
			grab = raw_input("> ")
			
			if "plaque" in grab:
				print "You hold the plaque in front of you as the robot fires."
				print "The blast strikes the plaque, bounces off, and hits the robot."
				print "The robot explodes, leaving a chip behind. You pocket the chip and go"
				print "back to the main hub."
				return 'MainHub2'
			
			else:
				print "The robot shoots you dead.  Station security finds"
				print "your corpse and assumes you killed the diplomat,"
				print "making you a posthumous assassin.  Way to go, pal."
				return 'death'

		else:
			print "You fail to dodge. The robot blows a hole in your head."
			print "Everyone assumes you killed the diplomat. Alien relations"
			print "are set back a billion years because you didn't move. You suck."
			return 'death'

d2 = DiplomatOffice2()
d2.room_setup()