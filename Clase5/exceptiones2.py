import os

try:
    os.mkdir("carpeta_prueba")
except FileExistsError as ex:
    print("Ya existe el  directorio, intenta con otro nombre")
except FileNotFoundError as ex:
    print("No se encuentra el  directorio proporcionado")
except Exception as ex:
    print("oops ocurrio un error")

print("fin del script")




