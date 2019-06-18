from datetime import timedelta


# Classe do piloto
class Pilot:
    def __init__(self, code, name):
        self.__code = code
        self.__name = name
        self._laps = []

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def add_lap(self, lap):
        self._laps.append(lap)
        self._laps.sort(key=self.sort_lap)

    def get_last_lap(self):
        return self._laps[-1]

    def sort_lap(self, lap):
        return lap.get_number()

    def sum_lap_time(self):
        lap_times = []
        for lap in self._laps:
            lap_times.append(lap.get_time())

        return sum(lap_times, timedelta())
