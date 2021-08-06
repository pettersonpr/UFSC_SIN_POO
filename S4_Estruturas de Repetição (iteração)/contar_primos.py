num1 = int(input())
num2 = int(input())


def verNumeroPrimo(num_primo):
    primo = True
    if num_primo == 1:
        primo = False
    else:
        for i in range(2, num_primo):
            if num_primo % i == 0:
                primo = False
                break
    return primo


contar_primo = 0
for i in range(num1, num2 + 1):
    if verNumeroPrimo(i):
        contar_primo += 1

print(contar_primo)
