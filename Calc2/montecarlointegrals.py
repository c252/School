import random
import math
import numpy as np

random.seed(1)

#f is the function to integrate
def f(x):
    return (x ** 2)

#upper and lower bounds of integration
a = 1
b = 3
y_range = np.linspace(a,b,1000)
fmax = 0

for i in y_range:
    if f(i) > fmax:
        fmax = f(i) 

def under_curve(x, y):
    return y < f(x)

def integrate(count):
    in_f = 0
    for _ in range(count):
        x = random.uniform(a, b)
        y = random.uniform(0, fmax)
        if under_curve(x, y):
            in_f += 1
    return fmax * (b - a) / (count / in_f)