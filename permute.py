"""
permute.py
"""

def permute(string):
    """
    >>> permute('ab')
    ['ab', 'ba']
    """
    if len(string) == 1:
        return list(string)
    else:        
        permutations = []
        for i in range(len(string)):
            sub = string[0:i] + string[i:]
            permutations.append(sub)
        return permutations