operacao = input()

matriz = []

for l in range(12):
    matriz.append([0] * 12)
    for c in range(12):
        matriz[l][c] = float(input())

soma = 0
inicial = 1
final = 11
for l in range(0, 5):
    for c in range(inicial, final):
        soma += matriz[l][c]
    inicial += 1
    final -= 1

if operacao == 'S':
    print(round(soma, 1))
else:
    num_elementos = 30
    media = round(soma / num_elementos, 1)
    print(media)
