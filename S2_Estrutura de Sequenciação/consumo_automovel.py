# Pegando valor da distancia e do consumo de combustivel
distancia = float(input())
combustivel = float(input())

# Calculando a media
media = distancia / combustivel

# Imprimindo valor com tres casas decimais
print("{:.3f} km/l".format(media))