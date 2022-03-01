# Esto es un comentario y sirve para dar contexto a lo que se hace, se hizo o se hara
# TODO: logica para este controlador
name = 'Gilmar'
age = 29

description = 'Parafforn de Muestra'

parrafoSaltoLinea = """Parrafo Liena 1
Liena 2
Linea 3"""

print('a', 'b', 'c')
print(description)

# variable numerica
year = 2022
print(type(year))

# En Python no se puede crear una variable sin un contenido
# None = null | undefined
speciality = None
print(type(speciality))

# En Python no se hace validacion del tipo de dato primarip, se puede cambiar el tipo de dato a otro
dni = 72690553
dni = 'Peruano'
dni = False
print(type(dni))
# id() => dara la ubicacion de esa variable en relacion  a la memoria del dispositivo
print(id(dni))

month, day = 'December', 7
del(month)
print(month)
