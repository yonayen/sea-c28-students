#!/bin/usr/env python
# -*-  coding: UTF-8 -*-

# Dict_Set Comprehensions

# New and bigger dict 
food_prefs =   {u"Name": u"Yonathan", u"city": u"Seattle", 
                u"breakfast": u"Oatmeal", u"fruit": u"Banana",
                u"Meat": u"Beef", u"drink": u"Water", u"flavor": u"Coffee"}

print u"{name} is from {city}, takes {drink} everywhere, begins thd day with {breakfast}, snacks on {fruit}, enjoys {Meat} and the aroma of {flavor}.".format(**food_prefs)

#Delete Meat Value
food_prefs.pop(u"Meat")
print food_prefs

# Add value for "icecream" with "chocolate" and print dict
food_prefs[u'icecream'] = u'chocolate'
print food_prefs

# display keys and values

print food_prefs.keys()
print food_prefs.values()

print u'chocolate' in food_prefs.values()

# use dict constructor and zip to create dict of numbers from 0-15 and hex equiv.

hexdecimal_dict = {i: hex(i) for i in range(16)}
print hexdecimal_dict


# using the food_prefs dict create new dict with the number of 'a's in each value 

a_dict = {key: val.count(u"a") for key, val in food_prefs.items()}

print a_dict


# change the values 

for key, val in food_prefs.items():
    food_prefs[key] = val.count(u'a')

print food_prefs


# 
# sets s2, s3, s4 with numbers from 0-20; divisible by 2, 3 and 4
# 

s2 = {i for i in range(21) if not i % 2}
s3 = {i for i in range(21) if not i % 3}
s4 = {i for i in range(21) if not i % 4}

print s2
print s3
print s4

# show if s3 is subset of s2
print s3.issubset(s2) # False

# show if s4 is subset of s2
print s4.issubset(s2) # True



# New set with 'Python' and add 'i' to set

s = set(u'Python')
s.add('i')

print s


# create frozenset with letters in 'marathon'

fs = frozenset(u'marathon')

# union/intersection of two sets

print u'union:', s.union(fs)
print u'intersection:', s.intersection(fs)


































































