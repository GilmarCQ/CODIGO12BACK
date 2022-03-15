import random
from faker import Faker

fake = Faker()


def generar_alumnos(limite):
    alumnos_indices = []
    indice_alumno = 0
    for persona in range(limite):
        indice_alumno += 1
        alumnos_indices.append({'id_alumno': indice_alumno})
        nombre = fake.first_name()
        apePat = fake.last_name()
        apeMat = fake.last_name()
        correo = fake.ascii_email()
        telefono = fake.bothify(text='9########')
        sql = '''INSERT INTO alumnos (nombres, apellido_paterno, apellido_materno, correo, numero_emergencia) VALUES
                                ('%s', '%s', '%s', '%s', '%s');''' % (nombre, apePat, apeMat, correo, telefono)
        # print(sql)
    return alumnos_indices


def generar_niveles():
    seccion = ['A', 'B', 'C']
    ubicaciones = ['Sotano', 'Primer Piso', 'Segundo Piso', 'Tercer Piso']
    niveles = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto']
    niveles_indice = []
    indice_nivel = 0
    for nivel_index in range(len(niveles)):
        for indice in range(random.randrange(2, 4)):
            indice_nivel += 1
            niveles_indice.append({'id_nivel': indice_nivel, 'grado': nivel_index + 1})
            sql = '''INSERT INTO niveles (nombre, seccion, ubicacion) VALUES ('%s', '%s', '%s');''' \
                  % (niveles[nivel_index], seccion[indice], ubicaciones[random.randrange(0, len(ubicaciones))])
            # print(sql)
    return niveles_indice


def generar_alumno_nivel(totalRegistros):
    periodos = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    niveles_inserts = generar_niveles()
    alumnos_inserts = generar_alumnos(10)
    print(niveles_inserts)
    # print(alumnos_inserts)

    contador_registros = 0

    while True:
        #
        # periodo_insert_in = periodos[random.randrange(0, len(periodos))]
        # nivel_insert = niveles_inserts[random.randrange(0, len(periodos))]
        for alumno in alumnos_inserts:
            num_alumnos = random.randrange(0, 6)
            for indice_insert in range(num_alumnos):


                sql = '''INSERT INTO alumnos_niveles (alumno_id, nivel_id, fecha_cursada) VALUES ('%s', '%s', '%s');''' \
                      % (alumno['id_alumno'], niveles_inserts[indice_insert]['id_nivel'], periodos[indice_insert])
                contador_registros += 1
                # print(sql)

        if contador_registros > totalRegistros:
            break

generar_alumno_nivel(10)
