
	#!/usr/bin/python

	# List_lab.py
	from __future__ import print_function

    # Part 1, creating the list

    fruit_list = [u"Apples", u"Pears", u"Oranges", u"Peaches"]
    print fruit_list

    new_fruit = raw_input(u'what other fruit would you like to add to list?-->')
    fruit_list.append(new_fruit)
    print fruit_list
    
    # using '1 is first' to dispay number corresponding to fruit
    user_number = raw_input(u'choose number between 1 and 5-->')
    print fruit_list[int(user_number)-1]

    fruit_list = [u'Bananas', u'Grapes'] + fruit_list
    print fruit_list

    fruit_list = fruit_list.insert(0, u'Kiwis')
    print fruit_list

    for fruits in fruit_list:
        if fruits[0] == 'P':
            print fruits

    # Part 2, 

    print fruit_list
    del fruit_list[-1]
    
    print fruit_list
    user_delete = raw_input(u'Choose fruit to remove from list-->')
    
    # delete selected fruit
    fruit_list.pop(fruit_list.index(user_delete))
    print fruit_list

    # Part 3

    [each_fruit.lower() for each_fruit in fruit_list]
    print fruit_list
    # Make fruit_list lower case

    for fruits in fruit_list:
        bad_fruit = raw_input(u'Would you like to remove the fruit?-->')
        
        # if fruit is chosen it's removed from the fruit_list
        if bad_fruit in fruit_list:
            fruit_list.remove(bad_fruit)
            print bad_fruit, "has been deleted"
        else:
            print bad_fruit, "can't be delted because it's not in the fruit_list"
        print "The fruit_list has", len(fruit_list), "fruits:", fruit_list

    # Part 4 
    
    newfruit_list = fruit_list[:]
    # make copy of original fruit_list
    newfruit_list.reverse()
    del newfruit_list[-1]
    # reverse and delete last fruit in copied list

    print newfruit_list and fruit_list


    

























 	