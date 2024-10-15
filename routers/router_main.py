from flask import Blueprint, render_template, request, redirect, jsonify, make_response, session

import hashlib
import random
import os
from werkzeug.utils import secure_filename
from bd import obtener_conexion
from bd import obtener_conexion
import controladores.controlador_usuario as controlador_usuario

import time

login_attempts = {}
router_main = Blueprint('router_main', __name__)

@router_main.route("/")
@router_main.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@router_main.route("/index")
def index():
    return render_template("/index.html")

@router_main.route("/procesar_login", methods=["POST"])
def procesar_login():
    try:
        conexion = obtener_conexion()
        if not conexion:
            # Retorna un mensaje claro de fallo de conexión
            return jsonify({
                'logeo': False,
                'mensaje': 'El servicio se encuentra inactivo.'
            }), 500
        username = request.json.get('username')
        password = request.json.get('password')
        #usuario = controlador_usuario.obtener_usuario_con_tipopersona_por_username(username)
        usuario = controlador_usuario.obtener_usuario_con_tipopersona_por_username(username)

        # Inicializar el diccionario de intentos para el usuario si no existe
        if username not in login_attempts:
            login_attempts[username] = {'attempts': 0, 'last_attempt_time': 0}
        """
        # Verificar si el usuario está bloqueado
        if login_attempts[username]['attempts'] >= 3 and (time.time() - login_attempts[username]['last_attempt_time']) < 300:
            return jsonify({'mensaje': 'Cuenta bloqueada. Intente de nuevo más tarde.', 'logeo': False})
        
        if usuario == None:
            return jsonify({'mensaje':'El usuario no existe', 'logeo':False})
        
        elif username != usuario[1]:
            return jsonify({'mensaje':'El username es incorrecto', 'logeo':False})
        
        elif not usuario[3]:
            return jsonify({'mensaje':'El usuario está inactivo', 'logeo':False})
        """
        #else:
        # Encriptar password ingresado por usuario
        h = hashlib.new("sha256")
        h.update(bytes(password, encoding="utf-8"))
        print(password)
        encpassword = h.hexdigest()
        if encpassword == usuario[3]:
            # Obteniendo token
            t = hashlib.new("sha256")
            entale = random.randint(1, 1024)
            strEntale = str(entale)
            t.update(bytes(strEntale, encoding="utf-8"))
            token = t.hexdigest()
            controlador_usuario.actualizar_token(username, token)

            """
            persona = controlador_persona.obtener_persona_por_id(usuario[4])
            foto = persona[9]
            nombre = persona[1].split()[0]
            """
            
            # Almacenar el ID del usuario en la sesión
            session['user_id'] = usuario[0]
            return jsonify({'logeo': True, 'token': token})
            #return jsonify({'logeo': True, 'token': token, 'foto':foto, 'nombre':nombre})
        else:
            print(password)
            print(encpassword)
            login_attempts[username]['attempts'] += 1
            login_attempts[username]['last_attempt_time'] = time.time()
            return jsonify({'mensaje': 'La contraseña es incorrecta', 'logeo': False})
    except NameError:
        return jsonify({'mensaje':'Error al procesar el login'+NameError, 'logeo':False})
    
@router_main.route('/home')
def home():
    return render_template('home.html')

@router_main.route('/estudiante')
def estudiante():
    return render_template('gestion_academica/estudiante.html')

@router_main.route('/ppp_registro')
def ppp_registro():
    return render_template('ppp_registro.html')

@router_main.route('/perfil')
def perfil():
    return render_template('perfil.html')

@router_main.route("/docente")
def docente():
    return render_template('dashboard/docente.html')  

@router_main.route("/facultad")
def facultad():
    return render_template('gestion_academica/facultad.html') 

@router_main.route("/escuela")
def escuela():
    return render_template('dashboard/escuela.html') 

@router_main.route("/InformeInicialEstudiante")
def informeInicialEstudiante():
    return render_template('gestion_academica/informeInicialEstudiante.html') 

@router_main.route("/InformeInicialEmpresa")
def informeInicialEmpresa():
    return render_template('gestion_academica/informeInicialEmpresa.html') 

