num = int(input())
binario = ''

if num == 0:
    binario = '0'
else:
    while num != 0:
        binario = str(num % 2) + binario
        num //= 2

print(binario)
