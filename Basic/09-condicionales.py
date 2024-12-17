### CONDICIONALES ###
'''
Es la manera de ejecutar flujos de ejecucion
'''
my_condition = False

# como usarlos 
if my_condition:    # es lo mismo que if my_condition == True:
    print("Se ejcuta la condicion del if")

my_condition = 5 * 5

if my_condition == 11:    
    print("Se ejcuta la condicion del segundo if")

elif my_condition > 10 and my_condition < 20:    
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("La ejecucion continua")

my_string = ""

if my_string:   # verifica si tiene contenido o no, si tiene contenido es True
    print("Hola")
else:
    print("Hola2")
