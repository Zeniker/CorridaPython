class LogLine:
    """Classe para obter informações das linhas do log"""

    HOUR_POSITION_END = 18
    PILOT_POSITION_END = 58
    LAP_NUMBER_POSITION_END = 64
    LAP_TIME_POSITION_END = 96
    LAP_AVERAGE_SPEED_POSITION_END = 102

    def __init__(self, line):
        self.__line = line

    def __get_info(self, begin, end):
        return self.__line[begin:end].strip()

    def get_lap_hour(self):
        return self.__get_info(0, self.HOUR_POSITION_END)

    def get_pilot(self):
        return self.__get_info(self.HOUR_POSITION_END, self.PILOT_POSITION_END)

    def __split_pilot_information(self):
        return self.get_pilot().split(" – ")

    def get_pilot_code(self):
        return self.__split_pilot_information()[0]

    def get_pilot_name(self):
        return self.__split_pilot_information()[1]

    def get_lap_number(self):
        return self.__get_info(self.PILOT_POSITION_END, self.LAP_NUMBER_POSITION_END)

    def get_lap_time(self):
        return self.__get_info(self.LAP_NUMBER_POSITION_END, self.LAP_TIME_POSITION_END)

    def get_lap_average_speed(self):
        return self.__get_info(self.LAP_TIME_POSITION_END, self.LAP_AVERAGE_SPEED_POSITION_END)

