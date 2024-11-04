from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_infoPPP as controlador_infoPPP

router_ppp = Blueprint('router_ppp', __name__)

@router_ppp.route("/info_practicas")
def info_practicas():
    # Renderiza la página infoPPP.html
    return render_template('gestion_academica/infoPPP.html')

@router_ppp.route("/datos_practicas", methods=["GET"])
def datos_practicas():
    # Obtiene todas las prácticas preprofesionales
    practicas = controlador_infoPPP.obtener_practicas()
    return jsonify(practicas)

@router_ppp.route("/obtener_practica_por_id/<int:idPractica>", methods=["GET"])
def obtener_practica_por_id(idPractica):
    # Obtiene una práctica específica por su ID
    practica = controlador_infoPPP.obtener_practica_por_id(idPractica)
    return jsonify(practica)

@router_ppp.route("/agregar_practica", methods=["POST"])
def agregar_practica():
    # Datos para agregar una nueva práctica
    numDocEstudiante = request.json.get('numDocEstudiante')
    numDocInstitucion = request.json.get('numDocInstitucion')
    fechaInicio = request.json.get('fechaInicio')
    fechaFin = request.json.get('fechaFin')
    numDocDocente = request.json.get('numDocDocente')
    idEscuela = request.json.get('idEscuela')
    idTipoPractica = request.json.get('idTipoPractica')
    estado = request.json.get('estado')
    
    # Llamada al controlador para agregar la práctica
    resultado = controlador_infoPPP.agregar_practica(numDocEstudiante, numDocInstitucion, fechaInicio, fechaFin, numDocDocente, idEscuela, idTipoPractica, estado)
    return jsonify(resultado)

@router_ppp.route("/modificar_practica", methods=["POST"])
def modificar_practica():
    # Datos para modificar una práctica existente
    idPractica = request.json.get('idPractica')
    numDocEstudiante = request.json.get('numDocEstudiante')
    numDocInstitucion = request.json.get('numDocInstitucion')
    fechaInicio = request.json.get('fechaInicio')
    fechaFin = request.json.get('fechaFin')
    numDocDocente = request.json.get('numDocDocente')
    idEscuela = request.json.get('idEscuela')
    idTipoPractica = request.json.get('idTipoPractica')
    estado = request.json.get('estado')
    
    # Llamada al controlador para modificar la práctica
    resultado = controlador_infoPPP.modificar_practica(idPractica, numDocEstudiante, numDocInstitucion, fechaInicio, fechaFin, numDocDocente, idEscuela, idTipoPractica, estado)
    return jsonify(resultado)

@router_ppp.route("/dar_de_baja_practica", methods=["POST"])
def dar_de_baja_practica():
    # Cambia el estado de una práctica a "Inactivo"
    idPractica = request.json.get('idPractica')
    resultado = controlador_infoPPP.dar_de_baja_practica(idPractica)
    return jsonify(resultado)

@router_ppp.route("/eliminar_practica", methods=["POST"])
def eliminar_practica():
    # Elimina una práctica de la base de datos
    idPractica = request.json.get('idPractica')
    resultado = controlador_infoPPP.eliminar_practica(idPractica)
    return jsonify(resultado)

@router_ppp.route("/cambiar_estado_practica", methods=["POST"])
def cambiar_estado_practica():
    # Cambia el estado de una práctica a "Activo" o "Inactivo"
    idPractica = request.json.get('idPractica')
    nuevo_estado = request.json.get('estado')
    resultado = controlador_infoPPP.cambiar_estado_practica(idPractica, nuevo_estado)
    return jsonify(resultado)

@router_ppp.route("/practicas_activas", methods=["GET"])
def practicas_activas():
    # Obtiene la cantidad de prácticas activas
    practicas_activas = controlador_infoPPP.obtener_practicas_activas()
    return jsonify(practicas_activas)

@router_ppp.route("/practicas_con_estado", methods=["GET"])
def practicas_con_estado():
    # Obtiene la lista de prácticas con su estado
    practicas = controlador_infoPPP.obtener_practicas_con_estado()
    return jsonify(practicas)
