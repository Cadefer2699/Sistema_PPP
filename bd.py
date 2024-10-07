import pymysql

def obtener_conexion():
    try:
        conexion = pymysql.connect(
            host='junction.proxy.rlwy.net',
            port=39981,
            user='root',
            password='pCWZPaxqsNKSYInhPHeyFknIWiRFpSpb',
            db='bd_ppp'
        )
        print("Conexión exitosa a la base de datos.")
        return conexion
    
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

conexion = obtener_conexion()

if conexion:
    conexion.close()
else:
    print("No se pudo establecer conexión con la base de datos.")
