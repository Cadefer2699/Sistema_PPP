from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_estudiante as controlador_estudiante

router_estudiante = Blueprint('router_estudiante', __name__)

@router_estudiante.route("/estudiante")
def estudiante():
    return render_template('gestion_academica/estudiante.html')

@router_estudiante.route("/datos_estudiantes", methods=["GET"])
def datos_estudiantes():
    estudiantes = controlador_estudiante.obtener_estudiantes()
    return jsonify(estudiantes)

@router_estudiante.route("/obtener_estudiante_por_id/<int:idEstudiante>", methods=["GET"])
def obtener_estudiante_por_id(idEstudiante):
    estudiantes = controlador_estudiante.obtener_estudiante_por_id(idEstudiante)
    return jsonify(estudiantes)

@router_estudiante.route("/agregar_estudiante", methods=["POST"])
def agregar_estudiante():
    nombre = request.json.get('nombre')
    estado = request.json.get('estado')
    resultado = controlador_estudiante.agregar_estudiante(nombre, estado)
    return jsonify(resultado)

@router_estudiante.route("/modificar_estudiante", methods=["POST"])
def modificar_estudiante():
    idestudiante = request.json.get('idEstudiante')
    nombre = request.json.get('nombre')
    estado = request.json.get('estado')
    resultado = controlador_estudiante.modificar_estudiante(idestudiante, nombre, estado)
    return jsonify(resultado)

@router_estudiante.route("/dar_de_baja_estudiante", methods=["POST"])
def dar_de_baja_estudiante():
    idestudiante = request.json.get('idEstudiante')
    resultado = controlador_estudiante.dar_de_baja_estudiante(idestudiante)
    return jsonify(resultado)

@router_estudiante.route("/eliminar_estudiante", methods=["POST"])
def eliminar_estudiante():
    idestudiante = request.json.get('idEstudiante')
    resultado = controlador_estudiante.eliminar_estudiante(idestudiante)
    return jsonify(resultado)
