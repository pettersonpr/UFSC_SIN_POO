qtdd_1_lista = int(input())
lista_1 = [input() for _ in range(qtdd_1_lista)]

qtdd_2_lista = int(input())
lista_2 = [input() for _ in range(qtdd_2_lista)]

lista_completa = sorted(lista_1 + lista_2)

for nome in lista_completa:
    print(nome)
