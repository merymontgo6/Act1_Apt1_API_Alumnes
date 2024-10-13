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

def create(NomAlumne, Cicle, Curs, Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "INSERT INTO alumnat (nom, cicle, curs, grup) VALUES (%s, %s, %s, %s)"
        values = (NomAlumne, Cicle, Curs, Grup)
        cur.execute(query, values)
        conn.commit()
        alumne_id = cur.lastrowid

        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de creació: {e}" }
    
    finally:
        conn.close()
    
    return alumne_id

def update_alumnat(NomAlumne, Cicle, Curs, Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "UPDATE alumnat SET nom=%s, cicle=%s, curs=%s, grup=%s WHERE id=%s"
        values = (NomAlumne, Cicle, Curs, Grup, id)
        cur.execute(query, values)
        conn.commit()
        updated_recs = cur.rowcount
        
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de actualització: {e}" }
    
    finally:
        conn.close()
    
    return updated_recs

def create(NomAlumne, Cicle, Curs, Grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "INSERT INTO alumnat (nom, cicle, curs, grup) VALUES (%s, %s, %s, %s)"
        values = (NomAlumne, Cicle, Curs, Grup)
        cur.execute(query, values)
        conn.commit()
        alumne_id = cur.lastrowid
        
    except Exception as e:
        return {"status": -1, "message": f"Error de creació: {e}" }
    
    finally:
        conn.close()
    
    return alumne_id

def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT * FROM alumnat WHERE IdAlumne = %s"  # Ensure this matches your column name
        value = (id,)
        cur.execute(query, value)

        alumne = cur.fetchone()
        
        if alumne is None:
            return None 

    except Exception as e:
        return {"status": -1, "message": f"Error de lectura: {e}"}
    
    finally:
        conn.close()

    return alumne

def check_aula_exists(id_aula):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT COUNT(*) FROM aula WHERE IdAula = %s"  # Adjust column name accordingly
        value = (id_aula,)
        cur.execute(query, value)

        count = cur.fetchone()[0]
        return count > 0  # Returns True if exists, otherwise False

    except Exception as e:
        return False  # Return False in case of an error

    finally:
        conn.close()
