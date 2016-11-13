import unittest
from solution import is_prime
from solution import simplify_fraction
from solution import sort_fractions


class tastFractions(unittest.TestCase):

    def test_simplify_fraction(self):
        self.assertEqual(simplify_fraction((3, 9)), (1, 3))
        self.assertEqual(simplify_fraction((1, 7)), (1, 7))
        self.assertEqual(simplify_fraction((4, 10)), (2, 5))
        self.assertEqual(simplify_fraction((63, 462)), (3, 22))

    def test_sort_fractions(self):
        # self.assertEqual(sort_fractions([(2, 3), (1, 2)]), [(1, 2), (2, 3)])
        # self.assertEqual(sort_fractions([(2, 3), (1, 2), (1, 3)]), [(1, 3), (1, 2), (2, 3)])
        self.assertEqual(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]), [(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)])


if __name__ == '__main__':
    unittest.main()
