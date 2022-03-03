#   coleccion -> variable que puede almacenar varios valores

#   Listas
#   ordeenadas y que pueden ser modificadas

list = ['Pedro', 'Luis', 'Dany', 'Cesar', 'Magaly', 'Anahi']

combined = ['Eduardo', 80, False, [1, 2, 3], 15.8]

#   las listas siempre empiezan en la posicion 0
print(list[0])

#   cuando hacemos el uso de valoires negativos en una lista intermitente, python le dara vuelta
print(list[-1])

print(list)

#   pop, eliminar el ultimo elemento de la lista, si desea se puede recuperar para una asignacion del valor
result = list.pop()
print(result)
print(list)

#   append, agrega un elemento a la lista
list.append('Juana')
print(list)

print('Eliminacion de elemento mediante una posicion de la lista')
del list[2]
print(list)

print('Clear -> limpia la lista y la deja como nueva')
list.clear()
print(list)

print('Impresion de elementos por rango, mediante una subseleccion')
#   =1 <3
print(combined[1:3])

#   [:] obtiene una copia de la lista si usar su misma posicion de memoria
x = combined[:]
y = combined
print(id(x))
print(id(y))
print(id(combined))

print(combined[:3])

months_discount = ['enero', 'febrero', 'marzo']
month1 = 'enero'
month2 = 'setiembre'

#   Indica si el valor esta en la lista
print(month1 in months_discount)
print(month2 in months_discount)
print(month2 not in months_discount)

print(combined + months_discount)
print(combined * 3)

#   Tuplas
#   similar a las listas solo que no se pueden modificar
courses = ('backen', 'frontend', True, 1)
print(courses)
print(courses[1])

multiple = (1, 2, 3, [4, 5, 6])
multiple[3][0] = 'Cambiazo'
print(multiple)

list_new = [1, 2, 3]
print(list_new)

print('len, obtiene el tamaños de una lista o tupla')
print(len(list_new))


#   Conjuntos
#   Coleccion de datos DESORDENADA, una vez se accede a las posiciones de sus elementos
seasons = {'Verano', 'Otonio', 'Invierno', 'Primavera'}

#   una vez se crea se asigna una posicion aleatoria, despues ya no se modifica el orden
print(seasons)
print(seasons)


#   Diccionarios
#   coleccion de datos desordenada, accedible mediante una llave definida
person = {
    'name': 'Gilmar',
    'lastName': 'Campana Quispe',
    'email': 'gacampanaq@gmail.com'
}
print(person['lastName'])
#   .keys devuelve las llaves del diccionario
print(person.keys())
#   values devuelve todos los contenidos de el diccionario
print(person.values())
#   values devuelve todos los contenidos de el diccionario con su valor -> llave
print(person.items())
#   GET, realiza la busque del valor de la llave, si existe retorna el valor
print(person.get('lastName', 'No hay no existe'))

#   Si se invoca a una llave al momento de igualar y esta no existe, se crea una nueva llave con el valor indicado
person['edad'] = 28
person['nombre'] = 'Alfredo'
print(person)

#   ELIMINACION de un valor -> llave
person.pop('edad')
print(person)
