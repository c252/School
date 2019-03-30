"""
tprime.py

A poisitive integer is considered to be a
T-prime if it has exactly 3 divisors.

The problem states that you are given an
array of n positive integers and must determine
whether or not they are T-prime
"""
def brute_force(nums):
    tprimes = []
    for n in nums:
        if _brute_force(n) == True:
            tprimes.append(n)
    return tprimes

def _brute_force(n):
    divisors = 1
    for i in range(1,n):
        if divisors > 3:
            return False
        if n % i == 0:
            divisors += 1
    
    #This last little bit of logic is because
    #a prime number is an edgecase
    if divisors < 3:
        return False
    return True