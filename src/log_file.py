from log_line import LogLine
from pilot import Pilot
from lap import Lap


class LogFile:

    def get_pilot_data(self):
        log_file = open("log.txt", "r")

        first_line = True

        list_of_pilots = {}

        for line in log_file:
            if first_line:
                first_line = not first_line
                continue

            log_line = LogLine(line)

            if log_line.get_pilot_code() in list_of_pilots:
                pilot = list_of_pilots.get(log_line.get_pilot_code())
            else:
                pilot = Pilot(log_line.get_pilot_code(), log_line.get_pilot_name())
                list_of_pilots[pilot.get_code()] = pilot

            lap = Lap(log_line.get_lap_number(), log_line.get_lap_time(), log_line.get_lap_average_speed(),
                      log_line.get_lap_hour())

            pilot.add_lap(lap)

        log_file.close()

        return list_of_pilots

