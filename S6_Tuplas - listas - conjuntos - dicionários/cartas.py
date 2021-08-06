lista_cartas = [int(w) for w in input().split()]

lista_crescente = lista_cartas.copy()
lista_crescente.sort()
lista_decrescente = lista_cartas.copy()
lista_decrescente.sort(reverse=True)

resultado = 'N'

if lista_cartas == lista_crescente:
    resultado = 'C'
elif lista_cartas == lista_decrescente:
    resultado = 'D'

print(resultado)
