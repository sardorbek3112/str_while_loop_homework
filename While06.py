def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    vowels = "a,e,i,o,u"

    idx = 0
    k = 0
    s = s.lower()
    
    while idx < len(s):
        # print(s[idx])
        if s[idx] not in vowels and s[idx].isalpha():
            k += 1
            print(s[idx])

        idx += 1

    return k

s = main("CodeschoolUz")
print(s)