# number of cars we have
cars = 100

# how many people fit in each car
space_in_a_car = 4.0

# how many drivers we have
drivers = 30

# how many passengers we have
passengers = 90

# how many cars will not be used today?
cars_not_driven = cars - drivers

# each driver has a car, so they're the same value
cars_driven = drivers

# the capacity of the carpool is the number of cars driven times their seating cap.
carpool_capacity = cars_driven * space_in_a_car

# the average number of passengers per car is the total amt of passengers
# divided by the number of cars in service today
# the space in a car is a float because averages are sometimes not integers
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
