"""
knapsack_1_0.py

knapsack problem using dymanic programming

The way that I implmeneted the knapsack problem was with 
a table, where the rows and columns are the items' weight and value.

The nth cell of the table will contain the best possible value when given
the choose of all the items less than n. So if adding n to the solution makes
the bag too heavy, we just keep the previous best solution. This gives us the
recurrance relation:
knapsack[i][j] = 
    if we are not over weight, add the ith item or keep the previous solution -> knapsack[]
    if adding the new item will be too heavy -> knapsack[i - 1][j] 

"""

def knapsack(items, weights, max_weight):
    """
    >>> items = [60, 100, 120]
    >>> weights = [10, 20, 30]
    >>> knapsack(items, weights, 50)
    220
    """
    n = len(items)
    cache = [[0 for i in range(max_weight + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        for j  in range(max_weight + 1):
            #this first condition is to fill in the solutions for which we use 0 items
            if i == 0 or j == 0:
                cache[i][j] = 0
            #if the solution does not go over the weight then choose either the previous
            #solution or add the new item, depending on which will be more optimal.
            elif weights[i - 1] <= j:
                #If we choose to add a new item, make sure to add its value and subtract its weight
                cache[i][j] = max(cache[i-1][j], items[i-1] + cache[i-1][j-weights[i-1]])
            else:
                cache[i][j] = cache[i-1][j]
    return cache[n][max_weight]

items = [505, 352, 458, 220, 354, 414, 498, 545, 473, 543]
weights = [23, 26, 20, 18, 32, 27, 29, 26, 30, 27]
knapsack_size = 67

print(knapsack(items, weights, knapsack_size))

if __name__ == "__main__":
    import doctest
    doctest.testmod()