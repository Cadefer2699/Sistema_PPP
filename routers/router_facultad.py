from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_facultad as controlador_facultad

router_facultad = Blueprint('router_facultad', __name__)

@router_facultad.route("/facultad")
def facultad():
    return render_template('dashboard/facultad.html')

@router_facultad.route("/datos_facultades", methods=["GET"])
def datos_facultades():
    facultades = controlador_facultad.obtener_facultades()
    return jsonify(facultades)

@router_facultad.route("/obtener_facultad_por_id/<int:idFacultad>", methods=["GET"])
def obtener_facultad_por_id(idFacultad):
    facultades = controlador_facultad.obtener_facultad_por_id(idFacultad)
    return jsonify(facultades)

@router_facultad.route("/agregar_facultad", methods=["POST"])
def agregar_facultad():
    nombre = request.json.get('nombre')
    estado = request.json.get('estado')
    resultado = controlador_facultad.agregar_facultad(nombre, estado)
    return jsonify(resultado)

@router_facultad.route("/modificar_facultad", methods=["POST"])
def modificar_facultad():
    idfacultad = request.json.get('idFacultad')
    nombre = request.json.get('nombre')
    estado = request.json.get('estado')
    resultado = controlador_facultad.modificar_facultad(idfacultad, nombre, estado)
    return jsonify(resultado)

@router_facultad.route("/cambiar_estado_facultad", methods=["POST"])
def cambiar_estado_facultad():
    idfacultad = request.json.get('idFacultad')
    nuevo_estado = request.json.get('estado')
    resultado = controlador_facultad.cambiar_estado_facultad(idfacultad, nuevo_estado)
    return jsonify(resultado)

@router_facultad.route("/eliminar_facultad", methods=["POST"])
def eliminar_facultad():
    idfacultad = request.json.get('idFacultad')
    resultado = controlador_facultad.eliminar_facultad(idfacultad)
    return jsonify(resultado)
