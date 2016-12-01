class HackTime:
    def __init__(self, seconds):
        self.all_sec = seconds
        self.hour = self.hours()
        self.mins = self.minutes()
        self.extra_day = False

    def hours(self):
        h = self.all_sec//3600
        if h > 24:
            self.extra_day = True
            h = h - 24
        return h

    def minutes(self):
        m = (self.all_sec % 3600)//60
        return m

    def __str__(self):
        return "{:02d}:{:02d}".format(self.hour, self.mins)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return HackTime(self.all_sec + other.all_sec)


def main():
    print(HackTime(4100))

if __name__ == '__main__':
    main()
