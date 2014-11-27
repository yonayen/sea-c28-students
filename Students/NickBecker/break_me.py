# Four Codes that break Python

# Name Error
games()
#games is an undefined function

# Syntax Error
if 4 $ 5:
# "$" isn't an operator

# Type Error
games = 42

for i in games:
	print i
# Not able to loop through an int

# Attribute Error
None.lower()
# None has no attribute to lower
