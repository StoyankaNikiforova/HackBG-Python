import unittest
from panda_class import Panda


class testPanda(unittest.TestCase):
    def setUp(self):
        self.p = Panda('Toshko')

    def test_to_json(self):
        self.assertEqual(self.p.to_json(), "{}")

    def test_to_xml(self):
        self.assertEqual(self.p.to_xml(), "<>")

    def test_from_xml(self):
        self.assertEqual(self.p.from_xml(self.p.to_xml), "")    


if __name__ == '__main__':
    unittest.main()
