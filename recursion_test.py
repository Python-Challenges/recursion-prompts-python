import unittest
from unittest.mock import call, Mock, patch
from recursion import *


class FactorialTest(unittest.TestCase):
    def test_output_int(self):
        self.assertIsInstance(factorial(5), int)

    def test_return_factorial(self):
        self.assertEquals(factorial(0), 1)
        self.assertEquals(factorial(1), 1)
        self.assertEquals(factorial(4), 24)
        self.assertEquals(factorial(5), 120)

    def test_return_None_for_negative(self):
        self.assertIsNone(factorial(-1))

    def test_recurse_by_calling_itself(self):
        for i in range(5, 10):
            with patch('recursion.counter') as mocked_counter:
                factorial(i)
                self.assertGreater(mocked_counter.call_count, 1)


class SumTest(unittest.TestCase):
    def test_outputs_int(self):
        self.assertIsInstance(sum_([1, 2, 3, 4, 5, 6]), int)

    def test_positive_ints_input(self):
        self.assertEquals(sum_([1, 2, 3, 4, 5, 6]), 21)
        self.assertEquals(sum_([3, 0, 34, 7, 18]), 62)

    def test_negative_ints_input(self):
        self.assertEquals(sum_([-1, -2, -3, -4, -5, -6]), -21)
        self.assertEquals(sum_([-3, -0, -34, -7, -18]), -62)

    def test_any_ints_input(self):
        self.assertEquals(sum_([1, -2, 3, -4, 5, -6]), -3)
        self.assertEquals(sum_([-12, 34, -56, 78]), 44)
        self.assertEquals(sum_([3, 0, -34, -7, 18]), -20)

    def test_empty_input_arr(self):
        self.assertEquals(sum_([]), 0, msg='should return 0 for empty array')

    def test_single_ele_arr(self):
        self.assertEquals(sum_([4]), 4)
        self.assertEquals(sum_([0]), 0)
        self.assertEquals(sum_([-37]), -37)

    def test_no_mutation_on_input(self):
        input_arr_copy = [1, 2, 3, 4, 5]
        input_arr = [1, 2, 3, 4, 5]
        sum_(input_arr)
        self.assertListEqual(input_arr_copy, input_arr)

    def test_calls_itself(self):
        with patch('recursion.counter') as mocked_counter:
            sum_([1, -2, 3, -4, 5, -6])
            self.assertGreater(mocked_counter.call_count, 1)


if __name__ == '__main__':
    # mySuite = unittest.loader.findTestCases(suiteClass=RecursionTest)
    # mySuite.addTests([FactorialTest, FactorialTest2])
    # mySuite.run()
    pass

    unittest.main()
