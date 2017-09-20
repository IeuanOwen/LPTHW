#Learn Python the hard way EX21
# -*- coding: utf-8 -*-

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def minus(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Lets do some math with just functions!"

age = add(30, 5)
height = minus(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#---A puzzle for extra credit, type it in anyway.---#
print "Here is a puzzle"

what = add(age, minus(height, multiply(weight, divide(iq, 2))))

print "That becomes", what, "Can you do it by hand?"

def FormulaByHand():
    print ((30+5)+((78-4)-((90*2)*((100/2)/2))))

# Study Drills
# 1 ~ If you aren’t really sure what return does, try writing a few of your own functions and have them return some values.
# I understand return, anything on the right hand side of an '=' can be be returned and used elsewhere in the program.

# 2 ~ What you should do is try to fi gure out the normal formula that would recreate this same set of operations.
#  = FormulaByHand Fuction

# 3 ~ modify the parts of the functions. Try to change it on purpose to make another value.
# changing any of the figures being passed to the functions and stored would affect the outcome.

# 4 ~ Finally, do the inverse. Write out a simple formula and use the functions in the same way to calculate it.
#
apples = add(40, 2)
pears = minus(20, 10)
oranges = multiply(2, 5)
strawberry = divide(20, 1)

fruit = add(apples, minus(pears, add(oranges, strawberry)))
print fruit, "How do you like them apples?"