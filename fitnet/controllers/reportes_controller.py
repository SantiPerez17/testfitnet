########################################################################
#
#					ACA PODRIA IR TODO LO QUE ES REPORTES
#
########################################################################


from flask import Flask,request,jsonify,make_response,Blueprint
from fitnet.models import * 
from fitnet import app, db
from fitnet.you_shall_not_pass import Login_rol_required
import datetime
from sqlalchemy import func

url_reportes = Blueprint('reportes', __name__)




@url_reportes.route('/calorias', methods=['GET'])
@Login_rol_required(roles=['usuario'])
def reportar_calorias(usuario):		# Funcion que recibe un id de usuario, una fecha inicial (por defecto el primer dia del mes a las 00:00:00 hs), una fecha final (por defecto la fecha actual) y un deporte (por defecto se consideran todos) y devuelve la cantidad max, min, promedio y total de calorias consumidas en los entrenamientos desde la fecha inicial a la final y del deporte elegido o todos los deportes.

	cond=parametros_busqueda(request,usuario)
	val=Entrenamiento.calorias_consumidas
	
	tot_calorias = db.session.query(func.sum(val)).filter(*cond).first() [0]      
	prom_calorias = db.session.query(func.avg(val)).filter(*cond).first() [0]
	max_calorias = db.session.query(func.max(val)).filter(*cond).first() [0]
	min_calorias = db.session.query(func.min(val)).filter(*cond).first() [0]
	return jsonify({'max_calorias': max_calorias, 'min_calorias' : min_calorias, 'prom_calorias' : prom_calorias, 'total_calorias' : tot_calorias})


@url_reportes.route('/cadencia', methods=['GET'])
@Login_rol_required(roles=['usuario'])
def reportar_cadencia(usuario):
	cond=parametros_busqueda(request,usuario)
	val=Entrenamiento.cadencia

	max_cadencia = db.session.query(func.max(val)).filter(*cond).first() [0]
	min_cadencia = db.session.query(func.min(val)).filter(*cond).first() [0]
	avg_cadencia = db.session.query(func.avg(val)).filter(*cond).first() [0]
	tot_cadencia = db.session.query(func.sum(val)).filter(*cond).first() [0]

	return jsonify({'max_cadencia':max_cadencia,'min_cadencia':min_cadencia,'avg_cadencia':avg_cadencia,'tot_cadencia':tot_cadencia })

@url_reportes.route('/pasos', methods=['GET'])
@Login_rol_required(roles=['usuario'])
def reportar_pasos(usuario):

	cond=parametros_busqueda(request,usuario)
	val=Entrenamiento.cadencia

	max_pasos = db.session.query(func.max(val)).filter(*cond).first() [0]
	min_pasos = db.session.query(func.min(val)).filter(*cond).first() [0]
	avg_pasos = db.session.query(func.avg(val)).filter(*cond).first() [0]
	tot_pasos = db.session.query(func.sum(val)).filter(*cond).first() [0]

	return jsonify({'max_pasos':max_pasos,'min_pasos':min_pasos,'tot_pasos':tot_pasos})



@url_reportes.route('/velocidad', methods=['GET'])
@Login_rol_required(roles=['usuario'])
def reportar_velocidad(usuario):
	
	cond=parametros_busqueda(request,usuario)
	val=Entrenamiento.distancia / Entrenamiento.tiempo_actividad

	velocidad_max = db.session.query(func.max(val)).filter(*cond).first() [0]
	velocidad_min = db.session.query(func.min(val)).filter(*cond).first() [0]
	velocidad_prom = db.session.query(func.avg(val)).filter(*cond).first() [0]

	return jsonify({'velocidad_prom':velocidad_prom,'velocidad_max':velocidad_max,'velocidad_min':velocidad_min })


@url_reportes.route('/distancia', methods=['GET'])
@Login_rol_required(roles=['usuario'])
def reportarDistancia(usuario):

	cond=parametros_busqueda(request,usuario)
	val=Entrenamiento.cadencia

	distanciaMaximaORM = db.session.query(func.max(val)).filter(*cond).first() [0]
	distanciaMinimaORM = db.session.query(func.min(val)).filter(*cond).first() [0]
	distanciaPromedioORM = db.session.query(func.avg(val)).filter(*cond).first() [0]
	distanciaTotalORM = db.session.query(func.sum(val)).filter(*cond).first() [0]

	return jsonify({'max_distance': distanciaMaximaORM,'min_distance': distanciaMinimaORM,'avg_distance': distanciaPromedioORM,'total_distance': distanciaTotalORM})


