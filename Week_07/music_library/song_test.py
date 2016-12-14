import unittest
from song_class import Song


class testSong(unittest.TestCase):
    def setUp(self):
        self.s = Song('fj', 'xhch', 'drdy', '4:09')

    def test_lenght(self):
        print(self.s.lenght(seconds=True))


if __name__ == '__main__':
    unittest.main()
