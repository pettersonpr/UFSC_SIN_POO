ordem = int(input())

while ordem != 0:
    try:
        matriz = []
        # criando linha
        for l in range(ordem):
            matriz.append([0] * ordem)
            # criando/atribuindo valor da coluna
            for c in range(ordem):
                # ponto central
                if l == c and l + c == ordem - 1:
                    matriz[l][c] = 4
                # diagonal principal
                elif c == l:
                    matriz[l][c] = 2
                # diagonal secundaria
                elif l + c == ordem - 1:
                    matriz[l][c] = 3
                # parte interna
                if round(ordem / 3) * 2 - 1 >= l >= round(ordem / 3) - 1 <= c <= round(ordem / 3) * 2 - 1 and not(l == c and l + c == ordem - 1):
                    matriz[l][c] = 1
        # imprimindo matriz
        for l in matriz:
            for c in l:
                print('{}'.format(c), end='')
            print()
        print()
        ordem = int(input())
    except EOFError:
        break
