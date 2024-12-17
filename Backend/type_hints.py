### Type Hints ###

my_string_variable = "My String variable"
print(my_string_variable)
print(type(my_string_variable))

my_string_variable = 5
print(my_string_variable)
print(type(my_string_variable))


my_typed_variable = str: "My typed String variable"     # declaramos que esta variable sea de tipo string
print(my_typed_variable)
print(type(my_string_variable))


my_typed_variable = 5   # aunque hemos especificadode tipo string no hace efecto, porque es tipado debil
print(my_typed_variable)
print(type(my_string_variable))