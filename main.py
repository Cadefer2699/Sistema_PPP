from flask import Flask
from routers.router_main import router_main  # Importa el Blueprint
from routers.router_facultad import router_facultad
from routers.router_estudiante import router_estudiante
from routers.router_docente import router_docente


app = Flask(__name__)
app.debug = False
app.secret_key = 'super-secret'

# Registra el Blueprint
app.register_blueprint(router_main)
app.register_blueprint(router_facultad)
app.register_blueprint(router_estudiante)
app.register_blueprint(router_docente)


if __name__ == "__main__":
    app.run(debug=True)