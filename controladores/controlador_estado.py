from bd import obtener_conexion

def obtener_estados():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    estados = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM estado")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                estado_dict = dict(zip(column_names, row))
                estados.append(estado_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return estados
