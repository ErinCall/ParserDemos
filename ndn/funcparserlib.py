from __future__ import absolute_import

import funcparserlib.parser as p

string = lambda x: x or ''
cat = ''.join

negative = p.maybe(p.a('-')) >> string
digits = p.oneplus(p.some(lambda char: char.isdigit())) >> cat
decimal_part = (p.maybe(p.a('.') + digits)) >> string >> cat
number = (negative + digits + decimal_part) >> cat >> float

addition = number + p.skip(p.a('+')) + number >> sum

expression = addition | number
expression = expression + p.finished

def calculate(text):
    return expression.parse(text)[0]
