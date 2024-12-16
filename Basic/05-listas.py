### Lists ### 
# un arreglo es diferente lista#
# nuestra liste sirve para agregar elemetos, como una caja(0,1,2,3,4,5,6,...)
# es una forma de agrupar datos  
#podemos hacer operaciones propias de las listas: ordenaciones, reverseds, injeccion de elemntos

my_list = list()        # declaracion de una lista
my_other_list = []      # declaracion de una lista

print(len(my_list)) # la longitud es 0 es vacio

my_list = [35, 24, 62, 52, 30, 30, 17] # un array de elementos 

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]  

print(type(my_list))        # imprimimos el tipo de dato
print(type(my_other_list))

print(my_other_list[0])     # imprime el primero elemento
print(my_other_list[1])     # imprime la el segundo elemento
print(my_other_list[-1])    # imprime el ultimo elemento
print(my_other_list[-2])    # imprime el penultimo elemento
print(my_other_list[-3])    # imprime el antepenultimo elemento 
print(my_other_list.count("Brais"))     # cuantos "Brais" hay?
print(my_list.count(30))                # cuantos <30> hay?

age, heigth, name, surname = my_other_list  # igualacion de datos a la nueva variables
print(age)
print(heigth)
print(name)
print(surname)

# nos complicamos un poquito:
print("Complicadornos: ")
name, heigth, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)
print(heigth)
print(age)
print(surname)
# end de complicaciones


print(my_list + my_other_list)  # concatenar 2 listas

my_other_list.append("MoureDev")    # agrega un nuevo elemento al final de la lista
print(my_other_list)

'''
INSERT agrega el la posicion 1 , el dato "Azul", y los que 
estaban en el lugar se desplazan a las siguientes posiciones 
'''
print("INSERT..................................................")
my_other_list.insert(1, "Rojo") 
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

