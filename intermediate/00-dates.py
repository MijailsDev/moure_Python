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
year_2023 = datetime(2025, 1, 1)    # para el año se necesita minimo los tres datos : año mes dia

print_date(year_2023)
 

# Import time
from datetime import time

current_time = time(21, 6, 0)   # la variable current_time significa hora actual

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


# Import date
from datetime import date

current_date = date.today()   # curren_date : fecha actual

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 10 ,6)

print(current_date.year)
print(current_date.month)
print(current_date.day)



# Operaciones con fechas
current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)


diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)


# Import timedelta
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)  # 200 dias, 100 segundos, 100 microsegundos, semanas = 10
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta) # resta
print(end_timedelta + start_timedelta) # suma

