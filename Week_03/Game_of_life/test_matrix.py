import unittest
from matrix import Matrix


class testMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(7, 7, [(1, 2), (0, 3), (5, 6)])

    def test_empty(self):
        self.assertEqual(self.matrix.fild, [['□', '□', '□', '□', '□', '□', '□'], ['□', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', '□', '□']])

    def test_set_living(self):
        self.matrix.set_living()
        self.assertEqual(self.matrix.fild,
            [['□', '□', '□', '■', '□', '□', '□'], ['□', '□', '■', '□', '□', '□', '□'],
        ['□', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '□'],
            ['□', '□', '□', '□', '□', '□', '■'],
            ['□', '□', '□', '□', '□', '□', '□']])

    def test_print_matrix(self):
        self.matrix.set_living()
        self.assertEqual(self.matrix.print_matrix(),
            ['□ □ □ ■ □ □ □', '□ □ ■ □ □ □ □', '□ □ □ □ □ □ □', '□ □ □ □ □ □ □',
                '□ □ □ □ □ □ □', '□ □ □ □ □ □ ■', '□ □ □ □ □ □ □'])


if __name__ == '__main__':
    unittest.main()
