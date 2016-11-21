import unittest
from binary_search import bin_search
from binary_search import find_turning_point


class testBinary_search(unittest.TestCase):

    def test_binary_search(self):
        self.assertEquals(bin_search([1, 2, 3, 4, 5], 0, 4, 3), 2)

    def test_find_turning_point_1(self):
        self.assertEqual(find_turning_point([1, 2, 3, 4, 7, 6, 5, 0], 0, 7), 5)

    def test_find_turning_point_3(self):
        self.assertEqual(find_turning_point([1, 3, 7, 9, 4, 2], 0, 5), 4)

    def test_find_turning_point_4(self):
        self.assertEqual(find_turning_point([1, 4, 5, 6, 2], 0, 4), 4)

    def test_find_turning_point_4(self):
        self.assertEqual(find_turning_point([7, 4, 5, 6, 8], 0, 4), 1)



if __name__ == '__main__':
    unittest.main()
