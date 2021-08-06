valor_horas = float(2500/200)
horas_trabalhadas = float(input())
hora_extra = float(input())

salario_horas_normais = valor_horas * horas_trabalhadas
valor_hora_extra = (hora_extra * valor_horas) * (1+20/100)
salario_bruto = salario_horas_normais + valor_hora_extra

INSS = salario_bruto * (9/100)
IR = salario_bruto * (13/100)

salario_liquido = salario_bruto - INSS - IR


print("- Salário Bruto : R$ ", round(salario_bruto, 2))
print("- IR (13%) : R$ ", round(IR, 2))
print("- INSS (9%) : R$ ", round(INSS, 2))
print("- Salário Líquido : R$ ", round(salario_liquido, 2))
