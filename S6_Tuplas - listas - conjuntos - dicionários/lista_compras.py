qtdd_lista_compras = int(input())

for _ in range(qtdd_lista_compras):
    lista_produtos_unicos = set()
    lista_produtos = [w for w in input().split()]
    for i in lista_produtos:
        lista_produtos_unicos.add(i)
    lista_produtos = [w for w in lista_produtos_unicos]
    lista_produtos.sort()
    for produto in lista_produtos:
        print(produto, end=' ')
    print()
