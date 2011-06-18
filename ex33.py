def count_numbers(end, inc):

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

number_list = count_numbers(23,2)

print "The numbers: "

for number in number_list:
	print number