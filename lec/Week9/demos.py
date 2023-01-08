# Fib call decorator


# def count(f):
#     """Return a counted version of f with a call_count attribute.
#
#     >>> def fib(n):
#     ...     if n == 0 or n == 1:
#     ...         return n
#     ...     else:
#     ...         return fib(n-2) + fib(n-1)
#     >>> fib = count(fib)
#     >>> fib(20)
#     6765
#     >>> fib.call_count
#     21891
#     """
#     def counted(*args):
#         counted.call_count += 1
#         return f(*args)
#     counted.call_count = 0
#     return counted
#
#
# def memo(f):
#     """Memoize f.
#
#     >>> def fib(n):
#     ...     if n == 0 or n == 1:
#     ...         return n
#     ...     else:
#     ...         return fib(n-2) + fib(n-1)
#     >>> fib = count(fib)
#     >>> fib(20)
#     6765
#     >>> fib.call_count
#     21891
#     >>> counted_fib = count(fib)
#     >>> fib  = memo(counted_fib)
#     >>> fib(20)
#     6765
#     >>> counted_fib.call_count
#     21
#     >>> fib(35)
#     9227465
#     >>> counted_fib.call_count
#     36
#     """
#     cache = {}
#     def memoized(n):
#         if n not in cache:
#             cache[n] = f(n)
#         return cache[n]
#     return memoized
#
# @count
# @memo
# def fib(n):
#     """The nth Fibonacci number.
#
#     >>> fib(20)
#     6765
#     """
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-2) + fib(n-1)

#
# @count
# def fib(n):
#     """The nth Fibonacci number.
#
#     >>> fib(20)
#     6765
#     """
#     if n == 0 or n == 1:
#         return n
#     else:
#         return fib(n-2) + fib(n-1)


def count_frames(f):
    """Return a counted version of f with a max_count attribute.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count_frames(fib)
    >>> fib(20)
    6765
    >>> fib.open_count
    0
    >>> fib.max_count
    20
    >>> fib(25)
    75025
    >>> fib.max_count
    25
    """
    def counted(n):
        counted.open_count += 1
        counted.max_count = max(counted.max_count, counted.open_count)
        result = f(n)
        counted.open_count -= 1
        return result
    counted.open_count = 0
    counted.max_count = 0
    return counted

@count_frames
def fib(n):
    """The nth Fibonacci number.

    >>> fib(20)
    6765
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

if __name__ == "__main__":
    fib(5)
    print(fib.open_count)
    print(fib.max_count)