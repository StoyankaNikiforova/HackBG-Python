class Song:
    def __init__(self, title="Odin", artist="Manomar",
                 album="The sons of Odin", lenght="3:44"):
        self.title = title
        self.artist = artist
        self.album = album
        self.lenght_string = lenght

    def __str__(self):
        return "{0} - {1} from {2} - {3}".format(self.artist, self.title,
                                                 self.album, self.lenght_string)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return (hash(self.title) ^ hash(self.lenght_string)) + 7, 56789

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album and self.lenght_string == other.lenght_string

    def lenght(self, seconds=False, minutes=False, hours=False):
        input_len = self.lenght_string.split(':')
        all_seconds = int(input_len[0])*60 + int(input_len[1])
        if seconds:
            return all_seconds
        if minutes:
            return all_seconds / 60
        if hours:
            return all_seconds / 3600
        return self.lenght


# def main
