from sqlalchemy.orm import relationship
from fitnet import db
from flask_login import UserMixin

# @login_manager.user_loader
# def load_user(user_id):
#     return Usuario.query.get(int(user_id))


class Usuario(db.Model, UserMixin):
    __tablaname__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    id_vinculo= db.Column(db.String(10),unique=True)
    habilitado = db.Column(db.Boolean)
    fecha_registro = db.Column(db.DateTime, nullable=False)
    nombre = db.Column(db.String(20))
    apellido = db.Column(db.String(20))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    sexo = db.Column(db.String(20))
    estatura = db.Column(db.Float)
    peso = db.Column(db.Float)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    rol = db.Column(db.String(30))
    entrenamientos = db.relationship('Entrenamiento', backref='usuario', lazy=True)
    locacion_id = db.Column(db.Integer, db.ForeignKey('locaciones.id'), nullable=False)
    locacion = relationship("Locacion", lazy="joined", innerjoin=True)


    def __repr__(self):
        return f"Usuario('{self.nombre}','{self.apellido}', '{self.email}')"


class Locacion(db.Model):
    __tablename__ = "locaciones"
    id = db.Column(db.Integer, primary_key=True)
    provincia = db.Column(db.String(120))
    ciudad = db.Column(db.String(120))
    cp = db.Column(db.String(20))

    def __repr__(self):
        return f"Locacion('{self.id}','{self.ciudad}', '{self.provincia}', '{self.cp}')"


class Entrenamiento(db.Model):
    __tablename__ = "entrenamientos"
    id = db.Column(db.Integer, primary_key=True)
    calorias_consumidas = db.Column(db.Float)
    cadencia = db.Column(db.Float)
    distancia = db.Column(db.Float)
    rc_promedio = db.Column(db.Float)
    tiempo_actividad = db.Column(db.Float)
    pasos = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    deporte_id = db.Column(db.Integer, db.ForeignKey('deporte.id'), nullable=False)
    deporte = relationship("Deporte", lazy="joined", innerjoin=True)

    def __repr__(self):
        return f"Entrenamiento('{self.id}', {self.deporte_id})"


class Deporte(db.Model):
    __table__name = "deportes"
    id = db.Column(db.Integer, primary_key=True)
    denominacion = db.Column(db.String(20))

    def __repr__(self):
        return f"Deporte('{self.id}', '{self.denominacion}')"