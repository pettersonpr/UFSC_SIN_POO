nota = float(input())

parte_int = int(nota)
parte_fracionaria = nota - parte_int

if parte_fracionaria < 0.25:
    nota_arredondada = parte_int
elif parte_fracionaria < 0.75:
    nota_arredondada = parte_int + 0.5
else:
    nota_arredondada = parte_int + 1

print(nota_arredondada)
