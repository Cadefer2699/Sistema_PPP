from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_ppp as controlador_practicas

router_ppp = Blueprint('router_ppp', __name__)

@router_ppp.route("/practicas")
def practicas():
    return render_template('ppp/ppp_registro.html')

@router_ppp.route("/datos_ppp", methods=["GET"])
def datos_ppp():
    practicas = controlador_practicas.obtener_practicas()
    return jsonify(practicas)

@router_ppp.route("/obtener_ultimo_id", methods=["GET"])
def obtener_ultimo_id():
    practicas = controlador_practicas.obtener_ultimo_id()
    return jsonify(practicas)

@router_ppp.route("/obtener_practica_por_id/<int:idPractica>", methods=["GET"])
def obtener_practica_por_id(idPractica):
    practica = controlador_practicas.obtener_practica_por_id(idPractica)
    return jsonify(practica)

@router_ppp.route("/agregar_practica", methods=["POST"])
def agregar_practica():
    data = request.json
    fechaInicio = data.get('fechaInicio')
    horario = data.get('horario')
    modalidad = data.get('modalidad')
    area = data.get('area')
    numeroHorasPPP = data.get('numeroHorasPPP')
    numeroHorasPendientes = data.get('numeroHorasPendientes')
    numeroHorasRealizadas = data.get('numeroHorasRealizadas')
    idSemestre = data.get('idSemestre')
    idLinea = data.get('idLinea')
    numDocInstitucion = data.get('numDocInstitucion')
    idTipoPractica = data.get('idTipoPractica')
    idPersona = data.get('idPersona')
    
    resultado = controlador_practicas.agregar_practica(fechaInicio, horario, modalidad, area, numeroHorasPPP, numeroHorasPendientes, numeroHorasRealizadas, idSemestre, idLinea, numDocInstitucion, idTipoPractica, idPersona)
    return jsonify(resultado)

@router_ppp.route("/modificar_practica", methods=["POST"])
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

@router_ppp.route("/eliminar_practica", methods=["POST"])
def eliminar_practica():
    idPractica = request.json.get('idPractica')
    resultado = controlador_practicas.eliminar_practica(idPractica)
    return jsonify(resultado)

@router_ppp.route("/cambiar_estado_practica", methods=["POST"])
def cambiar_estado_practica():
    idPractica = request.json.get('idPractica')
    nuevo_estado = request.json.get('nuevo_estado')
    resultado = controlador_practicas.cambiar_estado_practica(idPractica, nuevo_estado)
    return jsonify(resultado)

@router_ppp.route("/practicas_activas", methods=["GET"])
def practicas_activas():
    resultado = controlador_practicas.obtener_practicas_activas()
    return jsonify(resultado)

@router_ppp.route("/practicas_con_estado", methods=["GET"])
def practicas_con_estado():
    resultado = controlador_practicas.obtener_practicas_con_estado()
    return jsonify(resultado)
