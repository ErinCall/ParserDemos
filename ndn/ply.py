from __future__ import absolute_import

import ply.lex as lex
import ply.yacc as yacc

class SilentLogger(object):
    def warning(*args, **kwargs):
        pass

tokens = (
    'PLUS',
    'NUMBER',
)

def t_PLUS(token):
    r'\+'
    token.value = lambda a, b: a + b
    return token

def t_NUMBER(token):
    r'(-?)[0-9]+(\.[0-9]+)?'
    token.value = float(token.value)
    return token

lexer = lex.lex(errorlog=SilentLogger())

def p_expression_operator(p):
    'expression : expression PLUS expression'
    p[0] = p[2](p[1], p[3])

def p_number(p):
    'expression : NUMBER'

    p[0] = p[1]

parser = yacc.yacc()

def calculate(text):
    return parser.parse(text)
