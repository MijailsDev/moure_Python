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
    