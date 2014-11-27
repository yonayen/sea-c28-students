
# 
# SyntaxError Exception
# 

from __future__ import print_function

def a_function (return=u'This should be a SyntaxError'):
    print(return)

# or 

continue = u"this should raise a SyntaxError"

# 
# TypeError
# 

type(u'Uncle')
type=u'Sister'
type(u'Brother')

# error is that'unicode' isn't callable

# 
# NameError
# 

john = man()

# error is that name ''man' is not defined

# 
# AttributeError
# 

john = object()

john.length

# error is 'object' object has no attribute 'length'

