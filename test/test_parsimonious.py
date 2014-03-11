from unittest import TestCase
from parsimonious.exceptions import IncompleteParseError
from nose.tools import eq_, raises

from ndn.parsimonious import calculate

class TestParse(TestCase):
    def test_parse_a_single_number(self):
        eq_(1, calculate('1'))

    def test_parse_a_decimal_number(self):
        eq_(3.141, calculate('3.141'))

    @raises(IncompleteParseError)
    def test_numbers_can_have_at_most_one_decimal_point(self):
        calculate('2.7.2')
