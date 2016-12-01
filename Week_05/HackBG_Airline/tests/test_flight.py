import unittest
import sys
sys.path.append("/home/tanija/hack_bg/Week_05/HackBG_Airline/")
from flight import Flight
from date import Date


class testFlight(unittest.TestCase):
    def setUp(self):
        self.flight = Flight(Date(29, 11, 2016, '12:20'), Date(29, 11, 2016, '15:30'), 100, 120, "Sofia", "London", Terminal(2, 30), False)

    def test_init(self):
        self.assertEqual(flight.max_passengers, 120)

if __name__ == '__main__':
    unittest.main()
