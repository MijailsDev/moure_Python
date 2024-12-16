### Sets ###
'''
tiene de base un array
un SET no es una estructura ordenada
un SET no admite repetidos
'''
# declaracion de sets
my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))   # esto nos dice que inicialmente es un diccionario

my_other_set = {"Brais","Moure", 35}
print(type(my_other_set))   # dice que ya no es diccionario, ahora es SETs

print(len(my_other_set)) # cunta los elementos del SETS
my_other_set.add("MoureDev")    # agrega el dato "MoureDev" en posiciones aleatorias
my_other_set.add("MoureDev")    # no permite valores repetidos

print(my_other_set)

