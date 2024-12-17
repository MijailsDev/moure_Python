from fastapi import FastAPI     # importarmos fastAPI

# primer hola fastAPI con el servidor
app = FastAPI()

# Peticiones get
@app.get("/")       # va a la raiz del localhost - solo debe de existir una raiz(/)
async def root():
    return "Hola FastAPI!"


@app.get("/url")    # esto va a estar el 127.0.0.1:8000/url
async def url():    # ponemos un nombre distinto a root a la funcion
    return {"url":"https://mouredev.com/python"}


"""
las peticiones GET son las que interpretan el navegador
GET = obtener

POSTMAN = es un cliente para poder pedir peticiones a un API
POSTMAN = para interactuar con un backend

VS code Pluggins -> Thunder Client (alternativa a Postman)
"""


"""
#Peticiones HTTP

    POST > crear datos
    GET > leer datos
    PUT > actualizar datos
    DELETE > borrar datos
    
"""