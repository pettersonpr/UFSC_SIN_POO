texto = input()
lista_palavras = texto.split()
texto_convertido = ''


def converte_palavra(palavra):
    palavra_convertida = ''
    for i in range(1, len(palavra) + 1, 2):
        palavra_convertida = palavra_convertida + palavra[i]
    return palavra_convertida


for a in lista_palavras:
    texto_convertido = texto_convertido + converte_palavra(a) + ' '

print(texto_convertido.strip())
