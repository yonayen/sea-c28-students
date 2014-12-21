#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import string
import io
import sys

# 
# cleans strips whitespace off both front and back of each line.  
# original will be overwritten if altenative filename not given
# 

def map_clean(input_name, output_name):
    inlines = io.open(input_name).readlines()

    outlines = map(string.strip, inlines)

    outfile = io.open(output_name, 'w')
    for line in outlines:
        outfile.write(line + "\n")
    # newline back in when writing

def comprehension_clean(input_name, output_name):

    inlines = io.open(input_name).readlines()
    outlines = [line.strip()+ "\n" for line in inlines]

    io.open(output_name, 'w').writelines(outlines)

