n = int(input())
while n != 0:
    soma_pares_varetas = 0
    for i in range(n):
        cmp, num = [int(x) for x in input().split()]
        soma_pares_varetas += num // 2

    num_retangulos = soma_pares_varetas // 2
    print(num_retangulos)
    n = int(input())
