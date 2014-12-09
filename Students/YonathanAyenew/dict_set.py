# Dict/Set Lab

newd = {u'name': u'Chris', u'city': u'Seattle', u'cake': u'Chocolate'}
print newd

newd.pop(u'cake')
print newd

newd[u'fruit'] = u'mango'
print newd

for key in newd.iterkeys():
    print key

for val in d.itervalues():
	print val

newd.has_key(u'cake')
u'mango' in newd.values()

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 
l2 = [0, 1, 2, 3, 4, 5, 6 ,7, 8 ,9 ,'a', 'b', 'c', 'd', 'e', 'f']
new_list = dict(zip(l1, l2))
print new_list


newd = {u'name': u'Chris', u'city': u'Seattle', u'cake': u'Chocolate'}
# create new dict using same key but with number of 'a's in each value

for val in newd.itervalues():
	cal = val.count('a')
    newd = {k: cal for k in newd}

#  This isn't looping well and applies the same val.count to all keys.  The values all become 0.

s2 = ([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
s3 = ([3, 6, 9, 12, 15, 18])
s4 = ([4, 8, 12, 16, 20])

s4.issubset(s2) 
# true
# or s2 >= s4

s3.issubset(s2)
# false

# This attempt at creating sets wasn't working out


s2 = ()
for i in range(21):
	if i % 2 == 0:
    s2.update(i)
#  this is one way of creating s2

s3 =()
for i in range(21):
	if i % 3 == 0:
    s3.update(i)
#  this is one way of creating s3

s4 = ()
for i in range(21):
	if i % 4 == 0:
    s4.update(i)
# this is one way of creating s4

word = ['Python']
result = set()
print set(','.join (word).replace(',', ''))

# print 'python' as indivdual letters in set

my_set = {'p', 'y', 't', 'h','o', 'n'}
my_set |= {'i'}
print my_set

# adding 'i' to python set

# create  frozenset with letters from 'marathon'

marathon = frozenset(('m','a','r','a','t','h', 'o', 'n'))

word.issubset(marathon)
# return False












