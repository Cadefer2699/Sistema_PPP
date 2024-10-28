from bd import obtener_conexion

# Obtener todas las escuelas
def obtener_escuelas():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    escuelas = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT e.idEscuela, e.nombre, e.abreviatura, e.estado, 
                       f.nombre AS facultad, h.hRequeridas 
                FROM escuela e 
                INNER JOIN facultad f ON e.idFacultad = f.idFacultad 
                INNER JOIN horas_ppp h ON e.idHoras = h.idHoras
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                escuela_dict = dict(zip(column_names, row))
                escuelas.append(escuela_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return escuelas

# Obtener una escuela por su ID
def obtener_escuela_por_id(idEscuela):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM escuela WHERE idEscuela = %s", (idEscuela,))
            row = cursor.fetchone()
            if row:
                columnas = [desc[0] for desc in cursor.description]
                escuela_dict = dict(zip(columnas, row))
                return escuela_dict
            else:
                return {"error": "Escuela no encontrada"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_escuela_por_id_modificar(idEscuela):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM escuela WHERE idEscuela = %s", (idEscuela,))
            row = cursor.fetchone()
            if row:
                columnas = [desc[0] for desc in cursor.description]
                escuela_dict = dict(zip(columnas, row))
                return escuela_dict
            else:
                return {"error": "Escuela no encontrada"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

# Agregar una nueva escuela
def agregar_escuela(nombre, abreviatura, estado, idFacultad, idHoras):
    if not nombre or not abreviatura or not estado or not idFacultad or not idHoras:
        return {"error": "Todos los campos son requeridos."}
    if estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO escuela (nombre, abreviatura, estado, idFacultad, idHoras) 
                VALUES (%s, %s, %s, %s, %s)
            """, (nombre, abreviatura, estado, idFacultad, idHoras))
            conexion.commit()
            return {"mensaje": "Escuela agregada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

# Modificar una escuela
def modificar_escuela(idEscuela, nombre, abreviatura, estado, idFacultad, idHoras):
    if not idEscuela or not nombre or not abreviatura or not estado or not idFacultad or not idHoras:
        return {"error": "Todos los campos son requeridos."}
    if estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE escuela 
                SET nombre = %s, abreviatura = %s, estado = %s, idFacultad = %s, idHoras = %s 
                WHERE idEscuela = %s
            """, (nombre, abreviatura, estado, idFacultad, idHoras, idEscuela))
            conexion.commit()
            return {"mensaje": "Escuela modificada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": f"Error al modificar la escuela: {str(e)}"}
    finally:
        conexion.close()

# Eliminar una escuela
def eliminar_escuela(idEscuela):
    if not idEscuela:
        return {"error": "El ID de la escuela es requerido."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM escuela WHERE idEscuela = %s", (idEscuela,))
            conexion.commit()
            return {"mensaje": "Escuela eliminada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": f"Error al eliminar la escuela: {str(e)}"}
    finally:
        conexion.close()

# Dar de baja una escuela
def dar_de_baja_escuela(idEscuela):
    if not idEscuela:
        return {"error": "El ID de la escuela es requerido."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE escuela SET estado = 'I' WHERE idEscuela = %s", (idEscuela,))
            conexion.commit()
            return {"mensaje": "Escuela dada de baja correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": f"Error al dar de baja la escuela: {str(e)}"}
    finally:
        conexion.close()

# Otras funciones adicionales
def obtener_escuelas_activas():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS escuelas_activas FROM escuela WHERE estado = 'A'")
            row = cursor.fetchone()
            if row:
                return {"escuelas_activas": row[0]}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def obtener_escuelas_con_estado():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    escuelas = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    idEscuela, 
                    nombre, 
                    CASE 
                        WHEN estado = 'A' THEN 'Activo' 
                        ELSE 'Inactivo' 
                    END AS estado 
                FROM escuela 
                ORDER BY nombre
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                escuela_dict = dict(zip(column_names, row))
                escuelas.append(escuela_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return escuelas
