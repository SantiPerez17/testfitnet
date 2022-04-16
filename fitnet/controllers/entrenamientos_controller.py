from flask import Flask,request,jsonify,make_response,Blueprint
from fitnet import app, db
from fitnet.models import * 



url_entrenamiento = Blueprint('entrenamiento', __name__)

@url_entrenamiento.route("/",methods=['POST'])
def entrenamiento():
	
	data = request.get_json()
	usuario=Usuario.query.filter_by(id_vinculo=data['id_vinculo']).first()
	if(not usuario):
		return jsonify({'message': 'no se pudo realizar la operacion'}),401
	if(Entrenamiento.query.filter_by(usuario_id=usuario.id,fecha=data['fecha']).first()):
		return jsonify({'message': 'entrenamiento ya existe'}),400
	new_entrenamiento = Entrenamiento(
		calorias_consumidas=data['calorias_consumidas'],
		cadencia=data['cadencia'],
		distancia=data['distancia'],
		rc_promedio=data['rc_promedio'],
		tiempo_actividad=data['tiempo_actividad'],
		pasos=data['pasos'],
		fecha=data['fecha'],
		usuario_id=usuario.id,
		deporte_id=data['deporte_id'],
		)

	db.session.add(new_entrenamiento)
	db.session.commit()

	return jsonify({'message': 'ok'}),200

