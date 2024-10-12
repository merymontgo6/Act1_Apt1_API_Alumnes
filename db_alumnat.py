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
        query = "SELECT * FROM alumnat WHERE id= %s"
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