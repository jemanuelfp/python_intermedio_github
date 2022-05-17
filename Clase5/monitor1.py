# ejemplo de paquetes  de uso python
# psutil
#https://psutil.readthedocs.io/en/latest/

import psutil
import os

#nucleos del cpu
cpu_nucleos = psutil.cpu_count()

cpu_frecuencia = psutil.cpu_freq()

#Memoria
memoria_virtual = psutil.virtual_memory()

disco_uso = psutil.disk_usage('/')

os.system('clear')

print("=" * 50 )
print("informacion del sistema")
print("Nucleos del CPU => ", cpu_nucleos)
print("Frecuencia del CPU => ", cpu_frecuencia)

print("Memoria virtual => " , memoria_virtual)

print("=" * 50)


print("Uso de disco => " , disco_uso)

print("=" * 50)

