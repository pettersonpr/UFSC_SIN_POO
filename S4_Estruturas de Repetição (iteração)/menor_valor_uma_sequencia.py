import math

quantidade = int(input())
menor_valor = math.inf

for _ in range(quantidade):
    valor = int(input())
    if valor < menor_valor:
        menor_valor = valor

print(menor_valor)
