# Q7
# class HoopDice:
#     def __init__(self, values):
#         """Initialize a dice with possible values VALUES, and a starting INDEX
#         of 0. The INDEX indicates which value from VALUES to return when the
#         dice is rolled next.
#         """
#         self.values = values
#         self.index = 0
#     def roll(self):
#         """Roll this dice. Advance the index to the next step before returning.
#         """
#         value = ______________
#         ______________ = (______________) % ______________
#         return value
#
#     def next_player(self):
#         """Infinitely yields the next player in the game, in order.
#         >>> player_gen = game.next_player()
#         >>> next(player_gen) is player1
#         True
#         >>> next(player_gen) is player3
#         False
#         >>> next(player_gen) is player3
#         True
#         >>> next(player_gen) is player1
#         True
#         >>> next(player_gen) is player2
#         True
#         >>> new_player_gen = game.next_player()
#         >>> next(new_player_gen) is player1
#         True
#         >>> next(player_gen) is player3
#         True
#         """
#
#         yield from ______________
#         yield from ______________
#
#     def get_scores_except(self, player):
#         """Collects and returns a list of the current scores for all players
#         except PLAYER.
#         >>> game.get_scores_except(player2)
#         [0, 0]
#         """
#
#         return [______________ for pl in ______________ if ______________]
#
#     def roll_dice(self, num_rolls):
#         """Simulate rolling SELF.DICE exactly NUM_ROLLS > 0 times. Return sum of
#         the outcomes unless any of the outcomes is 1. In that case, return 1.
#         >>> game.roll_dice(4)
#         20
#         """
#
#         outcomes = [______________ for x in ______________]
#         ones = [______________ for outcome in outcomes]
#         return 1 if ______________(ones) else ______________(outcomes)
#
#     def play(self):
#         """Play the game while no player has reached or exceeded the goal score.
#         After the game ends, return all players' scores.
#         >>> game.play()
#         [20, 10, 60]
#         """
#         player_gen = self.next_player()
#         while max(self.get_scores()) < self.goal:
#             player = ______________(player_gen)
#             other_scores = self.get_scores_except(player)
#             num_rolls = ______________(player.score, other_scores)
#             outcome = self.roll_dice(num_rolls)
#             ______________ += outcome
#             return self.get_scores()
#
#
# class BrokenHoopDice(HoopDice):
#     def __init__(self, values, when_broken):
#         ______________(values)
#         self.when_broken = when_broken
#         self.______________ = False
#
#     def roll(self):
#         """
#         >>> broken = BrokenHoopDice([5, 6, 7], 11)
#         >>> broken.roll()
#         5
#         >>> [broken.roll() for _ in range(6)]
#         [11, 6, 11, 7, 11, 5]
#         """
#         if self.is_broken:
#             self.is_broken = not self.is_broken
#             return ______________
#         else:
#             self.is_broken = not self.is_broken
#             return ______________()



# Q8
# class SparseList:
#     """Represent a non-empty list as a most common value and a dictionary from
#     indices to values that contains only values that are not the most common.
#     >>> pi = SparseList([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
#     >>> pi.common
#     5
#     >>> pi.others
#     {0: 3, 1: 1, 2: 4, 3: 1, 5: 9, 6: 2, 7: 6, 9: 3}
#     >>> [pi.item(0), pi.item(1), pi.item(2), pi.item(3), pi.item(4)]
#     [3, 1, 4, 1, 5]
#     >>> pi.item(10)
#     5
#     >>> pi.item(11)
#     'out of range'
#     >>> pi.items()
#     [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#     """
#
#     def __init__(self, s):
#         assert s, 's cannot be empty'
#
#         self.n = len(s)
#         self.common = most_common(_________)
#         self.others = {_________: _________ for i in range(_________) if _________}
#
#     def item(self, i):
#         """Return s[i] or 'out of range' if i is not smaller than the length of s."""
#
#         assert i >= 0, 'index i must be non-negative'
#         if _________:
#             return 'out of range'
#         elif _________:
#             return _________
#         else:
#             return self.common
#
#     def items(self):
#         """Return a list with the same elements as s in the same order as s."""
#
#         return [_________ for i in _________]


def most_common(s):
    """Return the most common element in non-empty list s. In case of a tie,
    return the most common element that appears first in s.
    >>> most_common([3, 1, 4, 1, 5, 9])
    1
    >>> most_common([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    5
    >>> most_common([2, 7, 1, 8, 2, 8, 1, 8, 2, 8])
    8
    >>> most_common([3, 5, 7, 7, 7, 5, 5])
    5
    >>> most_common([3, 7, 5, 5, 7, 7])
    7
    """
    pass



# Q9
# class Version:
#     """A version of a string after an edit.
#     >>> s = Version('No power?', Delete(3, 6))
#     >>> print(Version(s, Insert(3, 'class!')))
#     No class!
#     >>> t = Version('Beary', Insert(4, 'kele'))
#     >>> print(t)
#     Bearkeley
#     >>> print(Version(t, Delete(2, 1)))
#     Berkeley
#     >>> print(Version(t, Delete(4, 5)))
#     Bear
#     """
#     def __init__(self, previous, edit):
#         self.previous, self.edit = previous, edit
#
#
#     def __str__(self):
#         return f'{self.edit.apply(str(self.previous))}'
#
#
# class Edit:
#     def __init__(self, i, c):
#         self.i, self.c = i, c
#
# class Insert(Edit):
#     def apply(self, t):
#         "Return a new string by inserting string c into t starting at position i."
#         return ''.join(list(t)[:self.i]+list(self.c)+list(t)[self.i:])
#
#
# class Delete(Edit):
#     def apply(self, t):
#         "Return a new string by deleting c characters from t starting at position i."
#         return ''.join(list(t)[:self.i]+list(t)[self.i+self.c:])


