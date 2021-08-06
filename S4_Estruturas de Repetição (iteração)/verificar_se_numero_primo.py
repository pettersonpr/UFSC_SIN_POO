n = int(input())
contador = 0

if n == 1:
    print('False')
elif n == 2:
    print('True')
else:
    for i in range(2, n):
        if n % i == 0:
            print('false')
            break
        if i == n-1:
            print('True')
            break

'''
n = int(input())
contador = 0

if n == 1:
    print('False')
else:
    for i in range(1, n+1):
        if n % i == 0:
            contador += 1
        if contador > 2:
            print('false')
            break
        if i == n:
            print('True')
'''