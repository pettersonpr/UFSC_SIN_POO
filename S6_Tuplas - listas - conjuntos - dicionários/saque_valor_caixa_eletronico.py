tipo_notas = int(input())
valores = {}
notas_saque = []
for i in range(tipo_notas):
    valor = float(input())
    valores[valor] = int(input())

valor_saque = float(input())

valores_notas = list(valores.keys())
for valor in valores_notas[::-1]:
    num_notas = min(valores[valor], int(valor_saque // valor))
    valor_saque -= num_notas * valor
    notas_saque.append(num_notas)

'''for x in notas_saque[::-1]:
    print(x, end=' ')'''

print(' '.join([str(x) for x in notas_saque[::-1]]))
