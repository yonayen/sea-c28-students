#!/usr/bin/env python
# -*-coding: UTF-8 -*-

# trigrams.py

from io import open
import string
import sys
# for if __name__== "__main__": block
import random
# for build_text method


data_source = u'sherlock.txt'


# 
# clean up the text (remove punctuation etc)
# 

def make_string(text):

    """ create string with no punctuation and special characters. """

    punctuation = string.punctuation.replace("'", "")
    # keep words with apostrophies

    punctuation = string.punctuation.replace("-", "")
    # keep words with hyphens

    group = dict([(ord(c), None) for c in punctuation])

    text = text.lower()
    # universal lower-case

    text = text.translate(group)
    # punctuation removed
    
    string_words = text.split()
    # create words by splitting

    string_words = [word for word in string_words if word != "'"]
    # single quotes removed

    return string_words


# 
# Read data source to elminate begining and end that isn't useful
# 

def in_data(data_source):

     # get rid of first 61 lines of Table of Contents and header.
    file = open(data_source, 'r')
    for i in range(61):
        file.readline()

    # read the rest of the file line by line until the end
    rest_of_text = []
    for line in file:
        if line.startswith(u"End of the Project Gutenberg EBook"):
            break
        rest_of_text.append(line)

    # combine lines together into one big string:
    return " ".join(rest_of_text)


# 
# Now Create the Trigram
# 

def trigram_create(string_words):
    """build a trigram dict from the text"""

    # Dictionary for trigram results:
    # Using String_words from above -- Word pairs will for the key for the trigram, values will follow each pair
    
    word_pairs = {}

    # loop through the words
    for i in range(len(string_words) - 2):
        pair = tuple(string_words[i:i+2])  #  tuple will be a key in the dict
        value_follower = string_words[i+2]
        word_pairs.setdefault(pair, []).append(value_follower)

        
    return word_pairs


# 
# Create new text from pair of words that will act as a key
# 

def create_text(word_pairs):

    """build new text from the word_pair dict above"""

    new_form = []
    for i in range(30):  # do thirty sentences
        # pick a word pair to start the sentence
        sentence = list(random.choice(word_pairs.keys()))

        # now add a random number of additional words to the sentence
        for j in range(random.randint(2, 10)):
             pair = tuple(sentence[-2:])
            sentence.append(random.choice(word_pairs[pair]))
        
    new_form = " ".join(new_form)

    return new_form


if __name__ == "__main__":

    # get the_file from the command line
    try:
        thefile = sys.argv[1]
    except IndexError:
        print "Pass in the file"
        sys.exit(1)

    data = in_data(thefile)
    string_words = make_string(data)
    word_pairs = trigram_create(sting_words)
    new_form = create_text(word_pairs)

    print new_form


