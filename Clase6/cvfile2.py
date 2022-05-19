#manupular archivos csv

import os
import csv

os.system
#with open('console_games.csv','r') as csv_file:   
    #print(csv_file.readline())
    #for line in csv_file.readlines():
    #   print(line)
    #print(type(csv_file.readlines()))
    #print(len(csv_file.readlines()))

      
with open('console_games.csv','r') as csv_file:
    reader =  csv.DictReader(csv_file)

    for row in reader:
        #print(row['Name'], row['Platform'])
        print(f"Plataforma => {row['Name']} año => {row['Platform']}")

        try:
            os.mkdir(row['Platform'])
        except Exception as ex:
            print("Ya estaba la carpeta")
        
        try:
            os.mkdir(row['Platform']+ "/" + row['Year'])
        except Exception as ex:
            print("Ya estaba la carpeta")
        
        #with open(row['Platform']+ "/" + row['Year'] + "/videogames.txt", "a") as archivo:
        with open(f"{row['Platform']}/{row['Year']} + /videogames.txt", "a") as archivo:
            archivo.write(str(row))



# id | Rank | Name | Platform | Year | Genre | Publisher | NA_Sales | EU_Sales | JP_Sales | Other_Sales

# Estructura de directorios

# Plataforma / Year / archivo.txt
# Nintendo/2000/videogames.txt
# en el archivo debe de ir el contenido de esa plataforma y ese año

#esctructura de directorios


