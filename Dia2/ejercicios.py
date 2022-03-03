# Validar si un numero (ingresos de una persona) ingresado por teclado es :
# * mayor a 500: indicar que no recibe el bono yanapay
# * entre 500 y 250: indicar que si recibe el bono
# * es menor que 250: indicar que recibe el bono y un balon de gas
# RESOLUCION DEL EJERCICIO

salary = int(input('Ingrese sueldo'))

if (salary > 500):
    print('Usted no recibe el bono')
elif (salary >= 250):
    print('Si recibe el Bono')
else:
    print('Usted recibe el bono y un balon de gas')

print('END')