# Learn Python the hard way EX8
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (
    "I had this thing.", 
    "That you could type up right", 
    "But it didn't sing",
    "So I said goodnight.
)

#Study drills
# 1 ~ Check for mistakes
# Did not type an "=" in while defining formatter

# 2 ~ Why is there single and double quotes in the output
# Python prints stings as efficiently as possible, as line 3 has an apostrophe in it, Python printed this string with double quote, so the apostrphe doesn't cut the string.
