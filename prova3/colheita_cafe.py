while True:
    try:
        linhas, colunas = [int(w) for w in input().split()]
        matriz = []
        soma = 0
        for i in range(linhas):
            matriz.append([int(w) for w in input().split()])
            soma += sum(matriz[i])
        sacos = soma // 60
        sobras_litros = soma % 60
        print('{} saca(s) e {} litro(s)'.format(sacos, sobras_litros))
    except EOFError:
        break
