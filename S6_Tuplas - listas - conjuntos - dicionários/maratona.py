num_posto, dist_interm = [int(w) for w in input().split()]

resultado = 'S'

lista_postos = [int(w) for w in input().split()]

for i in range(len(lista_postos)-1):
    if (lista_postos[i+1] - lista_postos[i]) > dist_interm:
        resultado = 'N'
        break

print(resultado)
