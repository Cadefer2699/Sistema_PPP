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
