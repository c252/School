import math
import numpy

def f(x):
    return x**x

def integrate(a, b, n):
    dx = numpy.linspace(a, b, n)
    area = 0
    for i in range(len(dx) - 1):
        area += f(dx[i]) * (dx[1] - dx[0]) #because dx is constant
    return area