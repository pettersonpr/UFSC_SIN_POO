qtdd_sorteio = int(input())

for _ in range(qtdd_sorteio):
    num_participantes, num_sorte = [int(x) for x in input().split()]
    escolhas = [int(x) for x in input().split()]

    diferencas = [abs(num_sorte - escolha) for escolha in escolhas]
    indice = diferencas.index(min(diferencas)) + 1

    print(indice)
