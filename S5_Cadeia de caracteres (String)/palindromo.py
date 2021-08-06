frase = input()

frase_limpa = '' # armazena apenas as letras; os demais caracteres são descartados
for caracter in frase.upper():     # percorre a frase caracter a caracter, já toda em letras minúsculas
    if caracter.isalpha():         # se o caracter for uma letra, concatena na frase limpa
        frase_limpa += caracter

print(frase_limpa == frase_limpa[::-1]) # compara a frase com ela invertida para ver se são iguais