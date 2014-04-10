from __future__ import absolute_import

from parsley import makeGrammar

grammar = makeGrammar("""
    number = <digit+>:ds -> int(ds)
""", {})

def calculate(text):
    return grammar(text).number()
