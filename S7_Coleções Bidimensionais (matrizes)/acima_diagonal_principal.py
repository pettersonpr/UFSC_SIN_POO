operacao = input()

matriz = []

for l in range(12):
    matriz.append([0] * 12)
    for c in range(12):
        matriz[l][c] = float(input())

soma = 0
for l in range(0, 11):
    for c in range(0, 11 - l):
        soma += matriz[l][c]

if operacao == 'S':
    print(round(soma, 1))
else:
    num_elementos = (144 - 12) / 2
    media = round(soma / num_elementos, 1)
    print(media)
