from __future__ import absolute_import

from parsley import makeGrammar

grammar = makeGrammar("""
    number = <'-'? digit+ ('.' digit+)?>:ds -> float(ds)
""", {})

def calculate(text):
    return grammar(text).number()
