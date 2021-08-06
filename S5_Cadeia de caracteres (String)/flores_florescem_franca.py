frase = input()
eh_tautograma = 'Y'

while frase != '*':
    letra = ''
    frase = frase.upper()
    frase = frase.split()
    for palavra in frase:
        letra += palavra[0]
    if letra.count(letra[0]) != len(letra):
        eh_tautograma = 'N'
    print(eh_tautograma)
    frase = input()
