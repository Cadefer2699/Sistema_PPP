from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_ppp as controlador_practicas

router_practicas = Blueprint('router_practicas', __name__)

@router_practicas.route("/practicas")
def practicas():
    return render_template('ppp/ppp_registro.html')

@router_practicas.route("/datos_practicas", methods=["GET"])
def datos_practicas():
    practicas = controlador_practicas.obtener_practicas()
    return jsonify(practicas)

@router_practicas.route("/obtener_practica_por_id/<int:idPractica>", methods=["GET"])
def obtener_practica_por_id(idPractica):
    practica = controlador_practicas.obtener_practica_por_id(idPractica)
    return jsonify(practica)

@router_practicas.route("/agregar_practica", methods=["POST"])
def agregar_practica():
    data = request.json
    fechaInicio = data.get('fechaInicio')
    fechaFin = data.get('fechaFin')
    modalidad = data.get('modalidad')
    area = data.get('area')
    numeroHorasPPP = data.get('numeroHorasPPP')
    numDocEstudiante = data.get('numDocEstudiante')
    idSemestre = data.get('idSemestre')
    idLinea = data.get('idLinea')
    numDocInstitucion = data.get('numDocInstitucion')
    idEstado = data.get('idEstado')
    idTipoPractica = data.get('idTipoPractica')
    
    resultado = controlador_practicas.agregar_practica(fechaInicio, fechaFin, modalidad, area, numeroHorasPPP, numDocEstudiante, idSemestre, idLinea, numDocInstitucion, idEstado, idTipoPractica)
    return jsonify(resultado)

@router_practicas.route("/modificar_practica", methods=["POST"])
def modificar_practica():
    data = request.json
    idPractica = data.get('idPractica')
    fechaInicio = data.get('fechaInicio')
    fechaFin = data.get('fechaFin')
    modalidad = data.get('modalidad')
    area = data.get('area')
    numeroHorasPPP = data.get('numeroHorasPPP')
    numDocEstudiante = data.get('numDocEstudiante')
    idSemestre = data.get('idSemestre')
    idLinea = data.get('idLinea')
    numDocInstitucion = data.get('numDocInstitucion')
    idEstado = data.get('idEstado')
    idTipoPractica = data.get('idTipoPractica')
    
    resultado = controlador_practicas.modificar_practica(idPractica, fechaInicio, fechaFin, modalidad, area, numeroHorasPPP, numDocEstudiante, idSemestre, idLinea, numDocInstitucion, idEstado, idTipoPractica)
    return jsonify(resultado)

@router_practicas.route("/eliminar_practica", methods=["POST"])
def eliminar_practica():
    idPractica = request.json.get('idPractica')
    resultado = controlador_practicas.eliminar_practica(idPractica)
    return jsonify(resultado)

@router_practicas.route("/cambiar_estado_practica", methods=["POST"])
def cambiar_estado_practica():
    idPractica = request.json.get('idPractica')
    nuevo_estado = request.json.get('nuevo_estado')
    resultado = controlador_practicas.cambiar_estado_practica(idPractica, nuevo_estado)
    return jsonify(resultado)

@router_practicas.route("/practicas_activas", methods=["GET"])
def practicas_activas():
    resultado = controlador_practicas.obtener_practicas_activas()
    return jsonify(resultado)

@router_practicas.route("/practicas_con_estado", methods=["GET"])
def practicas_con_estado():
    resultado = controlador_practicas.obtener_practicas_con_estado()
    return jsonify(resultado)
