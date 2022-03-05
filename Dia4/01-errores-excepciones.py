#   un error es una mala ejecucion del codigo que hara que mi prouecto o script deje de funcionar
#   local()['__builtins__'] > retornara el diccionario de locals(), con todos los errores dentro de python y
#   sus atributos
#   dir > permite listar los atributos como string para poder leerlos
#   locals() > devuleve todas las variables disponibles que tenemos en python en este scope


# print(dir(locals()['__builtins__']))


# try:
#     value = int(input('Ingrese un numero'))
#     print(value)
# except ValueError:
#     #   entrara a este except cuando el error sea de tipo ValueError (error de conversion de un str a un int)
#     print('Error al convertir un string en un entero')
# except Exception as error:
#     print(error.args)
#     #   capturamos el error impidiendo que el programa deje de funcionar
#     print('Ops algo salio mal nuevamente')
# #   se puede tener multiples except en un try, pero solo se executara uno de ellos
# print('Todo finalizo correctamente')
#
# while True:
#     try:
#         num = int(input('Ingrese numero'))
#         break
#     except:
#         print('Valor incorrecto, debe ingresar un numero')
#
# print(num)


try:
    res = 1 / 1
    prod = None
    if prod is None:
        raise Exception('El producto no existe en la BD')
except:
    print('Hubo un error')
else:
    print('Yo me ejecuto cuando no se lanza errores. Funcionamiento sin errores')
finally:
    print('Yo me muuestro estando bien o mal')
