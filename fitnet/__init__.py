from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c9f2907c6e760b384f32e59aae8cd529'

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/flask"

db = SQLAlchemy(app)
#from fitnet import models
#db.create_all()


from .controllers.usuarios_controller import url_usuario
from .controllers.reportes_controller import url_reportes
from .controllers.entrenamientos_controller import url_entrenamiento
app.register_blueprint(url_usuario, url_prefix="/usuario")
app.register_blueprint(url_reportes, url_prefix="/reportes")
app.register_blueprint(url_entrenamiento, url_prefix="/entrenamiento")


@app.errorhandler(404)
def error_404(e):
    return jsonify(error=str(e), message='URL Inválida.')
