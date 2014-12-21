#!/usr/bin/env python

# codingBat exercise in format

# def count_evens(nums):
#    one_line_comprehension_here


def count_evens(nums):
    return len([i for i in nums if not (i % 2)])