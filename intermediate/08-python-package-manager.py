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




"""

import numpy
 
print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))
print(numpy_array)

print(numpy_array * 2)

