### Strings ###

my_string = "My String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(len(my_string + " " + my_other_string))

my_new_line_string = "Este es un String \ncon salto de lineal"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)


# Formateo

name, surname, age = "Brais", "Moure", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)


# Division 
language_slice = language[1:3] # 0=P 1=y 2=t 3=h 4=o 5=n
print(language_slice)

language_slice = language[1:]
print(language_slice) 

language_slice = language[-2]
print(language_slice) 


# reversed

reversed_language = language[::-1] # imprime al reves
print(reversed_language)


# Funciones 

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.startswith("Py"))
