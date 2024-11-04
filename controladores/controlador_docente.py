from bd import obtener_conexion

# OPERACIONES CRUD

def obtener_docentes():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    docentes = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT 
                p.idPersona, p.numDoc, p.nombre, p.apellidos, t.tipo as cargo, p.tel1, p.tel2, p.correoP, p.correoUSAT, p.estado, 
                g.nombre as genero, td.nombre as tipoDocumento, u.username as usuario, e.nombre as escuela
                FROM persona p
                LEFT JOIN genero g ON p.idGenero = g.idGenero
                LEFT JOIN tipo_documento td ON p.idTipoDoc = td.idTipoDoc
                LEFT JOIN escuela e ON p.idEscuela = e.idEscuela
                LEFT JOIN usuario u ON p.idUsuario = u.idUsuario
                LEFT JOIN tipo_usuario t ON u.idTipoUsuario = t.idTipoUsuario
                WHERE u.idTipoUsuario IN (1, 2)
            """)
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

def obtener_docente_por_id(idDocente):
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    docente = None
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT 
                p.idPersona, p.numDoc, p.nombre, p.apellidos, p.tel1, p.tel2, p.correoP, p.correoUSAT, p.estado, 
                g.nombre as genero, td.nombre as tipoDocumento, u.username as usuario, e.nombre as escuela
                FROM persona p
                LEFT JOIN genero g ON p.idGenero = g.idGenero
                LEFT JOIN tipo_documento td ON p.idTipoDoc = td.idTipoDoc
                LEFT JOIN escuela e ON p.idEscuela = e.idEscuela
                LEFT JOIN usuario u ON p.idUsuario = u.idUsuario
                WHERE p.idPersona = %
            """, (idDocente,))
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

def agregar_docente(numDoc, nombre, apellidos, tel1, tel2, correoP, correoUSAT, estado, idGenero, idUsuario, idEscuela):
    # Validaciones
    if not numDoc or not nombre or not apellidos or not tel1 or not correoP or not estado or not idGenero or not idUsuario or not idEscuela:
        return {"error": "Todos los campos son requeridos."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                INSERT INTO docente (numDoc, nombre, apellidos, tel1, tel2, correoP, correoUSAT, estado, idGenero, idTipoDoc, idUsuario, idEscuela) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (numDoc, nombre, apellidos, tel1, tel2, correoP, correoUSAT, estado, idGenero, 1, idUsuario, idEscuela))
            conexion.commit()
            return {"mensaje": "Docente agregado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def modificar_docente(idDocente, numDoc, nombre, apellidos, tel1, tel2, correoP, correoUSAT, estado, idGenero, idUsuario, idEscuela):
    # Validaciones
    if not idDocente or not numDoc or not nombre or not apellidos or not tel1 or not correoP or not estado or not idGenero or not idUsuario or not idEscuela:
        return {"error": "Todos los campos son requeridos."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE persona 
                SET numDoc = %s, nombre = %s, apellidos = %s, tel1 = %s, tel2 = %s, correoP = %s, correoUSAT = %s, estado = %s, idGenero = %s, idTipoDoc = %s, idUsuario = %s, idEscuela = %s
                WHERE idPersona = %s
            """, (numDoc, nombre, apellidos, tel1, tel2, correoP, correoUSAT, estado, idGenero, idUsuario, idEscuela, idDocente))
            conexion.commit()
            return {"mensaje": "Docente modificado correctamente"}
    except Exception as e:
        conexion.rollback()
        return {"error": str(e)}
    finally:
        conexion.close()

def eliminar_docente(idDocente):
    # Validaciones
    if not idDocente:
        return {"error": "El id del docente es requerido."}

    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}

    try:
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM persona WHERE idPersona = %s", (idDocente,))
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
