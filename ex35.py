from sys import exit

def gold_room():
	"""Sets up the Gold Room.  How much gold
	do you take?"""
	
	print "This room is full of gold.  How much do you take?"
	
	next = raw_input("> ")
	
# I don't think Zed is driving at try/except
# in this case.  However, it does work.

	try:
		how_much = int(next)
	except:
		dead("Man, learn to type an integer.")

#	if "0" in next or "1" in next:
#		how_much = int(next)
#	else:
#		dead("Man, learn to type a number.")


		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")
		
	
def bear_room():
	"""Sets up the bear room."""
	
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		if next == "take honey":
			dead("The bear looks at you then pimp slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.  You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your crotch off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
			
			
def cthulhu_room():
	""" Creates the Cthulhu room. Options
	include fleeing or eating your own head."""
	
	print "here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()


def dead(why):
	""" Accepts a reason for player death and
	returns it before exiting the game."""
	print why, "Good job!"
	exit(0)
	

def start():
	"""Initializes the first room.  Options
	include going left or right."""

	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()