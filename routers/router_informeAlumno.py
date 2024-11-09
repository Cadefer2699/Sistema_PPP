from flask import Blueprint, jsonify, request, render_template
import controladores.controlador_informeAlumno as controlador_informeAlumno

router_informeAlumno = Blueprint('router_informeAlumno', __name__)

@router_informeAlumno.route("/informeAlumno")
def informeAlumno():
    return render_template('ppp/InformesAlumno.html')

@router_informeAlumno.route("/datos_informesAlumnos", methods=["GET"])
def datos_informesAlumnos():
    informesAlumnos = controlador_informeAlumno.obtener_informeAlumno()
    return jsonify(informesAlumnos)