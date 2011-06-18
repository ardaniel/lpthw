# import the argv function from the sys module
from sys import argv
from sys import exit

# Check for the number of arguments we're getting
# if it doesn't match our unpack variables, die
if len(argv) != 4:
    print "Usage: ex13.py <first value> <second value> <third value>"
    exit() # not sys.exit() because we imported exit separately
    
# unpack ARGV
# (argv = "argument vector," points to the arguments)
script, first, second, third = argv

# print the contents of our unpacked ARGV
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
