# Learn Python the hard way EX19

# imports argv from sys
from sys import argv

#Creates a function with 2 args
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "you have %d cheeses!" % cheese_count #prints string using formatter to replace %d
    print "You have %d boxes of crackers!" % boxes_of_crackers 
    print "Man that's enough for a party!" #prints string
    print "Get a blanket.\n"    #prints string with new line

print "We can just give the fucntion numbers directly:" #prints string
cheese_and_crackers(20, 30) #calls function using supplied values

print "OR, we can use variables from our script:"
amount_of_cheese = 10 #creates a global variable and sets its value
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #calls function using global variables

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) #calls function and does math to get its arg values

print "And we can combine the two variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #calls fucntion and does math on the global vars

# Study Drills
# 1 ~ Comment each line
# Done where needed

# 2 ~ Start at the bottom and read each line backwards saying all the imortant characters
# Done 

# 3 ~ Write at least one more function of your own design and run it 10 different ways
# i got 6 different ways

#def glasses_for_guests(glasses, guests):
    #print "you have %s glasses for %s guests" % (glasses, guests)

#script, cups, peeps = argv

#print "Enter two values"
#gs = raw_input("How many guests? > ")
#ps = raw_input("How many glasses? > ")
#glasses_for_guests(gs, ps)

#glasses_for_guests(cups, peeps)

#glasses_for_guests(20, 15)

#numGlasses = 30
#numGuests  = 20

#glasses_for_guests(numGlasses, numGuests)

#glasses_for_guests(12 + 8, 20+30)

#glasses_for_guests(numGlasses + 2, numGuests + 2)
