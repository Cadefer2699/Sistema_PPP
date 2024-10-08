from bd import obtener_conexion

# OPERACIONES CRUD

# Obtener todas las facultades
def obtener_facultades():
    conexion = obtener_conexion()
    facultades = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM FACULTAD")
        column_names = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        for row in rows:
            facultad_dict = dict(zip(column_names, row))
            facultades.append(facultad_dict)
    print(facultades)  # Agregar este print para verificar los datos
    conexion.close()
    return facultades

# Agregar una nueva facultad
def agregar_facultad(nombre, estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO FACULTAD (nombre, estado) VALUES (%s, %s)", (nombre, estado))
            conexion.commit()
            return {"mensaje": "Facultad agregada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

# Modificar una facultad existente
def modificar_facultad(idFacultad, nombre, estado):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE FACULTAD SET nombre = %s, estado = %s WHERE idFacultad = %s", (nombre, estado, idFacultad))
            conexion.commit()
            return {"mensaje": "Facultad modificada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

# Eliminar una facultad
def eliminar_facultad(idFacultad):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM FACULTAD WHERE idFacultad = %s", (idFacultad,))
            conexion.commit()
            return {"mensaje": "Facultad eliminada correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

# OTRAS OPERACIONES

# Obtener facultad por ID
def obtener_facultad_por_id(idFacultad):
    conexion = obtener_conexion()
    facultad = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM FACULTAD WHERE idFacultad = %s", (idFacultad,))
            facultad = cursor.fetchone()
            if facultad:
                columnas = [desc[0] for desc in cursor.description]
                facultad_dict = dict(zip(columnas, facultad))
                return facultad_dict
            else:
                return {"error": "Facultad no encontrada"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

# OBTENCIÓN DE ESTADÍSTICAS PARA DASHBOARD

# Obtener cantidad de facultades activas
def obtener_facultades_activas():
    conexion = obtener_conexion()
    facultades_activas = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS facultades_activas FROM FACULTAD WHERE estado = 'A'")
            column_names = [desc[0] for desc in cursor.description]
            row = cursor.fetchone()

            if row:
                facultad_dict = dict(zip(column_names, row))
                facultades_activas.append(facultad_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

    return facultades_activas

# Obtener lista de facultades con sus estados
def obtener_facultades_con_estado():
    conexion = obtener_conexion()
    facultades = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idFacultad, nombre, CASE WHEN estado = 'A' THEN 'Activo' ELSE 'Inactivo' END AS estado FROM FACULTAD ORDER BY nombre")
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
