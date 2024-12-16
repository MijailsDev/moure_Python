### Tuples ###
'''
Las tuplas son valores constantes, son inmutables
'''

# Declaracion de tuplas
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35,2.77,"Brais","Moure","Brais")
my_other_tuple = (35, 60,30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0]) # imprime el elemento en la posicion 0

# imprime el ultimo elemento
# comienza del ultimo hacia el principio
print(my_tuple[-1]) 
print(my_tuple[-2]) 
print(my_tuple[-3]) 

print(my_tuple.count("Brais"))  # cuenta cuanto "Brais" hay en la tupla
print(my_tuple.index("Moure"))  # en que indice esta "Moure" 

# my_tuple[1] = 1.80    # error, nose pude modificar el contenido 
# print(my_tuple)

