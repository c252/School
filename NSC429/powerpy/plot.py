""" 
 power.py
 Jim Mahoney | cs.marlboro.college | Jan 2019 | MIT License 
 Modified by Cyrus Burt
"""
import matplotlib.pyplot as plt
import statistics
import numpy as np

def power1(a, b, c):
    """ Return a**b mod c for integer a, b, c
        using repeated multiplication by a, b times.
        >>> power1(2, 10, 1000000)
        1024
        >>> power1(10, 5, 1000000)
        100000
        >>> power1(111111, 22222222, 123) # slow
        42
    """
    result = 1
    count = 1 #because intializing result is one step
    for i in range(int(b)): #1 step
        result *= a #2 steps
        result = result % c #2 steps
        count += 5
    return count

def power2(a, b, c):
    """ Return a**b for integer a, b 
        using exponentation by squaring.
        >>> power2(2, 10, 1000000)
        1024
        >>> power2(10, 5, 1000000)
        100000
        >>> power2(111111, 22222222, 123)
        42
        >>> power2(123456789, 11111111111, 9876) # too slow for power1
        7653
    """
    result = 1
    pow = b
    fact = a
    count = 3
    while pow > 0:
        if pow & 1:
            result = (result * fact) % c
        pow //= 2
        fact = (fact * fact) % c
        count += 1
    return count

def main():
    res1 = []
    res2 = []
    a = 5
    c = 10

    for b in range(1, 1000):
        res1.append(power2(a, b, c))

    for b in range(1, 1000):
        res2.append(power1(a, b, c))

    ns = np.array(range(1,len(res1)))
    nln = np.log(ns)

    fig1 = plt.figure(1)
    plt.plot(res1)
    plt.plot(nln)

    fig2 = plt.figure(2)
    plt.plot(res2)
    plt.show()

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main()
