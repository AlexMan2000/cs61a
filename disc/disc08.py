# Q3
def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    "*** YOUR CODE HERE ***"
    if s.rest is Link.empty:
        return s.first

    return s.first + sum_nums(s.rest)



# Q4
# def multiply_lnks(lst_of_lnks):
#     """
#     >>> a = Link(2, Link(3, Link(5)))
#     >>> b = Link(6, Link(4, Link(2)))
#     >>> c = Link(4, Link(1, Link(0, Link(2))))
#     >>> p = multiply_lnks([a, b, c])
#     >>> p.first
#     48
#     >>> p.rest.first
#     12
#     >>> p.rest.rest.rest is Link.empty
#     True
#     """
#     # Implementation Note: you might not need all lines in this skeleton code
#     # curr_product = 1
#     # for linked_list in lst_of_lnks:
#     #     if linked_list is Link.empty:
#     #         return linked_list
#     #     curr_product *= linked_list.first
#     # lst_of_lnks_rest = [lnk.rest for lnk in lst_of_lnks]
#     # return Link(curr_product,multiply_lnks(lst_of_lnks_rest))
#     curr_lnk_lst = lst_of_lnks
#     p = Link(Link.empty)
#     res = p
#     while Link.empty not in curr_lnk_lst:
#         curr_product = 1
#         for linked_list in curr_lnk_lst:
#             curr_product *= linked_list.first
#         curr_lnk_lst = [lnk.rest for lnk in curr_lnk_lst]
#         p.first = curr_product
#         p.rest = Link(Link.empty)
#         p = p.rest
#     return res
    #
    # import operator
    # from functools import reduce
    # def prod(factors):
    #     return reduce(operator.mul, factors, 1)
    #
    # head = Link.empty
    # tail = head
    # while Link.empty not in lst_of_lnks:
    #     all_prod = prod([l.first for l in lst_of_lnks])
    #     if head is Link.empty:
    #         head = Link(all_prod)
    #         tail = head
    #     else:
    #         tail.rest = Link(all_prod)
    #         tail = tail.rest
    #         lst_of_lnks = [l.rest for l in lst_of_lnks]
    # return head
    #

# Q5
def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    "*** YOUR CODE HERE ***"
    if s.rest is Link.empty or s is Link.empty:
        return

    # s.first, s.rest.first = s.rest.first, s.first
    #
    # flip_two(s.rest.rest)
    #
    # new_head = s.rest
    # tail = s.rest.rest
    # flip_two(tail)
    # s.rest = tail
    # new_head.rest = s
    # s = new_head

    # # For an extra challenge, try writing out an iterative approach as well below!
    # "*** YOUR CODE HERE ***"
    # pass
    while s.rest is not Link.empty and s is not Link.empty:
        s.first, s.rest.first = s.rest.first, s.first
        s = s.rest.rest


# Q6
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    "*** YOUR CODE HERE ***"
    if t.label % 2 == 1:
        t.label += 1

    for b in t.branches:
        make_even(b)





# Q7
def add_d_leaves(t, v):
    """Add d leaves containing v to each node at every depth d.

    >>> t_one_to_four = Tree(1, [Tree(2), Tree(3, [Tree(4)])])
    >>> print(t_one_to_four)
    1
      2
      3
        4
    >>> add_d_leaves(t_one_to_four, 5)
    >>> print(t_one_to_four)
    1
      2
        5
      3
        4
          5
          5
        5

    >>> t1 = Tree(1, [Tree(3)])
    >>> add_d_leaves(t1, 4)
    >>> t1
    Tree(1, [Tree(3, [Tree(4)])])
    >>> t2 = Tree(2, [Tree(5), Tree(6)])
    >>> t3 = Tree(3, [t1, Tree(0), t2])
    >>> print(t3)
    3
      1
        3
          4
      0
      2
        5
        6
    >>> add_d_leaves(t3, 10)
    >>> print(t3)
    3
      1
        3
          4
            10
            10
            10
          10
          10
        10
      0
        10
      2
        5
          10
          10
        6
          10
          10
        10
    """
    "*** YOUR CODE HERE ***"
    def helper(t, d):
        """
        The helper function to add_d_leaves
        :param t: tree structure
        :param v: value to be added
        :param d: curr depth
        :return:
        """
        for b in t.branches:
            helper(b, d+1)

        for _ in range(d):
            t.branches.append(Tree(v))


    helper(t,0)




# ADT
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(repr(self.label), branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines

    def is_leaf(self):
        return not self.branches


if __name__ == "__main__":
    a = Link(2, Link(3, Link(5)))
    b = Link(6, Link(4, Link(2)))
    c = Link(4, Link(1, Link(0, Link(2))))
    p = multiply_lnks([a, b, c])
    print(Link.empty)