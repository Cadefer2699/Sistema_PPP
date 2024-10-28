from bd import obtener_conexion

def obtener_tipopracticas():
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    tipoPracticas = []
    try: 
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idTipoPractica, nombre, abreviatura, estado FROM tipo_practicas")
            column_names = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            
            for row in rows:
                tipoPractica_dict = dict(zip(column_names, row))
                tipoPracticas.append(tipoPractica_dict)
    except Exception as e: 
        return {"error": str(e)}
    finally: 
        conexion.close()
    return tipoPracticas
        
def obtener_tipopractica_por_id(idTipoPractica):  
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    tipoPractica = None
    try: 
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM tipo_practicas WHERE idTipoPractica = %s", (idTipoPractica,))
            row = cursor.fetchone()
            if row: 
                column_names = [desc[0] for desc in cursor.description]
                tipoPractica_dict = dict(zip(column_names, row))
                return tipoPractica_dict
    except Exception as e: 
        return {"error": str(e)}
    finally: 
        conexion.close()
    
        
def agregar_tipopractica(nombre, abreviatura, estado):
    #validaciones 
    if not nombre or not abreviatura or not estado: 
        return {"error": "Todos los campos son requeridos."}
    if estado not in ['A', 'I']: 
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}

    conexion = obtener_conexion() 
    if not conexion:
        return {"error": "No se pudo establecer conexión con la base de datos."}
    try: 
        with conexion.cursor() as cursor:  
            cursor.execute("""
                INSERT INTO tipo_practicas (nombre, abreviatura, estado)
                VALUES (%s, %s, %s)
            """, (nombre, abreviatura, estado))
            conexion.commit()
            return {"mensaje": "Tipo de prácticas agregada correctamente"}
    except Exception as e: 
        conexion.rollback()
        return {"error": str(e)}
    finally: 
        conexion.close()

def modificar_tipopractica(idTipoPractica, nombre, abreviatura, estado): 
    #validaciones
    if not idTipoPractica or not nombre or not abreviatura or not estado:
        return {"error": "Todos los campos son requeridos."}
    if estado not in ['A', 'I']:
        return {"error": "El estado debe ser 'A' (Activo) o 'I' (Inactivo)."}
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    
    try: 
        with conexion.cursor() as cursor: 
            cursor.execute("""
                UPDATE tipo_practicas
                SET nombre = %s, abreviatura = %s, estado = %s
                WHERE idTipoPractica = %s
            """, (nombre, abreviatura, estado, idTipoPractica))
            conexion.commit()
            return {"mensaje": "Tipo de prácticas modificada correctamente"}
    except Exception as e: 
        conexion.rollback()
        return {"error": str(e)}
    finally: 
        conexion.close()
        
def eliminar_tipopractica(idTipoPractica): 
    #validaciones 
    if not idTipoPractica: 
        return {"error": "El ID del tipo de práctica es requerido."}
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    try: 
        with conexion.cursor() as cursor: 
            cursor.execute("DELETE FROM tipo_practicas WHERE idTipoPractica = %s", (idTipoPractica,))
            conexion.commit()
            return {"mensaje": "Tipo de práctica eliminada correctamente."}
    except Exception as e: 
        conexion.rollback()
        return {"error": str(e)}
    finally: 
        conexion.close()
        
def dar_de_baja_tipopractica(idTipoPractica):  
    #validaciones 
    if not idTipoPractica: 
        return {"error": "El ID del tipo de práctica es requerido."}
    conexion = obtener_conexion()
    if not conexion: 
        return {"error": "No se pudo establecer conexión con la base de datos."}
    try: 
        with conexion.cursor() as cursor: 
            cursor.execute("UPDATE tipo_practicas SET estado = 'I' WHERE idTipoPractica = %s", (idTipoPractica,))
            conexion.commit()
            return {"mensaje": "Tipo de práctica dado de baja correctamente."}
    except Exception as e: 
        conexion.rollback()
        return {"error": str(e)}
    finally: 
        conexion.close()

# OTRAS OPERACIONES.... 
