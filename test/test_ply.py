from unittest import TestCase
from nose.tools import eq_

from ndn.ply import calculate

class TestPlyParse(TestCase):
    def test_parse_a_single_number(self):
        eq_(1, calculate('1'))

