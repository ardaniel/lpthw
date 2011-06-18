from random import choice

terms = ['False', 'True']
operands = ['and', 'or', 'not', 'nand', 'nor', "==", "!="]

def pick_one(items):
	return choice(items)
	
def compile_problem(a, b, c):
	problem = a + " " + b + " " + c

	if b is 'not':
		problem = b + " " + a
	
	if b is 'nand':
		problem = "not" + "(" + a + " and " + c + ")"
	
	if b is 'nor':
		problem = "not" + "(" + a + " or " + c + ")"

	return problem

entry = ""

print "Enter q to quit at any time."

while True:

	term1 = pick_one(terms)
	op = pick_one(operands)
	term2 = pick_one(terms)

	problem = compile_problem(term1, op, term2)

	answer = str(eval(problem))

	entry = raw_input(problem+"?\n")
	
	if entry == 'q':
		break

	if answer == entry:
		print "Very good! Correct."
	
	if answer != entry:
		print "No, the answer is: %s" % answer