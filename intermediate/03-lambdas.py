### Lambdas ###

"""
        son como funciones, las lambdas van a ser
        funciones anonimas

        una lambda lo puedes almacenar en una variable
""" 

# Declaracion de una lambda
sum_two_values = lambda first_value, second_value: first_value + second_value    # esta funcion suma dos valores

# llamada a lambda
sum_two_values(2, 4)

# manera par mostrar en consola
print(sum_two_values(2, 4))


# Creando otra lambda
multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))



def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value 

print(sum_three_values(5)(2, 4))