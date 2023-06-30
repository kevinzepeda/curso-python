from fastapi import FastAPI
from db import insertarUsuario
from typing import Dict, List

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello Curso de Programacion"}


@app.get("/curso-python")
def participantes():
    return {"participantes": [
        "Fernado",
        "Kaled",
        "Armando",
        "Giovanni",
        "Leo"
    ]}

@app.post("/usuario-crear")
def crear(usuario: Dict):
    return insertarUsuario(usuario)

