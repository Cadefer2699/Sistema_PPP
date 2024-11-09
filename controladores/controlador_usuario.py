from bd import obtener_conexion

def obtener_usuarios():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    usuarios = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idUsuario, username, password FROM usuario")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                usuario_dict = dict(zip(column_names, row))
                usuarios.append(usuario_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    return usuarios

def obtener_usuarios_estudiantes():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    usuarios = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idUsuario, username, password FROM usuario where idTipoUsuario = 3")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                usuario_dict = dict(zip(column_names, row))
                usuarios.append(usuario_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    return usuarios

def obtener_usuarios_docentes():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    usuarios = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idUsuario, username, password FROM usuario where idTipoUsuario = 2")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                usuario_dict = dict(zip(column_names, row))
                usuarios.append(usuario_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    return usuarios

def obtener_usuario_con_tipopersona_por_username(username):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idUsuario, username, estado, password FROM usuario WHERE username =  %s", (username))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_usuario_por_username(username):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idusuario, username, password, estado, idpersona FROM usuario WHERE username = %s", (username,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def obtener_usuario_por_id(id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idusuario, username, password, estado, idpersona FROM usuario WHERE idusuario = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

def actualizar_token(username,token):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET token = %s WHERE username = %s",
                       (token,username))
    conexion.commit()
    conexion.close()

##PARA EL APATARDO DE PERFIL
def obtener_datos_usuario (id):
    conexion = obtener_conexion()
    usuario = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT p.nombre, p.apellidos, p.foto FROM persona p inner join usuario u on p.idusuario = u.idusuario WHERE u.idusuario = %s", (id,))
        usuario = cursor.fetchone()
    conexion.close()
    return usuario

# Función para actualizar los datos del usuario
def actualizar_datos_usuario(id, nombres, apellidos, n_documento, correo, telefono):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE persona SET nombres = %s, apellidos = %s, n_documento = %s, correo = %s, telefono = %s WHERE idpersona = (SELECT idpersona FROM usuario WHERE idusuario = %s)",
                           (nombres, apellidos, n_documento, correo, telefono, id))
            conexion.commit()
            return {"mensaje": "Datos actualizados correctamente"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()

#funciona para recibir datos del estudiante y cargarlo a informe desde el usuario

def obtener_datos_usuario_informe():
    conexion = obtener_conexion()
    usuario_informe = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("select p.nombre, p.apellidos, p.codUniversitario  from persona p inner join usuario u on p.idUsuario = u.idUsuario where u.idTipoUsuario=3")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                usuario_informe_dict = dict(zip(column_names, row))
                usuario_informe.append(usuario_informe_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
