import ex43rooms as rooms

class Engine(object):
		
	def __init__(self, start):
		self.start = start
			
	def play(self):
	
		LOCATIONS = {
		'Death': rooms.Death(),
		'MainHub': rooms.MainHub(),
		'MainHub2': rooms.MainHub2(),
		'DiplomatRoom': rooms.DiplomatRoom(),
		'DiplomatRoom2': rooms.DiplomatRoom2(),
		'AlienRoom': rooms.AlienRoom(),
		'SideDoor': rooms.SideDoor(),
		'Victory': rooms.Victory(),
		'Death': rooms.Death()
		}	
		
		next = self.start.room_setup()

		while True:
			next = LOCATIONS[next].room_setup()
				
			
the_game = Engine(rooms.MainHub())
the_game.play()