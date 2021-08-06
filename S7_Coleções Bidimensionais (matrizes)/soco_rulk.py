num_casos = int(input())

for z in range(num_casos):
    n_linhas, n_colunas, soco_x, soco_y = [int(w) for w in input().split()]

    matriz = []
    for i in range(n_linhas):
        matriz.append([int(w) for w in input().split()])

    for i in range(n_linhas):
        for j in range(n_colunas):
            dx = (10 - abs(soco_x - 1 - i)) if (10 - abs(soco_x - 1 - i)) >= 1 else 1
            dy = (10 - abs(soco_y - 1 - j)) if (10 - abs(soco_y - 1 - j)) >= 1 else 1
            matriz[i][j] += min(dx, dy)
    print('Parede {}:'.format(z + 1))
    for linha in matriz:
        print(' '.join([str(w) for w in linha]))
