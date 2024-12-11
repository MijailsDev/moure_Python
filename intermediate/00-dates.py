### Datos ###

from datetime import datetime

now = datetime.now()    # inicializamos un objeto y lo almacenanos en la variable now

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)


# crear una nueva fecha para el nuevo año
year_2023 = datetime(2023, 1, 1)    # para el año se necesita minimo los tres datos : año mes dia

print_date(year_2023)
 
