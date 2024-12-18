from fastapi import FastAPI     
from pydantic import BaseModel      #Pydantic es una librería de Python para validar y gestionar datos de forma sencilla, usando modelos basados en tipado estático para garantizar que los datos cumplen con las reglas definidas.

app = FastAPI()

# Inicia el server: uvicorn users:app --reload


# Entidad User

class User(BaseModel):      # BaseModel nos da la capacidad de crear un entidad
    id: int
    name: str 
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),     # Estas son instancias de la clase user
              User(id=2, name="Moure", surname="Dev", url="https://mouredev.com", age=35),    # Estas son instancias de la clase user
              User(id=3, name="Haakon", surname="Dahlberg", url="https://haakon.com", age=33)]    # Estas son instancias de la clase user


@app.get("/usersjson")
async def usersjson():
    return [{"name": "Brais", "surname": "Moure", "url": "https://moure.dev", "age": 35},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com", "age": 35},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age": 33}]


@app.get("/users")
async def users():
    return users_list   # Retornamos nuestra lista con la Clase User con todos sus valores


@app.get("/user/{id}")  # parametros
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    return list(users)[0]