# Learn Python the hard way EX16

#imports argv from sys
from sys import argv
#Creates 2 variables and assins them to argv
script, filename = argv

#These three seteps print the text inside the strings, replacing the % in line 1 with th value for filename
print "We're going to erase %r." % (filename)
print "If you don't want that, hit CTRL- C (^C)."
print "If you do want that, hit RETURN."

#Gets input from the user
raw_input("?")
#prints string
print "Opening the file..."
#opens the file with write permissions
target = open(filename, 'w')
#prints string
print "Truncating the file. Goodbye!"
#truncates file
target.truncate()
#prints string
print "Now I'm going to ask you for three lines."
#assings the input given by the user to 3 variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#prints string
print "I'm going to write these to the file."
#writes the values of the variales to the file, with each line seperated by a new line
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
#prints sting
print "And finally"

#<study drill 2>#
##print("Type the filename again:")
# creates a new variable that will contain user input.
##file_again = raw_input("> ")
# Opens the file specified in file_again
##text_again = open(file_again)
# Prints the data in the file.
##print(text_again.read())
##text_again.close()

# Study Drills
# 1 ~ Comments above each line
# Done

# 2 ~ Write a script similar to the last excersise that uses read and argv to read the file you just created. 
# Done

# 3 ~ Theres too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write command instead of six.
# Done

# 4 ~ Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly say you want to write a file
# Becuase open normally opens things in read-only

# 5 ~ If you open the file with w mode, then do you really need the target.truncate? Go read the docs for Pythons open function and see if thats true.
# You do not need to truncate it truncates automatically