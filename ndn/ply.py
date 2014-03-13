from __future__ import absolute_import

import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
)

def t_NUMBER(token):
    r'[0-9]+'
    token.value = float(token.value)
    return token

lexer = lex.lex()

def p_number(p):
    'number : NUMBER'
    p[0] = p[1]

parser = yacc.yacc()

def calculate(text):
    return parser.parse(text)
