from sys import argv

script, filename = argv

print "We're going to read in %r." % filename

target = open(filename)

print "Here's your file %r: \n" % filename

print target.read()

print "And now we close the file, as you do."

target.close()
