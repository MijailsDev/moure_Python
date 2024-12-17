### EXCEPTION MANDLING ###
# El manejo de errores

numberOne = 5
numberTwo = 1

numberTwo = "1"

# try except
try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una exception
    print("Se ha producido un error(try1)")

