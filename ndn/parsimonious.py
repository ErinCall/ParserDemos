from __future__ import absolute_import

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

grammar = Grammar("""
    expression = operation / number
    operation  = number operator expression
    operator   = ~"[+\-/*]"
    number     = "-"? ~"[0-9]+" ("." ~"[0-9]+")?
""")

class Calculator(NodeVisitor):
    def generic_visit(self, node, visited_children):
        pass

    def visit_expression(self, node, visited_children):
        return visited_children[0]

    def visit_operation(self, node, visited_children):
        #visited_children is [number, operator, number]
        return visited_children[1](visited_children[0], visited_children[2])

    def visit_operator(self, node, visited_children):
        return {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }[node.text]

    def visit_number(self, node, visited_children):
        return float(node.text)

def calculate(text):
    return Calculator().visit(grammar.parse(text))
