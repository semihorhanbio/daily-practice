def longest(a1, a2):
    """Take 2 strings a1 and a2 including only letters from ato z. Return a new sorted string, the longest possible, 
    containing distinct letters - each taken only once - coming from a1 or a2."""
    
    return "".join(sorted(set(a1 + a2)))
