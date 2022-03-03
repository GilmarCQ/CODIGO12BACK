# notes = [10, 5, 15, 12, 8, 13]
#
# for note in notes:
#     print(note)
#
# #   range, itera n veces hasta n
# print('Range 01')
# for number in range(4):
#     print(number)
# #   range con 2 parametro, el primero indica el inicio de la iteracion y el segundo el final del mismo
# print('Range 02')
# for number in range(5, 10):
#     print(number)
# #   range con 3 parametro, el primero indica el inicio de la iteracion, el segundo el final del mismo y el
# #   tercero de cuanto en cuanto avanzara
# print('Range 03')
# for number in range(5, 10, 2):
#     print(number)


# notes = [10, 20, 16, 8, 6, 1]
# print(notes[0:3])


products = ['Manzana', 'Pera', 'Tallarin', 'Taza']
search = input('Ingrese producto a buscar')

for product in products:
    if product == search:
        print('Producto encontrado')
        break
else:
    print('No se encontro el producto')
