from __future__ import absolute_import

from parsley import makeGrammar
from random import randint

def roll(num, size):
    return sum(map(lambda x: randint(size), range(0, int(num))))

grammar = makeGrammar("""
    expression = operation | number
    operation  = number:a operator:op expression:b -> op(a, b)
    number     = <'-'? digit+ ('.' digit+)?>:ds -> float(ds)
    operator   = ( '+' -> lambda a, b: a + b
                 | '-' -> lambda a, b: a - b
                 | '*' -> lambda a, b: a * b
                 | '/' -> lambda a, b: a / b
                 | 'd' -> roll)
""", {'roll': roll})

def calculate(text):
    return grammar(text).expression()
