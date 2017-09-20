# Learn Python the hard way EX5
myName = 'Zed A. Shaw'
myAge = 35 # not a lie
myHeight = 74 # inches
myWeight = 180 # lbs
myEyes = 'Blue' 
myTeeth = 'White'
myHair = 'Brown'
percent = 100

print "Lets talk about %s" % myName
print "He's %d inches tall" % myHeight
print "He's %d pounds heavy" % myWeight
print "Actually thats not too heavy"
print "He's got %s eyes and %s hair." % (myEyes, myHair)
print "His teeth are usually %s depending on his coffee" % myTeeth

print "If i add %d, %d, and %d i get %d." % (myAge, myHeight, myWeight, myAge + myHeight + myWeight)

print "This task is %r percent complete" % percent

#Study drills
# 1 ~ Change all the variables so there isnt the my in front. Make sure you change the name everywhere, not just where you used  to set them.
# done 

# 2 ~ Try more format characters. %r is a very useful one. Its like saying print this no matter what.
# The term floating point refers to the fact that a number's radix point (decimal point, or, more commonly in computers, binary point) can "float"; that is, it can be placed anywhere relative to the significant digits of the number.

# 3 ~ Search online for all the python format characters:
# %c - character
# %i - signed decimal int
# %d - signed decimal int
# %u - unsigned decimal int
# %o - octal integer
# %x - hexi int (Lowercase letters)
# %X - hexi int (Uppercase)
# %e - expenential notation with lowercase e
# %E - exponential notation with uppercase E
# %f - float
# %g - the shorter of %f and %e
# %G - the shorter of %f and %E

# 4 ~ Try to write some variables that convert the inches and pounds to centimeters and kilos. Do not just type in the measurements. Work out the math in Python.

inches = 5.0
pounds = 125
centimeters = 5.0 * 2.5
kilos = pounds / 2.2

print "%f inches in centimeters is %f cm" % (inches, centimeters)
print "%d lbs in Kilos is %f Kg" % (pounds, kilos )
