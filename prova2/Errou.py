num = int(input())

for i in range(num):
    equação = input().split()
    if equação[1] == '+':
        resultado = int(equação[0]) + int(equação[2])
    elif equação[1] == '-':
        resultado = int(equação[0]) - int(equação[2])
    else:
        resultado = int(equação[0]) * int(equação[2])
    diferenca_resultado = abs(resultado - int(equação[4]))
    print('E{}ou!'.format('r' * diferenca_resultado))
