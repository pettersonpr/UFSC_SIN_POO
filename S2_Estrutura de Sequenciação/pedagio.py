from math import *

# Pegar dados
L, D = [int(i) for i in input('Comprimento e dist pedagio :\n').split()]
K, P = [int(i) for i in input('custo km e valor pedagio :\n').split()]

# Calcular custo total
qtdd_pedagios = floor(L / D)  # Descobrindo quantidade de pedágios
custo_combustivel = K * L
custo_pedagio = qtdd_pedagios * P
custo_total = round(custo_combustivel + custo_pedagio)


print(custo_total)
