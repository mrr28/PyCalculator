import math

from csvreader import CsvReader

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

class CSVnums(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        for row in data:
            x = row[0]
            y = row[1]
        pass

    def add(self, x, y):
        return addition(x, y)

    def subtract(self, x, y):
        return subtraction(x, y)

    def multiply(self, x, y):
        return multiply(x, y)

    def divide(self, x, y):
        return divide(x, y)

    def square(self, x):
        return square(x)

    def squarert(self, x):
        return squarert(x)


