# Menejo de excepciones python


try:
    respuesta = int(input("Please enter a number: "))
except ValueError as ex:
    print("Hubo un error de valor => ", ex)
except Exception as ex:
    print("Hubo una excepcion => ", ex)


