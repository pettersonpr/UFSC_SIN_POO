qtdd = int(input())

for _ in range(qtdd):
    num = int(input())
    numero_perfeito = 0
    for i in range(1, num):
        if num % i == 0:
            numero_perfeito += i
    if numero_perfeito == num:
        print('{} eh perfeito'.format(num))
    else:
        print('{} nao eh perfeito'.format(num))
