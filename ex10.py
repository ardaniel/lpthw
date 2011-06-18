# \t is a tab and \n is a newline.
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."

# Double your backslash to escape it and print a single backslash.
backslash_cat = "I'm \\ a \\ cat."


# The only use case I can think of for single-triple-quote here?
# is if you have double-triple-quotes in your list items,
# which seems improbable at best.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Escaping a percent requires a percent sign.
print "The very literal tabby cat uses %%r and says: '%r'" % tabby_cat
print "The formatted tabby cat uses %%s and says: '%s'" % tabby_cat
