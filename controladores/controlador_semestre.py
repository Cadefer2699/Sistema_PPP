from bd import obtener_conexion

def obtener_semestres():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    semestres = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM semestre_academico ORDER BY nombre DESC")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                semestre_dict = dict(zip(column_names, row))
                semestres.append(semestre_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return semestres
