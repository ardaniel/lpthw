# get the argument vector function from sys
from sys import argv

# unpack the command line arguments
# I might do 'script = argv[1]' instead
# but that's me

script, filename = argv

# txt is a file descriptor that points to the
# specified file

txt = open(filename)

# print the name of the file in the "here's your file"
print "Here's your file %r:" % filename

# print each line as it's read from the file
print txt.read()

# close your goddamn FDs
txt.close()

# print a prompt for entering the filename again
print "I'll also ask you to type it again:"
file_again = raw_input("> ")

# create an FD for the file again
# (is read() iterating?)
txt_again = open(file_again)

# print out the file contents again
print txt_again.read()

# close your goddamn FDs
txt_again.close()

