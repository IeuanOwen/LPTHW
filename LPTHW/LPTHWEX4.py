# Learn Python the hard way EX4

cars = 100  #assigns 100 to cars
SpaceInCar = 4.0 # assigns 4.0 to Space in Car
drivers = 30 #assigns 3- to drivers
passengers = 90 # assigns 90 to passengers
carsNotDriven = cars - drivers #calcuates variable by subtracting drivers from cars
carsDriven = drivers #makes carsDriven equal to the value of drivers
carpoolCapcity = carsDriven * SpaceInCar #calculates variable by multiplying carsDriven by SpaceInCar
PeoplePerCar = passengers / carsDriven #calculates variable by dividing passengers by carsDriven 

print "There are", cars, "cars available."
print "There are only", drivers, "drivers avaialable."
print "There will be", carsNotDriven, "empty cars"
print "We can transport", carpoolCapcity, "people today."
print "We have", passengers, "to carpool today."
print "we need to put about", PeoplePerCar, "in each car"

#Study drills
# 1 ~ 4.0 is used in SpaceInCar instead of 4, what would happen if 4 is used
# in this example chaning the 4.0 to 4 does not affect the answers, but does remove the decimal point from the 120. using floats is however more accurate.

# 2 ~ What does a floating point mean?
# The term floating point refers to the fact that a number's radix point (decimal point, or, more commonly in computers, binary point) can "float"; that is, it can be placed anywhere relative to the significant digits of the number.

# 3 ~ Write comments aboive each of the assignment statments
# done

# 4 ~ Make sure you know what = is called (equals) and that it’s making names for things
# Understood

# 5 ~ Remember that _ is an underscore character.
# done

# 6 ~ Try running Python as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.
# done
