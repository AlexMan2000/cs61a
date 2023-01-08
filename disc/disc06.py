def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"
    s.extend(len(list(filter(lambda t: t == x, s))) * [el])



def iterator():
    d = {'one': 1, 'two': 2, 'three': 3}  # Keys and values
    k = iter(d)  # next(k), default to iterate through the keys
    v = iter(d.values())  # next(v), iterate through the values
    k = iter(d)  # new iterator object
    d.get('four',0)
    print(list(k))
    # s = [1, 2, 3, 4]
    # i = iter(s)
    # s.pop(0)
    # print(next(i))
    # s.pop(0)
    # print(next(i))
    # j = iter(next(i))
    # print(next(j))


# def filter_iter(iterable, f):
    # """
    # >>> is_even = lambda x: x % 2 == 0
    # >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    # [0, 2, 4]
    # >>> all_odd = (2*y-1 for y in range(5))
    # >>> list(filter_iter(all_odd, is_even))
    # []
    # >>> naturals = (n for n in range(1, 100))
    # >>> s = filter_iter(naturals, is_even)
    # >>> next(s)
    # 2
    # >>> next(s)
    # 4
    # """
    # "*** YOUR CODE HERE ***"
    # yield from iter([1,2,3,4,5])


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)


def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n-1)


def primes_gen_ascending(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen_ascending(7)
    >>> list(pg)
    [2, 3, 5, 7]
    """
    if n == 1:
        return
    yield from primes_gen_ascending(n - 1)
    if is_prime(n):
        yield n



def generate_preorder(t):
    """Yield the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> gen = generate_preorder(numbers)
    >>> next(gen)
    1
    >>> list(gen)
    [2, 3, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"


    yield label(t)
    for b in branches(t):
        yield from generate_preorder(b)


def test(i):
    if i % 2 == 0:
        yield "haha"

    yield "normal"


# Tree ADT

def change_abstraction(change):
    """
    For testing purposes.
    >>> change_abstraction(True)
    >>> change_abstraction.changed
    True
    """
    change_abstraction.changed = change


change_abstraction.changed = False


def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)



def mystery(p, q):
    p[1].extend(q)
    q.append(p[1:])





if __name__ == "__main__":
    # s = [1, 2, 4, 2, 1]
    # add_this_many(1,5,s)
    # add_this_many(2, 2, s)
    # print(s)
    # iterator()
    # g = filter_iter(range(5), lambda x: x%2==0)
    # print(next(g))
    # print(next(g))
    # print(type(range(5)))
    # g = test(1)
    # print(next(g))
    # print(next(g))
    p = [2, 3]
    q = [4, [p]]
    mystery(p, q)
