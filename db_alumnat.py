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
def update_alumnat(IdAlumne, NomAlumne, IdAula, Cicle, Curs, Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        # SQL query per actualitzar l'alumne
        query = """
            UPDATE alumnat
            SET NomAlumne=%s, IdAula=%s, Cicle=%s, Curs=%s, Grup=%s
            WHERE IdAlumne=%s
        """
        values = (NomAlumne, IdAula, Cicle, Curs, Grup, IdAlumne)
        cur.execute(query, values)
        
        # Confirma els canvis
        conn.commit()
        
        # Retorna el nombre de registres actualitzats
        updated_recs = cur.rowcount
    
    except Exception as e:
        # Afegeix log per veure l'error a la base de dades
        print(f"Error de base de dades: {e}")
        return {"status": -1, "message": f"Error d'actualització: {e}"}
    
    finally:
        conn.close()
    
    return updated_recs


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
def read_all_alumnes_aula():
    try:
        conn = db_client()
        cur = conn.cursor()

        # SQL uneix alumnat amb aula
        query = """
        SELECT 
            a.IdAlumne, a.IdAula, a.nomAlumne, a.cicle, a.curs, a.grup, a.CreatedAt, a.UpdatedAt,
            au.DescAula, au.edifici, au.pis
        FROM alumnat a
        JOIN aula au ON a.IdAula = au.IdAula
        """
        
        cur.execute(query)
        alumnes = cur.fetchall()

    except Exception as e:
        return {"status": -1, "message": f"Error de lectura: {e}" }
    
    finally:
        conn.close()

    return alumnes

