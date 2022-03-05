class Animal:
    def __init__(self, name, sex, number_patas):
        self.name = name
        self.sex = sex
        self.number_patas = number_patas

    def description(self):
        return 'Yo soy un {}, soy {}, y tengo {}'.format(
            self.name,
            self.sex,
            self.number_patas
        )

foca = Animal('Foca', 'M', 2)
caballo = Animal('Caballo', 'M', 4)
gato = Animal('Gato', 'F', 4)

print(foca.description())
print(caballo.description())
print(gato.description())