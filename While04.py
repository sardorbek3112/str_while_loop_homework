def main(s):
    """
    A variable of type str is given. Find how many uppercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    c = 0
    i = 0
    while i < len(s):
        if s[i].isupper():
            c += 1
        i += 1
    return c