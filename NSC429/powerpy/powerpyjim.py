""" 
 power.py
 Jim Mahoney | cs.marlboro.college | Jan 2019 | MIT License 
"""

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
    for i in range(int(b)):
        result *= a
        result = result % c
    return result

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
    while pow > 0:
        if pow & 1:
            result = (result * fact) % c
        pow //= 2
        fact = (fact * fact) % c
    return result

def main():
    print("--- power(a,b,c) = a**b mod c ---")
    a = int(input(" a = ? "))
    b = int(input(" b = ? "))
    c = int(input(" c = ? "))
    fast = input(" fast (y/n) ? ")[0] == 'y'
    if fast:
        power = power2
    else:
        power = power1
    print(" {}**{} % {} is {}".format(a, b, c, power(a,b,c)))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()