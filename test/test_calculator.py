# tests/test_calculator.py
from unittest import mock
# from calculator.calculator import Calculator
import unittest
# from calculator.calculator import Calculator
import sys
import os
import pytest


# Insert the path to the directory containing the calculator module
sys.path.insert(0, os.path.abspath
                (os.path.join(os.path.dirname(__file__), "..")))

from calculator.calculator import Calculator


class TestCalculator(unittest.TestCase):
    # @pytest.mark.benchmark(group="addition")
    # def test_add_benchmark(self, benchmark):
    #     calc = Calculator()
    #     result = benchmark(calc.add, 5, 3)
    #     print(result)
    #     assert result == 8

    def test_add(self):
        calc = Calculator()
        result = calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative(self):
        calc = Calculator()
        result = calc.add(-5, 3)
        self.assertEqual(result, -2)

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_subtract_negative(self):
        calc = Calculator()
        result = calc.subtract(-5, 3)
        self.assertEqual(result, -8)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 6)
        self.assertEqual(result, 24)

    def test_multiply_negative(self):
        calc = Calculator()
        result = calc.multiply(-5, 3)
        self.assertEqual(result, -15)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError) as context:
            calc.divide(5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_operate_from_input(self):
        input_values = ["5 + 3", "5 - 3", "5 * 3", "5 / 3", "exit"]
        with mock.patch("builtins.input", side_effect=input_values):
            with mock.patch("builtins.print") as mock_print:
                Calculator.operate_from_input(input_values)
                mock_print.assert_has_calls(
                    [mock.call(8.0), mock.call(2.0), mock.call(15.0), mock.call(1.6666666666666667)]
                )

    # def test_operate_from_input(self): 
    #     with mock.patch("builtins.input", return_value="5 + 3"):
    #         with mock.patch("builtins.print") as mock_print:
    #             Calculator.operate_from_input()
    #             mock_print.assert_called_with(8.0)
    #     with mock.patch("builtins.input", return_value="5 - 3"):
    #         with mock.patch("builtins.print") as mock_print:
    #             Calculator.operate_from_input()
    #             mock_print.assert_called_with(2.0) 
    #     with mock.patch("builtins.input", return_value="5 * 3"):
    #         with mock.patch("builtins.print") as mock_print:
    #             Calculator.operate_from_input()
    #             mock_print.assert_called_with(15.0)
    #     with mock.patch("builtins.input", return_value="5 / 3"):
    #         with mock.patch("builtins.print") as mock_print:
    #             Calculator.operate_from_input()
    #             mock_print.assert_called_with(1.6666666666666667)
    #     # with mock.patch("builtins.input", return_value="5 & 3"):
    #     #     with mock.patch("builtins.print") as mock_print:
    #     #         with self.assertRaises(ValueError) as context:
    #     #             Calculator.operate_from_input()
    #     #         self.assertEqual(str(context.exception),
    #     # "Invalid operator. Please use +, -, * or /.")


if __name__ == '__main__':
    unittest.main()
