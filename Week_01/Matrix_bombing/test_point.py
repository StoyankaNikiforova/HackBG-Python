import unittest
from point import Point
from matrix import Matrix


class testPoint(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(0, 2, 40)
        self.point2 = Point(1, 1, 35)
        self.m = Matrix(3, 3)

    # def test_adding_element(self):
    #     self.assertEqual(self.point1 + self.point2, 75)
    #
    # def test_reduce_element(self):
        # self.assertEqual(self.point1 - self.point2, 5)

    # def test_null_neighbours(self):
    #     self.assertEqual(self.point1.get_null_neighb(), [(-1, -1, 0),
    #                                                      (-1, 0, 0),
    #                                                      (-1, 1, 0),
    #                                                      (0, -1, 0),
    #                                                      (0, 1, 0),
    #                                                      (1, -1, 0),
    #                                                      (1, 0, 0),
    #                                                      (1, 1, 0)])

    def test_neighbours(self):
        self.assertEqual(self.point1.neighbours(self.m), [(-1, -1, 0),
                                                              (-1, 0, 0),
                                                              (-1, 1, 0),
                                                              (0, -1, 0),
                                                              (0, 1, 0),
                                                              (1, -1, 0),
                                                              (1, 0, 0),
                                                              (1, 1, 0)])


if __name__ == '__main__':
    unittest.main()
