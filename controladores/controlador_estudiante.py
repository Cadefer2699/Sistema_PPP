from bd import obtener_conexion

# OPERACIONES CRUD

def obtener_estudiantes():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    estudiantes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM estudiante")
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
            cursor.execute("SELECT * FROM estudiante WHERE idEstudiante = %s", (idEstudiante,))
            row = cursor.fetchone()
            if row:
                columnas = [desc[0] for desc in cursor.description]
                estudiante_dict = dict(zip(columnas, row))
                return estudiante_dict
            else:
                return {"error": "Estudiante no encontrada"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def agregar_estudiante(nombre, estado):
    # Validaciones
    if not nombre or not estado:
        return {"error": "El nombre y el estado son requeridos."}
    if estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Llamar al procedimiento almacenado para insertar
            cursor.callproc('GestionEstudiante', [1, None, nombre, estado])
            conexion.commit()
            return {"mensaje": "Estudiante agregada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_estudiante(idEstudiante, nombre, estado):
    # Validaciones
    if not idEstudiante or not nombre or not estado:
        return {"error": "El ID, nombre y estado son requeridos."}
    if estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Llamar al procedimiento almacenado para modificar
            cursor.callproc('GestionEstudiante', [2, idEstudiante, nombre, estado])
            conexion.commit()
            return {"mensaje": "Estudiante modificada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def eliminar_estudiante(idEstudiante):
    # Validaciones
    if not idEstudiante:
        return {"error": "El ID de la estudiante es requerido."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Llamar al procedimiento almacenado para eliminar
            cursor.callproc('GestionEstudiante', [3, idEstudiante, None, None])
            conexion.commit()
            return {"mensaje": "Estudiante eliminada correctamente"}
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
