from flask import Blueprint, jsonify
import controladores.controlador_tipo_practicas as controlador_tipo_practicas

router_tipo_practicas = Blueprint('router_tipo_practicas', __name__)

# Ruta para obtener la lista de tipo practicas
@router_tipo_practicas.route("/datos_tipo_practicas", methods=["GET"])
def datos_tipo_practicas():
    tipo_practicas = controlador_tipo_practicas.obtener_tipo_practicas()
    return jsonify(tipo_practicas)
