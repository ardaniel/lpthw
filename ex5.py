my_name = "Zed A. Shaw"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

my_height_cm = my_height * 2.54
my_weight_kg = my_weight * .4536 # that's avoirdupois, thx

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
# %r is "print exactly what you have, Python"
# %f is floating-point and introduces a bit of rounding
print "In metric, he's %r cm tall and %r kg heavy." % (my_height_cm, my_weight_kg)
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right:
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

