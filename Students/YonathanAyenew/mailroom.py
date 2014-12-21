#!/usr/bin/env python

from __future__ import print_function
from __future__ import division
from operator import itemgetter



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
    """ Return report of the list of donors, average donation amount, 
    number of donations and total donations. """
    
    matrix = []  # Where data will be displayed

    for name in Donor_list:
        donor = name
        
        donations = Donor_list[name] # list of donations (values in dict)
        
        total_donations = sum(donations) # sum of donations (values in dict)
        
        number_donations = len(donations) # Total number of donations

        average_donation = total_donations / number_donations   # Average donation

        matrix += [[donor, total_donations, number_donations, average_donation]]

    # Sort the matrix by total donor amount in decending order.
    edited_matrix = sorted(matrix, key = itemgetter(1), reverse = True)

    # Titles for Matrix Columns
    title = [u'Donor', u'Total Donations', u'Number of Donations', u'Average Donation']

    print(u'{0:<20}{1:>20}{2:>30}{3:>30}'.format(title)
    for content in range(len(matrix)):
        args = [edited_matrix[content][0],
                "${:.2f}".format(edited_matrix[content][1]),
                edited_matrix[content][2],
                "{:.2f}".format(edited_matrix[content][3])
                ] 

        # Right align in colums with dollar sign    
        print(u"{0:<20}{1:>20}{2:>30}{3:>30}".format(*args))

    user_response = navigate_prompt() # Goes back to first prompt
    return user_response


if __name__ == '__main__':

    # Begins mailroom prompt

    user_response = navigate_prompt()





