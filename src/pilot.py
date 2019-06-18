# Classe do piloto
class Pilot:
    __code = 0
    __name = ""
    _laps = []

    def __init__(self, code, name):
        self.__code = code
        self.__name = name

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def add_lap(self, lap):
        self._laps.append(lap)

