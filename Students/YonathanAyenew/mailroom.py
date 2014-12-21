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
        user_response = thank_you() # use this to create thank you email
    
    elif user_response == u'2':
        user_response = create_report() # create donor report
    
    else:
        # invalid selection
        print(u'Not a valid option, choose again.')
        .....

def thank_you():
    """Prompt to (1) see list of donors; (2) donor name and donation amount and compose thank you email.  
       Append new donor to list if user provides it. """
    
    if user_response.lower() == u'q':
        quit() #quit the mailroom
    
    elif user_response == u's':     
        user_response = navigate_prompt()  #Takes user back to navigate_prompt

    elif user_response.lower() == u'list': #Prints list of donors and returns to prompt
        for name in Donor_list.keys():
            print(u'{}'.format(name))
        user_response = thank_you()
        
    else:
        name, donation = name_donation(user_response) # Verify user inputted name
        user_response = create_email(name, donation) # Create thank you email

    return user_response


def name_donation(name):
    """ Show name of donor and respective donation amount. """
    Donor_list.setdefault(name, []) # Will add new donor name to list
    donation = new_donation() # ask for donation amount
    Donor_list.get(name).append(donation)

    return name, donation 

def new_donation():
    """ Return donation amount. """

    prompt = u'What is the Donation amount? (\n q: Quit \n s: Start over) --> '
    user_response = raw_input(prompt)

    if user_response.lower() == 'q': # Quit Mailroom
        quit()
    elif user_response == u's': # Takes user back to navigation prompt
        user_response = navigate_prompt()
        return user_response
    
    else: #verify if input is a real number
        try:
            donation = float(user_response)
        except ValueError:
            print (u'Input not a number, please try again!')
            donation = new_donation()
        else:
            donation = donation

    return donation    

def create_email(name, donation):
    """ Compose Email from given template. """
    
    # The email template
    template = u'{name}, thank you for your donation of ${donation}'.format(name, donation)
    print (template)

    user_response = navigate_prompt() # Start again from first prompt.
    return user_response

def create_report():






# Print email to the terminal and return to original prompt (quit)


# IF 'CREATE A REPORT' is Selected
# print list of donors sorted by historical donation amount; include donation amount

# Donor name, total donated, number of donations, average donation, (all as values in each row)

# Use string formatting to 







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