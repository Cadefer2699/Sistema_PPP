from bd import obtener_conexion

def obtener_horas_ppp(idEstudiante):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    horas_ppp = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                           SELECT h.hRequeridas FROM persona p
                           LEFT JOIN escuela e ON e.idEscuela = p.idEscuela
                           INNER JOIN horas_ppp h ON e.idHoras = h.idHoras
                           WHERE p.idPersona = %s """, (idEstudiante,))
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                hora_ppp_dict = dict(zip(column_names, row))
                horas_ppp.append(hora_ppp_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return horas_ppp
