from __future__ import absolute_import

import ply.lex as lex
import ply.yacc as yacc
from random import randint

class SilentLogger(object):
    def warning(*args, **kwargs):
        pass

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'ROLL',
    'OPAREN',
    'CPAREN',
)

def t_PLUS(token):
    r'\+'
    token.value = lambda a, b: a + b
    return token

def t_MINUS(token):
    r'-'
    token.value = lambda a, b: a - b
    return token

def t_MULTIPLY(token):
    r'\*'
    token.value = lambda a, b: a * b
    return token

def t_DIVIDE(token):
    r'/'
    token.value = lambda a, b: a / b
    return token

def t_ROLL(token):
    r'd'
    def roll(num, size):
        return sum(map(lambda x: randint(size), range(0, int(num))))
    token.value = roll
    return token

def t_NUMBER(token):
    r'[0-9]+(\.[0-9]+)?'
    token.value = float(token.value)
    return token

t_OPAREN = r'\('
t_CPAREN = r'\)'

lexer = lex.lex(errorlog=SilentLogger())

def p_expression_operator(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression ROLL expression'''
    p[0] = p[2](p[1], p[3])

def p_unary_minus(p):
    'expression : MINUS expression'
    p[0] = p[1](0, p[2])

def p_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_parenthetical(p):
    'expression : OPAREN expression CPAREN'
    p[0] = p[2]

parser = yacc.yacc()

def calculate(text):
    return parser.parse(text, debug=ErrorRaiser())

class ErrorRaiser(object):
    def error(self, error, message, *args, **kwargs):
        raise ParseError(error % message)

    def black_hole(*args, **kwargs):
        pass

    def __getattr__(self, *args, **kwargs):
        return self.black_hole

class ParseError(StandardError):
    pass
