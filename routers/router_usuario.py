from flask import Blueprint, jsonify
import controladores.controlador_usuario as controlador_usuario

router_usuario = Blueprint('router_usuario', __name__)

@router_usuario.route("/datos_usuarios", methods=["GET"])
def datos_usuarios():
    usuarios = controlador_usuario.obtener_usuarios()
    return jsonify(usuarios)

@router_usuario.route("/datos_usuarios_estudiantes", methods=["GET"])
def datos_usuarios_estudiantes():
    usuarios = controlador_usuario.obtener_usuarios_estudiantes()
    return jsonify(usuarios)