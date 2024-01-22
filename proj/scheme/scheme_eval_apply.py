import sys

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Here we see expr is the result of scheme_read parsing process,
    # which return the data structure (Pair) for the expression to be evaluated.

    # 1. Evaluate atoms，evaluate the operator
    # Look up the name of the variables, it contains the builtin procedures
    if scheme_symbolp(expr):
        return env.lookup(expr)
    # Evaluate the self-evaluating expression
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    # 如果expr以 ' (quote)开头，比如 '(1 2 3), 就是一个Pair(1, Pair(2, Pair(3, nil0)))
    # ' 也是special form的一种
    # 如果是special forms
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3
        "*** YOUR CODE HERE ***"
        # If first is basic operation like +/-
        # 1. Evaluate/validate the operator -> Procedure instance
        operator = scheme_eval(first, env)
        validate_procedure(operator)
        # 2. Evaluate the operands
        operands = rest.map(lambda x: scheme_eval(x, env))
        # 3. Apply the procedure by calling scheme_apply
        return scheme_apply(operator, operands, env)
        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    # 检查传入的procedure是否具有`ISA Procedure`的性质，不是则报错
    validate_procedure(procedure)
    if not isinstance(env, Frame):
       assert False, "Not a Frame: {}".format(env)
    # 判断传入的procedure call是什么类型
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        # 1. Convert the args(Pair), which is a scheme list(recursive linked list)
        # into the python list(flattening process)
        arg_list = []
        p = args
        while p != nil:
            arg_list.append(p.first)
            p = p.rest
        # 2. If procedure.need_env is True, then append the env argument to the arg_list
        if procedure.need_env:
            arg_list.append(env)
        # END PROBLEM 2
        try:
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            return procedure.py_func(*arg_list)
            # END PROBLEM 2
        except TypeError as err:
            raise SchemeError('incorrect number of arguments: {0}'.format(procedure))
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        "*** YOUR CODE HERE ***"
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        "*** YOUR CODE HERE ***"
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    if expressions == nil:
        return None
    p = expressions
    while p.rest != nil:
        scheme_eval(p.first, env)
        p = p.rest
    return scheme_eval(p.first, env)
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env


def complete_apply(procedure, args, env):
    """Apply procedure to args in env; ensure the result is not an Unevaluated."""
    validate_procedure(procedure)
    val = scheme_apply(procedure, args, env)
    if isinstance(val, Unevaluated):
        return scheme_eval(val.expr, val.env)
    else:
        return val


def optimize_tail_calls(unoptimized_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr, env)

        result = Unevaluated(expr, env)
        # BEGIN PROBLEM EC
        "*** YOUR CODE HERE ***"
        # END PROBLEM EC
    return optimized_eval


################################################################
# Uncomment the following line to apply tail call optimization #
################################################################

# scheme_eval = optimize_tail_calls(scheme_eval)
