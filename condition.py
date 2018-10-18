from re import match
from operator import lt, le, gt, ge

"""
Convert a tuple of (pair, operator, value) to a lambda given a mapping of
a label to its value.
return a lambda
"""
def evalTupleCond(tuple, mapper):
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
return a lambda condition
"""
def evalCondExpression(expression, mapper):
    rem = match(r"([a-zA-Z]+) (<|>|<=|>=) ([1-9]\d*(\.\d+)?)", expression)
    if rem is not None:
        groups = rem.groups()
        return evalTupleCond(groups, mapper)
    return None
   
   
print(evalCondExpression("A < 6000.0", lambda x : 3000.0))
    
# { condition: "A < 6000.0", destination: "bla@gmail.com" }