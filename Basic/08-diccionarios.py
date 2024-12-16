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

