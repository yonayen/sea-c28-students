

# Fibonacci Series

def fibonacci(n):
    """Using looping technique, start with integers 0 and 1."""
    a,b = 0, 1
    for i in range (n-1):
   	    a,b = b, a + b
    return a

# Lucas Numbers

def lucas(n):
	""" Using looping technique, start with integers 2 and 1 """
    a, b = 2, 1
    for i in range (n-1):
        a, b = b, a + b
    return a