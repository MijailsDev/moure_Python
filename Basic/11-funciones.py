### FUNCTIONS ###

# declaracion de  funciones

def my_function ():
    print("Esto es una funcion")

my_function()
my_function()
my_function()
 
# declaracion de funciones con parametros 
def sum_two_values (first_number, second_number):
    print(first_number + second_number)

sum_two_values(5,7)
sum_two_values(53,27)
sum_two_values("5","7")
sum_two_values(1.4,5.2)

# Nota Importante : parametros y argumentos son iguales

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum
'''
# no recomendable 
my_result = sum_two_values(1.4,5.2)
print(my_result)
'''
my_result = sum_two_values_with_return(10,5)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")

# nombre es Brais y apellido es Moure
print_name(surname = "Moure",name = "Brais") # reordenar el orden del 

def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Brais", "Moure")

