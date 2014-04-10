from unittest import TestCase
from nose.tools import eq_, raises
from parsley import ParseError
from mock import patch

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
        eq_(35.2, calculate('5.2 + 30'))

    def test_add_several_numbers(self):
        eq_(56, calculate('18 + 2 + 40 + -4'))

    def test_multiply_two_numbers(self):
        eq_(48, calculate('6 * 8'))

    def test_divide_two_numbers(self):
        eq_(2.5, calculate('5 / 2'))

    def test_subtract_two_numbers(self):
        eq_(8, calculate('13 - 5'))

    @patch('ndn.parsley.randint')
    def test_roll_the_dice(self, mock_randint):
        mock_randint.return_value = 4
        eq_(8, calculate('2 d 6'))

    def test_operators_are_right_associative(self):
        eq_((23 - (10 - 5)), calculate('23 - 10 - 5'))
        eq_((24 / (16 / 2)), calculate('24 / 16 / 2'))
        eq_((8 + (5 * 3)), calculate('8 + 5 * 3'))

    def test_a_single_number_in_parens(self):
        eq_(5, calculate('(5)'))

    def test_use_parens_to_override_associativity(self):
        eq_(32, calculate('( 5 + 3 ) * ( 8 - 4 )'))

    def test_a_lot_of_whitespace(self):
        eq_(4, calculate('    8   /     2   '))
