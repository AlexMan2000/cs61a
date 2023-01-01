# def get_k_run_starter(n, k):
#     """Returns the 0th digit of the kth increasing run within n.
#     >>> get_k_run_starter(123444345, 0) # example from description
#     3
#     >>> get_k_run_starter(123444345, 1)
#     4
#     >>> get_k_run_starter(123444345, 2)
#     4
#     >>> get_k_run_starter(123444345, 3)
#     1
#     >>> get_k_run_starter(123412341234, 1)
#     1
#     >>> get_k_run_starter(1234234534564567, 0)
#     4
#     >>> get_k_run_starter(1234234534564567, 1)
#     3
#     >>> get_k_run_starter(1234234534564567, 2)
#     2
#     """
#     i = 0
#     final = None
#     while n > 0 and i <= k:
#         while n > 10 and ((n // 10) % 10) < (n % 10):
#             n //= 10
#         final = n % 10
#         i = i + 1
#         n = n // 10
#         print(final)
#     return final


def num_eights(pos):
    if pos < 10:
        return int(pos == 8)
    return num_eights(pos // 10) + int((pos % 10) == 8)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    """
    "*** YOUR CODE HERE ***"
    # def helper(curr_number, curr_step, direction):
    #
    #     if curr_step == n:
    #         return curr_number
    #
    #     if curr_step % 8 == 0 or num_eights(curr_step):
    #         return helper(curr_number + (-direction) , curr_step + 1, -direction)
    #     else:
    #         return helper(curr_number + direction, curr_step + 1, direction)
    #
    #
    # return helper(1, 1, 1)

    curr_number, curr_step, direction = 1, 1, 1
    while curr_step != n:
        if curr_step % 8 == 0 or num_eights(curr_step):
            curr_number, direction = curr_number + (-direction), -direction
        else:
            curr_number, direction =  curr_number + direction, direction
        curr_step += 1
    return curr_number

if __name__ == "__main__":
    # get_k_run_starter(123444345, 3)
    print()