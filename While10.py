def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = '13579'
    c = 0
    i = 0
    while i < len(s):
        if s[i] in l:
            c += int(s[i])
        i += 1
    return c