valor_veiculo = float(input())
classe_desconto = input()
procedencia = input()
idade_segurado = int(input())

if procedencia == 'nacional':
    percentual_premio = 0.1
else:
    percentual_premio = 0.15
premio_bruto = valor_veiculo * percentual_premio

if classe_desconto == 'A':
    percentual_classe_desconto = 0.3
elif classe_desconto == 'B':
    percentual_classe_desconto = 0.2
elif classe_desconto == 'C':
    percentual_classe_desconto = 0.1
elif classe_desconto == 'D':
    percentual_classe_desconto = 0.05
else:
    percentual_classe_desconto = 0

desconto_classe = premio_bruto * percentual_classe_desconto

if idade_segurado > 24:
    desconto_idade = premio_bruto * 0.1
else:
    desconto_idade = 0

premio_liquido = round(premio_bruto - desconto_classe - desconto_idade, 2)

print(premio_liquido)
