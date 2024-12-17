from fastapi import FastAPI     # importarmos fastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI!"