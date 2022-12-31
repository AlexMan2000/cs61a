def tik(tok):
    """Returns a function that takes gram and prints tok and gram on a line.
    >>> tik(5)(6)
    5 6
    """
    def insta(gram):
        # The implementation of this function has been omitted.
        print(tok," ",gram)
    return insta

if __name__ == "__main__":
    tik(tik(5)(print(6)))(print(7))