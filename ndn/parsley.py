from __future__ import absolute_import

from parsley import makeGrammar
from random import randint

def roll(num, size):
    return sum(map(lambda x: randint(size), range(0, int(num))))

grammar = makeGrammar("""
    expression    = operation | element
    operation     = ws element:a ws operator:op ws expression:b ws -> op(a, b)
    element       = parenthetical | number
    parenthetical = '(' ws expression:e ws ')' -> e
    number        = <'-'? digit+ ('.' digit+)?>:ds -> float(ds)
    operator      = ( '+' -> lambda a, b: a + b
                    | '-' -> lambda a, b: a - b
                    | '*' -> lambda a, b: a * b
                    | '/' -> lambda a, b: a / b
                    | 'd' -> roll)
    ws            = (' ' | '\t')*
""", {'roll': roll})

def calculate(text):
    return grammar(text).expression()
