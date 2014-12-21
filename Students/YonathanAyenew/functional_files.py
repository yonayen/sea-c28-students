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

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print u'clean the input_name -- clean whitespace in front and back.  Give output_name file to prenvent input_name from being overwritten"
    
        sys.exit(1)

    else:
        input_name = sys.argv[1]
        try: 
            output_name = sys.argv[2]
        except IndexError:
            input_name = output_name

    map_clean(input_name, output_name)
    comprehension_clean(input_name, output_name)      











