#import saludos

#saludos.saludos()

#saludos.nombre

#from saludos import saludo_nombre

#saludo_nombre("Emma")
#saludo_nombre("Janet")

from saludos import *

#saludos()
#saludo_nombre("Vane")
#saludo_nombre_completo("Carlos", "Lopez")

# ejemplo de alias
#from saludos_miguel import saludos as saludo_1
#from saludos_sarai  import saludos as sadulo_2
#

from carpetas import crear_carpetas, elimina_carpetas

crear_carpetas("pruebas_carpeta",3)

elimina_carpetas("pruebas_carpeta",3)