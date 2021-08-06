nome = input()
partes = nome.split()

for i in range(1, len(partes) - 1):
    if len(partes[i]) > 3:
        partes[i] = partes[i][0] + '.'
nome_abreviado = ' '.join(partes)

print(nome_abreviado)
