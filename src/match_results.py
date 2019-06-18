# Blauzen
from log_line import LogLine
from pilot import Pilot
from lap import Lap


def sort_pilots_by_hour(pilot):
    last_lap = pilot.get_last_lap()
    return last_lap.get_hour(), last_lap.get_number()


log_file = open("log.txt", "r")
print("Nome do arquivo: ", log_file.name)

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

ordem_chegada = []

for code in list_of_pilots:
    pilot = list_of_pilots[code]
    last_lap = pilot.get_last_lap()

    ordem_chegada.append(pilot)

ordem_chegada.sort(key=sort_pilots_by_hour)

for i in range(len(ordem_chegada)):
    pilot = ordem_chegada[i]
    resultado_piloto = "Posição Chegada: " + str(i+1) + "\t"
    resultado_piloto += "Código Piloto: " + pilot.get_code() + "\t"
    resultado_piloto += "Nome Piloto: " + pilot.get_name() + "\t"
    resultado_piloto += "Qtde Voltas Completadas: " + str(pilot.get_last_lap().get_number()) + "\t"
    resultado_piloto += "Tempo total de Prova: " + str(pilot.sum_lap_time()) + "\t"

    print(resultado_piloto)
