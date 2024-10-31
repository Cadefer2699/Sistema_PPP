from flask import Blueprint, jsonify
import controladores.controlador_semestre as controlador_semestre

router_semestre = Blueprint('router_semestre', __name__)

# Ruta para obtener la lista de semestres
@router_semestre.route("/datos_semestres", methods=["GET"])
def datos_semestres():
    semestres = controlador_semestre.obtener_semestres()
    return jsonify(semestres)
