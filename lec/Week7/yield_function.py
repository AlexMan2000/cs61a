def countdown(k):
    """Count down to zero.

    >>> list(countdown(5))
    [5, 4, 3, 2, 1]
    """
    if k > 0:
        yield k
        # countdown(k-1) returns a iterable object so that yield from can be used
        # to extract all the values from it
        yield countdown(k-1)

def yie(m):

    yield 1
    yield 2

def count(k):

    yield from yie(2)


def partitions(n, m):
    """List partitions.

    >>> for p in partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)

        for part in partitions(n-m, m):
            yield str(m) + " + " + part

        yield from partitions(n, m-1)




if __name__ == "__main__":
    for p in partitions(6,4): print(p)