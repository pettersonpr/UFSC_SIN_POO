# Pegando valor das notas
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))

# Pegando Valor dos pesos
p1 = float(input('Peso N1: '))
p2 = float(input('Peso N2: '))
p3 = float(input('Peso N3: '))

# Calcular nota final
nota_final = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print(nota_final)
print(nota_final >= 6)
