from __future__ import absolute_import

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

grammar = Grammar("""
    number = "-"? ~"[0-9]+" ("." ~"[0-9]+")?
""")

class Calculator(NodeVisitor):
    def generic_visit(self, node, visited_children):
        pass

    def visit_number(self, node, visited_children):
        return float(node.text)

def calculate(text):
    return Calculator().visit(grammar.parse(text))
