while True:
    try:
        frase = input().upper().split('-')
        cobol = ('C', 'O', 'B', 'O', 'L')
        resultado = 'GRACE HOPPER'
        for i in range(len(frase)):
            if frase[i][0] != cobol[i] and frase[i][-1] != cobol[i]:
                resultado = 'BUG'
                break
        print(resultado)
    except EOFError:
        break
