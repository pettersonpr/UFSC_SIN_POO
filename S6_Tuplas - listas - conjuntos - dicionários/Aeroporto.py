qtdd_aeroportos, qtdd_voos = [int(w) for w in input().split()]
teste = 0

while qtdd_aeroportos != 0 and qtdd_voos != 0:
    teste += 1
    lista_voos = []
    mais_movimentado = ''
    qtdd_mais_movimentado = -1
    for i in range(qtdd_voos):
        voos_unicos = [int(w) for w in input().split()]
        lista_voos.append(voos_unicos[0])
        lista_voos.append(voos_unicos[1])
    for w in range(1, qtdd_voos + 1):
        if lista_voos.count(w) > qtdd_mais_movimentado:
            qtdd_mais_movimentado = lista_voos.count(w)
            mais_movimentado = str(w)
        elif lista_voos.count(w) == qtdd_mais_movimentado:
            mais_movimentado += ' ' + str(w)
    print('Teste {}\n{}'.format(teste, mais_movimentado))
    qtdd_aeroportos, qtdd_voos = [int(w) for w in input().split()]
