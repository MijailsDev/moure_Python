from fastapi import FastAPI     
from pydantic import BaseModel      #Pydantic es una librería de Python para validar y gestionar datos de forma sencilla, usando modelos basados en tipado estático para garantizar que los datos cumplen con las reglas definidas.

app = FastAPI()

# Inicia el server: uvicorn users:app --reload

@app.get("/users")
async def root():
    return [{"name": "Brais", "surname": "moure", "url": "https://moure.dev"},
            {"name": "Moure", "surname": "Dev", "url": "https://mouredev.com"},
            {"name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com"}]