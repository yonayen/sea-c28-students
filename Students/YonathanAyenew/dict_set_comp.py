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
# sets s2, s3, s4 with numbers from 0-20

























