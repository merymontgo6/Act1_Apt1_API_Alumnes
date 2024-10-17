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
async def update_alumne(id: int, data: alumne):
    try:
        print(data)
        # Comprova si l'Aula existeix
        aula = db_alumnat.readAula(data.idAula)
        if aula is None:
            raise HTTPException(status_code=400, detail="IdAula no existent")
        # Actualitza l'alumne si es troba
        update_records = db_alumnat.update_alumnat(id, data.nomAlumne, data.idAula, data.cicle, data.curs, data.grup)
        if update_records == 0:
            raise HTTPException(status_code=404, detail="Alumne no trobat")
        
        return {"msg": "S'ha actualitzat correctament"}
    
    except HTTPException as e:
        # Re-llançar HTTPException si es detecta
        raise e
    
    except Exception as e:
        # Log d'error més detallat
        raise HTTPException(status_code=500, detail=f"Error al servidor: {str(e)}")

    
# @app.put("/update_alumne/{id}")
# def update_alumne(nomAlumne: str, cicle: str, curs: str, grup: str):
#     updated_records = db_alumnat.update_alumnat(nomAlumne, cicle, curs, grup)
#     if updated_records == 0:
#         raise HTTPException(status_code=404, detail="Alumne no trobat")

# Permet eliminar un alumne de la BBDD per id
# @app.delete("/alumne/delete/{id}")
# async def delete_alumne(id: int):
#     deleted_records = db_alumnat.delete_alumne(id)
    
#     if deleted_records == 0:
#         raise HTTPException(status_code=404, detail="Alumne no trobat")
    
#     # Retorna un objecte json amb el missatge “S’ha esborrat correctament”
#     return {
#         "msg": "S’ha esborrat correctament"
#     }

# # Retorna una llista json amb tota la informació d’alumne
# @app.get("/alumne/listAll", response_model=List[dict])
# async def list_all_alumnes():
    
#     alumnes = db_alumnat.read_all_alumnes_aula()

#     if not alumnes:
#         raise HTTPException(status_code=404, detail="No s'han trobat alumnes")

#     return alumnes

