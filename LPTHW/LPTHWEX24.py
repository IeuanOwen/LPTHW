#Learn Python the hard way EX24
# Ex's 22 & 23 were revision excersises with no practical aspects, just reading other peoples code, and making a cheatsheet
# -*- coding: utf-8 -*-

print "Lets practice everything"
print 'you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs'

poem = """
\t The Lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprhend passion from intuition 
and requires an explanation
\n\t\twhere there is none.
"""
print "----------"
print poem
print "----------"

five = 10 -2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
    """A function that calculates how many beans jars and crates there would be"""
    jelly_beans = started * 500
    jars = jelly_beans /1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "with a starting point of: %d" % start_point
print "We'd have %d beans, %d jars and %d crates." % (beans, jars, crates)

start_point = start_point / 10                          #overwrites start_point and assigns it a new value by deividing its previous value by 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars and %d crates." % secret_formula(start_point) #Uses most recently defined version of start_point

# Study Drills
# 1 ~ Do checks, read through and make notes
# Done

# 2 ~ Break the file on purpose and see what errors you get
# Skipped