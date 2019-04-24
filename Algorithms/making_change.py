def brute_force():
    """
    My super gross brute force solution
    """
    ways = 1
    for a in range(3):
        for b in range(1+(200 - 100 * a)//50):
            for c in range(1+(200 - 100 * a - 50 * b)//20):
                for d in range(1+(200 - 100 * a - 50 * b - 20 * c)//10):
                    for e in range(1+(200 - 100 * a - 50 * b - 20 * c - 10 * d)//5):
                        for _ in range(1+(200 - 100 * a - 50 * b - 20 * c - 10 * d - 5 * e)//2):
                            ways += 1

    return ways

def make_change(target):
    """
    A nice dynamic programming version
    based on these two:
    http://interactivepython.org/courselib/static/pythonds/Recursion/DynamicProgramming.html
    https://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    cache = [0] * (target + 1)

    cache[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], target + 1):
            cache[j] += cache[j - coins[i]]

    return cache[len(cache) - 1] #-1 because lists start a 0

print(make_change(200))