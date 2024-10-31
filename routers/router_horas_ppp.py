from flask import Blueprint, jsonify, request
import controladores.controlador_horas_ppp as controlador_horas_ppp

router_horas_ppp = Blueprint('router_horas_ppp', __name__)

@router_horas_ppp.route("/datos_horas_ppp", methods=["GET"])
def datos_horas_ppp():
    id_estudiante = request.args.get('id')
    if id_estudiante is None:
        return jsonify({'error': 'ID del estudiante no proporcionado'}), 400

    horas_ppp = controlador_horas_ppp.obtener_horas_ppp(id_estudiante)

    return jsonify(horas_ppp)
