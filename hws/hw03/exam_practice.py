def collapse(n):
    """For non-negative N, the result of removing all digits that are equal
    to the digit on their right, so that no adjacent digits are the same.
    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(3)
    3
    >>> collapse(11200000013333)
    12013
    """
    left, last = n // 10, n % 10
    if last < 10:
        return last
    elif left % 10  ==  last:
        return collapse(left)
    else:
        return collapse(left) * 10 + last



def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234)
    11223344
    """
    last, rest = n // 10, n % 10
    if last == 0:
        return rest * 10 + rest
    return repeat_digits(last) * 100 + rest*10 + rest


def contains(a, b):
    """Return whether the digits of a are contained in the digits of b.
    >>> contains(357, 12345678)
    True
    >>> contains(753, 12345678)
    False
    >>> contains(357, 37)
    False
    """
    if a == b:
        return True
    if a > b:
        return False
    if a % 10 == b % 10:
        return contains( a // 10 , b // 10 )
    else:
        return contains( a , b // 10 )


if __name__ == "__main__":
    print(repeat_digits(1234))