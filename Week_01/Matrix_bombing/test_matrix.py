import unittest
from matrix import Matrix


class testMatrix(unittest.TestCase):
    def setUp(self):
        self.matrix = Matrix(3, 3)

    def test_fulling(self):
        self.assertEqual(self.matrix.full_matrix(), [[1,2,3], [4,5,6], [7,8,9]])

if __name__ == '__main__':
    unittest.main()
