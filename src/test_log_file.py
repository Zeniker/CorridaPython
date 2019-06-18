import unittest
from log_file import LogFile


class TestLogFile(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.__log_file = LogFile()

    def test_get_pilot_data(self):
        pilot_data = self.__log_file.get_pilot_data()
        self.assertEqual(6, len(pilot_data))

