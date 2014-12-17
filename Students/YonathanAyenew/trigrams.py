#!/usr/bin/env python
# -*-coding: UTF-8 -*-

# trigrams.py

from io import open
import string
# import sys
# import random

data_source = u'sherlock.txt'


def make_string(text):

    """ create string with no punctuation and special characters. """

    

    punctuation = string.punctuation.replace("'", "")
    # keep words with apostrophies

    punctuation = string.punctuation.replace("-", "")
    # keep words with hyphens

    text = text.lower()
    # universal lower-case
    
    words = text.split()
    # create words by splitting


def make_words(text):

    """strips all the punctuation and other stuff from a string"""

    # build a translation table for string.translate:
    # there are other ways to do this:
    #   a_word.strip() works well, too.

    punctuation = unicode(string.punctuation)
    punctuation = string.punctuation.replace("'", "")  # keep apostropies
    punctuation = string.punctuation.replace("-", "")  # keep hyphenated words
    table = dict([(ord(c), None) for c in punctuation])

    # lower-case everything to remove that complication:
    text = text.lower()

    # remove punctuation
    text = text.translate(table)

    # split into words
    words = text.split()

    # remove the bare single quotes
    # " ' " is both a quote and an apostrophe
    words = [word for word in words if word != "'"]

    return words

# 
# d 
# 

def read_in_data(data_source):

    in_data = open(data_source, 'r')
    # get rid of first 61 lines of Table of Contents and header.
    for i in range(61):
        in_data.readline()

    rest_of_text = []
    # read the rest of the file line by line
    for line in in_data:
        if line.startswith(u"End of the Project Gutenberg EBook"):
            break
        rest_of_text.append(line)

    # combine lines together into one big string:
    return " ".join(rest_of_text)


# 
# Now Create the Trigram
# 


def trigram_create(words):
    """build a trigram dict from the passed-in text"""

    # Dictionary for trigram results:
    # The keys will be all the word pairs
    # The values will be a list of the words that follow each pair
    word_pairs = {}

    # loop through the words
    for i in range(len(words) - 2):
        pair = tuple(words[i:i+2])  # a tuple so it can be a key in the dict
        follower = words[i+2]
        word_pairs.setdefault(pair, []).append(follower)

        # setdefault() returns the value if pair is already in the dict
        #    if it's not, it adds it, setting the value to a an empty list
        #    then it returns the list, which we then append the following
        #    word to -- cleaner than:
        # if pair in word_pairs:
        #     word_pairs[pair].append(follower)
        # else:
        #     word_pairs[pair] = [follower]
    return word_pairs


# 
# Build new text from pair of words that will act as a key
# 

def build_text(word_pairs):

    """build some new text from the word_pair dict supplied"""

    new_text = []
    for i in range(30):  # do thirty sentences
        # pick a word pair to start the sentence
        sentence = list(random.choice(word_pairs.keys()))

        # now add a random number of additional words to the sentence
        for j in range(random.randint(2, 10)):
            pair = tuple(sentence[-2:])
            sentence.append(random.choice(word_pairs[pair]))
        # capitalize the first word:
        sentence[0] = sentence[0].capitalize()
        # Add the period
        sentence[-1] += u"."
        new_text.extend(sentence)

    new_text = " ".join(new_text)

    return new_text


if __name__ == "__main__":

    # get the filename from the command line
    try:
        filename = sys.argv[1]
    except IndexError:
        print "You must pass in a filename"
        sys.exit(1)

    in_data = read_in_data(filename)
    words = make_words(in_data)
    word_pairs = trigram_create(words)
    new_text = build_text(word_pairs)

    print new_text


