from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_docente as controlador_docente

router_docente = Blueprint('router_docente', __name__)

# Ruta para renderizar la página de docentes
@router_docente.route("/docente")
def docente():
    return render_template('dashboard/docente.html')

@router_docente.route("/datos_docentes", methods=["GET"])
def datos_docentes():
    docentes = controlador_docente.obtener_docentes()
    return jsonify(docentes)

# Ruta para obtener un docente por su nombre y apellidos concatenados
@router_docente.route("/obtener_docente_por_nombre/<string:nombre_completo>", methods=["GET"])
def obtener_docente_por_nombre(nombre_completo):
    docente = controlador_docente.obtener_docente_por_nombre_completo(nombre_completo)
    return jsonify(docente)

# Ruta para agregar un nuevo docente
@router_docente.route("/agregar_docente", methods=["POST"])
def agregar_docente():
    numDoc = request.json.get('numDoc')
    nombre = request.json.get('nombre')
    apellidos = request.json.get('apellidos')
    cargo = request.json.get('cargo')
    correo = request.json.get('correo')
    idTipoDoc = request.json.get('idTipoDoc')
    idUsuario = request.json.get('idUsuario')
    
    resultado = controlador_docente.agregar_docente(numDoc, nombre, apellidos, cargo, correo, idTipoDoc, idUsuario)
    return jsonify(resultado)

# Ruta para modificar los datos de un docente
@router_docente.route("/modificar_docente", methods=["POST"])
def modificar_docente():
    numDoc = request.json.get('numDoc')
    nombre = request.json.get('nombre')
    apellidos = request.json.get('apellidos')
    cargo = request.json.get('cargo')
    correo = request.json.get('correo')
    idTipoDoc = request.json.get('idTipoDoc')
    idUsuario = request.json.get('idUsuario')

    resultado = controlador_docente.modificar_docente(numDoc, nombre, apellidos, cargo, correo, idTipoDoc, idUsuario)
    return jsonify(resultado)

# Ruta para dar de baja a un docente (cambiar su estado a inactivo)
@router_docente.route("/dar_de_baja_docente", methods=["POST"])
def dar_de_baja_docente():
    numDoc = request.json.get('numDoc')
    resultado = controlador_docente.dar_de_baja_docente(numDoc)
    return jsonify(resultado)

# Ruta para eliminar un docente
@router_docente.route("/eliminar_docente", methods=["POST"])
def eliminar_docente():
    numDoc = request.json.get('numDoc')
    resultado = controlador_docente.eliminar_docente(numDoc)
    return jsonify(resultado)
