### Regular Expressions ###

#       Es un estandar para inspeccioar si una cadena 
#       de texto tiene cosas

import re

# match

my_string = "Esta es la leccion numero 7: llamada leccion Expresiones regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de ficheros"

# trata de encontrar un patron
match = re.match("Esta es la leccion", my_string, re.I)     # encuentra el string solo desde el principio del texto

print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta es la leccion", my_other_string)
#if not(match == None):     # Otra forma de comprobar el None
#if match != None:       # Otra forma de comprobar el None
if  match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])        

#print(re.match("Expresiones regulares", my_string))



# search

search = re.search("leccion", my_string, re.I) # encuentra el string en cualquier parte
print(search)
start, end = search.span()
print(my_string[start:end])



# findall

findall = re.findall("leccion", my_string, re.I) # encuentra todos los string en cualquier parte, y lo almacena en un array
print(findall)


# split 
print(re.split(":", my_string)) # busca el patron a buscar y llos divide en dos



# sub
print(re.sub("leccion|leccion", "LECCION", my_string))      # Reemplaza el string leccion por LECCION
print(re.sub("Expresiones regulares", "RegEx", my_string))  # Reemplaza el string leccion por LECCION