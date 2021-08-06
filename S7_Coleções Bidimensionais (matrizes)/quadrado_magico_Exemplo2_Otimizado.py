ordem = int(input())
matriz = []
for i in range(ordem):  # Criar matriz
    matriz.append([float(w) for w in input().split()])

lista_valores_somas = []
soma_diag_principal = 0
soma_diag_secundaria = 0
for l in range(ordem):
    lista_valores_somas.append(sum(matriz[l]))  # Soma linha
    soma_diag_principal += matriz[l][l]  # Somando diagonal principal
    soma_diag_secundaria += matriz[l][ordem - 1 - l]  # Somando diagonal secundaria
    soma_coluna = 0
    for c in range(ordem):  # Soma coluna
        soma_coluna += matriz[c][l]
    lista_valores_somas.append(soma_coluna)
lista_valores_somas.append(soma_diag_principal)
lista_valores_somas.append(soma_diag_secundaria)
print(min(lista_valores_somas) == max(lista_valores_somas))
