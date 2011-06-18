from sys import argv
from os import environ
import re

# let's make sure we have a name
# if we don't, we'll use your login name
if len(argv) == 1:
    argv.append(environ['USER'])
    
script, user_name = argv
prompt = '> '
article = 'a'


print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd ike to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# Proper grammar counts!

if re.match(r'[AEIOUaeiou]',computer):
    article = 'an'

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have %s %r computer. Nice.
""" % (likes, lives, article, computer)

