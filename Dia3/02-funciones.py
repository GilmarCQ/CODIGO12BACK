#   funciones
#   almacena un bloque de codigo con su comportamiento y solamente se ejecutara cuando esta sea invocada

def suma(a, b):
    '''Funcion que recibe dos valores y devuleve la suma de ambas'''
    print('La sumatoria es ', format(a + b))


suma(5, 4)

print(suma.__doc__)

users = []


def registrar(nombre, email, telefono):
    '''Funciones que registra un usuario y lo guarda en una lista'''
    users.append({
        'nombre': nombre,
        'email': email,
        'telefono': telefono
    })
    return {
               'message': 'Usuario registrado exitosamente',
               'usuario': users[0]
           }, 1, True


#   si una funciona retorna mas de un valor (retorna una tupla) entonces podemos hacer dos cosas
#   1. si solamente declaramos una variable, ahi se almacenara toda la tupla
#   2. si queremos almacenar cada valor de la tupla en una variable podemos hacer una destructuracion de esa tupla
#   declarando el mismo numero de variables que el numero de contenidos en la tupla

resultado, numero, booleano = registrar('Gilmar Campana Quispe', 'gacampanaq@gmail.com', '959424271')
print(resultado)
print(numero)
print(booleano)

products = []


def registrar_productos(
        nombre,
        precio,
        estado=True,
        almacen='Almacen de Cercado'):
    products.append({
        'nombre': nombre,
        'precio': precio,
        'estado': estado,
        'almacen': almacen
    })


registrar_productos('Tomates', 4.50)
registrar_productos('Apio', 1.40, True)
registrar_productos('Cebolla', 4.30, True, 'Almacen nuevo mercado')
registrar_productos(almacen='Almacen de la costa', nombre='Pescao', precio=2.5)
print(products)


#   *args, permite recibir un numero indeterminado de valores como parametros; sin tener en cuenta el tipo de dato
def alumns(clase, *args):
    print('la clase es ', clase)
    print(args)
    # if len(args) and args[0] is not None:
    #     print('Si hay el valor del puerto')


alumns('gilmar', 'jose', 'pablo', 'eduardo')
alumns('frontend', 'roxana', 'luis', 'yoshua', 'jean carlo')
alumns('juanito', True, 15.2)
alumns('argumento solo')


#   kwargs > keyword argument
#   se usa para recibir un numero ilimitado de argumentos con su nombre de parametro y su valor, estos se
#   almacenan en un diccionario
def ingresarProducto(**kwargs):
    if (kwargs.get('nombre')):
        print('El usuario quiere agregar un producto con nombre')
    if (kwargs.get('cantidad')):
        print('El usuario quiere agregar un producto con cantidad')


ingresarProducto(nombre='manzana', cantidad=2.4, estado=True, pais_procedencia='Peru')
ingresarProducto(nombre='papa')


#   recursividad
#   reutilización de la funcion dentro de la misma funcion
def saludar_n_veces(limite):
    if (limite == 0):
        return 'Llegue al limite'

    print('Saludo', limite)
    return saludar_n_veces(limite - 1)


resultado = saludar_n_veces(10)
print(resultado)


def factorial(numero):
    if (numero == 1):
        return 1
    return factorial(numero - 1) * numero


res = factorial(4)
print(res)

#   Operadores Ternarios

namePerson = 'Maria'
originPerson = 'Arequipa'


def duda(nombre_persona, origin_person):
    if nombre_persona == 'Maria' and origin_person == 'Arequipa':
        return 'Me caso'
    else:
        return 'Next'


res01 = duda('Maria', 'Lima')
res02 = 'Me caso' if namePerson == 'Maria' and originPerson == 'Arequipa' else 'Next'

print(res01)
print(res02)

#   Funciones Lambda

cuadrado = lambda numero: numero ** 2
sacar_igv = lambda precio: precio * 0.18
division = lambda n1, n2: n1 / n2

rpta = cuadrado(8)
print('Repusta Cuadrado', rpta)
igv = sacar_igv(100)
print('IGV', igv)
div = division(100, 20)
print('Division', div)



