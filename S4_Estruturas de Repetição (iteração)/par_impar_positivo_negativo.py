par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(5):
    num = int(input())

    if num > 0:
        positivo += 1
    elif num < 0:
        negativo += 1
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativos'.format(negativo))
