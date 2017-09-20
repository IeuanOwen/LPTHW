# Learn Python the hard way EX12
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much did you weigh? ")

print "So, you're %r old, %r tall and %r in weight" % (age, height, weight)
# Study Drills
# 1 ~ type python -m pydoc raw_input into terminal and read it
# output from command :
#Help on built-in function raw_input in module __builtin__:

#raw_input(...)
    #raw_input([prompt]) -> string

    #Read a string from standard input.  The trailing newline is stripped.
    #If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    #On Unix, GNU readline is used if enabled.  The prompt string, if given,
    #is printed without a trailing newline before reading.


# 2 ~ get out of pydoc by typing q to quit
# Done


# 3 ~ Look online for what the pydoc command does
# Pydoc allows Python programmers to access Python's documentation help files, generate text and HTML pages with documentation specifics, and find the appropriate module for a particular job

# 4 ~ Use pyDoc to read about open, file, os and sys
# Open :
# open(...)
# open(name[, mode[, buffering]]) -> file object
# Open a file using the file() type, returns a file object.  This is the
# preferred way to open a file.  See file.__doc__ for further information.
# ---------
# File :
# Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
# writing or appending.  The file will be created if it doesn't exist
#  when opened for writing or appending; it will be truncated when
#  opened for writing.  Add a 'b' to the mode for binary files.
#  Add a '+' to the mode to allow simultaneous reading and writing.
#  If the buffering argument is given, 0 means unbuffered, 1 means line
#  buffered, and larger numbers specify the buffer size.  The preferred way
#  to open a file is with the builtin open() function.
#  Add a 'U' to mode to open the file for input with universal newline
#  support.  Any line ending in the input file will be seen as a '\n'
#  in Python.  Also, a file so opened gains the attribute 'newlines';
#  the value for this attribute is one of None (no newline read yet),
#  '\r', '\n', '\r\n' or a tuple containing all the newline types seen.
#  'U' cannot be combined with 'w' or '+' mo
# --------
# os :
#    This exports:
#   - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
#   - os.path is one of the modules posixpath, or ntpath
#   - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
#   - os.curdir is a string representing the current directory ('.' or ':')
#   - os.pardir is a string representing the parent directory ('..' or '::')
#   - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
#   - os.extsep is the extension separator ('.' or '/')
#   - os.altsep is the alternate pathname separator (None or '/')
#   - os.pathsep is the component separator used in $PATH etc
#   - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
#   - os.defpath is the default search path for executables
#   - os.devnull is the file path of the null device ('/dev/null', etc.)
#  Programs that import and use 'os' stand a better chance of being
#  portable between different platforms.  Of course, they must then
#  only use functions that are defined by all platforms (e.g., unlink
#  and opendir), and leave all pathname manipulation to os.path
#  (e.g., split and join).
# --------
# sys :
# This module provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter.
# --------