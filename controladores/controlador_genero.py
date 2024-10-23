from bd import obtener_conexion

def obtener_generos():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    generos = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM genero")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                genero_dict = dict(zip(column_names, row))
                generos.append(genero_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return generos
