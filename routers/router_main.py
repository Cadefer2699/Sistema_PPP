from flask import Blueprint, render_template, request

# Crea el Blueprint
router_main = Blueprint('router_main', __name__)

# Define las rutas en el blueprint
@router_main.route("/")
@router_main.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")