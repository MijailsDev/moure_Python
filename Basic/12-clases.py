### CLASES ### 

# declaracion de clases

class MyEmptyPerson:
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname):     # tenemos un constructor de clase
        self.name = name
        self.surname = surname 

my_person = Person("Brais","Moure")

print(f"{my_person.name} {my_person.surname}")