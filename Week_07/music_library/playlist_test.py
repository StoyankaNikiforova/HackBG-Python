import unittest
import json
from song_class import Song
from playlist_class import Playlist


class playlistTest(unittest.TestCase):
    def setUp(self):
        self.pl = Playlist("My_list", repeat=True, shuffle=True)
        self.pl.add_song(Song("Odin1", "Manomar1", "The sons of Odin_01", "2:44"))
        self.pl.add_song(Song("Odin2", "Manomar2", "The sons of Odin_02", "2:44"))
        self.pl.add_song(Song("Odin3", "Manomar3", "The sons of Odin_03", "2:44"))
        self.pl.add_song(Song("Odin4", "Manomar4", "The sons of Odin_04", "2:44"))

    def test_total_lenght(self):
        self.assertEqual(self.pl.total_lenght(), '78:446')

    def test_pprint_playlist(self):
        self.pl.pprint_playlist()

    def test_add_song(self):
        print(self.pl.songs[0])

if __name__ == '__main__':
    unittest.main()
