from flask import Blueprint, jsonify
import controladores.controlador_usuario as controlador_usuario

router_usuario = Blueprint('router_usuario', __name__)

# Ruta para obtener la lista de géneros
@router_usuario.route("/datos_usuarios", methods=["GET"])
def datos_usuarios():
    usuarios = controlador_usuario.obtener_usuarios()
    return jsonify(usuarios)