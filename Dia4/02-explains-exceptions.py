productId = input('Ingrese el id del producto')

try:
    if productId == '10':
        raise Exception('El producto no se encontro en la base de datos')
except Exception as e:
    print('Algo salio mal')
    print('Error: ', e)
else:
    print('El producto encontrado es...')
finally:
    print(
        {'message': 'Resultadao final'})
