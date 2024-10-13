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

def check_aula_existeix(id_aula):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "SELECT COUNT(*) FROM aula WHERE IdAula = %s"
        value = (id_aula,)
        cur.execute(query, value)

        count = cur.fetchone()[0]
        return count > 0

    except Exception as e:
        return False 

    finally:
        conn.close()

def read_all_alumnes_with_aula():
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
