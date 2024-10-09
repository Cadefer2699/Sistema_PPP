from bd import obtener_conexion

# OPERACIONES CRUD

def obtener_facultades():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    facultades = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM facultad")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                facultad_dict = dict(zip(column_names, row))
                facultades.append(facultad_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return facultades

def obtener_facultad_por_id(idFacultad):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    facultad = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM facultad WHERE idFacultad = %s", (idFacultad,))
            row = cursor.fetchone()
            if row:
                columnas = [desc[0] for desc in cursor.description]
                facultad_dict = dict(zip(columnas, row))
                return facultad_dict
            else:
                return {"error": "Facultad no encontrada"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def agregar_facultad(nombre, estado):
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
            cursor.callproc('GestionFacultad', [1, None, nombre, estado])
            conexion.commit()
            return {"mensaje": "Facultad agregada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_facultad(idFacultad, nombre, estado):
    # Validaciones
    if not idFacultad or not nombre or not estado:
        return {"error": "El ID, nombre y estado son requeridos."}
    if estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Llamar al procedimiento almacenado para modificar
            cursor.callproc('GestionFacultad', [2, idFacultad, nombre, estado])
            conexion.commit()
            return {"mensaje": "Facultad modificada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def eliminar_facultad(idFacultad):
    # Validaciones
    if not idFacultad:
        return {"error": "El ID de la facultad es requerido."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Llamar al procedimiento almacenado para eliminar
            cursor.callproc('GestionFacultad', [3, idFacultad, None, None])
            conexion.commit()
            return {"mensaje": "Facultad eliminada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def cambiar_estado_facultad(idFacultad, nuevo_estado):
    # Validaciones
    if not idFacultad or not nuevo_estado:
        return {"error": "El ID y el nuevo estado son requeridos."}
    if nuevo_estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Llamar al procedimiento almacenado para cambiar estado
            cursor.callproc('GestionFacultad', [4, idFacultad, None, nuevo_estado])
            conexion.commit()
            return {"mensaje": "Estado de la facultad actualizado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

# OTRAS OPERACIONES

def obtener_facultades_activas():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS facultades_activas FROM facultad WHERE estado = 'A'")
            row = cursor.fetchone()

            if row:
                return {"facultades_activas": row[0]}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_facultades_con_estado():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    facultades = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    idFacultad, 
                    nombre, 
                    CASE 
                        WHEN estado = 'A' THEN 'Activo' 
                        ELSE 'Inactivo' 
                    END AS estado 
                FROM facultad 
                ORDER BY nombre
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                facultad_dict = dict(zip(column_names, row))
                facultades.append(facultad_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return facultades
