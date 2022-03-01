#   Operadores de comparación
number1, number2 = 10, 20

#   Igual que
print(number1 == number2)
#   Mayor que | Mayor igual que
print(number1 > number2)
print(number1 >= number2)
#   Menor que | Menor igual que
print(number1 < number2)
print(number1 <= number2)
#   Direferente de
print(number1 != number2)

#   Operadores Logicos
#   compara varias comparaciones
print((10 > 5) and (10 < 20))
print((10 > 5) or (10 < 20))


#   Operadores de Identidad
#   is
#   is not
#   sirve para ver si estan apuntando a la misma posicion de memoria
print('Operadores de Identidad')
verduras = ['papas', 'cebollas']
#   Por defecto la copia de un arreglo hace una copia a la referencia, por lom cual una modificacion en en cualquiera
#   de las dos variables afectara a la otra
verduras2 = verduras
#   el metodo copy genera una copia del contenido de la variable copiada
verduras3 = verduras.copy()
print(id(verduras))
print(id(verduras2))
print(id(verduras3))
print(verduras is verduras2)
print(verduras is verduras3)

#   Si hablamos de variables primitivas (str, int, float, booblean, date), tambien hace la copia a la referencia PERO
#   al modificarse el valor de cualquiera de las variables se genera una copia automaticamente asignando su propio
#   espacio de memoria para la variable