@url_reportes.route('/tiempo', methods=['GET'])
@Login_rol_required(roles=['usuario'])
def reportarTiempo(usuario):
	cond=parametros_busqueda(request,usuario)
	val=Entrenamiento.cadencia

	tiempoMaximoORM = db.session.query(func.max(val)).filter(*cond).first() [0]
	tiempoMinimoORM = db.session.query(func.min(val)).filter(*cond).first() [0]
	# se reporta tiempo promedio? tiempo_Prom= db.session.query(func.avg(val)).filter(*cond).first() [0]          
	tiempoTotalORM = db.session.query(func.sum(val)).filter(*cond).first() [0]

	return jsonify({'max_time': tiempoMaximoORM,'min_time': tiempoMinimoORM,'total_time': tiempoTotalORM})#,'avg_time':tiempo_Prom})




@url_reportes.route('/ritmocardiaco', methods=['GET'])
@Login_rol_required(roles=['usuario'])
def reportar_ritmo_cardiaco(usuario):
	
	cond=parametros_busqueda(request,usuario)
	val=Entrenamiento.cadencia

	ritmocardiacomax = db.session.query(func.max(val)).filter(*cond).first() [0]
	ritmocardiacomin = db.session.query(func.min(val)).filter(*cond).first() [0]

	return jsonify({'ritmocardiacomax': ritmocardiacomax,'ritmocardiacomin': ritmocardiacomin})


@url_reportes.route('/distanciatotalrecorrida', methods=['GET'])
@Login_rol_required(roles=['operario'])
def reportar_distancia_total_recorrida(usuario):   

	distancia_total_recorrida = db.session.query(func.sum(Entrenamiento.distancia)).all() [0][0]       # Sumo la distancia recorrida de todos los entraenamientos. Tomo el primer valor de la lista ya que es uno solo y el primer lugar de la tupla que es donde se encuentra el valor.
	return jsonify({'distancia_total_recorrida': distancia_total_recorrida})

@url_reportes.route('/deportemenospracticado', methods=['GET'])
@Login_rol_required(roles=['operario'])
def reporte_deporte_menos_practicado(operario):
	
	deporteMenosPrac= db.session.query(Deporte.denominacion,func.count(Entrenamiento.deporte_id)).join(Deporte, Deporte.id == Entrenamiento.deporte_id).group_by(Entrenamiento.deporte_id,Deporte.denominacion).order_by((func.count(Entrenamiento.deporte_id)).asc()).first() [0]
	return jsonify({'deporteMenosPrac':deporteMenosPrac})

@url_reportes.route('/deportemaspracticado', methods=['GET'])
@Login_rol_required(roles=['operario'])
def reportar_deporte_mas_practicado(operario):

	deporte_mas_practicado= db.session.query(Deporte.denominacion,func.count(Entrenamiento.deporte_id)).join(Deporte, Deporte.id == Entrenamiento.deporte_id).group_by(Entrenamiento.deporte_id,Deporte.denominacion).order_by((func.count(Entrenamiento.deporte_id)).desc()).first() [0]

	return jsonify({'deporte_mas_practicado':deporte_mas_practicado})



@url_reportes.route('/top10', methods=['GET'])
@Login_rol_required(roles=['operario'])
def Top10(operario):
        top10_pasos =  db.session.query(Usuario.email, func.sum(Entrenamiento.pasos)).join(Usuario, Usuario.id == Entrenamiento.usuario_id).group_by(Usuario.email).order_by(func.sum(Entrenamiento.pasos).desc()).limit(10).all()
        top10_distancia = db.session.query(Usuario.email, func.sum(Entrenamiento.distancia)).join(Usuario, Usuario.id == Entrenamiento.usuario_id).group_by(Usuario.email).order_by(func.sum(Entrenamiento.distancia).desc()).limit(10).all()
        return jsonify({'top10pasos' : top10_pasos, 'top10distancia': top10_distancia})

def parametros_busqueda(request,usuario):
	
	data,fecha_inicio,fecha_fin,id_dep=tuple([None]*4) #asigno None a todo
	
	try:
		data = request.get_json()
	except Exception as e:
		pass

	if data != None: # implica que algun parametro le pase, pero no se cual.
		fecha_inicio = data.get('fecha_inicio')
		fecha_fin = data.get('fecha_fin')
		id_dep=data.get('deportes')

	#print(fecha_inicio,fecha_fin,id_dep)
	#asigno valor por defecto si la variable continua siendo None. 
	if not fecha_inicio:fecha_inicio= datetime.datetime.utcnow().replace(day=1,hour=0,minute=0,second=0,microsecond=0)
	if not fecha_fin:fecha_fin= str(datetime.datetime.utcnow()) 
	#deportes_bd_tuplas = db.session.query(Deporte.id).all()
	deportes_bd_id = [_id[0] for _id in db.session.query(Deporte.id).all()]

	if not id_dep:
		id_dep = deportes_bd_id
	else:
		for x in id_dep:
			if x not in deportes_bd_id:
				raise Exception("Error al pasar los id de deportes.") 
	#Falta capturar el error


	
	return [Entrenamiento.usuario_id == usuario.id , 
			Entrenamiento.deporte_id.in_(tuple(id_dep)),
			Entrenamiento.fecha.between(fecha_inicio, fecha_fin)]