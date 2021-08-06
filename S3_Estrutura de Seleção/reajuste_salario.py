salario_atual = float(input())
salario_minimo = float(input())
qtd_salario_minimo = salario_atual / salario_minimo


def calculaSalario(aliquota):
    salario_ajustado = salario_atual * aliquota
    qtd_salario_ajustado_minimo = salario_ajustado / salario_minimo
    if qtd_salario_ajustado_minimo < 1.5:
        salario_ajustado = salario_minimo * 1.5
    elif qtd_salario_ajustado_minimo > 20:
        salario_ajustado = salario_minimo * 20
    return salario_ajustado


if qtd_salario_minimo <= 3:
    salario_ajustado = calculaSalario(1.2)
    print(salario_ajustado)
elif qtd_salario_minimo > 5:
    salario_ajustado = calculaSalario(1.1)
    print(salario_ajustado)
else:
    salario_ajustado = calculaSalario(1.15)
    print(salario_ajustado)
