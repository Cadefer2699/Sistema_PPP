import pymysql

#Desarrollo
def obtener_conexion():
    return pymysql.connect(host='roundhouse.proxy.rlwy.net',
                                port=54363,
                                user='root',
                                password='UAumJRVIMWnTGqRdkZNDqvocCpHjzHKl',
                                db='db_calidad')


