#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
# Dict/Set Lab
# 

newd = {'name': 'Chris', 'city': 'Seattle', 'cake': 'chocolate'}
print newd

newd.pop('cake')
print newd

newd['fruit'] = 'mango'
print newd

#  print newd keys
print newd.keys()

# print newd values
print newd.values()

# this should return false
print 'cake' in newd.keys()

print 'mango' in newd.values()

# dict constructor and zip to build range(16) and it's hexidecimal pair

numbers = range(16)
hexidecimal = []
for number in numbers:
    hexidecimal.append(hex(number))

print hexidecimal

# put both numbers and hexidecimals into dict
hexidecimal_d = dict(zip(numbers, hexidecial))

print hexidecimal_d

# create new dict using same key from begining of this exercise but with number of 'a's in each value 

newd = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

newddict = {}
for key, val in newd.items():
    newddict[key] = val.count ('a')

print newddict

# changing the values

for key, val in newd.items():
    newd[key] = val.count('a')

print newd

# 
# sets s2, s3 and s4 that range(21) -- divisible by 2, 3 and 4
# 


s2 = set()
s3 = set()
s4 = set() 

for i in range(21):
    if not i % 2:
        s2.add(i)
    if not i % 3:
        s3.add(i)
    if not i % 4:
        s4.add(i)

print s2
print s3
print s4

# s3 as subset of s2

s3.issubset(s2)
# false

# s4 as subset of s2
s4.issubset(s2) 
# true
# or s2 >= s4

# 
# add 'i' to set with letters in 'Python'
# 

s = set(u'python')
s.add('i')

print s 

# create  frozenset with letters from 'marathon'
word = frozenset(u'marathon')

# union & intersection of sets

print "union:", s.union(word)
print "intersection:", s.intersection(word)

print "union:", word.union(s)
print "intersection:", word.union(s)












