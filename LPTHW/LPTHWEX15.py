# Learn Python the hard way EX15

# Imports argv from the sys module
##from sys import argv

# Creates 2 variables called script and filename and puts them into argv
##script, filename = argv

# Creates a variable called txt that opens a file with the name given as an argument
##txt = open(filename)


# Prints out the string and replaces the formatter with the filename
##print("Here's your file %r:") % filename

# Prints out the contents of the given file.
##print txt.read()

# Prints the string
print("Type the filename again:")
# creates a new variable that will contain user input.
file_again = raw_input("> ")
# Opens the file specified in file_again
text_again = open(file_again)
# Prints the data in the file.
print(text_again.read())
text_again.close()
# Study Drills
# 1 ~ Above each line, write a comment saying what it does
# Done

# 2 ~ Google Python open
# Open a file, returning an object of the file type described in section File Objects. If the file cannot be opened, IOError is raised. When opening a file,
# its preferable to use open instead of invoking the file constructor directl

# 3 ~ Search online to see what people call Commands/methods/functions are called.
# I Prefer the word function

# 4 ~ Get rid of the part from line 10 - 15 and run the script
# Done - Success

# 5 ~ Use only raw_input and try the script that way. Think of why one way of getting the filename would be better than another.
# Done - Success - I belive that this final way is better becuase you are beung promoted.

# 6 ~ Run pydoc file and scroll down until you see the read() command (method/function). See all the other ones you can use? Skip the ones that have __ (two underscores) in front
# because those are junk. Try some of the other commands.
# Done

# 7 ~  Start python again and use open from the prompt. Notice how you can open fi les and run read on them right there?
# Couldnt do

# 8 ~ insert a close()
# Done
