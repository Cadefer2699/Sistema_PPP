from bd import obtener_conexion

# OPERACIONES CRUD

def obtener_estudiantes():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    estudiantes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT p.numDoc, p.nombre, p.apellidos, p.codUniversitario, p.tel1, p.tel2, 
                       p.correoP, p.correoUSAT, p.estado, g.nombre as genero, td.nombre as tipoDocumento, 
                       e.nombre as escuela, u.username as usuario
                FROM persona p
                LEFT JOIN genero g ON p.idGenero = g.idGenero
                LEFT JOIN tipo_documento td ON p.idTipoDoc = td.idTipoDoc
                LEFT JOIN escuela e ON p.idEscuela = e.idEscuela
                LEFT JOIN usuario u ON p.idUsuario = u.idUsuario
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                estudiante_dict = dict(zip(column_names, row))
                estudiantes.append(estudiante_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return estudiantes

def obtener_estudiante_por_id(idEstudiante):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    estudiante = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT p.numDoc, p.nombre, p.apellidos, p.codUniversitario, p.tel1, p.tel2, 
                       p.correoP, p.correoUSAT, p.estado, g.nombre as genero, td.nombre as tipoDocumento, 
                       e.nombre as escuela, u.username as usuario
                FROM persona p
                LEFT JOIN genero g ON p.idGenero = g.idGenero
                LEFT JOIN tipo_documento td ON p.idTipoDoc = td.idTipoDoc
                LEFT JOIN escuela e ON p.idEscuela = e.idEscuela
                LEFT JOIN usuario u ON p.idUsuario = u.idUsuario
                WHERE p.idPersona = %s
            """, (idEstudiante,))
            row = cursor.fetchone()

            if row:
                columnas = [desc[0] for desc in cursor.description]
                estudiante_dict = dict(zip(columnas, row))
                return estudiante_dict
            else:
                return {"error": "Estudiante no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def agregar_estudiante(numDoc, nombre, apellidos, codUniversitario, tel1, tel2, correoP, correoUSAT, estado, idGenero, idTipoDoc, idUsuario, idEscuela):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Inserta el nuevo estudiante en la tabla persona
            cursor.execute("""
                INSERT INTO persona (numDoc, nombre, apellidos, codUniversitario, tel1, tel2, correoP, correoUSAT, estado, idGenero, idTipoDoc, idUsuario, idEscuela)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (numDoc, nombre, apellidos, codUniversitario, tel1, tel2, correoP, correoUSAT, estado, idGenero, idTipoDoc, idUsuario, idEscuela))
            conexion.commit()
            return {"mensaje": "Estudiante agregado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_estudiante(idEstudiante, numDoc, nombre, apellidos, codUniversitario, tel1, tel2, correoP, correoUSAT, estado, idGenero, idTipoDoc, idUsuario, idEscuela):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Actualiza la información del estudiante en la tabla persona
            cursor.execute("""
                UPDATE persona
                SET numDoc = %s, nombre = %s, apellidos = %s, codUniversitario = %s, tel1 = %s, tel2 = %s, 
                    correoP = %s, correoUSAT = %s, estado = %s, idGenero = %s, idTipoDoc = %s, 
                    idUsuario = %s, idEscuela = %s
                WHERE idPersona = %s
            """, (numDoc, nombre, apellidos, codUniversitario, tel1, tel2, correoP, correoUSAT, estado, idGenero, idTipoDoc, idUsuario, idEscuela, idEstudiante))
            conexion.commit()
            return {"mensaje": "Estudiante modificado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def eliminar_estudiante(idEstudiante):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Elimina al estudiante de la tabla persona
            cursor.execute("DELETE FROM persona WHERE idPersona = %s", (idEstudiante,))
            conexion.commit()
            return {"mensaje": "Estudiante eliminado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def dar_de_baja_estudiante(idEstudiante):
    # Validaciones
    if not idEstudiante:
        return {"error": "El ID de la estudiante es requerido."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.callproc('GestionEstudiante', [4, idEstudiante, None, None])
            conexion.commit()
            return {"mensaje": "Estudiante dada de baja correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def cambiar_estado_estudiante(idEstudiante, nuevo_estado):
    # Validaciones
    if not idEstudiante or not nuevo_estado:
        return {"error": "El ID y el nuevo estado son requeridos."}
    if nuevo_estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Llamar al procedimiento almacenado para cambiar estado
            cursor.callproc('GestionEstudiante', [4, idEstudiante, None, nuevo_estado])
            conexion.commit()
            return {"mensaje": "Estado de la estudiante actualizado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

# OTRAS OPERACIONES

def obtener_estudiantes_activas():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS estudiantes_activas FROM estudiante WHERE estado = 'A'")
            row = cursor.fetchone()

            if row:
                return {"estudiantes_activas": row[0]}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_estudiantes_con_estado():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    estudiantes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    idEstudiante, 
                    nombre, 
                    CASE 
                        WHEN estado = 'A' THEN 'Activo' 
                        ELSE 'Inactivo' 
                    END AS estado 
                FROM estudiante 
                ORDER BY nombre
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                estudiante_dict = dict(zip(column_names, row))
                estudiantes.append(estudiante_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return estudiantes
