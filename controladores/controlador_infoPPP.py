from bd import obtener_conexion

# OPERACIONES CRUD

def obtener_practicas():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    practicas = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    p.idPractica, 
                    e.nombres AS estudiante, 
                    e.apellidos AS apellidos_estudiante,
                    i.razonSocial AS empresa, 
                    p.fechaInicio AS fecha_inicio, 
                    p.fechaFin AS fecha_fin,
                    d.nombres AS docente, 
                    d.apellidos AS apellidos_docente,
                    es.nombre AS carrera
                FROM 
                    PRACTICAS_PREPROFESIONALES p
                JOIN 
                    ESTUDIANTE e ON p.numDocEstudiante = e.numDoc
                JOIN 
                    INSTITUCION i ON p.numDocInstitucion = i.numDoc
                JOIN 
                    DOCENTE d ON p.numDocDocente = d.numDoc
                JOIN 
                    ESCUELA es ON e.idEscuela = es.idEscuela;
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                practica_dict = dict(zip(column_names, row))
                practicas.append(practica_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return practicas

def obtener_practica_por_id(idPractica):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    practica = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    p.idPractica, 
                    e.nombres AS estudiante, 
                    e.apellidos AS apellidos_estudiante,
                    i.razonSocial AS empresa, 
                    p.fechaInicio AS fecha_inicio, 
                    p.fechaFin AS fecha_fin,
                    d.nombres AS docente, 
                    d.apellidos AS apellidos_docente,
                    es.nombre AS carrera
                FROM 
                    PRACTICAS_PREPROFESIONALES p
                JOIN 
                    ESTUDIANTE e ON p.numDocEstudiante = e.numDoc
                JOIN 
                    INSTITUCION i ON p.numDocInstitucion = i.numDoc
                JOIN 
                    DOCENTE d ON p.numDocDocente = d.numDoc
                JOIN 
                    ESCUELA es ON e.idEscuela = es.idEscuela
                WHERE 
                    p.idPractica = %s;
            """, (idPractica,))
            row = cursor.fetchone()

            if row:
                columnas = [desc[0] for desc in cursor.description]
                practica = dict(zip(columnas, row))
            else:
                return {"error": "Práctica no encontrada"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return practica

def agregar_practica(numDocEstudiante, numDocInstitucion, fechaInicio, fechaFin, numDocDocente, idEscuela, idTipoPractica, estado):
    # Validaciones
    if not numDocEstudiante or not numDocInstitucion or not fechaInicio or not fechaFin or not numDocDocente:
        return {"error": "Todos los campos son requeridos."}
    if estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO PRACTICAS_PREPROFESIONALES (numDocEstudiante, numDocInstitucion, fechaInicio, fechaFin, numDocDocente, idEscuela, idTipoPractica, estado) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (numDocEstudiante, numDocInstitucion, fechaInicio, fechaFin, numDocDocente, idEscuela, idTipoPractica, estado))
            conexion.commit()
            return {"mensaje": "Práctica preprofesional agregada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_practica(idPractica, numDocEstudiante, numDocInstitucion, fechaInicio, fechaFin, numDocDocente, idEscuela, idTipoPractica, estado):
    # Validaciones
    if not idPractica or not numDocEstudiante or not numDocInstitucion or not fechaInicio or not fechaFin or not numDocDocente:
        return {"error": "Todos los campos son requeridos."}
    if estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE PRACTICAS_PREPROFESIONALES 
                SET numDocEstudiante = %s, numDocInstitucion = %s, fechaInicio = %s, fechaFin = %s, 
                    numDocDocente = %s, idEscuela = %s, idTipoPractica = %s, estado = %s 
                WHERE idPractica = %s
            """, (numDocEstudiante, numDocInstitucion, fechaInicio, fechaFin, numDocDocente, idEscuela, idTipoPractica, estado, idPractica))
            conexion.commit()
            return {"mensaje": "Práctica preprofesional modificada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def eliminar_practica(idPractica):
    # Validaciones
    if not idPractica:
        return {"error": "El ID de la práctica es requerido."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM PRACTICAS_PREPROFESIONALES WHERE idPractica = %s", (idPractica,))
            conexion.commit()
            return {"mensaje": "Práctica preprofesional eliminada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def dar_de_baja_practica(idPractica):
    # Validaciones
    if not idPractica:
        return {"error": "El ID de la práctica es requerido."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE PRACTICAS_PREPROFESIONALES SET estado = 'I' WHERE idPractica = %s", (idPractica,))
            conexion.commit()
            return {"mensaje": "Práctica preprofesional dada de baja correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def cambiar_estado_practica(idPractica, nuevo_estado):
    # Validaciones
    if not idPractica or not nuevo_estado:
        return {"error": "El ID y el nuevo estado son requeridos."}
    if nuevo_estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE PRACTICAS_PREPROFESIONALES SET estado = %s WHERE idPractica = %s", (nuevo_estado, idPractica))
            conexion.commit()
            return {"mensaje": "Estado de la práctica preprofesional actualizado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

# OTRAS OPERACIONES

def obtener_practicas_activas():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS practicas_activas FROM PRACTICAS_PREPROFESIONALES WHERE estado = 'A'")
            row = cursor.fetchone()

            if row:
                return {"practicas_activas": row[0]}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_practicas_con_estado():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    practicas = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    idPractica, 
                    numDocEstudiante, 
                    numDocInstitucion, 
                    CASE 
                        WHEN estado = 'A' THEN 'Activo' 
                        ELSE 'Inactivo' 
                    END AS estado 
                FROM PRACTICAS_PREPROFESIONALES 
                ORDER BY fechaInicio DESC
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                practica_dict = dict(zip(column_names, row))
                practicas.append(practica_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return practicas
