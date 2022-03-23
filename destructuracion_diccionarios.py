def sum(a, b):
    return a + b


print(sum(4, 8))
print(sum(a=4, b=8))

parametros = {
    'a': 7,
    'b': 9
}
# al momento de nosotros querer pasar los parametros pero en forma de un diccionario se puede hacer la destructuracion
# usando los ** antes del diccionario
print(sum(**parametros))
