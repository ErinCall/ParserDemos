from unittest import TestCase
from nose.tools import eq_

from ndn.parsley import calculate

class TestParsleyParse(TestCase):
    def test_parse_a_single_number(self):
        eq_(1, calculate('1'))
