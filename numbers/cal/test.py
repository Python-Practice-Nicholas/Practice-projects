from unittest import TestCase
from numbers.cal.Calculator import Calculator


class CalculatorTestCases(TestCase):

    def test_find_para(self):
        c = Calculator()
        lst1 = c.find_para("(1+1)")
        lst2 = c.find_para("(1-1)")
        lst3 = c.find_para("(1*1)")
        lst4 = c.find_para("(1/1)")
        no_lst = c.find_para("1+1")

        self.assertEqual(lst1, ["add", 1, 1])
        self.assertEqual(lst2, ["subtract", 1, 1])
        self.assertEqual(lst3, ["multiply", 1, 1])
        self.assertEqual(lst4, ["divide", 1, 1])
        self.assertEqual(no_lst, ["add", 1, 1])

    def test_check_operator(self):
        c = Calculator()
        lst1 = c.check_operator("1+1")
        lst2 = c.check_operator("1-1")
        lst3 = c.check_operator("1*1")
        lst4 = c.check_operator("1/1")

        self.assertEqual(lst1, ["add", 1, 1])
        self.assertEqual(lst2, ["subtract", 1, 1])
        self.assertEqual(lst3, ["multiply", 1, 1])
        self.assertEqual(lst4, ["divide", 1, 1])

    def test_select_operation(self):
        c = Calculator()
        sum = c.select_operation(["add", 1, 1])

        self.assertEqual(sum, 2)
