#!/usr/bin/env python

from __future__ import print_function



# Dict with Donor name and Donation amounts.
Donor_list = {u'John' : [30.00, 10.00, 20.00], 
              u'Carl' : [15.00], 
              u'Kate' : [25.00, 15.00], 
              u'Kent' : [20.00, 10.00], 
              u'Alice': [50.00, 100.00, 40.00]}


# Choose 'Send a Thank You Note' or 'Create a Report'
def start_prompt():
    """ Returns the input selected between 'Send a Thank You Note' and 'Create a Report' """
    try: 
        user_response = raw_input("\n 1:'Send a Thank You' \n 2:'Create a List' \n q: Quit -->")
    except (EOFError, KeyboardInterrupt):
        quit()
    else:
        return user_response.decode('utf-8') # Response in unicode format

def navigate_prompt():
    """ Navigate to Quit, 'Send a Thank You', or 'Create a Report' """
    user_response = start_prompt()
    if user_response.lower() == u'q':
        quit() #quit the mailroom
    elif user_response == u'1':
        user_response = thank_you_prompt() # use this to create thank you email
    elif user_response == u'2':
     


# if they type 'list' -- show list of donor names and reprompt

# if they type name not on list -- add to data structure and use it
# if name is already on the list then use it

# Once name is selected -- prompt for a donation amount

# Verify that input is in fact a number -- reprompt if necessary

# Once number is given -- add it to the donation history

# Use string formatting to compose an email thanking donor for their donation

# Print email to the terminal and return to original prompt (quit)


# IF 'CREATE A REPORT' is Selected
# print list of donors sorted by historical donation amount; include donation amount

# Donor name, total donated, number of donations, average donation, (all as values in each row)

# Use string formatting to 



In [47]: d
Out[47]: {u'something': u'a value'}
In [48]: item_view = d.viewitems()
In [49]: item_view
Out[49]: dict_items([(u'something', u'a value')])
In [50]: d['something else'] = u'another value'

In [51]: item_view
Out[51]: dict_items([('something else', u'another value'), (u'something', u'a value')])



In [26]: d = {'name': 'Brian', 'score': 42}

In [27]: for k, v in d.items():
   ....:     print("%s: %s" % (k,v))
   ....:
score: 42
name: Brian



try:
    num_in = int(num_in)
except ValueError:
    print(u"Input must be an integer, try again.")


if __name__ == '__main__':