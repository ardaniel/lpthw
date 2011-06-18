# Set up the joke with x
# then define some boilerplate strings
# then insert them into a longer punchline string (y)

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Deliver the assembled joke.

print x
print y

# Show the two lines of the joke.
# I don't *think* there's a diff between %r and %s for this usage?

print "I said: %r." % x
print "I also said: '%s'." % y

# Define the hilarity of the joke as a boolean value
# Set up the evaluation as a string that incorporates another variable

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Deliver the evaluation by substituting the value of "hilarious"
# for that %r in joke_evaluation.

# %r is a wildcard formatter: "print whatever this is, if you can."

print joke_evaluation % hilarious

# Define two strings to concatenate later.

w = "This is the left side of..."
e = "a string with a right side."

# String concatenation! Woo! Stick the two strings together and deliver the sentence.

print w + e
