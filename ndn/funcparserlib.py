from __future__ import absolute_import

import funcparserlib.parser as p

cat = lambda x: ''.join(x or '')
digits = p.oneplus(p.some(lambda char: char.isdigit())) >> cat
decimal_part = (p.maybe(p.a('.') + digits)) >> cat
number = (digits + decimal_part) >> cat >> float
number = number + p.finished

def calculate(text):
    return number.parse(text)[0]
