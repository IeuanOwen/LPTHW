# Learn Python the hard way EX17
#A program that copies the contents of a given file, to a different specified file.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

##print "Copying from %s to %s" % (from_file, to_file)

# -> we could do these two on one line too, how?
##in_file = open(from_file)
##indata = infile.read()
indata = open(from_file).read()

##print "the input file is %d bytes long" % len(indata)

##print "does the output file exist? %r" % exists(to_file)
##print "Ready, hit RETURN to continue, CTRL-C to abort"
##raw_input()

out_file = open(to_file, "w").write(indata)
##out_file.write(indata)

##print "All done"

##out_file.close()
##from_file.close()





# Study Drills
# 1 ~ Go read up on Pythons import statement, and start python to try it out. Try importing some things and see if you can get it right. Its alright if you do not.
# Python code in one module gains access to the code in another module by the process of importing it. The import statement is the most common way of invoking the import machinery, but it is not the only way. Functions such as importlib.import_module() and built-in __import__() can also be used to invoke the import machinery.

# 2 ~ This script is really annoying. Theres no need to ask you before doing the copy, and it prints too much out to the screen. Try to make it more friendly to use by removing features.
# Removed the exists checker and the "hit RETURN to continue" step.

# 3 ~ See how short you can make the script. I could make this one line long
# i got it to 4 lines long!

# 4 ~ Notice at the end of the WYSS I used something called cat? Its an old command that concatenates files together, but mostly its just an easy way to print a file to the screen. Type man cat to read about it.
# Done - its Name is Get-Content

# 5 ~ Windows people, find the alternative to cat that Linux/OSX people have. Do not worry about man since there is nothing like that.
# DD can extract specified amounts of data, head prints the first 10 lines of a file, and grep can be used to extract specific lines/info

# 6 ~ Find out why you had to do output.close() in the code
# UNKNOWN