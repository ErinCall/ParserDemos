from __future__ import absolute_import

import funcparserlib.parser as p

digits = p.oneplus(p.some(lambda char: char.isdigit()))
number = digits >> (lambda ds: int(''.join(ds)))

def calculate(text):
    return number.parse(text)
