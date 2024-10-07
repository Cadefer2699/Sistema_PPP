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
    #junction.proxy.rlwy.net:39981
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def obtener_usuarios(conexion):
    try:
        with conexion.cursor() as cursor:
            # Ejecutar la consulta
            cursor.execute("SELECT * FROM usuario")
            # Obtener los resultados
            resultados = cursor.fetchall()
            return resultados
    
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

conexion = obtener_conexion()

if conexion:
    usuarios = obtener_usuarios(conexion)
    if usuarios:
        print("Resultados de la consulta:")
        for usuario in usuarios:
            print(usuario)
    else:
        print("No se encontraron usuarios o ocurrió un error.")
    
    conexion.close()
else:
    print("No se pudo establecer conexión con la base de datos.")
