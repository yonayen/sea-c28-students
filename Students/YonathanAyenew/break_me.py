#!/usr/bin/env python

#break_me.py (SyntaxError, TypeError, NameError and AttributeError) 


from __future__ import print_function

# 
# SyntaxError Exception
# 


def a_function (a, b):
    if a == 42 and b == a
        return (u"it's all the same")

# error because I didn't put an ':'  after the if statement.

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

def ind():
    print (u"I am exceptional")

ind.length

# error is 'object' object has no attribute 'length'

