# raw_input() takes user input and converts it to a string
# it will also take a prompt argument, but if you do that
# you'll need a space at the end of your prompt string for formatting

#print "How old are you?",
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weigh?",
#weight = raw_input()

# You prolly shouldn't assume an int() for age, etc.
# (it'll throw the hell up if someone types a mixed string)
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "More nicely, you're %s old, %s tall and %s heavy." % (age, height, weight)
