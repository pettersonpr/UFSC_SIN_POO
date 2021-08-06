import re


def verifica_dv(numero):
    soma = 0
    peso = len(numero)
    for i in range(len(numero) - 1):
        soma += int(numero[i]) * peso
        peso -= 1
    dv = 11 - soma % 11
    if dv >= 10:
        dv = 0

    return dv == int(numero[-1])


cpf = input()
cpf = re.sub('[^0-9]', '', cpf)  # ^ -> é chamado regex - retirar tudo que não for número

cpf_valido = len(cpf) == 11 and cpf != cpf[0]*11 and verifica_dv(cpf) and verifica_dv(cpf[:-1])

print(cpf_valido)
