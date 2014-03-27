from unittest import TestCase
from nose.tools import eq_, raises
from mock import patch

from ndn.ply import calculate
from ndn.ply import ParseError

from ply.lex import LexError

class TestPlyParse(TestCase):
    def test_parse_a_single_number(self):
        eq_(1, calculate('1'))

    def test_parse_a_decimal_number(self):
        eq_(3.141, calculate('3.141'))

    @raises(LexError)
    def test_numbers_can_have_at_most_one_decimal_point(self):
        calculate('2.7.2')

    def test_parse_a_negative_number(self):
        eq_(-1, calculate('-1'))

    def test_perform_operations_on_a_negative_number(self):
        eq_(-5, calculate('10/-2'))

    def test_add_two_numbers(self):
        eq_(7, calculate('5+2'))

    def test_add_several_numbers(self):
        eq_(32, calculate('8+14+3+7'))

    def test_multiply_two_numbers(self):
        eq_(48, calculate('6*8'))

    def test_divide_two_numbers(self):
        eq_(2.5, calculate('5/2'))

    def test_subtract_two_numbers(self):
        eq_(8, calculate('13-5'))

    def test_operators_are_right_associative(self):
        eq_((23 - (10 - 5)), calculate('23-10-5'))
        eq_((24 / (16 / 2)), calculate('24/16/2'))
        eq_((8 + (5 * 3)), calculate('8+5*3'))

    @patch('ndn.ply.randint')
    def test_roll_the_dice(self, mock_randint):
        mock_randint.return_value = 5
        eq_(10, calculate('2d6'))

    def test_a_parenthesized_number(self):
        eq_(1, calculate('(1)'))

    def test_a_parenthesized_expression(self):
        eq_(13, calculate('(5+8)'))

    def test_operate_on_a_parenthetical(self):
        eq_(13, calculate('(5*3)-2'))

    @raises(ParseError)
    def test_parenthetcals_must_be_closed(self):
        eq_('yeppo!', calculate('(5*3-2'))

