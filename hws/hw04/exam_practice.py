def exp_tree(values):
    """
    Returns the exponential tree that can be made from VALUES
    with the greatest possible root label
    >>> print_tree(exp_tree([5]))
    5
    >>> print_tree(exp_tree([3, 2]))
    9
      3
      2
    >>> print_tree(exp_tree([2, 3, 2]))
    512
      2
      9
        3
        2
    >>> lst = [3, 1, 2, 3]
    >>> print_tree(exp_tree(lst))
    6561
      3
        3
        1
      8
        2
        3
    """
    if len(values) == 1:
        return tree(values[0])
    else:
        def tree_at_split(i):
            base = exp_tree(values[:i])
            exponent = exp_tree(values[i:])
            return tree(label(base) ** label(exponent), [base, exponent])
        trees = [tree_at_split(i) for i in range(1, len(values))]
        return max(trees, key=lambda x:x[0])


def max_path(t, k):
    """ Return a list of the labels on any path in tree t of length at most k with the greatest sum
    >>> t1 = tree(6, [tree(3, [tree(8)]), tree(1, [tree(9), tree(3)])])
    >>> max_path(t1, 3)
    [6, 3, 8]
    >>> max_path(t1, 2)
    [3, 8]
    >>> t2 = tree(5, [t1, tree(7)])
    >>> max_path(t2, 1)
    [9]
    >>> max_path(t2, 2)
    [5, 7]
    >>> max_path(t2, 3)
    [6, 3, 8]
    """
    def helper(t, k, can_skip):
        # length =0 无解
        if k == 0:
            return []
        # 到头了
        elif is_leaf(t):
            return [label(t)]
        a = [[label(t)] + helper(b, k-1, False) for b in branches(t)]
        if not can_skip:
            return max(a, key = lambda x:sum(x))
        else:
            b = [helper(b, k, True) for b in branches(t)]
            return max(a + b, key = lambda x:sum(x))
    return helper(t, k, True)


    # def helper(t, k):
    #     # length =0 无解
    #     if k == 0:
    #         return []
    #     # 到头了
    #     elif is_leaf(t):
    #         return [label(t)]
    #     a = [[label(t)] + helper(b, k-1) for b in branches(t)]
    #     b = [helper(b, k) for b in branches(t)]
    #     return max(a + b, key = lambda x:sum(x))
    # return helper(t, k)
    #


def count_ways(t, total):
    """Return the number of ways that any sequence of consecutive nodes in a root-to-leaf path
    can sum to total.
    >>> t1 = tree(5, [tree(1, [tree(2, [tree(1)]),
    ... tree(1, [tree(4, [tree(2, [tree(2)])])])]),
    ... tree(3, [tree(2, [tree(2),
    ... tree(3)])]),
    ... tree(3, [tree(1, [tree(3)])])])
    >>> count_ways(t1, 7)
    4
    >>> count_ways(t1, 4)
    6
    >>> t2 = tree(2, [tree(-10, [tree(12)]),
    ... tree(1, [tree(1),
    ... tree(-1, [tree(2)])])])
    >>> count_ways(t2, 2)
    6
    >>> count_ways(t2, 4)
    3
    """
    def paths(t, total, can_skip):
        ways = 0
        if total == label(t):
            ways += 1
        ways += sum([paths(b, total - label(t), False) for b in branches(t)])
        if can_skip:
            ways += sum([paths(b, total, True) for b in branches(t)])
        return ways
    return paths(t, total, True)



# tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
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


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])


if __name__ == " __main__":
    pass