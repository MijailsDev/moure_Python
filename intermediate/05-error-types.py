### Error Types ###

# SyntaxError
#print "Hola comunidad!"     # Descomentar para Error
print("Hola comnunidad!")


# NameError
language = "Spanish"    # Comentar para Erro
print(language)


# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5])     # Descomentar para Error


# ModuleNotFoundError
# import maths    # Descomentar para Error
import math



# AttributeError
# print(math.PI)      # Descomentar para Error
print(math.pi)



# KeyError
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print(my_dict["Edad"])