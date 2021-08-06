'''n1 = int(input())
n2 = int(input())

menor = min(n1, n2)
divisor = 2
mdc = 1
while divisor <= menor:
    if n1 % divisor == 0 and n2 % divisor == 0:
        mdc = divisor
    divisor += 1

print(mdc)
'''

'''
n1 = int(input())
n2 = int(input())

resto = n1 % n2
while resto > 0:
    n1 = n2
    n2 = resto
    resto = n1 % n2

print(n2)'''

# Cálculo de MDC com o método de Euclides

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

a = n1
b = n2
while b > 0:
    resto = a % b;
    a = b
    b = resto

print("MDC de {} e {} = {}".format(n1, n2, a))
