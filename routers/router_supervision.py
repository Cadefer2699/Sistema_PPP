from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_supervision as controlador_supervision

router_supervision = Blueprint('router_supervision', __name__)

@router_supervision.route("/supervision")
def supervision(): 
    return render_template("supervision.html")

@router_supervision.route("/datos_supervision", methods=["GET"])
def datos_supervision(): 
    supervisiones = controlador_supervision.obtener_supervisiones()
    return jsonify(supervisiones)

@router_supervision.route("/obtener_supervision_por_id/<int:idSupervision>", methods=["GET"])
def obtener_supervision_por_id(idSupervision): 
    supervision = controlador_supervision.obtener_supervision_por_id(idSupervision)
    return jsonify(supervision)

@router_supervision.route("/agregar_supervision", methods=["POST"])
def agregar_supervision():  
    fecha = request.json.get('fecha')
    funciones = request.json.get('funciones')
    observaciones = request.json.get('observaciones')
    estado = request.json.get('estado')
    idPractica = request.json.get('idPractica')
    
    resultado = controlador_supervision.agregar_supervision(fecha, funciones, observaciones, estado, idPractica)
    return jsonify(resultado)

@router_supervision.route("/modificar_supervision", methods=["POST"])
def modificar_supervision():  
    idSupervision = request.json.get('idSupervision')
    fecha = request.json.get('fecha')
    funciones = request.json.get('funciones')
    observaciones = request.json.get('observaciones')
    estado = request.json.get('estado')
    idPractica = request.json.get('idPractica')
    
    resultado = controlador_supervision.modificar_supervision(idSupervision, fecha, funciones, observaciones, estado, idPractica)
    return jsonify(resultado)

@router_supervision.route("/dar_de_baja_supervision", methods=["POST"])
def dar_de_baja_supervision():  
    idSupervision = request.json.get('idSupervision')
    resultado = controlador_supervision.dar_de_baja_supervision(idSupervision)
    return jsonify(resultado)

@router_supervision.route("/eliminar_supervision", methods=["POST"])
def eliminar_supervision():  
    idSupervision = request.json.get('idSupervision')
    resultado = controlador_supervision.eliminar_supervision(idSupervision)
    return jsonify(resultado)
    