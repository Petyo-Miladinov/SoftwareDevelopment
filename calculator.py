class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        assert y != 0, "Cannot divide by zero" 
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y