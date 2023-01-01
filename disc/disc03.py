# def is_prime(n):
#     """Returns True if n is a prime number and False otherwise.
#
#     >>> is_prime(2)
#     True
#     >>> is_prime(16)
#     False
#     >>> is_prime(521)
#     True
#     """
#     "*** YOUR CODE HERE ***"
#
#     def helper(i):
#         if i > n ** 0.5:
#             return True
#         else:
#             if n % i == 0:
#                 return False
#             else:
#                 return helper(i + 1)
#
#     return helper(2)


def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    # def helper(i, s):
    #     print(i)
    #     if i != 1:
    #         if i % 2 == 0:
    #             return helper(i // 2, s+1)
    #         else:
    #             return helper(3*i + 1, s+1)
    #     return s
    #
    # return helper(n, 1)
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(3 * n + 1)



def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    "*** YOUR CODE HERE ***"
    # Base Case
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1

    # Recursive Step
    all_but_last1, last1 = n1 // 10 , n1 % 10
    all_but_last2, last2 = n2 // 10 , n2 % 10
    if last1 >= last2:
        return merge(n1, all_but_last2) * 10 + last2
    else:
        return merge(all_but_last1, n2) * 10 + last1


def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10



if __name__ == "__main__":
    a = merge(21,31)
    print(a)