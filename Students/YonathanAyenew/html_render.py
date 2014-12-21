#!/usr/bin/env python

import cStringIO
import itertools

class Element(object): 
    tags = (u"<>", u"</>")
    indent = u"    "

    def __init__(self, contents=None, **kwargs):
        #Start list for content of html elements

        if contents:
            self.contents = [contents]
        else:
            self.contents = []

        self.kwargs = kwargs

    def append(self, string):
        