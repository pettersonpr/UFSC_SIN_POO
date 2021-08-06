n3 = int(input())
n1 = int(input())
n2 = int(input())

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

print(maior >= n3 >= menor)
