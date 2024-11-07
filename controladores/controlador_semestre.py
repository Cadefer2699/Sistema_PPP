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
                if 'fechaInicio' in semestre_dict and semestre_dict['fechaInicio']:
                    semestre_dict['fechaInicio'] = semestre_dict['fechaInicio'].strftime('%d/%m/%Y')
                if 'fechaFin' in semestre_dict and semestre_dict['fechaFin']:
                    semestre_dict['fechaFin'] = semestre_dict['fechaFin'].strftime('%d/%m/%Y')
                
                semestres.append(semestre_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return semestres

def obtener_semestre_por_id(idSemestre):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}    
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM semestre_academico WHERE idSemestre = %s", (idSemestre,))
            row = cursor.fetchone()
            if row:
                columnas = [desc[0] for desc in cursor.description]
                semestre_dict = dict(zip(columnas, row))
                return semestre_dict
            else:
                return {"error": "Semestre no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def agregar_semestre(nombre, fechaInicio, fechaFin, estado):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO semestre_academico (nombre, fechaInicio, fechaFin, estado) 
                VALUES (%s, %s, %s, %s)
            """, (nombre, fechaInicio, fechaFin, estado))
            conexion.commit()
            return {"mensaje": "Semestre agregado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_semestre(idSemestre, nombre, fechaInicio, fechaFin, estado):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE semestre_academico 
                SET nombre = %s, fechaInicio = %s, fechaFin = %s, estado = %s 
                WHERE idSemestre = %s
            """, (nombre, fechaInicio, fechaFin, estado, idSemestre))
            conexion.commit()
            return {"mensaje": "Semestre modificado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def eliminar_semestre(idSemestre):
    if not idSemestre:
        return {"error": "El ID del semestre es requerido."}
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM semestre_academico WHERE idSemestre = %s", (idSemestre,))
            conexion.commit()
            return {"mensaje": "Semestre eliminado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def dar_de_baja_semestre(idSemestre):
    if not idSemestre:
        return {"error": "El ID del semestre es requerido."}
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE semestre_academico SET estado = 'I' WHERE idSemestre = %s", (idSemestre,))
            conexion.commit()
            return {"mensaje": "Semestre dado de baja correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()