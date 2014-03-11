from __future__ import absolute_import

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

grammar = Grammar("""
    expression = addition / number
    addition   = number plus expression
    plus       = "+"
    number     = "-"? ~"[0-9]+" ("." ~"[0-9]+")?
""")

class Calculator(NodeVisitor):
    def generic_visit(self, node, visited_children):
        pass

    def visit_expression(self, node, visited_children):
        return visited_children[0]

    def visit_addition(self, node, visited_children):
        #visited_children is [number, plus, number]
        return visited_children[1](visited_children[0], visited_children[2])

    def visit_plus(self, node, visited_children):
        return lambda x, y: x + y

    def visit_number(self, node, visited_children):
        return float(node.text)

def calculate(text):
    return Calculator().visit(grammar.parse(text))
