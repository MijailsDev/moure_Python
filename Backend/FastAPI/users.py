from fastapi import FastAPI     


app = FastAPI()

# Inicia el server: uvicorn users:app --reload

@app.get("/users")
async def root():
    return "Hola Users!"