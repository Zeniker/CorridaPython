from datetime import datetime, timedelta


class Lap:
    """Classe para guardar informações das voltas realizadas durante a corrida"""

    def __init__(self, number, time, average_speed, hour):
        self.__number = int(number)
        self.__average_speed = self.__convert_average_speed_to_float(average_speed)
        self.__time = self.__convert_string_to_timedelta(time)
        self._hour = self.__convert_string_to_datetime(hour)

    def __convert_average_speed_to_float(self, average_speed_string):
        average_speed_string = average_speed_string.replace(",", ".")
        return float(average_speed_string)

    def __convert_string_to_datetime(self, string_hour):
        return datetime.strptime(string_hour, "%H:%M:%S.%f")

    def __convert_string_to_timedelta(self, string_time):
        temp_datetime = datetime.strptime(string_time, "%M:%S.%f")
        return timedelta(minutes=temp_datetime.minute,
                         seconds=temp_datetime.second,
                         microseconds=temp_datetime.microsecond)

    def get_number(self):
        return self.__number

    def get_hour(self):
        return self._hour

    def get_time(self):
        return self.__time

    def get_average_speed(self):
        return self.__average_speed
