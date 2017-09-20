# Learn Python the hard way EX11
from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Study Drills
# 1 ~ Try giving fewer than three argument to your script.see that error you get? See if you can explain it. 
# The program see that 4 variables have been declared but less than the required number have been given a value

# 2 ~ Write 2 mor scripts, one with less arguments and one with more.
# -----Less-----

#scriptname, name, date = argv

#print "The script is called ", scriptname + ", My name is ", name + ". Todays date is : ", date

# -----More-----

#scriptname, name, date, age, colour, starsign = argv

#print "My name is ", name + ", I am ", age + " years old and my favourite colour is ", colour + ", and my Zodiac is ", starsign + ". Todays date is : ", date + " and this has been my script named ", scriptname


# 3 ~ Combine raw_input with argv to make a script that gets more input from a user
# -----Start-----

#w, x = argv
#y = int(raw_input())
#z = (int(x) * y) 
#print z

# -----End-----
# 4 ~ Moudules give you features!
