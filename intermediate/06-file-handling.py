### File Handling ###

import os

# .txt File

# Leer, escribir y sobrescribir si ya existe
txt_file = open("intermediate/my-file.txt", "w+")

txt_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python")

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

with open("intermediate/my-file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")



# .json file
import json
 
json_file = open("intermediate/my-file.json", "w+") # crea el fichero .json

json_test = {
    "name":"Brais",
    "surname":"Moure",
    "age":"35",
    "language":["Python", "Swift", "Kotlin"],
    "website":"https://moure.dev"
}

json.dump(json_test, json_file, indent=2)


json_file.close()

with open("intermediate/my-file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("intermediate/my-file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

