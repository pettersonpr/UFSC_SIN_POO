qntd = int(input())

while qntd != 0:
    resultado = input().split()
    maria = 0
    joao = 0
    for i in resultado:
        if i == '0':
            maria += 1
        else:
            joao += 1
    print('Mary won {} times and John won {} times'.format(maria, joao))
    qntd = int(input())
