#!/usr/bin/env python

#Ackerman Function

def ack (m, n):
    """ Solve for Ackerman fucntion (values m and n are non-negative integers)."""
    if m < 0 or n < 0:
        return None
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))


if __name__ == '__main__':

    assert ack(0, 0) == 1
    assert ack(0, 4) == 5
  
    assert ack(1, 2) == 4
    assert ack(1, 4) == 6
 
    assert ack(2, 2) == 7
    assert ack(2, 4) == 11
    
    assert ack(3, 2) == 29
    assert ack(3, 4) == 125
    
    assert ack(-1, 0) is None
    assert ack(2, -1) is None
    
    # When m > 3, RuntimeError: maximum recursion depth exceeded 
    assert ack(4, 1)

    print u"all the tests passed"
