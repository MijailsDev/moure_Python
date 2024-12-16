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

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)     # se puede 'sumar' ambas tuplas

print(my_sum_tuple[3:6])    # buscar elementos concretos entree posicion 3 y 6

my_tuple = list(my_tuple)  # convierto mi tupla en una lista
print(type(my_tuple))

print("estado actual:\n",my_tuple) # estado actual mi tupla/lista

my_tuple[4] = "MoureDev"    # reemplazar el datos del indice 4
my_tuple.insert(1, "Azul")  # meter en el indice 1 "Azul" sin afectar al resto
print(my_tuple)


my_tuple = tuple(my_tuple)  # cambiar a tupla : modo seguro, despues de cambios importantes

print(type(my_tuple))  

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple

# print(my_tuple) # NameError: name 'my_tuple' is not defined