### Highter Order Functions ###

#       Son ciudados de primera clase (metafora)


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))



### Closures ###

def sum_ten(original_value):  # Define una función llamada sum_ten que toma un parámetro original_value.
    def add(value):  # Define una función interna llamada add que toma un parámetro value.
        return value + 10 + original_value  # La función add devuelve el resultado de sumar value, 10 y original_value.
    return add  # La función sum_ten devuelve la función add.

add_closure = sum_ten(1)  # Llama a sum_ten con el argumento 1 y asigna la función resultante a add_closure.
print(add_closure(5))  # Llama a add_closure con el argumento 5, lo que resulta en 5 + 10 + 1 = 16, e imprime 16.
print((sum_ten(5))(1))  # Llama a sum_ten con el argumento 5, lo que devuelve una función. Luego, llama a esa función con el argumento 1, lo que resulta en 1 + 10 + 5 = 16, e imprime 16.




### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map


def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce


def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))
