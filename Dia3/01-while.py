#   mientras que
number = 0
while number < 10:
    #   pass > sirve para indicar dentro de un bloque de codigo que aun no hemos definido la logica
    #   , haciendo que no de error
    number += 1
    break
else:
    print('El while termino correctamente')

numbers = [1, 5, 16, 28, 234, 67, 29]

countPars = 0
countImpars = 0
for number in numbers:
    if number % 2 == 0:
        countPars += 1
    else:
        countImpars += 1
print('Hay ', countPars, ' pares')
print('Hay ', countImpars, ' impares')
