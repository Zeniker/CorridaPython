from log_file import LogFile
from datetime import timedelta


def sort_pilots(pilot):
    last_lap = pilot.get_last_lap()
    return last_lap.get_hour(), last_lap.get_number()


ordem_chegada = []

pilot_data = LogFile().get_pilot_data()

for code in pilot_data:
    pilot = pilot_data[code]
    last_lap = pilot.get_last_lap()

    ordem_chegada.append(pilot)

ordem_chegada.sort(key=sort_pilots)
best_lap_time = timedelta()

print("Informações dos pilotos:")
for i in range(len(ordem_chegada)):
    pilot = ordem_chegada[i]

    if best_lap_time == timedelta() or best_lap_time > pilot.get_best_lap_time():
        best_lap_time = pilot.get_best_lap_time()

    resultado_piloto = "Posição Chegada: " + str(i+1) + "\t"
    resultado_piloto += "Código Piloto: " + pilot.get_code() + "\t"
    resultado_piloto += "Nome Piloto: " + pilot.get_name() + "\t"
    resultado_piloto += "Qtde Voltas Completadas: " + str(pilot.get_last_lap().get_number()) + "\t"
    resultado_piloto += "Tempo total de Prova: " + str(pilot.sum_lap_time()) + "\t"
    resultado_piloto += "Melhor Volta: " + str(pilot.get_best_lap_time()) + "\t"
    resultado_piloto += "Velocidade Média: " + str(pilot.get_average_match_speed()) + "\t"
    resultado_piloto += "Tempo Chegada Após Vencedor: " + str(pilot.get_interval_from_pilot(ordem_chegada[0])) + "\t"

    print(resultado_piloto)

print("\nInformações gerais:")
print("Melhor volta da corrida: " + str(best_lap_time))
