from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Tests that two numbers are added correctly """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ tests correctly subtract 2 numbers ans return results """
        self.assertEqual(subtract(5, 11), 6)