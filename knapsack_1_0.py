def knapsack(items, wts, max_weight):
    """
    >>> items = [60, 100, 120]
    >>> wts = [10, 20, 30]
    >>> knapsack(items, wts, 50)
    220
    """
    n = len(items)
    cache = [[0 for i in range(max_weight + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j  in range(max_weight + 1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif wts[i - 1] <= j:
                cache[i][j] = max(cache[i-1][j], items[i-1] + cache[i-1][j-wts[i-1]])
            else:
                cache[i][j] = cache[i-1][j]
    return cache[n][max_weight]

items = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]
wts = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]
knapsack_size = 67

print(knapsack(items, wts, knapsack_size))

if __name__ == "__main__":
    import doctest
    doctest.testmod()