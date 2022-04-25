from flask import Flask, request, jsonify, make_response, Blueprint
from fitnet import app, db
from fitnet.models import *
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import random
import smtplib
import ssl
from fitnet.you_shall_not_pass import Login_rol_required
import re

@app.route("/")
@app.route("/home", methods=['GET'])
@Login_rol_required(roles=['usuario'])
def home(usuario):
	pdb.set_trace()
	return f'<h1>hola{usuario.nombre}</h1>'


url_usuario = Blueprint('usuario', __name__)


@url_usuario.route('/registro', methods=['POST'])
def signup_user():

	data = request.get_json()
	for val in data.values():
		if val == None:
			return jsonify({'message': 'campo nulo'}),400

	if(not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',data['email'])):
		return jsonify({'message': 'el email ingresado no es valido'}),400	

	if(Usuario.query.filter_by(email=data['email']).first() != None):
		return jsonify({'message': 'el email ya esta registrado'}),400
	

	hashed_password = generate_password_hash(data['password'], method='sha256')
	# public_id=str(uuid.uuid4()),admin=False

	new_user = Usuario(
		id_vinculo=nuevo_vinculo(),
		fecha_registro=datetime.datetime.utcnow(),
		email=data['email'],
		nombre=data['nombre'],
		password=hashed_password,
		apellido=data['apellido'],
		sexo=data['sexo'],
		estatura=data['estatura'],
		peso=data['peso'],
		fecha_nacimiento=data['fecha_nacimiento'],
		habilitado=False,
		rol='usuario',
		locacion_id=data['locacion_id'])

	db.session.add(new_user)
	db.session.commit()
	#enviar_email(new_user, 'confirmar')
	return jsonify({'message': 'ya casi estamos! solo fata que entre al link de confirmar cuenta que enviamos a su email.'})


@url_usuario.route('/new_operario', methods=['POST'])
@Login_rol_required(roles=['admin'])
def alta_operario():
	data = request.get_json()
	for val in data.values():
		if val == None:
			return jsonify({'message': 'campo nulo'}),400

	if(not re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',data['email'])):
		return jsonify({'message': 'el email ingresado no es valido'}),400	

	if(Usuario.query.filter_by(email=data['email']).first() != None):
		return jsonify({'message': 'el email ya esta registrado'}),400
	
	new_operario = Usuario(
		id_vinculo=nuevo_vinculo(),
		fecha_registro=datetime.datetime.utcnow(),
		nombre=data['nombre'],
		password=hashed_password,
		apellido=data['apellido'],
		email=data['email'],
		sexo=data['sexo'],
		estatura=data['estatura'],
		peso=data['peso'],
		fecha_nacimiento=data['fecha_nacimiento'],
		habilitado=True,
		rol='operario',
		locacion_id=data['locacion_id'])

	db.session.add(new_operario)
	db.session.commit()

	return jsonify({'message': 'operario creado'})


@url_usuario.route('/confirm', methods=['GET'])
def confirm():

	token = request.args.get('tk')
	try:
		token = jwt.decode(token, app.config['SECRET_KEY'])
	except Exception as e:
		return jsonify({'message': 'error, el link ha caducado o es invalido4'})
		# raise e

	email = token['email']
	user = Usuario.query.filter_by(email=email).first()

	if ((datetime.datetime.utcnow()-user.fecha_registro) < datetime.timedelta(minutes=59)):
		user.habilitado = True
		db.session.commit()
		return jsonify({'message': 'listo! ya estas reistrado'})
	else:
		return jsonify({'message': 'error, el link ha caducado o es invalido'})


@url_usuario.route('/login', methods=['GET', 'POST']) # Sensitive
def login_user():

	auth = request.authorization
	if not auth or not auth.username or not auth.password:
		return make_response('could not verify', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

	user = Usuario.query.filter_by(email=auth.username).first()

	if check_password_hash(user.password, auth.password):
		token = jwt.encode({'email': user.email, 'exp': datetime.datetime.utcnow(
		) + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
		return jsonify({'token': token.decode('UTF-8')})

	return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})


def nuevo_vinculo():
	id_vinculo = ""
	while True:
		id_vinculo = str(random.randrange(0, 9999999999))
		id_vinculo = "0"*(10-len(id_vinculo))+id_vinculo
		if (Usuario.query.filter_by(id_vinculo=id_vinculo).first() == None):
			return id_vinculo

# el usuario no recuerda su contraseña. se le envia un link  a su email


@url_usuario.route('/pedirnuevapass', methods=['GET'])
def pedir_nueva_pass():

	data = request.get_json()
	user = Usuario.query.filter_by(email=data['email']).first()
	if (user):
		enviar_email(user, 'cambio_pass')
	else:
		return jsonify({'message': 'el email es invalido'})
	return jsonify({'message': 'se ha enviado a su email un link para que pueda cambiar su password'})

# este metodo retorna un token de autenticacion. Solo puede ser accedido si el usuario ingreso al link envido a su email


@url_usuario.route('/nuevapass', methods=['GET'])
def nuevapass():
	token = request.args.get('tk')
	try:
		token = jwt.decode(token, app.config['SECRET_KEY'])
	except Exception as e:
		return jsonify({'message': 'error, el link ha caducado o es invalido'})

	token = jwt.encode({'email': token['email'], 'exp': datetime.datetime.utcnow(
	) + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
	return jsonify({'token': token.decode('UTF-8')})

# cambio de contraseña, solo se puede usar si el usuario tiene un token valido.


@url_usuario.route('/cambiopass', methods=['PUT'])
@Login_rol_required(roles=['usuario', 'operario', 'admin'])
def cambio_pass(usuario):
	data = request.get_json()
	new_pass = generate_password_hash(data['password'], method='sha256')
	usuario.password = new_pass
	db.session.commit()
	return jsonify({'message': 'Contrasenia cambiada'})


def enviar_email(user, tipo):
	destinatario = user.email
	token = jwt.encode({'email': user.email, 'rnd': random.randrange(
	    0, 10000000)}, app.config['SECRET_KEY']).decode('UTF-8')
	if tipo == 'confirmar':
		mensage = f'''\\
de: fitnet@gdp2020.com
Subject: confirmacion de cuenta'
http://127.0.0.1:8080/usuario/confirm?tk={token}
'''
	elif tipo == 'cambio_pass':
		mensage = f'''\\
de: fitnet@gdp2020.com
Subject: cambio password'
http://127.0.0.1:8080/usuario/nuevapass?tk={token}
'''

	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	fitnet_email = ""
	password = ""

	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(fitnet_email, password)
		server.sendmail(fitnet_email, destinatario, mensage)
	print(mensage)


@url_usuario.route('/update/<id>', methods=['PUT'])
def update(id):

        user = Usuario.query.get(id)

        nombre = request.json['nombre']
        apellido = request.json['apellido']
        email = request.json['email']
        sexo = request.json['sexo']
        estatura = request.json['estatura']
        peso = request.json['peso']
        fecha_nacimiento = request.json['fecha_nacimiento']
        
        
        if nombre != "None":
            user.nombre=nombre
        if apellido != "None":
            user.apellido=apellido
        if email != "None":
            user.email=email
        if sexo != "None":
            user.sexo=sexo
        if estatura != 0.0:
            user.estatura=estatura
        if peso != 0.0:
            user.peso=peso
        if fecha_nacimiento != "None":
            user.fecha_nacimiento=fecha_nacimiento
      
     
 
        db.session.commit()

      
        
        return jsonify({'message':'Datos actualizados correctamente'})
