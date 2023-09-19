from unittest import TestCase
from numbers.cal.Calculator import Calculator as c


class CalculatorTestCases(TestCase):

    def test_check_operator(self):
        lst1 = c.check_operator("1+1")
        lst2 = c.check_operator("1-1")
        lst3 = c.check_operator("1*1")
        lst4 = c.check_operator("1/1")

        self.assertEqual(lst1, ["add", 1, 1])
        self.assertEqual(lst2, ["subtract", 1, 1])
        self.assertEqual(lst3, ["multiply", 1, 1])
        self.assertEqual(lst4, ["divide", 1, 1])
