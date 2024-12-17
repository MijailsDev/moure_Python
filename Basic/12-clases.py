### CLASES ### 

# declaracion de clases

class MyEmptyPerson:
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):     # tenemos un constructor de clase
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} Esta caminado")


my_person = Person("Brais","Moure")
print(my_person.full_name)
my_person.walk()



# --------------------------------------------------------------
### CLASES ### 

# declaracion de clases
print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")

class MyEmptyPerson2:
    pass 

print(MyEmptyPerson2)
print(MyEmptyPerson2())

class Person2:
    def __init__(self, name, surname, alias = "sin alias"):     # tenemos un constructor de clase
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad publica
        self.__name = name  # Propiedad privada
        

    def get_name(self):
        return self.__name
    
    def walk(self):
        print(f"{self.full_name} Esta caminado")



my_person = Person2("Brais","Moure")
print(my_person.full_name)
print("Hola ",my_person.get_name())
my_person.walk()

my_other_person = Person2("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hector de Leon (El loco de los perros)"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)