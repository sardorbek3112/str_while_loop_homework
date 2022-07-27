def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    c = 0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            c += int(s[i])
        i += 1
    return c