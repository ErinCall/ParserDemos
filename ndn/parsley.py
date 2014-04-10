from __future__ import absolute_import

from parsley import makeGrammar

grammar = makeGrammar("""
    expression = addition | number
    addition   = number:a plus:op number:b -> op(a, b)
    number     = <'-'? digit+ ('.' digit+)?>:ds -> float(ds)
    plus       = '+' -> lambda a, b: a + b
""", {})

def calculate(text):
    return grammar(text).expression()
