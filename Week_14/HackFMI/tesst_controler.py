import unittest
from model import Mentor
from controler import fill_row


class TestControler(unittest.TestCase):
    def test_fill_row(self):
        # filds = eval('name="Mima", description="bdshcbks", picture="bdscn.jpg"')
        self.assertTrue(fill_row('Mentor', name="Mima", description="bdshcbks", picture="bdscn.jpg"))


if __name__ == '__main__':
    unittest.main()
