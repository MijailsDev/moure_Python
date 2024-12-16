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

print(my_dict.items())  # muestra todos loas datos del diccionario
print(my_dict.keys())   # muestra solo las claves en un formato lista
print(my_dict.values()) # muestra solo los valores en un formato list

my_new_dict = dict.fromkeys(my_dict)    # creamos un diccionario sin valores, que va a reaprovechar todas las claves existentea
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,"Moure")    # creamos un diccionario con todos sus valores igual  a  = "Moure"
print(my_new_dict)                              ; print("-------------")

print(list(my_new_dict))
print(tuple(my_new_dict))
print(set(my_new_dict))