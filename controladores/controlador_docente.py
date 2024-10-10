from bd import obtener_conexion

# OPERACIONES CRUD

def obtener_docentes():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM docente")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                docente_dict = dict(zip(column_names, row))
                docentes.append(docente_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return docentes

def obtener_docente_por_nombre_apellido(nombre, apellidos):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try:
        with conexion.cursor() as cursor:
            # Realizamos la búsqueda concatenando nombre y apellidos
            cursor.execute("""
                SELECT * FROM docente 
                WHERE nombre = %s AND apellidos = %s
            """, (nombre, apellidos))
            
            row = cursor.fetchone()
            if row:
                columnas = [desc[0] for desc in cursor.description]
                docente_dict = dict(zip(columnas, row))
                return docente_dict
            else:
                return {"error": "Docente no encontrado"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

def agregar_docente(numDoc, nombre, apellidos, cargo, correo, idTipoDoc, idUsuario):
    # Validaciones
    if not numDoc or not nombre or not apellidos or not cargo or not correo or not idTipoDoc or not idUsuario:
        return {"error": "Todos los campos son requeridos."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO docente (numDoc, nombre, apellidos, cargo, correo, idTipoDoc, idUsuario) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (numDoc, nombre, apellidos, cargo, correo, idTipoDoc, idUsuario))
            conexion.commit()
            return {"mensaje": "Docente agregado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_docente(numDoc, nombre, apellidos, cargo, correo, idTipoDoc, idUsuario):
    # Validaciones
    if not numDoc or not nombre or not apellidos or not cargo or not correo or not idTipoDoc or not idUsuario:
        return {"error": "Todos los campos son requeridos."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE docente 
                SET nombre = %s, apellidos = %s, cargo = %s, correo = %s, idTipoDoc = %s, idUsuario = %s
                WHERE numDoc = %s
            """, (nombre, apellidos, cargo, correo, idTipoDoc, idUsuario, numDoc))
            conexion.commit()
            return {"mensaje": "Docente modificado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def eliminar_docente(numDoc):
    # Validaciones
    if not numDoc:
        return {"error": "El número de documento del docente es requerido."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM docente WHERE numDoc = %s", (numDoc,))
            conexion.commit()
            return {"mensaje": "Docente eliminado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def cambiar_cargo_docente(numDoc, nuevo_cargo):
    # Validaciones
    if not numDoc or not nuevo_cargo:
        return {"error": "El número de documento y el nuevo cargo son requeridos."}
    
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            # Realizar la actualización directamente en la tabla docente
            cursor.execute("""
                UPDATE docente 
                SET cargo = %s 
                WHERE numDoc = %s
            """, (nuevo_cargo, numDoc))
            
            if cursor.rowcount > 0:
                conexion.commit()
                return {"mensaje": "Cargo del docente actualizado correctamente"}
            else:
                return {"error": "Docente no encontrado"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()
