from random import choice

class MainHub(object):

	def room_setup(self):
		room_desc = """
This is the main hub of the space station. There is a 
guide here.  He tells you to go north to the Diplomatic Office
and give the Chief Diplomat the codeword 'cookie.'"
"""
		print room_desc
		
		prompt = raw_input("> ")
		
		if prompt == "go north":
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
			return 'DiplomatOffice2'
			
		else:
			print "The alien shrugs and eats you, the faster to obtain the envelope."
			print "You might be pooped out in 500 years."
			return 'death'

a = AlienRoom()
a.room_setup()