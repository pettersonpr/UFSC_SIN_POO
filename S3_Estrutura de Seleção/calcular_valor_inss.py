salario = float(input())

if salario > 2400.00:
    inss = 2400 * 0.11
    print(inss)
elif salario > 1200:
    inss = salario * 0.11
    print(inss)
elif salario >720:
    inss = salario * 0.09
    print(inss)
else:
    inss = salario * 0.0765
    print(inss)
