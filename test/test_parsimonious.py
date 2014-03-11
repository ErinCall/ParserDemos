from unittest import TestCase
from nose.tools import eq_

from ndn.parsimonious import calculate

class TestParse(TestCase):
    def test_parse_a_single_number(self):
        eq_(1, calculate('1'))
