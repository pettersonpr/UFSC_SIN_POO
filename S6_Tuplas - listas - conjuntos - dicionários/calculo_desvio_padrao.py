import math

n = int(input())
valores = list()  # cria uma lista vazia (pode ser também:  valores = []  )
for _ in range(n):
    valores.append(float(input()))  # acrescenta o valor lido no final da lista

media = sum(valores) / len(valores)

soma = 0
for x in valores:  # percorre a lista, elemento a elemento
    soma += (x - media) ** 2

desvio_padrao = math.sqrt(soma / (len(valores) - 1))
print(desvio_padrao)
