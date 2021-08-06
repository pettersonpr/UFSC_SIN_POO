valor_veioculo = float(input())
sexo = input()
idade = int(input())

premio = valor_veioculo * 0.1

if sexo == 'M':
    if idade <= 24:
        print(premio)
    elif idade > 33:
        premio -= premio * 0.2
        print(premio)
    else:
        premio -= premio * 0.1
        print(premio)
elif sexo == 'F':
    if idade <= 24:
        premio -= premio * 0.05
        print(premio)
    elif idade > 33:
        premio -= premio * 0.35
        print(premio)
    else:
        premio -= premio * 0.2
        print(premio)
