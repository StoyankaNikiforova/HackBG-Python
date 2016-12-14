import json
from random import randint
from tabulate import tabulate


class Playlist:
    def __init__(self, name="Code", repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = []
        
    def add_song(self, song):
        self.songs.append(song)

    def total_lenght(self):
        lengh = 0
        for s in self.songs:
            lengh += s.lenght(seconds=True)
        hours = int(lengh//3600)
        minutes = int((lengh % 3600) / 60)
        seconds = int((lengh % 3600) % 60)

        return "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)

    def artists(self):
        artists = {}
        for song in self.songs:
            if song.artist in artists:
                artists[song.artist] += 1
            else:
                artists[song.artist] = 1
        return artists

    def current_song(self):
        pass

    def next_song(self):
        return randint(0, len(self.add_songs))

    def pprint_playlist(self):
        table = []
        headers = ["Artist", "Song", "Lenght"]
        for song in self.songs:
            table.append([song.artist, song.title, song.lenght_string])

        print(tabulate(table, headers, tablefmt="fancy_grid"))
