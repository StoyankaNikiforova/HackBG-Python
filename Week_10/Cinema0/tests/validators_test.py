import unittest
from user_interface.validators import *


class TestValidators(unittest.TestCase):
    def validate_password(self):
        self.assertEqual(validate_password('anija#4@67'), None)

    def test_encrypt(self):
        self.assertEqual(encrypt("ncdhue5S&%"), '/nd/&%cA%/jjj')


if __name__ == '__main__':
    unittest.main()
