import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    l = string.punctuation
    c = 0
    i = 0
    while i < len(s):
        if s[i] in l:
            c += 1
        i += 1
    return c