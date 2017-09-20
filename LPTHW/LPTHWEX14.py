# Learn Python the hard way EX14
from sys import argv

script, user_name, = argv
prompt = '~~ '

print "Hi %s, I'm the %s script." % (user_name, script)
print "i'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What is your favourite colour?"
colour = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)        #asks the user for input to answer the printed question. prints prompt before the users input.

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
Your favourite colour is %s.
And you have a %r computer. Nice.
""" % (likes, lives, colour, computer)   #uses a formatter to feed the variables into the string

# Study Drills
# 1 ~ Find out what Zork and Adventure were, Try and find a copy and play it
# Zork and Adventure are text adventure games, played zork before i think. 

# 2 ~ Change prompt to something else entirely
# Done (was '>')

# 3 ~ Add another argument
# added colour

# 4 ~ make sure you understand
# comments added to code for clarity.