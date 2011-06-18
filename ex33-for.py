def count_numbers_while(end, inc):

	i = 0
	numbers = []

	while i < end:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

# note to self: it helps if you return
# something if you want to see something
# back in __main__

	return numbers	
	
def count_numbers_for(end,inc):
	numbers = []
	
	# range() takes a third argument
	# which is the increment
	# pydoc is your friend
	for i in range (0, end, inc):
		print "Adding %d to the list." % i
		numbers.append(i)
	return numbers


while_list = count_numbers_while(23, 2)

print "The numbers with while():"

for number in while_list:
	print number
	
for_list = count_numbers_for(23, 2)

print "The numbers with for():"

for number in for_list:
	print number