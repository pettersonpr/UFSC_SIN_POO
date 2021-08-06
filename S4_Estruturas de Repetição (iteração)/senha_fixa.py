senha = int(2002)

while senha != 0:
    tentarSenha = int(input())
    if tentarSenha == senha:
        print('Acesso permitido')
        break
    else:
        print('Senha Invalida')
