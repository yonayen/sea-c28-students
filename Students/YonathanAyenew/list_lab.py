
#!/usr/bin/python

# List_lab.py

from __future__ import print_function

# 
# Part 1, creating the list
# 

fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
print fruit_list

new_fruit = raw_input('what other fruit would you like to add to list?-->')
fruit_list.append(new_fruit)
print fruit_list
    
# using '1 is first' to dispay number corresponding to fruit
ind = int(raw_input('choose number from index-->')
    
print "You chose fruit number: %i, which is %s" % (ind, fruit_list[ind-1])

print fruit_list

fruit_list = ['Bananas', 'Grapes'] + fruit_list
print fruit_list

fruit_list.insert(0, 'Kiwis')
print fruit_list

for fruits in fruit_list:
    if fruits[0] == 'P':
        print fruits

# 
# Part 2 -- use a duplicate list for changes (removals) 
# 

doublefruit_list = fruit_list * 2
    
print "The fruits are: ", fruit_list
user_delete = raw_input(u'Choose fruit to remove from list-->')

# delete selected fruit
while user_delete in doublefruit_list:
    doublefruit_list.remove(user_delete)

print doublefruit_list

# 
# Part 3
# 

originalfruit_list = fruit_list[:]
# this copy will be used for part 4

for fruits in fruit_list:
    bad_fruit = raw_input('Would you like to remove the fruit: %s?' % fruits)
    if bad_fruit[0].lower() == "no":
        while fruits in fruit_list:
            fruit_list.remove(fruits)
    elif bad_fruit[0].lower() == "yes":
        pass
    else:
        print fruit_list

fruit_list = originalfruit_list[:]

# 
# Part 4 
# 

newfruit_list = []
for fruits in fruit_list:
    r_fruits.append(fruit[::-1])

print newfruit_list and fruit_list


    

























    