#
#
# # Q10
# def wins(states, k):
#     """Yield each linked list of two-letter state codes that describes a win by at least k.
#     >>> print_all(wins(battleground, 50))
#     <AZ PA NV GA WI MI>
#     <AZ PA NV GA MI>
#     <AZ PA GA WI MI>
#     <PA NV GA WI MI>
#     >>> print_all(wins(battleground, 75))
#     <AZ PA NV GA WI MI>
#     """
#     if _________:
#         yield Link.empty
#     if states:
#         first = states[0].electors
#         for win in wins(states[1:], _________):
#             yield Link(_________, win)
#         yield from wins(states[1:], _________)
#
#
#
# def must_win(states, k):
#     """List all states that must be won in every scenario that wins by k.
#     >>> must_win(battleground, 50)
#     ['PA', 'GA', 'MI']
#     >>> must_win(battleground, 75)
#     ['AZ', 'PA', 'NV', 'GA', 'WI', 'MI']
#     """
#     def contains(s, x):
#         """Return whether x is a value in linked list s."""
#         return (_________) and (_________)
#     # (a) (b)
#     return [_________ for s in states if _________([_________ for w in wins(states, k)])]
#
#
# class State:
#     electors = {}
#     def __init__(self, code, electors):
#         self.code = code
#         self.electors = electors
#         State.electors[code] = electors
#
# battleground = [State('AZ', 11), State('PA', 20), State('NV', 6),
# State('GA', 16), State('WI', 10), State('MI', 16)]
#
#
# def is_minimal(state_codes, k):
#     """Return whether a non-empty list of state_codes describes a minimal win by
#     at least k.
#     >>> is_minimal(['AZ', 'NV', 'GA', 'WI'], 0) # Every state is necessary
#     True
#     >>> is_minimal(['AZ', 'GA', 'WI'], 0) # Not a win
#     False
#     >>> is_minimal(['AZ', 'NV', 'PA', 'WI'], 0) # NV is not necessary
#     False
#     >>> is_minimal(['AZ', 'PA', 'WI'], 0) # Every state is necessary
#     True
#     """
#     assert state_codes, 'state_codes must not be empty'
#     votes_in_favor = _________
#     total_possible_votes = sum(_________)
#     def win_margin(n):
#         "Margin of victory if n votes are in favor and the rest are against."
#         return n - (total_possible_votes - n)
#     if win_margin(sum(votes_in_favor)) < k:
#         return False # Not a win
#     in_favor_no_smallest = _________
#     return win_margin(in_favor_no_smallest) < k
#
#
#
# # Q11
def replace(s, t, i, j):
    """Replace the slice of s from i to j with t.
    >>> s, t = Link(3, Link(4, Link(5, Link(6, Link(7))))), Link(0, Link(1, Link(2)))
    >>> replace(s, t, 2, 4)
    >>> print(s)
    <3, 4, 0, 1, 2, 7>
    >>> t.rest.first = 8
    >>> print(s)
    <3, 4, 0, 8, 2, 7>
    """
    assert s is not Link.empty and t is not Link.empty and i > 0 and i < j
    if i > 1:
        replace(s.rest, t, i - 1, j - 1)
    else:
        for k in range(j - i):
            s.rest = s.rest.rest
        end = t
        while end.rest != Link.empty:
            end = end.rest
        s.rest, end.rest = t, s.rest

#
# Q12
# def link_insert(lnklst, value, before):
#     """Return a linked list identical to LNKLST, but with VALUE inserted just
#     before the first occurrence of BEFORE in the list, if any. The returned
#     list is identical to LNKLST if BEFORE does not occur in LNKLST.
#     The operation is non-destructive.
#     >>> L = link(2, link(3, link(7, link(1))))
#     >>> print_link(L)
#     (2, 3, 7, 1)
#     >>> Q = link_insert(L, 19, 7)
#     >>> print_link(Q)
#     (2, 3, 19, 7, 1)
#     >>> print_link(link_insert(L, 19, 20))
#     (2, 3, 7, 1)
#     """
#     if lnklst == Link.empty:
#         return lnklst
#     elif lnklst.first == before:
#         return Link(value, lnklst)
#     else:
#         return Link(lnklst.first, link_insert(lnklst.rest, value, before))


# Link ADT
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


if __name__ == "__main__":
    # s = Version('No power?', Delete(3, 6))
    # print(Version(s, Insert(3, 'class!')))
    # t = Version('Beary', Insert(4, 'kele'))
    # print(t)
    # print(Version(t, Delete(2, 1)))
    # print(Version(t, Delete(4, 5)))
    # L = Link(2, Link(3, Link(7, Link(1))))
    # print(L)
    # Q = link_insert(L, 19, 7)
    # print(Q)
    # print(link_insert(L, 19, 20))

    s, t = Link(3, Link(4, Link(5, Link(6, Link(7))))), Link(0, Link(1, Link(2)))
    replace(s, t, 2, 4)
    print(s)
    t.rest.first = 8
    print(s)

