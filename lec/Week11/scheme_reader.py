class Pair:
    """
    A pair has two instance attributes: first and rest. rest is a Pair or nil
    Like a linked list structure
    """



class nil:
    """The empty list"""



def cal_apply(operator, args):
    """Apply the named operator to a list of args"""
    from functools import reduce
    from operator import add, sub,  mul, truediv

    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' is not a symbol')
    if operator == "+":
        return reduce(add, args, 0)
    elif operator == "-":
        if len(args) == 0:
            raise TypeError(operator + ' requires at least 1 argument')
        elif len(args) == 1:
            return -args.first
        else:
            return reduce(sub, args.second, args.first)