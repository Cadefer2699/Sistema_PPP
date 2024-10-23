from flask import Blueprint, jsonify
import controladores.controlador_genero as controlador_genero

router_genero = Blueprint('router_genero', __name__)

# Ruta para obtener la lista de géneros
@router_genero.route("/datos_generos", methods=["GET"])
def datos_generos():
    generos = controlador_genero.obtener_generos()
    return jsonify(generos)
