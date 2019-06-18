import unittest
from pilot import Pilot
from lap import Lap
from datetime import timedelta


class TestPilot(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.__pilot = Pilot("038", "F.MASSA")

    def test_get_code(self):
        self.assertEqual("038", self.__pilot.get_code())

    def test_get_name(self):
        self.assertEqual("F.MASSA", self.__pilot.get_name())

    def test_add_lap(self):
        lap = Lap("1", "1:02.852", "44,275", "23:49:08.277")
        self.__pilot.add_lap(lap)
        self.assertEqual(lap, self.__pilot.get_last_lap())

    def test_get_last_lap(self):
        lap1 = Lap("1", "1:02.852", "44,275", "23:49:08.277")
        lap2 = Lap("2", "1:02.852", "44,275", "23:49:08.277")
        self.assertIsNone(self.__pilot.get_last_lap())
        self.__pilot.add_lap(lap2)
        self.__pilot.add_lap(lap1)
        self.assertEqual(lap2, self.__pilot.get_last_lap())

    def test_sum_lap_time(self):
        lap1 = Lap("1", "1:02.852", "44,275", "23:49:08.277")
        lap2 = Lap("2", "1:02.851", "44,275", "23:49:08.277")
        self.__pilot.add_lap(lap2)
        self.__pilot.add_lap(lap1)
        self.assertEqual(lap2.get_time() + lap1.get_time(), self.__pilot.sum_lap_time())

    def test_best_lap_time(self):
        lap1 = Lap("1", "1:02.852", "44,275", "23:49:08.277")
        lap2 = Lap("2", "1:02.851", "63,235", "23:49:08.277")
        self.__pilot.add_lap(lap2)
        self.__pilot.add_lap(lap1)
        self.assertEqual(lap2.get_time(), self.__pilot.get_best_lap_time())

    def test_get_average_match_speed(self):
        lap1 = Lap("1", "1:02.852", "44,275", "23:49:08.277")
        lap2 = Lap("2", "1:02.851", "63,235", "23:49:08.277")
        self.__pilot.add_lap(lap2)
        self.__pilot.add_lap(lap1)
        self.assertEqual(53.755, self.__pilot.get_average_match_speed())

    def test_get_interval_from_pilot(self):
        lap1 = Lap("1", "1:02.852", "44,275", "23:49:08.277")
        lap2 = Lap("2", "1:02.851", "63,235", "23:49:08.277")

        pilot2 = Pilot("037", "R.MASSA")
        self.assertEqual("N/D", self.__pilot.get_interval_from_pilot(pilot2))

        self.__pilot.add_lap(lap2)
        self.__pilot.add_lap(lap1)

        lap1 = Lap("1", "1:02.852", "44,275", "23:49:08.277")
        lap2 = Lap("2", "1:02.851", "63,235", "23:49:08.277")
        pilot2.add_lap(lap2)
        pilot2.add_lap(lap1)

        pilot3 = Pilot("037", "R.MASSA")
        lap1 = Lap("1", "1:02.852", "44,275", "23:49:08.277")
        pilot3.add_lap(lap1)

        self.assertEqual(timedelta(), self.__pilot.get_interval_from_pilot(pilot2))
        self.assertEqual("N/D", self.__pilot.get_interval_from_pilot(pilot3))


