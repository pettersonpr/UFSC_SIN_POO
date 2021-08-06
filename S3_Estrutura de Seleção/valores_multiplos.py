n1, n2 = [int(i) for i in input().split()]

if n1 % n2 == 0 or n2 % n1 == 0:
    print('São múltiplos: ')
else:
    print('Não são múltiplos ')
