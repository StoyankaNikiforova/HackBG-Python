class Date:
    def __init__(self, day, mont, year, str_hour):
        self.day = day
        self.month = month
        self.year = year
        self.hour = HackTime(self.seconds())

    def __str__(self):
        return "{0}.{1}.{2} {3}".format(self.day, self.month,
                                        self.year, self.hour)

    def __repr__(self):
        return self.__str_()

    def copy(self):
        return self

    def seconds(self):
        input_hour = str_hour.split(':')
        hour = input_hour[0].strip('0')
        minutes = input_hour[1].strip('0')

        return (hour * 3600) + (minutes * 360)
