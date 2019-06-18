import unittest
from log_line import LogLine


class TestLogLine(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.__log_line = LogLine("23:49:08.277      038 – F.MASSA                           1	    1:02.852"
                             "                        44,275")

    def test_get_lap_hour(self):
        self.assertEqual("23:49:08.277", self.__log_line.get_lap_hour())

    def test_get_pilot(self):
        self.assertEqual("038 – F.MASSA", self.__log_line.get_pilot())

    def test_get_pilot_code(self):
        self.assertEqual("038", self.__log_line.get_pilot_code())

    def test_get_pilot_name(self):
        self.assertEqual("F.MASSA", self.__log_line.get_pilot_name())

    def test_get_lap_number(self):
        self.assertEqual("1", self.__log_line.get_lap_number())

    def test_get_lap_time(self):
        self.assertEqual("1:02.852", self.__log_line.get_lap_time())

    def test_get_lap_average_speed(self):
        self.assertEqual("44,275", self.__log_line.get_lap_average_speed())
