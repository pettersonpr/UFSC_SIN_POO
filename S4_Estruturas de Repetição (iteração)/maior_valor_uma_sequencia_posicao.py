import math

quantidade = int(input())
maior_valor = -math.inf
posicao = 0

for _ in range(quantidade):
    valor = int(input())
    posicao += 1
    if valor > maior_valor:
        maior_valor = valor
        posicao_maior_valor = posicao

print(maior_valor, posicao_maior_valor)
