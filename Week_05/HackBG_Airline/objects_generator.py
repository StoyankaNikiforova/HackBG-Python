import random
import json
import pickle
from flight import Flight
from passenger import Passenger
from reservation import Reservation
from terminal import Terminal
from date import Date
from hack_time import HackTime


class Generator:
    # todo: females and males names
    first_names = ['Miro', 'Mila', 'Maria', 'Elka', 'Ivan', 'Ceco', 'Petyr',
                                                                    'Vasko']
    last_names = ['Ivanov', 'Valiev', 'Smit', 'Jones', 'Vasilev', 'Petrov',
                            'Dimitrov']
    destinations = ['Sofia', 'Atlanta', 'Madrid',
                    'Oslo', 'Varna', 'Viena', 'Paris', 'Bratislava']
    passengers_counts = [110, 451, 700, 200, 120, 150, 280, 230, 189, 255]
    count_flights = [50, 60, 20, 68, 25, 10, 5]
    # terminal_num = [1, 2, 3, 4, 5]
    declined = [True, False]

    def __init__(self, term_count, fl_count, pass_count, reserv_count):
        self.term_count = term_count
        self.fl_count = fl_count
        self.pass_count = pass_count
        self.reserv_count = reserv_count
        self.terminals = self.terminals()
        self.flights = self.flights()
        self.passengers = self.passengers()
        self.reservations = self.reservations()

    def dateTime(self):
        return Date(random.randint(1, 31),  random.randint(1, 12),
                    random.randint(2000, 2016),
                    str(HackTime(random.randint(3600, 86400))))

    def terminals(self):
        terms = []
        for num in range(1, self.term_count+1):
            terms.append(Terminal(num, random.choice(self.count_flights)))
        return terms

    def get_terminal(self, count_fl_in_term):
        is_get = False
        while not is_get:
            terminal = random.choice(self.terminals)
            if terminal.max_flights > count_fl_in_term[terminal.number]:
                count_fl_in_term[terminal.number] += 1
                is_get = True
                return terminal

    def flights(self):
        fls = []
        count_fl_in_term = {}
        for i in range(1, self.term_count+1):
            count_fl_in_term[i] = 0
        for i in range(self.fl_count):
            id_flight = "{:04d}".format(i)
            from_dest = random.choice(self.destinations)
            to_dest = random.choice(self.destinations)
            passengers = random.choice(self.passengers_counts)
            max_passengers = passengers + random.randint(0, 100)
            date_time_start = self.dateTime()
            start_time = Date.copy(date_time_start)
            date_time_start.hour += str(HackTime(random.randint(2400, 9000)))
            date_time_end = date_time_start
            end_time = date_time_end
            terminal = self.get_terminal(count_fl_in_term)
            decl = random.choice(self.declined)
            current_fl = Flight(id_flight, start_time, end_time,
                                passengers, max_passengers,
                                from_dest, to_dest, terminal, decl)
            fls.append(current_fl)
            terminal.flights.append(current_fl)
        return fls

    def passengers(self):
        list_pass = []
        for i in range(self.pass_count):
            flight = self.flights[
                            random.randint(0, len(self.flights)-1)]
            list_pass.append(Passenger(random.choice(self.first_names),
                             random.choice(self.last_names),
                             flight, random.randint(1, 100)))
        return list_pass

    def reservations(self):
        res = []
        for i in range(self.reserv_count):
            res.append(Reservation("{:04}".format(i),
                       random.choice(self.flights),
                       random.choice(self.passengers),
                       random.choice(self.declined)))
        return res

    def to_json(self):
        return "{},{},{},{}".format(self.terminals, self.flights,
                                    self.passengers, self.reservations)


def test():
    g = Generator(3, 10, 500, 300)
    with open('data1.pickle', 'wb') as outfile:
        pickle.dump(g, outfile)

    print(g.terminals)
    print(g.flights)
    print(g.reservations)
    print(g.passengers)


if __name__ == '__main__':
    test()
