from bd import obtener_conexion  


def obtener_supervisiones():  
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    supervisiones = []
    try: 
        with conexion.cursor() as cursor: 
            cursor.execute("select idSupervision, fecha, funciones, observaciones, estado, idPractica from supervision")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            
            for row in rows: 
                supervison_dict = dict(zip(column_names, row))
                supervisiones.append(supervison_dict)
    except Exception as e: 
        return {"error": str(e)}
    finally:
        conexion.close()
    
    return supervisiones

def obtener_supervision_por_id(idSupervision):  
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    supervision = None
    try: 
        with conexion.cursor() as cursor: 
            cursor.execute("select * from supervision where idSupervision = %s", (idSupervision,))
            row = cursor.fetchone()
            if row: 
                columnas = [desc[0] for desc in cursor.description]
                escuela_dict = dict(zip(columnas, row))
                return escuela_dict
    except Exception as e: 
        return {"error": str(e)}
    finally: 
        conexion.close()
        

def agregar_supervision(fecha, funciones, observaciones, estado, idPractica): 
    #Validaciones
    if not fecha or not funciones or not observaciones or not estado or not idPractica: 
        return {"error": "Todos los campos son requeridos."}
    if estado not in ['A', 'I']:  
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}
    
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try: 
        with conexion.cursor() as cursor: 
            cursor.execute("""
            INSERT INTO supervision (fecha, funciones, observaciones, estado, idPractica)
            VALUES (%s, %s, %s, %s, %s)
            """), (fecha, funciones, observaciones, estado, idPractica)
            conexion.commit()
            return {"mensaje": "Supervisión agregada correctamente."}
    except Exception as e: 
        conexion.rollback()
        return {"error": str(e)}
    finally: 
        conexion.close()
        

def modificar_supervision(idSupervision, fecha, funciones, observaciones, estado, idPractica):  
    #validaciones
    if not idSupervision or not fecha or not funciones or not observaciones or not estado or not idPractica: 
        return {"error": "Todos los campos son requeridos."}
    if estado not in ['A', 'I']:  
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}
    
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try: 
        with conexion.cursor() as cursor: 
            cursor.execute("""
            UPDATE supervision
            SET fecha = %s, funciones = %s, observaciones = %s, estado = %s, idPractica = %s
            WHERE idSupervision = %s
            """), (fecha, funciones, observaciones, estado, idPractica, idSupervision)
            conexion.commit()
            return {"mensaje": "Supervisión modificada correctamente."}
    except Exception as e: 
        return {"error": str(e)}
    finally:
        conexion.close()
        
def eliminar_supervision(idSupervision): 
    #validaciones
    if not idSupervision:
        return {"error": "El ID de la supervision es requerido."}
    
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    try: 
        with conexion.cursor() as cursor:  
            cursor.execute("DELETE FROM supervision WHERE idSupervision = %s", (idSupervision,))
            conexion.commit()
            return {"mensaje": "Supervisión eliminada correctamente."}    
    except Exception as e: 
        conexion.rollback()
        return {"error": str(e)}
    finally: 
        conexion.close()
    

def dar_de_baja_supervision(idSupervision):  
    #validaciones
    if not idSupervision:
        return {"error": "El ID de la supervision es requerido."}
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    try: 
        with conexion.cursor() as cursor: 
            cursor.execute("UPDATE supervision SET estado = 'I' WHERE idSupervision = %s", (idSupervision,))
            conexion.commit()
            return {"mensaje": "Supervisión dada de baja correctamente."}
    except Exception as e: 
        conexion.rollback()
        return {"error": str(e)}
    finally: 
        conexion.close()