# Archivo principal para la API generada con Flask.
from flask import Flask

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/")
def home():
    return "Hello, Flask!"
