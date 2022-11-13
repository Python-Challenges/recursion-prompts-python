import unittest
from unittest.mock import call, Mock
from recursion import *


# class RecursionTest(unittest.TestSuite):
#     def test_output_type(self):
#         self.assertIsInstance(factorial(5), int)

#     pass


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

    # def test_recurse_by_calling_itself(self):
    #     factorial_mock = Mock(side_effect=factorial)
    #     factorial_mock(3)

    #     # self.assertGreater(factorial_mock.call_count, 1)
    #     factorial_mock.assert_has_calls([
    #         call(5),
    #         call(4),
    #         call(3),
    #         call(2),
    #         call(1),
    #     ])


if __name__ == '__main__':
    # mySuite = unittest.loader.findTestCases(suiteClass=RecursionTest)
    # mySuite.addTests([FactorialTest, FactorialTest2])
    # mySuite.run()
    pass

    unittest.main()
