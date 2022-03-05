#   herencia    >   extraccion informacion de una clase padre
#   DRY don´t repeat yoursel (no te repitas a ti mismo)

class User:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = correo

    def greet(self):
        return 'Hola soy {} '.format(self.nombre)


class Alumno(User):
    def __init__(self, nombre, apellido, correo, padres):
        #   super   >   sirve para llamar a los metodos del padre, unicamente sirve para acceder a los
        #   metodos de la clase de la cual estamos heredando
        super().__init__(nombre, apellido, correo)
        self.parents = padres

    def info(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'padres': self.parents,
            'saludar': super().greet()
        }


alumnoGilmar = Alumno('Gilmar', 'Campana Quispe', 'gacampanaq@gmail.com', [
    {
        'nombre': 'Juan',
        'apeliido': 'Campana Cama'
    },
    {
        'nombre': 'Diola',
        'apellido': 'Quispe Cruz'
    }
])
print(alumnoGilmar.info())