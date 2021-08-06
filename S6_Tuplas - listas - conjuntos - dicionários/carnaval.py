notas = [float(i) for i in input().split()]
notas.sort()
nota_final = sum(notas[1:4])

print(nota_final)
