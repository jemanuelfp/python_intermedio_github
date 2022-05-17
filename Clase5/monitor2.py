# pasar todo lo del monitor 1 a un archivo de texto
# crear una carpeta donde se almacenaran los logs 
# crear un archivo con X nombre 
# insertar la informacion recabada en el archivo

import psutil
import os

#nucleos del cpu
cpu_nucleos = psutil.cpu_count()

cpu_frecuencia = psutil.cpu_freq()

#Memoria
memoria_virtual = psutil.virtual_memory()

disco_uso = psutil.disk_usage('/')


#os.mkdir(f"monitor")

with open("monitor/cpu_nucleos.txt", "w") as archivo:
    archivo.write("informacion del sistema\n")
    archivo.write("Nucleos del CPU => " + str(cpu_nucleos) + "\n")
    archivo.write("Frecuencia del CPU => " + str(cpu_frecuencia)+ "\n")
    archivo.write("Disco de uso => " + str(disco_uso) + "\n")
    archivo.write("Memoria virtual => " + str(memoria_virtual) + "\n")

    archivo.close()
    

with open("monitor/cpu_nucleos.txt") as archivo:
    for linea in archivo.readlines():
        print(linea)

