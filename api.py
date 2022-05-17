# Archivo principal para la API generada con Flask.
from flask import Flask

sonar.python.version=2.7, 3.7, 3.8, 3.9

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/")
def home():
    return "Hello, Flask!"
