from __future__ import absolute_import

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

grammar = Grammar("""
    expression    = operation / element
    operation     = ws element ws operator ws expression ws
    element       = parenthetical / number
    parenthetical = "(" ws expression ws ")"
    ws            = ~"\s"*
    operator      = ~"[+\-/*]"
    number        = "-"? ~"[0-9]+" ("." ~"[0-9]+")?
""")

class Calculator(NodeVisitor):
    def generic_visit(self, node, visited_children):
        pass

    def visit_expression(self, node, visited_children):
        return visited_children[0]

    def visit_operation(self, node, visited_children):
        #visited_children is [ws, number, ws, operator, ws, number, ws]
        return visited_children[3](visited_children[1], visited_children[5])

    def visit_element(self, node, visited_children):
        return visited_children[0]

    def visit_parenthetical(self, node, visited_children):
        #visited_children is ['(', whitespace, some_expression, whitespace, ')']
        return visited_children[2]

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
