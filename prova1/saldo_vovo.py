num_oper, saldo = [int(w) for w in input().split()]

menor_saldo = saldo
for _ in range(num_oper):
    valor = int(input())
    saldo += valor
    if saldo < menor_saldo:
        menor_saldo = saldo

print(menor_saldo)
