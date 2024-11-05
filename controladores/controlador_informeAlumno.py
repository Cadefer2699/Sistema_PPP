from bd import obtener_conexion

# Obtener todas las escuelas
def obtener_informeAlumno():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    informesAlumnos = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
            SELECT 
                p.nombre AS Nombre_Alumno,
                p.apellidos AS Apellidos_Alumno,
                sa.nombre AS Semestre_Academico,
                ppp.idPractica AS ID_Practica,
                IFNULL(ii.idInforme, 'Por subir') AS Informe_Inicial,
                IFNULL(ifin.idInforme, 'Por subir') AS Informe_Final
            FROM 
                persona p
            JOIN 
                usuario u ON p.idUsuario = u.idUsuario
            JOIN 
                practicas_preprofesionales ppp ON p.idPersona = ppp.idPersona
            JOIN 
                semestre_academico sa ON ppp.idSemestre = sa.idSemestre
            LEFT JOIN 
                informes_practicas_preprofesionales ippp_i ON ppp.idPractica = ippp_i.idPractica
            LEFT JOIN 
                informe ii ON ippp_i.IidInforme = ii.idInforme AND ii.idTipoInforme = 1 -- Informe inicial
            LEFT JOIN 
                informes_practicas_preprofesionales ippp_f ON ppp.idPractica = ippp_f.idPractica
            LEFT JOIN 
                informe ifin ON ippp_f.IidInforme = ifin.idInforme AND ifin.idTipoInforme = 2 -- Informe final
            WHERE 
                u.idTipoUsuario = 3;
            """)
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            for row in rows:
                informesAlumnos_dict = dict(zip(column_names, row))
                informesAlumnos.append(informesAlumnos_dict)
    except Exception as e:
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return informesAlumnos