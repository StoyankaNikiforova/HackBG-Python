import unittest
from user_interface.interface import show_available_spots


class interfaceTest(unittest.TestCase):
    def test_show_available_spots(self):
        self.assertEqual(show_available_spots('1'), "ciudjcliidkc")


if __name__ == '__main__':
    unittest.main()
