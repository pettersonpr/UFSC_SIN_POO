salario_bruto = float(input())
num_dependentes = int(input())
desconto_dependente = num_dependentes * 137.99

if 1372.82 <= salario_bruto <= 2400:
    IRRF = (salario_bruto - desconto_dependente - salario_bruto * 0.11) * 0.15 - 205.92
    if IRRF < 0:
        IRRF = 0
    print('{:2f}'.format(IRRF))
elif 2400 < salario_bruto <= 2743.25:
    IRRF = (salario_bruto - desconto_dependente - 2400 * 0.11) * 0.15 - 205.92
    if IRRF < 0:
        IRRF = 0
    print('{:2f}'.format(IRRF))
elif 2743.25 < salario_bruto:
    IRRF = (salario_bruto - desconto_dependente - 2400 * 0.11) * 0.275 - 548.82
    if IRRF < 0:
        IRRF = 0
    print('{:2f}'.format(IRRF))
else:
    print(0)
