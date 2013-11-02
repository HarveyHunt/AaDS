#!/usr/bin/python3

def factorial(n):
    """
    Recursively calculate the factorial of n.
    n!
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print(factorial(0))
    print(factorial(12))
