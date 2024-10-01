from flask import (Flask,render_template,request,redirect,jsonify,url_for,make_response,session,)

import os
import hashlib
import datetime
import random
import time


#from werkzeug.utils import secure_filename
#from bd import obtener_conexion
from main import app


login_attempts = {}

@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("/login.html")