# Menejo de excepciones python




try:
    respuesta = int(input("Por favor ingrese un numero"))    
except Exception as ex:
    print("Hubo un error")


print("Est codigo siempre se ejecuta")
