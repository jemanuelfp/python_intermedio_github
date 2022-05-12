import os

def crear_carpetas(sufijo, cantidad):
    """
    Crea n numero de carpetas
    """
    for i in range(cantidad):
        os.mkdir(f"{sufijo}{i}")
        print(f"Creando carpeta {sufijo}{i}")


def elimina_carpetas(sufijo, cantidad):
    """
    Crea n numero de carpetas
    """
    for i in range(cantidad):
        os.rmdir(f"{sufijo}{i}")
        print(f"Eliminando carpeta {sufijo}{i}")


