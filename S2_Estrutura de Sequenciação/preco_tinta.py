area_pintada = int(input("area a ser pintada: "))

litros_necessarios = round((area_pintada * 3.6) / 18, 1)
galoes_necessarios = round(litros_necessarios / 3.6)

valor_galao = galoes_necessarios * 25

if galoes_necessarios < 1:
    galoes_necessarios = 1

print("- área de cobertura: {}".format(area_pintada))
print("- número de galões: {}".format(galoes_necessarios))
print("- valor a ser pago: R$ {:.2f}".format(valor_galao))
