# Blauzen
from log_line import LogLine
from pilot import Pilot
from lap import Lap

log_file = open("log.txt", "r")
print("Nome do arquivo: ", log_file.name)

first_line = True

list_of_pilots = {}

for line in log_file:
    if first_line:
        first_line = not first_line
    else:
        # print(line)
        # informations = line.split("  ")
        # print(line[0:18])
        log_line = LogLine(line)
        # print(log_line.get_hour())
        # print(log_line.get_pilot())
        # print(log_line.get_lap_number())
        # print(log_line.get_lap_time())
        # print(log_line.get_lap_average_speed())

        if log_line.get_pilot_code() in list_of_pilots:
            pilot = list_of_pilots.get(log_line.get_pilot_code())
        else:
            pilot = Pilot(log_line.get_pilot_code(), log_line.get_pilot_name())
            list_of_pilots[pilot.get_code()] = pilot

        lap = Lap(log_line.get_lap_number(), log_line.get_lap_time(), log_line.get_lap_average_speed(),
                  log_line.get_lap_hour())

        pilot.add_lap(lap)


log_file.close()
