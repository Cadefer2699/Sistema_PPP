from flask import Blueprint, jsonify, request
import controladores.controlador_institucion as controlador_institucion

router_institucion = Blueprint('router_institucion', __name__)

# Ruta para obtener la lista de instituciones
@router_institucion.route("/datos_instituciones", methods=["GET"])
def datos_instituciones():
    instituciones = controlador_institucion.obtener_instituciones()
    return jsonify(instituciones)

@router_institucion.route("/jefe_institucion", methods=["GET"])
def jefe_institucion():
    ruc = request.args.get('ruc')
    jefes = controlador_institucion.obtener_jefe(ruc)
    return jsonify(jefes)

