# Learn Python the hard way EX6
# Assigns a string to the variable x, and will replace the formatter '%d' with the number given
x = "There are %d types of people." % 10
# Assigns a string to the variable
binary = "binary"
# Assigns a string to the variable
do_not = "Don't"
# Assigns a string to the variable y, and will replace the formatters '%s' with the values of the given variables
y = "Those who know %s and those who %s." % (binary, do_not) #1st and 2nd strings in string

# Print te values of x and y respectively
print x 
print y 

# Prints the given strings replacing the formatters with the values of x and y
print "I said: %r." % x
print "I also said: '%s'." % y #3rd string in string

# Assigns hilarious the value False
hilarious = False
# Assings a string to the variable
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints the given string and replaces the formatter with the value of hilarious
print joke_evaluation % hilarious

# Assigns strings to the variables w and e
w = "This is the left side of ..."
e = "a string wih a right side."

# Prints a concatonated version of strings w + e
print w + e      #4th string in string



#Study drills
# 1 ~ Comment above each line
# Done

# 2 ~ There are 4 strings inside strings, find them
# Done

# 3 ~ Are there really only 4?
# Yes

# 4 ~ Explain why adding the two strings w and e with + makes a longer string.
# Adding 2 strings together with + joins the strings together


