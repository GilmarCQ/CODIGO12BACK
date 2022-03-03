#   IF - ELSE
#   python no hace uso de llaves, lo que maneja es la identacion que tiene que estar al mismo nivel
edad = int(input('Ingresa tu edad '))

if (edad > 18):
    print('La persona es mayor de edad')
#   ELIF se usa para agregar una condicional si fallo el IF anterior
elif(edad > 15):
    print('Puedes ingresar a preparatoria')
#   el else es opcional
else:
    print('Eres menor de edad')

print('Finalizacion dekl programa')