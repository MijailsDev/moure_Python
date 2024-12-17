
FastAPI  > nos proporciona nuestro propio servidor llamado "uvicorn"

# instalamos fastAPI con todas sus dependencias
pip install "fastapi[all]"

# Primeros pasos luego de instalar fast API
https://fastapi.tiangolo.com/tutorial/first-steps/


# levantamos el servidor
cd Backend/FastAPI
uvicorn main:app --reload 

## Documentacion de FastAPI en tu servidor

# Documentacion con Swagger 
http://127.0.0.1:8000/docs

# Documentacion con Redocly
http://127.0.0.1:8000/redoc

# Como detener tu Servidor
Ctrl + C

