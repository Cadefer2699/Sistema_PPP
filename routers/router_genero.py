from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_genero as controlador_genero

router_genero = Blueprint('router_genero', __name__)

@router_genero.route("/genero")
def genero():
    return render_template('gestion_academica/genero.html')

@router_genero.route("/datos_generos", methods=["GET"])
def datos_generos():
    generos = controlador_genero.obtener_generos()
    return jsonify(generos)

@router_genero.route("/obtener_genero_por_id/<int:idGenero>", methods=["GET"])
def obtener_genero_por_id(idGenero):
    generos = controlador_genero.obtener_genero_por_id(idGenero)
    return jsonify(generos)

@router_genero.route("/agregar_genero", methods=["POST"])
def agregar_genero():
    nombre = request.json.get('nombre')
    estado = request.json.get('estado')
    resultado = controlador_genero.agregar_genero(nombre, estado)
    return jsonify(resultado)

@router_genero.route("/modificar_genero", methods=["POST"])
def modificar_genero():
    idgenero = request.json.get('idGenero')
    nombre = request.json.get('nombre')
    estado = request.json.get('estado')
    resultado = controlador_genero.modificar_genero(idgenero, nombre, estado)
    return jsonify(resultado)

@router_genero.route("/dar_de_baja_genero", methods=["POST"])
def dar_de_baja_genero():
    idgenero = request.json.get('idGenero')
    resultado = controlador_genero.dar_de_baja_genero(idgenero)
    return jsonify(resultado)

@router_genero.route("/eliminar_genero", methods=["POST"])
def eliminar_genero():
    idgenero = request.json.get('idGenero')
    resultado = controlador_genero.eliminar_genero(idgenero)
    return jsonify(resultado)
