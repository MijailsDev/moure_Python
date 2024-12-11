### List Comprehension ###

# formas de crear una lista

# primera forma
my_oroginal_list = [1, 2, 3, 4, 5, 6, 7]
print(my_oroginal_list)

# Segunda forma
my_range = range(8)
print(list(my_range))   # esta forma inicializamos un lista con todos los numeros del rango

# Tercera forma
my_list = [i for i in range(8)]   # de esta forma tambien creamos una lista con elementos del 0 - 8
print(my_list)


my_list = [i + 1 for i in range(8)]   # a cada numero del rango se suma + 1
print(my_list)

my_list = [i * 2 for i in range(8)]   # a cada numero del rango se multiplica * 2
print(my_list)

my_list = [i * i for i in range(8)]   
print(my_list)

# Cuarta forma
def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]   # en la funcion sum_five le pasamos el parametro de i, osea los numeros del rango
print(my_list)