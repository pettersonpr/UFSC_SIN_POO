# Pegando as tres notas do aluno
nA = float(input())
nB = float(input())
nC = float(input())

# Calculando media com pesos
media = ((nA*2) + (nB*3) + (nC*5)) /  (2+3+5)

# Imprimindo nota
print("nota final: {:.1f}".format(media))
