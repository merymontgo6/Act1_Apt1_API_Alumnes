from fastapi import FastAPI, HTTPException
import db_alumnat
import alumnes
from typing import List

from pydantic import BaseModel

app = FastAPI()

class alumne(BaseModel):
    idAula: int
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
def create_alumn(alumne: alumne):
    try:
        aula = db_alumnat.readAula(alumne.idAula)
        if aula is None:
            raise HTTPException(status_code=400, detail="Aula no existent")
        print(aula)
        result = db_alumnat.add_alumne(alumne.idAula, alumne.nomAlumne, alumne.cicle, alumne.curs, alumne.grup)
        
        return {"status": "success", "message": "Alumne afegit amb èxit", "IdAlumne": result}
    
    except HTTPException as e:
        # Gestiona HTTPExceptions (per exemple, si no existeix l'aula)
        raise e
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al afegir alumne: {e}")
    
# modificar el camp d’un alumne
@app.put("/alumne/update/{id}")
def update_alumne(id: int, alumne: alumne):
    try:
        print(f"Verificant l'Aula amb idAula: {alumne.idAula}")
        aula = db_alumnat.readAula(alumne.idAula)
        if aula is None:
            raise HTTPException(status_code=400, detail="IdAula no existent")
        # Actualitza l'alumne si es troba
        result = db_alumnat.update_alumne(id, alumne.idAula, alumne.nomAlumne, alumne.cicle, alumne.curs, alumne.grup)
        if result == 0:
            raise HTTPException(status_code=404, detail="Alumne amb id {id} no trobat")
        
        return {"status": "success", "message": "Alumne actualitzat amb èxit", "IdAlumne": id}
    
    except HTTPException as e:
        raise e
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualitzar l'alumne: {e}")

# Permet eliminar un alumne de la BBDD per id
@app.delete("/alumne/delete/{id}")
def delete_alumne(id: int):
    try:
        alumne = db_alumnat.read_id(id)
        if alumne is None:
            raise HTTPException(status_code=404, detail="Alumne amb id {id} no trobat")
        print(alumne)
        result = db_alumnat.delete_alumne(id)
        return {"status": "success", "message": f"Alumne amb id {id} eliminat amb èxit"}
    except HTTPException as e:
        raise e
    
    except Exception as e:
        print(f"Error al eliminar alumne: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error al eliminar alumne: {str(e)}")

# Retorna una llista json amb tota la informació d’alumne
@app.get("/alumne/listAll", response_model=List[dict])
def read_all_alumnes():
    alumnes = db_alumnat.fetch_all_alumnes()  # Crida al mètode per recuperar alumnes

    if not alumnes or (isinstance(alumnes, dict) and 'status' in alumnes):  # Comprova si hi ha un error
        raise HTTPException(status_code=404, detail="No hi ha alumnes enregistrats")
    
    return alumnes