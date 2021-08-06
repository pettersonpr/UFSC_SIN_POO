ordem = int(input())

contador = 0
while ordem != 0:
    if contador != 0:
        print()
    num_aux = 1
    matriz = []
    for l in range(ordem):
        if l > 0:
            num_aux = matriz[l - 1][0] * 2
        matriz.append([num_aux] * ordem)
        for c in range(1, ordem):
            matriz[l][c] = num_aux * 2
            num_aux *= 2
    tamanho_maior = len(str(matriz[ordem - 1][ordem - 1]))
    for l in matriz:
        for elemento in l[:-1]:
            print('{:{}}'.format(elemento, tamanho_maior), end=' ')
        print('{:{}}'.format(l[-1], tamanho_maior))
        # print(' '.join(['{:{}}'.format(elemento, tamanho_maior) for elemento in l]))
    contador += 1
    ordem = int(input())
