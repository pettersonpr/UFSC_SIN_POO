linhas, colunas = [int(w) for w in input().split()]

while True:
    try:
        matriz = []
        pos_pokemon = []
        pos_pessoa = []
        for i in range(linhas):
            matriz.append([int(w) for w in input().split()])
            for j in range(colunas):
                if matriz[i][j] == 2:
                    pos_pokemon = [i, j]
                elif matriz[i][j] == 1:
                    pos_pessoa = [i, j]
        distancia = abs(pos_pokemon[0] - pos_pessoa[0]) + abs(pos_pokemon[1] - pos_pessoa[1])
        print(distancia)
        linhas, colunas = [int(w) for w in input().split()]
    except EOFError:
        break
