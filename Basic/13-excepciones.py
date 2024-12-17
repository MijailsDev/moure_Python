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

# try except else finally
try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error(try2)")
else:
    # Se ejecuta si no se produce una excepcion
    print("La ejecucion continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecucion continua")


# Exceptiones por tipo
try : 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la informacion de la excepcion
try : 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error: # cual nombre ejemplo: e
    print(error)
except Exception as exceptionError: # ponle el nombre que quieras 
    print(exceptionError)