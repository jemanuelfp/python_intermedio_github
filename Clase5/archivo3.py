#Ejemplo de lectura de archivos
with open("text2.txt") as archivo:
    print(archivo.read())


with open("texto.txt") as archivo:
    print(archivo.readline())
    print(archivo.readline())

with open("carpetas.txt") as archivo:
    for linea in archivo.readlines():
        print(linea)

