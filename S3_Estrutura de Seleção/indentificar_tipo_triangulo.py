n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 == n2 == n3:
    print('equilátero')
elif n1 == n2 and n2 != n3:
    print('isóceles')
elif n1 == n3 and n3 != n2:
    print('isóceles')
elif n2 == n3 and n3 != n1:
    print('isóceles')
else:
    print('escaleno')
