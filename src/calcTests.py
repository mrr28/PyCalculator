import unittest
from calculator import Calculator

class MyTestCase(unittest.TestCase):
    def test_calcc(self):
        calculator=Calculator()
        self.assertEqual(calculator, Calculator)


if __name__ == '__main__':
    unittest.main()
