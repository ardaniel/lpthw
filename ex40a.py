cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found."
		
# ok pay attention!

# cities['_find'] = find_city

while True:
	print "State? (ENTER to quit)",
	state = raw_input("> ")
	
	if not state: break
	
	# this line is the most important ever! study!
	city_found = find_city(cities, state)
	print city_found
	
	# this is, really, an incredibly bad
	# way of doing this-- if the user types
	# "_find" they get an obj ref
	# and why would you do it anyhow