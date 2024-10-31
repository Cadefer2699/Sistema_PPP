from bd import obtener_conexion

def obtener_tipo_practicas():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    tipo_practicas = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM tipo_practicas")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                tipo_practica_dict = dict(zip(column_names, row))
                tipo_practicas.append(tipo_practica_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return tipo_practicas
