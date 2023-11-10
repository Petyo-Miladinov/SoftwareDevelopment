import re


class Calculator:
    def __init__(self):
        self.current_value = 0
        self.max_value = 10**10

    def add(self, x, y):
        self.check_max_value(x, y)
        return x + y

    def subtract(self, x, y):
        self.check_max_value(x, y)
        if isinstance(y, (int, float)):
            return x - y
        else:
            if y.startswith('-'):
                y = y[1:]
            return x + float(y)

    def multiply(self, x, y):
        self.check_max_value(x, y)
        return x * y

    def divide(self, x, y):
        self.check_max_value(x, y)
        # assert y != 0, "Cannot divide by zero" 
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    def modulus(self, x, y):
        return x % y

    def check_max_value(self, x, y):
        if abs(x) > self.max_value or abs(y) > self.max_value:
            raise ValueError("Numbers are too big. Please use smaller numbers.")

    def operate_from_input(self):
        while True:
            try:
                operation = input("Enter operation in format 'number operator number' or type 'exit' to stop: ")
                if operation.strip().lower() == 'exit':
                    break  # Stops the program if 'exit' is entered
                match = re.match(r"(-?\d*\.?\d+)\s*([+\-*/])\s*(-?\d*\.?\d+)", operation)
                if not match:
                    raise ValueError("Invalid format. Please provide 'number operator number'.")
                x, operator, y = match.groups()
                x, y = float(x), float(y)
                # elements = operation.split()
                # if len(elements) != 3:
                #     raise ValueError("Invalid format. Please provide 'number operator number'.")
                # x, operator, y = elements
                # x, y = float(x), float(y)

                calc = Calculator()
                if operator == '+':
                    print(calc.add(x, y))
                elif operator == '-':
                    print(calc.subtract(x, y))
                elif operator == '*':
                    print(calc.multiply(x, y))
                elif operator == '/':
                    print(calc.divide(x, y))
                elif operator == '%':
                    print(calc.modulus(x, y))
                else:
                    raise ValueError("Invalid operator. Please use +, -, * or /.")

            except ValueError as e:
                print(e)


Calculator.operate_from_input(self="")
