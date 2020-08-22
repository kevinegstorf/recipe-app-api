from django.test import TestCase
from app.calc import add, subtract 

class CalcTests(TestCase):
    def test_add_numbers(self):
        # TEST THAT TWO NUMBERS ARE ADDED TOGETHER
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        # VALUES ARE SUBTRACTED AND RETURNED
        self.assertEqual(subtract(5, 11), 6)
