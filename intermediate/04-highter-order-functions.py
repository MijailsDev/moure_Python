### Highter Order Functions ###

#       Son ciudados de primera clase (metafora)

def sum_one(value):
    return value + 1


def sum_two_values_and_add_one(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values_and_add_one(5, 2))