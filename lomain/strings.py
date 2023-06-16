
def get_nth_to_last_instance(s, char, n=0):
    """Returns the index of the nth-to-last instance of a provided character in a
    provided string.

    Parameters
    ----------
    s : str
        The string to search
    char : str
        The character to lookup in s
    n : int
        The n in nth-to-last instance
    """
    for _ in range(n+1):
        idx = s.rfind(char)
        s = s[:idx]
    return idx