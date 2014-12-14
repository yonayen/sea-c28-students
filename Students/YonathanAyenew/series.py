#!/usr/bin/env python

# series.py -- Fibonacci Series and Lucas Numbers

# 
# Fibonacci Series
# 

def fibonacci(n):
    """ Begin computation starting with integers 0 and 1."""
    if n < 0:
        return None
    a, b = 0, 1
    # a and b represent first two numbers in sequence
    for i in range (n):
        a, b = b, a + b
    return a

# 
# Lucas Numbers
# 

def lucas(n):
    """ Begin computation starting with integers 2 and 1. """
    if n < 0:
        return None
    # a and b represent first two numbers in sequence
    a, b = 2, 1
    for i in range (n):
        a, b = b, a + b
    return a

# 
# Sum_Series function
# 
# if first two integers are 0 and 1 it is a Fibonacci series; if it's 2 and 1 it's a Lucas number series

def sum_series(n):
    """ Begin computation of a summation series. """
    if n < 0:
        return None
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a    


if __name__ == '__main__':

# asset tests

    assert fibonacci(-5) == None

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(-1) == None

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(4) == 7
    assert lucas(5) == 11

    # sum series equal to Fibonacci test
    for n in range(0, 10):
        assert sum_series(n) == fibonacci(n)

    # sum series equal to Lucas number series
    for in in range(0, 10):
        assert sum_series(n) == lucas(n)

    print "passed test"

  

  