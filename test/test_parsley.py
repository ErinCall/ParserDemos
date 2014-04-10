from unittest import TestCase
from nose.tools import eq_, raises
from parsley import ParseError

from ndn.parsley import calculate

class TestParsleyParse(TestCase):
    def test_parse_a_single_number(self):
        eq_(1, calculate('1'))

    def test_parse_a_decimal_number(self):
        eq_(3.141, calculate('3.141'))

    @raises(ParseError)
    def test_numbers_can_have_at_most_one_decimal_point(self):
        calculate('2.7.2')

    def test_parse_a_negative_number(self):
        eq_(-1, calculate('-1'))

    def test_add_two_numbers(self):
        eq_(35.2, calculate('5.2+30'))
