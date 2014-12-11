#!/usr/bin/env python

# trigrams.py

from io import open
import string

infilename = u'sherlock.txt'

def make_string(text):

    """ create string with no punctuation and special characters. """

    text = text.lower()
    # universal lower-case
    words = text.split()
    # create words by splitting
