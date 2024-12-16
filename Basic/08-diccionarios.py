### DICCIONARIOS ###

# Declaracion de diccionarios (dict)
'''
Una estructura para relacionar datos
podemos tener dentro de un diccionario otro diccionario o lo que sea
'''
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Brais","Apellido":"Moure","Edad":35, 1:"Python"}

my_dict = {
    "Nombre":"Brais",
    "Apellido":"Moure",
    "Edad":35,
    "Lenguajes": {"Python","Swift","Kotlin"},    # como clave tiene un string, pero como valor tine un SET dentro
    1:1.77
    }
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))   # cantidad de elemtos del dict
print(len(my_dict))

print(my_dict["Nombre"])    # imprime el valor de la clave 'Nombre'

my_dict["Nombre"] = "Pedro" # actualizamos la valor de la clave a 'Pedro'
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle MoureDev" # add a diccionario una nueva clave y su valor
print(my_dict)

# Para eliminar
del my_dict["Calle"]
print(my_dict)

print("Moure" in my_dict)   # Estamos buscando por la 'Claves'
print("Nombre" in my_dict)

