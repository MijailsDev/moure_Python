### MODULES ###
# nuestro ficheros que hemos creado se van a comportar como modulos
# si tenumos acceso a esos modulos, podemos trabajar con el codigo 
# que tiene esos ficheros

import my_module 

my_module.sumValue(100,200,300)
my_module.printValue("Hola Python")


from my_module import printValue, sumValue

sumValue(10,20,50)
printValue("Hola C++")

