class Persona:
    fec_nac = '2000-01-01'
    nombre = 'Gilmar Campana'
    soltero = True
    estatura = 1.75
    def greet(self):
        print('Hola como estan')
        self.say_name()
    def say_name(self):
        print('Su nombre es: {}'.format(self.nombre))

persona1 = Persona()
persona2 = Persona()
persona3 = Persona()
#
# persona1.nombre = 'Manucho'
# print(persona1.nombre)
# print(persona2.nombre)
# print(persona3.nombre)
#
# Persona.nombre = 'Jose'
#
# print(persona1.nombre)
# print(persona2.nombre)
# print(persona3.nombre)

persona1.nombre = 'Miguel'

persona1.greet()
persona2.greet()