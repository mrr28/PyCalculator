def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a // b

def square(a, b):
    return a ** b

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        self.result = a // b
        return self.result

    def square(self, a, b):
        self.result = a ** b
        return self.result