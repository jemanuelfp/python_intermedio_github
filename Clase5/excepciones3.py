# Actividad excepciones
# Replicar el comportamiento de creacion de carpetas con windows

import os

# al crear un directorio si ya existe agregarle entre parantesis el consecutivo
# carpeta
# carpeta(1)
# carpeta(2)

#contenido = os.listdir("D:/200.- Python/python_intermedio_github")

#print(contenido)


def crear_carpetas(nombre_de_la_carpeta, consecutivo = 0):
    try:
        if consecutivo < 1:
            os.mkdir(nombre_de_la_carpeta)
        else:
            os.mkdir(nombre_de_la_carpeta + f'({consecutivo})')

    except FileExistsError as ex:
        crear_carpetas(nombre_de_la_carpeta, consecutivo + 1)



crear_carpetas("funcion_recursiva")

