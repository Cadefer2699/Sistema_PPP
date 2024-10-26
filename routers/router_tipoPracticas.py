from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_tipoPracticas as controlador_tipoPracticas

router_tipoPracticas = Blueprint('router_tipoPracticas', __name__)

@router_tipoPracticas.route('/tipopracticas')
def tipopracticas(): 
    return render_template('gestion_academica/tipoPracticas.html')

@router_tipoPracticas.route('/datos_tipopracticas', methods=['GET'])
def datos_tipopracticas(): 
    tipopracticas = controlador_tipoPracticas.obtener_tipopracticas()
    return jsonify(tipopracticas)

@router_tipoPracticas.route("/obtener_tipopracticas_por_id/<int:idTipoPracticas>", methods=["GET"])
def obtener_tipopracticas_por_id(idTipoPracticas): 
    tipopracticas = controlador_tipoPracticas.obtener_tipopracticas_por_id(idTipoPracticas)
    return jsonify(tipopracticas)

@router_tipoPracticas.route("/agregar_tipopractica", methods=["POST"])
def agregar_tipopracticas(): 
    nombre = request.json.get('nombre')
    abreviatura = request.json.get('abreviatura')
    estado = request.json.get('estado')
    
    resultado = controlador_tipoPracticas.agregar_tipopractica(nombre, abreviatura, estado)
    return jsonify(resultado)

@router_tipoPracticas.route("/modificar_tipopractica", methods=["POST"])
def modificar_tipopracticas(): 
    idTipoPractica = request.json.get('idTipoPractica')
    nombre = request.json.get('nombre')
    abreviatura = request.json.get('abreviatura')
    estado = request.json.get('estado')
    
    resultado = controlador_tipoPracticas.modificar_tipopractica(idTipoPractica, nombre, abreviatura, estado)
    return jsonify(resultado)

@router_tipoPracticas.route("/dar_de_baja_tipopractica", methods=["POST"] )
def dar_de_baja_tipopractica(): 
    idTipoPractica = request.json.get('idTipoPractica')
    resultado = controlador_tipoPracticas.dar_de_baja_tipopractica(idTipoPractica)
    return jsonify(resultado)

@router_tipoPracticas.route("/eliminar_tipopractica", methods=["POST"])
def eliminar_tipopractica(): 
    idTipoPractica = request.json.get('idTipoPractica')
    resultado = controlador_tipoPracticas.eliminar_tipopractica(idTipoPractica)
    return jsonify(resultado)
