# Learn Python the hard way EX10
tabby_cat = "\tI'm Tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a lisst:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#while True:
    #for i in ["/", "-", "|", "\\", "|"]:
        #print "%s\r" % i


# <------Escape Characters------>
# \\ Backslash (\)
# \' Single- quote (')
# \" Double- quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only)
# \r ASCII carriage return (CR)
# \t ASCII horizontal tab (TAB)
# \uxxxx Character with 16- bit hex value xxxx (Unicode only)
# \Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
# \v ASCII vertical tab (VT)
# \ooo Character with octal value oo
# \xhh Character with hex value hh
# \t*  Bullet points made of '*'

# Study Drills
# 1 ~ Memorise all the escape characters by putting them on flashcards
# Ive posted the list above so i can use it in reference

# 2 ~ Use ''' instead. Can you see why you might use that instead of """?
# It makes no difference

# 3 ~ Combine escape sequences and format strings to create a more complex format
print "This string will be divided here %s and here %s and so this should be the third and final line, exclamation mark -> %s" % ("\n", "\n", "!")

# 4 ~ Remember the %r format? Compare using """ and ''', %r and %s and look at the differences.

print """This is a tester string that will have stuff %r (<- like that) pasted in it
i can type on %r (<- Another one) sevral lines but 2 should be enough dont you think?""" % (12, "word")

print '''This is a tester string that will have stuff %s (<- like that) pasted in it
i can type on %s (<- Another one) sevral lines but 2 should be enough dont you think?''' % (12, "word")