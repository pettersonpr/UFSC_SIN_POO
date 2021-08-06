l = int(input())
opera = input()


def somar(operacao):
    soma = 0
    for k in m[l]:
        soma += k
    if operacao == 'M':
        med = soma / 12
        print('{:.1f}'.format(med))
    else:
        print('{:.1f}'.format(soma))


m = []
for i in range(12):
    m.append([])
    for j in range(12):
        m[i].append(float(input()))

somar(opera)
