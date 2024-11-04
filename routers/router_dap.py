from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_dap as controlador_dap

router_dap = Blueprint('router_dap', __name__)

@router_dap.route("/dap")
def estudiante():
    return render_template('gestion_academica/estudiante.html')

@router_dap.route("/datos_dap", methods=["GET"])
def datos_dap():
    estudiantes = controlador_dap.obtener_dap()
    return jsonify(estudiantes)

@router_dap.route("/obtener_dap_por_id/<int:idEstudiante>", methods=["GET"])
def obtener_dap_por_id(idEstudiante):
    estudiante = controlador_dap.obtener_dap_por_id(idEstudiante)
    return jsonify(estudiante)

@router_dap.route("/obtener_dap_por_id_modificar/<int:idEstudiante>", methods=["GET"])
def obtener_dap_por_id_modificar(idEstudiante):
    estudiante = controlador_dap.obtener_dap_por_id_modificar(idEstudiante)
    return jsonify(estudiante)

@router_dap.route("/agregar_dap", methods=["POST"])
def agregar_dap():
    data = request.json
    numDoc = data.get('numDoc')
    nombre = data.get('nombre')
    apellidos = data.get('apellidos')
    codUniversitario = data.get('codUniversitario')
    tel1 = data.get('tel1')
    tel2 = data.get('tel2')
    correoP = data.get('correoP')
    correoUSAT = data.get('correoUSAT')
    estado = data.get('estado')
    idGenero = data.get('idGenero')
    idTipoDoc = data.get('idTipoDoc')
    idUsuario = data.get('idUsuario')
    idEscuela = data.get('idEscuela')

    resultado = controlador_dap.agregar_dap(numDoc, nombre, apellidos, codUniversitario, tel1, tel2, correoP, correoUSAT, estado, idGenero, idTipoDoc, idUsuario, idEscuela)
    return jsonify(resultado)

@router_dap.route("/modificar_dap", methods=["POST"])
def modificar_dap():
    data = request.json
    idEstudiante = data.get('idPersona')
    numDoc = data.get('numDoc')
    nombre = data.get('nombre')
    apellidos = data.get('apellidos')
    codUniversitario = data.get('codUniversitario')
    tel1 = data.get('tel1')
    tel2 = data.get('tel2')
    correoP = data.get('correoP')
    correoUSAT = data.get('correoUSAT')
    estado = data.get('estado')
    idGenero = data.get('idGenero')
    idTipoDoc = data.get('idTipoDoc')
    idUsuario = data.get('idUsuario')
    idEscuela = data.get('idEscuela')

    resultado = controlador_dap.modificar_dap(idEstudiante, numDoc, nombre, apellidos, codUniversitario, tel1, tel2, correoP, correoUSAT, estado, idGenero, idTipoDoc, idUsuario, idEscuela)
    return jsonify(resultado)

@router_dap.route("/dar_de_baja_dap", methods=["POST"])
def dar_de_baja_dap():
    idEstudiante = request.json.get('idEstudiante')
    resultado = controlador_dap.modificar_dap(idEstudiante, None, None, None, None, None, None, None, 'I', None, None, None, None)
    return jsonify(resultado)

@router_dap.route("/eliminar_dap", methods=["POST"])
def eliminar_dap():
    idEstudiante = request.json.get('idEstudiante')
    resultado = controlador_dap.eliminar_dap(idEstudiante)
    return jsonify(resultado)
