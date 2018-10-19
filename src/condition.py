from re import match
from operator import lt, le, gt, ge

"""
Convert a tuple of (pair, operator, value) to a lambda given a mapping of
a label to its value.
returns the evaluated lambda
"""
def evalTuple(tuple, mapper):
    actualVal = mapper(tuple[0])
    
    if not (type(actualVal) == float or type(actualVal) == int):
        return None

    operator = tuple[1]
    val = float(tuple[2])

    operators = { '<' : lt(actualVal, val), \
                  '>' : gt(actualVal, val), \
                  '<=' : le(actualVal, val), \
                  '>=' : ge(actualVal, val) }

    return operators[operator]

"""
Parse a string polish notation string expr
returns the evaluated expression
"""
def eval(expression, mapper):
    rem = match(r"([a-zA-Z]+) (<|>|<=|>=) ([0-9]\d*(\.\d+)?)", expression)
    if rem is not None:
        groups = rem.groups()
        return evalTuple(groups, mapper)
    return None
