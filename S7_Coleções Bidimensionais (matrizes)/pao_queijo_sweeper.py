while True:
    try:
        num_linhas, num_colunas = [int(x) for x in input().split()]

        matriz = []
        for i in range(num_linhas):
            matriz.append([int(x) * 9 for x in input().split()])

        for i in range(num_linhas):
            for j in range(num_colunas):
                if matriz[i][j] == 0:
                    for di, dj in ((0,1), (0,-1), (1, 0), (-1, 0)):
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < num_linhas and 0 <= nj < num_colunas and matriz[ni][nj] == 9:
                            matriz[i][j] += 1
                print(matriz[i][j], end='')
            print()
    except EOFError:
        break
