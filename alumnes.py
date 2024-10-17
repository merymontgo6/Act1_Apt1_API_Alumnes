def alumne_schema(alumne) -> dict:
    return {
        "IdAlumne": alumne[0],
        "IdAula": alumne[1],
        "NomAlumne": alumne[2],
        "Cicle": alumne[3],
        "Curs": alumne[4],
        "Grup": alumne[5],
        "CretedAt": alumne[6],
        "UpdatedAt": alumne[7]
    }
def alumnes_schema(alumnes) -> dict:
    return [alumne_schema(alumne) for alumne in alumnes]

def aula_schema(aula) -> dict:
    return {
        "IdAula": aula[0],
        "DescAula": aula[1],
        "Edifici": aula[2],
        "Pis": aula[3],
        "CretedAt": aula[4],
        "UpdatedAt": aula[5]
    }
def aules_schema(aules) -> dict:
    return [aula_schema(aula) for aula in aules]