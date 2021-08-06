# Pegando duração de tempo em segundos
segundos = int(input())

# Converter os segundos em horas
minutos = segundos // 60
# Descontar os minutos dos segungos
segundos = segundos % 60

# Converter os minutos em horas
horas = minutos // 60
# Descontar as horas dos minutos
minutos = minutos % 60

print(f"{horas}:{minutos}:{segundos}")
