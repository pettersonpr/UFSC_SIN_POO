'''frase = input()

palavras = frase.split()

palavras_decodificadas = []
for palavra in palavras:
    palavras_decodificadas.append(palavra[1::2])

print(' '.join(palavras_decodificadas))
'''

'''
decodifica = [palavra[1::2] for palavra in input().split()]
print(' '.join(decodifica))'''

print(' '.join([palavra[1::2] for palavra in input().split()]))