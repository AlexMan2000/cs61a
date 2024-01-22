# # Non-empty subsets of integer list that have an even sum
# def even_subsets(lst):
#     if len(lst) == 0:
#         return []
#
#     res = even_subsets(lst[1:])
#     if lst[0] % 2 == 1:
#         res.extend(list(map(lambda x: [lst[0]] + x, odd_subsets(lst[1:]) )))
#     else:
#         res.extend(list(map(lambda x:  [lst[0]] + x, even_subsets(lst[1:]))))
#         res.append([lst[0]])
#     return res[:]
#
#
#
# # Non-empty subsets og integer list that have an odd sum
# def odd_subsets(lst):
#     if len(lst) == 0:
#         return []
#
#     res = odd_subsets(lst[1:])
#     if lst[0] % 2 == 1:
#         res.extend(list(map(lambda x: [lst[0]] + x, even_subsets(lst[1:]))))
#         res.append([lst[0]])
#     else:
#         res.extend(list(map(lambda x:  [lst[0]] + x, odd_subsets(lst[1:]))))
#
#     return res[:]



# Higher-Order Function
# Non-empty subsets of integer list that have an even sum
def even_subsets(lst):
    if len(lst) == 0:
        return []

    res = even_subsets(lst[1:])
    helper = subset_helper(lambda x: x % 2 == 0, lst)
    res = helper + res

    return res[:]

# Non-empty subsets og integer list that have an odd sum
def odd_subsets(lst):
    if len(lst) == 0:
        return []

    res = odd_subsets(lst[1:])
    helper = subset_helper(lambda x: x % 2 == 1, lst)
    res = helper + res

    return res[:]


def subset_helper(f, lst):
    res = []
    if f(lst[0]):
        res.extend(list(map(lambda x: [lst[0]] + x, even_subsets(lst[1:]))))
    else:
        res.extend(list(map(lambda x:  [lst[0]] + x, odd_subsets(lst[1:]))))
    if f(lst[0]):
        res.append([lst[0]])

    return res[:]


# Alternate Version - First figure out all the subset, then filter out the even ones
def non_empty_subset(lst):
    if len(lst) == 0:
        return []

    res = non_empty_subset(lst[1:])
    res.extend((list(map(lambda x: [lst[0]] + x, non_empty_subset(lst[1:])))))
    res.append([lst[0]])

    return res[:]



def filter_even_sum(lst):
    return list(filter(lambda x: sum(x) % 2 == 0, lst))



if __name__ == "__main__":
    s = [3,4,5,7]
    print(filter_even_sum(non_empty_subset(s)))