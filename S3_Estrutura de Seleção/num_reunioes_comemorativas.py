dia1 = int(input())
dia2 = int(input())
dia3 = int(input())

dias_iguais = (dia1 == dia2) + (dia1 == dia3) + (dia2 == dia3)

if dias_iguais == 3:
    print('1')
elif dias_iguais == 1:
    print('2')
else:
    print('3')
