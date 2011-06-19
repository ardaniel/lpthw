# Basic setup for Exercise 43's adventure game.
# Generating all my room setups first,
# then hacking on the engine and mapping....

from sys import exit

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
		room_desc = """
This is the office of the station's chief diplomat.
She smiles and asks you for the codeword.
"""

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
		room_desc = """
This room is hot, and a little damp, and contains the biggest,
leafiest alien you've ever seen.  It extends a tendril towards you inquiringly.
"""

		print room_desc
		offer_item = raw_input("> ")
		
		if "give" in offer_item and "envelope" in offer_item and "do not" not in offer_item:
			print "You think the alien looks pleased; it takes the envelope and"
			print "promptly digests it.  One of its vines points you back to the diplomat's office.\n"
			print "(You think you hear a noise in there...)"
			return 'DiplomatOffice2'
			
		else:
			print "The alien shrugs and eats you, the faster to obtain the envelope."
			print "You might be pooped out in 500 years."
			return 'death'

class DiplomatOffice2(object):
	def room_setup(self):
		room_desc = """
Back in the diplomat's office, you find that she's been replaced with a robot.
The robot levels a blaster at you and fires.
"""

		print room_desc
		evade = raw_input("> ")
		
		if ("dodge" or "move") and not ("don't" or "do not") in evade:
			print "You dodge expertly.  You spot a shiny plaque on the wall near your head."
			print "What are you going to do now? The robot prepares to fire again."
			
			grab = raw_input("> ")
			
			if "plaque" in grab:
				print "You grab the plaque and hold it in front of you as the robot fires."
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

class MainHub2(object):
	def room_setup(self):
		room_desc = """
You return to the main hub to find the guide there, a robot, and the
diplomat.  All three of them hold out their hand for the chip.  Whom do you give it to?
"""

		print room_desc
		give_chip = raw_input("> ")
		
		if "guide" in give_chip:
			print "The guide hands the chip to the diplomat, then motions you to"
			print "follow them out the side door as he shoot down the robot with"
			print "a hidden blaster."
			return 'SideDoor'
			
		elif "robot" in give_chip:
			print "The robot takes the chip, shoots you, kidnaps the diplomat,"
			print "and runs for the door, covered by the traitorous guide!"
			print "Way to go, idiot-- didn't that other robot try to kill you?"
			return 'death'
		
		elif "diplomat" in give_chip:
			print "The diplomat takes the chip, then turns around and disables"
			print "the robot with a tiny blaster hidden in her sleeve. She"
			print "motions to you and the guide to escape through a side door."
			return 'SideDoor'
			
class SideDoor(object):
	def room_setup(self):
		room_desc = """
You pile out the side door with the guide and the diplomat.  There is a four-man escape
pod here. As you arrive, the alien opens the pod's hatch and gestures at you.
"""

	print room_desc
	pod_enter = raw_input("> ")
	
	if "enter" and "pod" in pod_enter:
		print "You pile into the pod and shut the hatch.  The diplomat puts the chip"
		print "into the navigation computer and presses a button."
		print "You soar into space, leaving the station and its murderous robots"
		print "behind.  Next stop, the alien homeworld!"
		exit(1)
	
	elif "do not" or "don't" in pod_enter:
		print "You hesitate as the others enter the pod."
		print "As they beckon you towards the hatch, robots enter the room"
		print "and shoot you dead.  The others, at least, manage to escape."
		return 'death'
		
	else:
		print "The alien gestures again, more intently."
		return 'SideDoor'

class death(object):
	def death(self):
		self.quips = [
			"Well, you picked a bad day to stop sniffing space glue.",
			"You came, you saw, you messed up and died.",
			"Buzz Lightyear you're not.",
			"Not a space ninja, you."
			]
			
		print self.quips[randint(0, len(self.quips)-1)]
		exit(1)