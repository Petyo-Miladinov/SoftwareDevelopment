# tests/test_calculator.py
from calculator import Calculator
import unittest 

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(4, 6)
        self.assertEqual(result, 24)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError) as context:
            calc.divide(5, 0)
        
        self.assertEqual(str(context.exception), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
