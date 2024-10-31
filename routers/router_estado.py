from flask import Blueprint, jsonify
import controladores.controlador_estado as controlador_estado

router_estado = Blueprint('router_estado', __name__)

# Ruta para obtener la lista de estados
@router_estado.route("/datos_estados", methods=["GET"])
def datos_estados():
    estados = controlador_estado.obtener_estados()
    return jsonify(estados)
