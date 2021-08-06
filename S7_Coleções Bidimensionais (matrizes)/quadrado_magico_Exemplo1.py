ordem = int(input())

matriz = []

for l in range(ordem):
    matriz.append([0] * ordem)
    for c in range(ordem):
        matriz[l][c] = float(input())

lista_valores_somas = []

# Calcular linhas
for l in range(ordem):
    lista_valores_somas.append(sum(matriz[l]))
print(lista_valores_somas)

# Calcular colunas
for c in range(ordem):
    soma = 0
    for l in range(ordem):
        soma += matriz[l][c]
    lista_valores_somas.append(soma)
print(lista_valores_somas)

# Calcular diagonal principal
soma = 0
for i in range(ordem):
    soma += matriz[i][i]
lista_valores_somas.append(soma)
print(lista_valores_somas)

# Calcular diagonal secundária
soma = 0
for i in range(ordem):
    soma += matriz[i][ordem-1-i]
lista_valores_somas.append(soma)
print(lista_valores_somas)

print(min(lista_valores_somas) == max(lista_valores_somas))
