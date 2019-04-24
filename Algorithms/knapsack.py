def smallestFirst(s, t):
  result = []

  for _ in s:
    result.append(min(s))
    s.remove(min(s))

    if sum(result) == t:
      return result

def largestFirst(s, t):
  result = []

  for _ in s:
    result.append(max(s))
    s.remove(max(s))

    if sum(result) == t:
      return result