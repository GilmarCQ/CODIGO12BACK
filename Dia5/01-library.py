from camelcase import CamelCase

instanciaCC = CamelCase('mundo')

text = 'Bienvenidos al mundo del backend'

print(instanciaCC.hump(text))
