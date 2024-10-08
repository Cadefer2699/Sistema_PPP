from flask import Flask
from routers.router_main import router_main  # Importa el Blueprint
from routers.router_facultad import router_facultad


app = Flask(__name__)
app.debug = False
app.secret_key = 'super-secret'

# Registra el Blueprint
app.register_blueprint(router_main)
app.register_blueprint(router_facultad)


if __name__ == "__main__":
    app.run(debug=True)