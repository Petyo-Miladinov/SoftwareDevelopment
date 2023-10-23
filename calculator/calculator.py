class Calculator:
    def __init__(self): 
        self.current_value = 0
        
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        # assert y != 0, "Cannot divide by zero" 
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y
    
    def operate_from_input():
        operation = input("Enter operation in format 'number operator number': ")
        elements = operation.split()
        if len(elements) != 3:
            raise ValueError("Invalid format. Please provide 'number operator number'.")
        x, operator, y = elements
        x, y = float(x), float(y)

        calc = Calculator()
        if operator == '+':
            print(calc.add(x, y))
        elif operator == '-':
            print(calc.subtract(x, y))
        elif operator == '*':
            print(calc.multiply(x, y))
        elif operator == '/':
            print(calc.divide(x, y))
        else:
            raise ValueError("Invalid operator. Please use +, -, * or /.")
        
Calculator.operate_from_input()