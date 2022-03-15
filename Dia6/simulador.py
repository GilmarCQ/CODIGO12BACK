import random

from faker import Faker

# from faker.providers import internet, person

fake = Faker()


# fake.add_provider([internet, person])

# Para lkas versiones modernas de python, no es necesario importar los provider que sean propios de la libreria
# en caso se use provider de la comunidad si se debe importar los provider y add_provider()

# print('Nombre -> ', fake.name())
# print('Apellido Mat -> ', fake.last_name_male())
# print('Apellido Pat -> ', fake.last_name_female())
# print('Correo -> ', fake.ascii_email())
# print('Telefono -> ', fake.phone_number())

def generar_alumnos(limite):
    for persona in range(limite):
        nombre = fake.first_name()
        apePat = fake.last_name()
        apeMat = fake.last_name()
        correo = fake.ascii_email()
        telefono = fake.bothify(text='9########')
        sql = '''INSERT INTO alumnos (nombres, apellido_paterno, apellido_materno, correo, numero_emergencia) VALUES
                                ('%s', '%s', '%s', '%s', '%s');''' % (nombre, apePat, apeMat, correo, telefono)
        print(sql)


def generar_niveles():
    seccion = ['A', 'B', 'C']
    ubicaciones = ['Sotano', 'Primer Piso', 'Segundo Piso', 'Tercer Piso']
    niveles = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto']
    for nivel in niveles:
        for indice in range(random.randrange(2, 4)):
            # print(nivel, seccion[indice], ubicaciones[random.randrange(0, len(ubicaciones))])
            sql = '''INSERT INTO niveles (nombre, seccion, ubicacion) VALUES ('%s', '%s', '%s');''' \
                  % (nivel, seccion[indice], ubicaciones[random.randrange(0, len(ubicaciones))])
            print(sql)

def generar_alumno_nivel(totalAlumnos):
    seccion = ['A', 'B', 'C']
    ubicaciones = ['Sotano', 'Primer Piso', 'Segundo Piso', 'Tercer Piso']
    niveles = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto']
    alumnos = []
    niveles_indice = []
    indice_nivel = 0
    for nivel in niveles:
        for indice in range(random.randrange(2, 4)):
            indice_nivel += 1
            niveles_indice.append({'grado': nivel, 'id_nivel': indice_nivel})
            sql = '''INSERT INTO niveles (nombre, seccion, ubicacion) VALUES ('%s', '%s', '%s');''' \
                  % (nivel, seccion[indice], ubicaciones[random.randrange(0, len(ubicaciones))])
            # print(sql)
    print(niveles_indice)
    for indiceAl in range(1, totalAlumnos + 1 ):
        # print(indiceAl)
        random.randrange(0, 6)

generar_alumno_nivel(5)