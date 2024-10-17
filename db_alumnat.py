from client import db_client

def read():

    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("SELECT * FROM alumnat")
        alumnes = cur.fetchall()

    except Exception as e:
        return {"status": -1, "message": f"Error de lectura: {e}" }
    
    finally:
        conn.close()

    return alumnes

# Retorna un alumne segons l'id
def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT * FROM alumnat WHERE IdAlumne= %s"
        value = (id,)
        cur.execute(query, value)

        alumne = cur.fetchone()

    except Exception as e:
        return {"status": -1, "message": f"Error de lectura: {e}" }
    
    finally:
        conn.close()

    return alumne

# creació d'un nou alumne
def add_alumne(IdAula, NomAlumne, Cicle, Curs, Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        
        # SQL query to insert a new alumne into the database
        query = "INSERT INTO alumnat (IdAula, NomAlumne, Cicle, Curs, Grup) VALUES (%s, %s, %s, %s, %s);"
        values = (IdAula, NomAlumne, Cicle, Curs, Grup)
        cur.execute(query, values)
        
        # Commit the changes to the database
        conn.commit()
        
        # Get the last inserted ID
        insert_id = cur.lastrowid
    
    except Exception as e:
        # Log or handle the error and return an appropriate status
        return {"status": -1, "message": f"Error de connexió: {e}"}
    
    finally:
        # Ensure the connection is closed
        conn.close()
    
    return insert_id

def readAula(idAula):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT * FROM alumnat WHERE IdAlumne= %s"
        value = (id,)
        cur.execute(query, value)
        select_aula = cur.fetchone()
    
    except Exception as e:
        # En cas d'error mostrem un missatge
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return select_aula

# modificació d'un alumne
def update_alumne(IdAlumne, IdAula, NomAlumne, Cicle, Curs, Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = """
            UPDATE alumnat
            SET IdAula = %s, NomAlumne = %s, Cicle = %s, Curs = %s, Grup = %s
            WHERE IdAlumne = %s
        """
        values = (IdAula, NomAlumne, Cicle, Curs, Grup, IdAlumne)
        cur.execute(query, values)
        conn.commit()
        updated_recs = cur.rowcount
    
    except Exception as e:
        return {"status": -1, "message": f"Error d'actualització: {e}"}
    
    finally:
        conn.close()
    
    return updated_recs

# eliminar un alumne per id alumnat
def delete_alumne(IdAlumne):
    try:
        conn = db_client()
        cur = conn.cursor()
        print(f"Intentant eliminar alumne amb IdAlumne: {id}")
        query = "DELETE FROM alumnat WHERE IdAlumne = %s"
        values = (IdAlumne,)
        cur.execute(query, values)
        conn.commit()
        deleted_recs = cur.rowcount
    
    except Exception as e:
        print(f"Error de base de dades: {e}")
        return {"status": -1, "message": f"Error al eliminar alumne: {e}"}
    
    finally:
        conn.close()
    
    return deleted_recs

# verificació de l'existència d'una aula per id
def check_aula_exists(idAula):
    try:
        conn = db_client()
        cur = conn.cursor()
        
        # Consulta SQL per verificar si existeix l'aula amb l'id passat per paràmetres       
        query = "select count(*) from aula where idAula = %s"
        cur.execute(query,(idAula,))
        
        result = cur.fetchone()
        
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    
    finally:
        conn.close()
    
    return result[0]>0

# Llegir tots els alumnes amb la informació de l'aula per id
def fetch_all_alumnes():
    try:
        conn = db_client()
        cur = conn.cursor()

        # SQL uneix alumnat amb aula
        query = """
        SELECT 
            a.IdAlumne, a.IdAula, a.NomAlumne, a.Cicle, a.Curs, a.Grup,
            a.CreatedAt, a.UpdatedAt,
            au.DescAula, au.edifici, au.pis
        FROM alumnat a
        JOIN aula au ON a.IdAula = au.IdAula
        """
        
        cur.execute(query)
        alumnes = cur.fetchall()

        # Convertim els resultats a un format de diccionari
        alumnes_list = []
        for alumne in alumnes:
            alumnes_list.append({
                "IdAlumne": alumne[0],
                "IdAula": alumne[1],
                "NomAlumne": alumne[2],
                "Cicle": alumne[3],
                "Curs": alumne[4],
                "Grup": alumne[5],
                "CreatedAt": alumne[6],
                "UpdatedAt": alumne[7],
                "DescAula": alumne[8],
                "Edifici": alumne[9],
                "Pis": alumne[10],
            })


    except Exception as e:
        return {"status": -1, "message": f"Error de lectura: {e}" }
    
    finally:
        conn.close()

    return alumnes_list