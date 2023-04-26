from rearrenge import rearrenge_name
import unittest

class TestRearrenge(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEquals(rearrenge_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEquals(rearrenge_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEquals(rearrenge_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEquals(rearrenge_name(testcase), expected)
    
unittest.main()
