from fastapi import FastAPI     # importarmos fastAPI

# primer hola fastAPI con el servidor
app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI!"