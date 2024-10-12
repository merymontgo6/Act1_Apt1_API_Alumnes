def alumne_schema(film) -> dict:
    return {
        "IdAlumne": film[0],
        "IdAula": film[1],
        "NomAlumne": film[2],
        "Cicle": film[3],
        "Curs": film[4],
        "Grup": film[5],
        "CretedAt": film[6],
        "UpdatedAt": film[7]
    }
def alumnes_schema(alumnes) -> dict:
    return [alumne_schema(alumne) for alumne in alumnes]