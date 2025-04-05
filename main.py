from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message":  "Olá, DevOps!"}

# 127.0.0.1:8000/teste
@app.get("/formativa")
async def funcaoteste():
    return {"formativa": "deu certo"}