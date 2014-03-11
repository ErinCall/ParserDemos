from __future__ import absolute_import

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

grammar = Grammar("""
    number = ~"[0-9]+"
""")

class Calculator(NodeVisitor):
    def visit_number(self, node, visited_children):
        return int(node.text)

def calculate(text):
    return Calculator().visit(grammar.parse(text))
