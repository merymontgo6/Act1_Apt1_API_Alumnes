from fastapi import FastAPI, HTTPException
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

@app.get("/")
def read_root():
    return {"Alumnes API"} 

# Retorna una llista json amb tota la informació d’alumnes
@app.get("/alumnes/list", response_model=List[dict])
def read_alumnes():
    return alumnes.alumnes_schema(db_alumnat.read())

# Retorna un objecte json amb la informació d’un alumne en concret
@app.get("/alumnes/show/{id}", response_model=dict)
def show_alumne(id: int):
    alumne = db_alumnat.read_id(id)
    if alumne is None:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return alumnes.alumne_schema(alumne)

# Permet afegir un nou alumne a la base de dades
@app.post("/alumne/add")
async def add_alumne(data: alumne):
    # comprova q si existeix l'aula
    if not db_alumnat.check_aula_existeix(data.IdAula):
        raise HTTPException(status_code=400, detail="IdAula no existent")

    # si l'aula existeix llavors afegeix l'alumne
    l_alumne_id = db_alumnat.create(data.nomAlumne, data.IdAula, data.cicle, data.curs, data.grup)

    return {
        "msg": "S’ha afegit correctament",
        "idAlumne": l_alumne_id,
        "NomAlumne": data.nomAlumne
    }

# modificar el camp d’un alumne
@app.put("/alumne/update/{id}")
async def update_alumne(id: int, data: alumne):

    if not db_alumnat.check_aula_existeix(data.IdAula):
        raise HTTPException(status_code=400, detail="IdAula no existent")
    # si no hi troba no es pot modificar l'alumne
    update_records = db_alumnat.update_alumnat(data.nomAlumne, data.IdAula, data.cicle, data.curs, data.grup)
    
    if update_records == 0:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    return {
        "msg": "S’ha actualitzat correctament"
    }

# @app.put("/update_alumne/{id}")
# def update_alumne(nomAlumne: str, cicle: str, curs: str, grup: str):
#     updated_records = db_alumnat.update_alumnat(nomAlumne, cicle, curs, grup)
#     if updated_records == 0:
#         raise HTTPException(status_code=404, detail="Alumne no trobat")

# Permet eliminar un alumne de la BBDD per id
@app.delete("/alumne/delete/{id}")
async def delete_alumne(id: int):
    deleted_records = db_alumnat.delete_alumne(id)
    
    if deleted_records == 0:
        raise HTTPException(status_code=404, detail="Alumne no trobat")
    
    # Retorna un objecte json amb el missatge “S’ha esborrat correctament”
    return {
        "msg": "S’ha esborrat correctament"
    }

