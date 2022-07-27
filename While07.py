def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = '02468'
    c = 0
    i = 0
    while i < len(s):
        if s[i] in l:
            c += 1
        i += 1
    return c