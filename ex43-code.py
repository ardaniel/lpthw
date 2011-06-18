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
		
		if codeguess == "cookie":
			print "She hands you an envelope and points you to the door to the right."
			return 'AlienRoom'
			
		else:
			print 'She looks appalled and pushes a button on her desk. "Intruder!" she yells,'
			print "and you are sucked into a tube and vented into space, where you die."
			return 'death'
		
#class AlienRoom(object):

#class Engine(object):
#	def __init__(self, start):
		# set up the codeword for the diplomat's room
#		codelist = ['bunny', 'turtle', 'tribble', 'horta', 'cookie']
#		codeword = choice(codelist)


diplo = DiplomatRoom()
diplo.room_setup()