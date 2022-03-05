class Producto:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        #   privado, cuando se define el atributo con '__', se esta indicando que esta sera de caracter privado;
        #   no sera posible que accedan a el desde fuera de la clase (la clase si puede acceder a ella desde la misma)
        self.__gain = self.price * 0.3

    def show_info(self):
        return {
            'name': self.name,
            'price': self.price,
            'gain': self.__gain,
            # {:.3f}    >   convierte este valor en un string y lo formateara a 3 decimales, este redondea el numero
            'igv': '{:.3f}'.format(self.__calculate_igv())
        }
    def increment_gain(self):
        self.__gain = self.__gain * 1.10

    def __calculate_igv(self):
        return self.price * 0.18


cepillo = Producto('Cepillo Dental', 3.80)

#   attributo publico, puede ser accedido desde la clase y la instancia si problemas
#   cepillo.name

#   atributo privado
#   cepillo.__gain

print(cepillo.show_info())
cepillo.increment_gain()
print(cepillo.show_info())
