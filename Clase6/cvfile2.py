#manupular archivos csv

import os
import csv
import time

os.system
#with open('console_games.csv','r') as csv_file:   
    #print(csv_file.readline())
    #for line in csv_file.readlines():
    #   print(line)
    #print(type(csv_file.readlines()))
    #print(len(csv_file.readlines()))

start = time.time()
ruta = "D:\\200.- Python\\python_intermedio_github\\Clase6\\practica\\";  
with open('console_games.csv','r') as csv_file:
    reader =  csv.DictReader(csv_file)


    for row in reader:
        #print(row['Name'], row['Platform'])
        print(f"Plataforma => {row['Name']} año => {row['Platform']}")

        #Ejemplo manuel
        #try:
        #    os.mkdir(row['Platform'])
        #except Exception as ex:
        #    print("Ya estaba la carpeta")
        #
        #try:
        #    os.mkdir(row['Platform']+ "/" + row['Year'])
        #except Exception as ex:
        #    print("Ya estaba la carpeta")
        #
        ##with open(row['Platform']+ "/" + row['Year'] + "/videogames.txt", "a") as archivo:
        #with open(f"{row['Platform']}/{row['Year']} + /videogames.txt", "a") as archivo:
        #    archivo.write(str(row))

        try:
            if(row['Platform']):
                os.makedirs(f"{ruta}{row['Platform']}\\{row['Year']}")
        except FileExistsError as ex:
            pass
        

        if row['Platform']:
            ruta_archivo = f"{ruta}{row['Platform']}\\{row['Year']}\\archivo.txt"
            cadena = ''

            for key, value in row.items():
                cadena += value + ","

            cadena += "\n"

            with open(ruta_archivo, 'a') as archivo:
                archivo.write(cadena)

end = time.time()
print(end - start)
# id | Rank | Name | Platform | Year | Genre | Publisher | NA_Sales | EU_Sales | JP_Sales | Other_Sales

# Estructura de directorios

# Plataforma / Year / archivo.txt
# Nintendo/2000/videogames.txt
# en el archivo debe de ir el contenido de esa plataforma y ese año

#esctructura de directorios


