"""
square_sum.py

Find the minimum number of squares that equal n
ie:
n = 10

min_sqr = 3^2 + 1^2
"""
from math import sqrt

def min_sqr(n):
    cache = [0] * (n + 1)

    cache[0] = 0 #0^2 = 0
    cache[1] = 1 #1^2 = 1

    for i in range(2, n + 1):
        cache[i] = i
        j = 1
        while j**2 <= i:
            cache[i] = min(cache[i], 1 + cache[i - j**2])
            j += 1

    return cache[n] 