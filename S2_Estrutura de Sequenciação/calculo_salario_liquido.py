valor_horas = 2500/200
horas_trabalhadas = float(input())
hora_extra = float(input())

salario_horas_normais = valor_horas * horas_trabalhadas
valor_hora_extra = (hora_extra * valor_horas) * (1+20/100)
salario_bruto = salario_horas_normais + valor_hora_extra

INSS = salario_bruto * (9/100)
IR = salario_bruto * (13/100)

salario_liquido = salario_bruto - INSS - IR


print("- Salário Bruto : R$ {:.2f}".format(salario_bruto))
print("- IR (13%) : R$ {:.2f}".format(IR))
print("- INSS (9%) : R$ {:.2f}".format(INSS))
print("- Salário Líquido : R$ {:.2f}".format(salario_liquido))
