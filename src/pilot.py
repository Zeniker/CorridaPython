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
        self._laps.sort(key=lambda k: k.get_number())

    def get_last_lap(self):
        return self._laps[-1]

    def sum_lap_time(self):
        lap_times = []
        for lap in self._laps:
            lap_times.append(lap.get_time())

        return sum(lap_times, timedelta())

    def get_best_lap_time(self):
        lap_times = []
        for lap in self._laps:
            lap_times.append(lap.get_time())

        lap_times.sort()

        return lap_times[0]

    def get_average_match_speed(self):
        lap_average_speed = []
        for lap in self._laps:
            lap_average_speed.append(lap.get_average_speed())

        return round(sum(lap_average_speed) / len(lap_average_speed), 3)

    def get_interval_from_pilot(self, pilot):
        self_last_lap = self.get_last_lap()
        target_last_lap = pilot.get_last_lap()

        if self_last_lap.get_number() != target_last_lap.get_number():
            return 'N/D'

        return self_last_lap.get_time() - target_last_lap.get_time()
