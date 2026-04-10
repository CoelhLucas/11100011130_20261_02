import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Estudante(BaseModel):
    nome: str
    curso: str
    ativo: bool

# 127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:8000/lucas
@app.get("/lucas")
async def lucas():
    return {"Num aleatorio": random.randint(0, 1000), "Test": True}

@app.post("/estudantes/cadastro")
async def estudante_cadastro(estudante: Estudante):
    return estudante

@app.put("/estudantes/update/{id_estudante}")
async def estudante_update(id_estudante: int):
    return id_estudante > 0

@app.delete("/estudantes/delete/{id_estudante}")
async def estudante_delete(id_estudante: int):
    return id_estudante > 0
