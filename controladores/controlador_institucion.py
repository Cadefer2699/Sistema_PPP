from bd import obtener_conexion

def obtener_instituciones():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    instituciones = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM institucion ORDER BY razonSocial")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                institucion_dict = dict(zip(column_names, row))
                instituciones.append(institucion_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return instituciones

def obtener_jefe(ruc):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    instituciones = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT p.apellidos, p.nombre FROM persona p INNER JOIN institucion i ON p.idPersona = i.idPersona where i.numdoc = %s", (ruc,))
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                institucion_dict = dict(zip(column_names, row))
                instituciones.append(institucion_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return instituciones
