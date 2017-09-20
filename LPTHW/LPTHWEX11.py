# Learn Python the hard way EX11
print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So you are %r years old, %r tall and %r in weight" % (age, height, weight)
print "<-----End----->"

# Study Drills
# 1 ~ Go online and find out what pythons raw_input does.
# It presents a prompt to the user (the optional arg of raw_input([arg])), gets input from the user and returns the data input by the user in a string. See the docs for raw_input().

# 2 ~ Can you find other ways to use it?
# this little chunk of code does the 2 times table up to a number given by the user.
print "Please enter a number"
i = int(raw_input())
for j in range(1, i):
    print i+i
print "<-----End----->"

# 3 ~ Write another "Form" like this to ask some other questions 
#
print "What is your favourite colour?"
colour = raw_input()
print "What is your favourite animal?"
animal = raw_input()
print "What is the answer to life the universe and everything?"
the_answer = raw_input

print "your favourite colour is %s, your favourite animal is a %s, and the answer to the ultimate question is %r !!!" % ("Blue", "Monkey", 42)

# 4 ~ Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence. 
# The single quote needs to be escaped so it doesnt end the string.
