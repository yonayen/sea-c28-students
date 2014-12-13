#!/usr/bin/env python

#break_me.py (SyntaxError, TypeError, NameError and AttributeError) 


from __future__ import print_function

# 
# SyntaxError Exception
# 


def a_function():
    if a == 42 and b == a
        return (u"it's all the same")

# SyntaxError: invalid syntax, because I didn't put an ':'  after the if statement.

# 
# TypeError
# 

def phrase():
    phrase = u'Life is good'
    phrase[13] = 'r'
    return (phrase)

# immutable 'str' object doesn't accpet new assignment on line 25


# 
# NameError
# 

def parts():
    foobar = 'Jim'
    return ('My name is ' + foo)
    
    # NameError: global name 'foo' is not defined

# 
# AttributeError
# 

def change_case():
    word = 'THIS IS UPPER CASE'
    word = word.lowerr()
    return (word)

# AttributeError: 'str' object has no attribute 'lowerr'

# 
#  call following fucntions to test errors
# 

# AttributeError: change_case()
# NameError: parts()
# TypeError: phrase()
# SyntaxError: a_function()
