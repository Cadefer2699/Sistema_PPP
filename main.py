from flask import Flask
from routers.router_main import router_main  # Importa el Blueprint

app = Flask(__name__)
app.debug = False
app.secret_key = 'super-secret'

# Registra el Blueprint
app.register_blueprint(router_main)

if __name__ == "__main__":
    app.run(debug=True)