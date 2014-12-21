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
