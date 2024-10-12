from fastapi import FastAPI,HTTPException
import db_alumnat
import alumnes
from typing import List

from pydantic import BaseModel

app = FastAPI()

class alumne(BaseModel):
    nomAlumne: str
    cicle: str
    curs: str
    grup: str   
    createdAt: int
    updatedAt: int

# retorna llista d'alumnes
@app.get("/")
def read_root():
    return {"Alumnes API"} 

@app.get("/alumnes", response_model=List[dict])
def read_alumnes():
    return alumnes.alumnes_schema(db_alumnat.read())

@app.get("/alumnes/{id}", response_model=alumne)
def read_alumnes_id(id:int):
    if db_alumnat.read_id(id) is not None:
        alumne = alumnes.alumne_schema(db_alumnat.read_id(id))
    else:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumne

@app.post("/create_alumne")
async def create_alumne(data: alumne):
    nomAlumne = data.nomAlumne
    cicle = data.cicle
    curs = data.curs
    grup = data.grup
    l_alumne_id = db_alumnat.create(nomAlumne, cicle, curs, grup)
    return {
        "msg": "we got data succesfully",
        "id film": l_alumne_id,
        "NomAlumne": nomAlumne
    }

@app.put("/update_alumne/{id}")
def update_alumne(nomAlumne: str, cicle: str, curs: str, grup: str):
    updated_records = db_alumnat.update_alumnat(nomAlumne, cicle, curs, grup)
    if updated_records == 0:
        raise HTTPException(status_code=404, detail="Alumne no trobat")

@app.post("/create_alumne")
async def create_alumne(data: alumne):
    nomAlumne = data.nomAlumne
    cicle = data.cicle
    curs = data.curs
    grup = data.grup
    l_alumne_id = db_alumnat.create(nomAlumne, cicle, curs, grup)
    return {
        "msg": "we got data succesfully",
        "id film": l_alumne_id,
        "NomAlumne": nomAlumne
    }