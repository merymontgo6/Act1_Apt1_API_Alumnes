from fastapi import FastAPI,HTTPException
import db_alumnat
import alumnes
from typing import List

from pydantic import BaseModel

app = FastAPI()

class alumne(BaseModel):
    nomAlumne: str
    Cicle: str
    Curs: str
    Grup: str   
    CreatedAt: int
    UpdatedAt: int

@app.get("/")
def read_root():
    return {"Films API"} #REVISAR
