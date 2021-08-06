num = int(input())

for i in range(num+1):  # Devido ao espaço em branco no começo será acrecentado o '+1'
    lista_arvores = []
    lista_verificadas = []
    arvore = input()
    while arvore != '':
        lista_arvores.append(arvore)
        arvore = input()
    lista_arvores.sort()
    qtdd_total_arvores = len(lista_arvores)
    for arvore_unica in lista_arvores:
        if arvore_unica not in lista_verificadas:
            lista_verificadas.append(arvore_unica)
            qtdd_arvore_unica = lista_arvores.count(arvore_unica)
            porcentagem = (qtdd_arvore_unica / qtdd_total_arvores) * 100
            print('{} {:.4f}'.format(arvore_unica, porcentagem))
