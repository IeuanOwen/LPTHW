#Learn Python the hard way EX20

#imports argv from sys
from sys import argv

script, input_file = argv

#creates a function with one arg, that reads the file stored in that arg.
def print_all(f):
    print f.read()  #prints the contents of the file f

#Creates a function with one arg that finds the begining of a file
def rewind(f):  
    f.seek(0)

#Creates a function with 2 args, that prints the line number and contents of a line
def print_a_line(line_count, f):
    print line_count, f.readline()

#creates a variable (current_file) and opens a specified file.
current_file = open(input_file)

#prints string
print "First let's print the whole file: \n"

#prints the current file
print_all(current_file)

# prints string
print "Now let's rewind, kind of like a VHS"

#calls the rewind function and finds the start of a file
rewind(current_file)

# prints string
print "Let's print three lines:"

#sets current line to 1
current_line = 1
#calls the print_a_line function feeding in the supplied variables.
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# Study Drills
# 1 ~ Comments on lines
# Done where needed

# 2 ~ Each time print_a_line is run, you are passing in a variable current_line. Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line.
#     1, 1, 2, 3 --> It becomes line_count when the print_a_line function is called and the current_variable is passsed to it as an argument.

# 3 ~ Find each place a function is used, and go check its def to make sure that you are giving it the right arguments.
# Done - All Correct

# 4 ~ Research online what the seek function for file does. Try pydoc file and see if you can figure it out from there.
# Seek is finding a certain number of bytes in a file to create a atart point, from which lines are read.

# 5 ~ Research the shorthand notation += and rewrite the script to use that.
# This is kind of like a contraction for the two operations = and +. That means x = x + y is the same as x += y.

