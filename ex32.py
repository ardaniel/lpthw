the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# ("iterates over")

for number in the_count:
	print "This is count %d" % number
	
# more iterating over a list

for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
# also we can go through mixed lists too
# notice we have to use %r since
# we don't know what's in it

for i in change:
	print "I got %r" % i
	
# we can also build lists, first start with an empty one
elements = []

# then use the range() function to do 0 to 5 counts
#for i in range (0, 6):
#	print "Adding %d to the list." % i
#	# append adds items to lists
#	elements.append(i)

# alternatively:
# this works because range() returns a list
# which is iterable.  append() hates iters.
# you can't do elements.append() for this,
# but you can do elements.extend():

elements = range(0,6)
elements.extend(range(6,11))

# now we can print them out too
for i in elements:
	print "Element was: %d" % i
	
# other list operations:
# count, extend, index, insert, pop
# remove, reverse, sort
# (extend is like append, but for iterables,
# not objects)