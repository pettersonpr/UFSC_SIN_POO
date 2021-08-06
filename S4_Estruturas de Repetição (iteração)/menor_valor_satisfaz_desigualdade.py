x = 1

def calculaFatorial(num):
    fatorial = 1
    for i in range(num, 1, -1):
        fatorial *= i

    return fatorial

while calculaFatorial(x) <= x**10:
    x += 1

print(x)
