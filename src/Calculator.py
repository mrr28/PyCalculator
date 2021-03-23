import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a // b

def square(a):
    return a ** 2

def squarert(a):
    return math.sqrt(a)

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

    def square(self, a):
        self.result = a ** 2
        return self.result

    def squarert(self, a):
        self.result = math.sqrt(a)
        return self.result