

def camelCase(texto):
    cadenas = texto.split(' ')
    frase = ''
    for cadena in cadenas:
        palabra = cadena[0].upper() + cadena[1:len(cadena)]
        frase = frase + palabra + ' '
    return frase

print(camelCase('arriba peru , pais de la buena comida'))