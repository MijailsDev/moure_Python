### Python Package Manager ###

#       Es un gestor de paquetes para Python
#       Si queremos utilizar algun modulo que no
#       tenemos descargado entonces debemos de usar esto        

# PIP https://pypi.org

"""
pip --version

pip install pip

pip install --upgrade pip

pip install numpy

pip install pandas

pip list

pip uninstall pandas

pip show numpy

pip install requests

"""

import numpy
 
print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array)

print(numpy_array * 2)



# import pandas

# Consumir una API
import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


# Atithmetics Package 
from mypackage import arithmetics
print(arithmetics.sum_two_values(1, 4))