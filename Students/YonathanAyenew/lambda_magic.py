#!/usr/bin/env python
# -*- coding: UTF-8 -*-



# Returns n functions, each will return input value when called (by an increasing number)

def function_builder(n):
    return [lambda x, i=i: x+i for i in range(n)]



if __name__ == '__main__':
    
    # list of length input
    assert len(function_builder(0)) == 0
    assert len(function_builder(5)) == 5
    assert len(function_builder(10)) == 10

    #  the_list will increment value 

    the_list = function_builder(5)

    assert the_list[0](2) == 2
    assert the_list[1](2) == 3
    assert the_list[2](2) == 4
    assert the_list[3](2) == 5
    assert the_list[4](2) == 6

    the_list = function_builder(10)

    assert the_list[0](10) == 10
    assert the_list[1](10) == 11
    assert the_list[2](10) == 12

    print "all tests passed"
