import unittest
from lap import Lap
from datetime import datetime, timedelta


class TestLap(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.__lap = Lap("1", "1:02.852", "44,275", "23:49:08.277")

    def test_get_number(self):
        self.assertEqual(1, self.__lap.get_number())

    def test_get_average_speed(self):
        self.assertEqual(44.275, self.__lap.get_average_speed())

    def test_get_time(self):
        temp_timedelta = timedelta(minutes=1, seconds=2, microseconds=852000)
        self.assertEqual(temp_timedelta, self.__lap.get_time())

    def test_get_hour(self):
        temp_datetime = datetime(year=1900, month=1, day=1, hour=23, minute=49, second=8, microsecond=277000)
        self.assertEqual(temp_datetime, self.__lap.get_hour())
