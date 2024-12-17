### LOOPS ###
'''
Ciclos, bucles: es una mecanismo que nos sirve para iterar
'''

# While 

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # es opcional  
    print("Este es del elese")

print("Este es fuera del bucle1")


while my_condition < 20:
    my_condition += 1
    if my_condition == 16:
        print("se detien la ejecucion: break")
        break
    print(my_condition)



# For 

my_list = [35,24,62,52,30,30,17]

for element in my_list:
    print(element)

my_set = {"Brais","Moure", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Brais","Apellido":"Moure","Edad":35,1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El else del bucle for dict ")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue            # esto deja de ejecutar hasta esta linea, y comienza desde el inicio de este bucle :(
    print("Se ejecuta")
else:
    print("El else del bucle for dict ")