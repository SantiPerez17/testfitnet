import datetime
import pytest
import requests
import json
#from fitnet import app



'''
Para realizar los tests utilizaremos dos librerias: requests y pytest. (Para mas información en la wiki)

Los test se definen se esta forma 
   
	def test_index_page():
	r = requests.get(url+'/test') # Assumses that it has a path of "/"
	assert r.status_code == 200 # Assumes that it will return a 200 response

Para correrlos, parados en master, ejecutar pytest tests.py -s

El flag -s nos permite ver los prints que ponemos a las funciones de tests..

'''



url = 'http://127.0.0.1:8080' # URL RAIZ
token_usuario='' # se inicializa al correr test_login
token_operario=''
token_admin=''

#-------------------------------------------test usuarios---------------------
#CODIGO DE TEST 900: LOGIN DE USUARIO Y DE OPERARIO
#IMPORTANTE: ESTOS TESTS TIENEN QUE IR PRIMEROS QUE TODOS.


def test_login_usuario():

	response = requests.get(url + '/usuario/login', headers={'Authorization': 'Basic amdvbnphbGVzQGdtYWlsLmNvbToxMjM0'})
	assert response.status_code==200
	global token_usuario
	token_usuario='bearer  ' + response.json()['token']

def test_login_operario():

	response = requests.get(url + '/usuario/login', headers={'Authorization':'Basic b3BlcmFyaW9AZ21haWwuY29tOjEyMzQ='})
	assert response.status_code==200
	global token_operario
	token_operario='bearer  ' + response.json()['token']

#CODIGO DE TEST 901: LOGIN DE USUARIO ADMIN 
def test_login_admin():

	response = requests.get(url + '/usuario/login', headers={'Authorization': 'Basic YWRtaW5AZ21haWwuY29tOjEyMzQ='})
	assert response.status_code==200
	global token_admin
	token_admin='bearer  ' + response.json()['token']

def test_update_usuario():
		#Le paso la id del usuario que se logueo en la función de más arriba. 
		# Cambio el nombre solamente
		data = {"nombre": "Juan", "apellido": "None", "email": "None","sexo": "None", "estatura": 0.0, "peso": 0.0, "fecha_nacimiento":"None"} 
		response = requests.put(url + '/usuario/update/2', json=data)
		
		print('test_update_usuario')
		print(response.content.decode('utf8'))
		assert response.status_code == 200 


#-------------------------------------test reportes----------------------------
#CODIGO DE TEST 101: SOLICITAR REPORTE SIN HABERSE LOGUEADO PARA DISTANCIA
def test_no_login_request_report_distancia():
	r = requests.get(url+'/reportes/distancia') # Elegimos un reporte al azar
	assert r.status_code == 401 # Asumimos que esto nos devolvera un 401, error de acceso no autorizado

#CODIGO DE TEST 102: SOLICITAR REPORTE SIN HABERSE LOGUEADO PARA TIEMPO
def test_no_login_request_report_tiempo():
	r = requests.get(url + '/reportes/tiempo')
	assert r.status_code == 401

#CODIGO DE TEST 103: SOLICITAR REPORTE SIN HABERSE LOGUEADO PARA CALORIAS
def test_no_login_request_report_calorias():
	r = requests.get(url + '/reportes/calorias')
	assert r.status_code == 401

#CODIGO DE TEST 104: SOLICITAR REPORTE SIN HABERSE LOGUEADO PARA VELOCIDAD
def test_no_login_request_report_velocidad():
	r = requests.get(url + '/reportes/velocidad')
	assert r.status_code == 401

#CODIGO DE TEST 105: CONSULTA REPORTES ID DEPORTES ERRONEOS
def test_get_reporte_calorias_deportes_erroneos():
	
	data = {'fecha_inicio':'2020-01-01',
			'fecha_fin':'2020-06-02',
			'deportes':["asd",2,3,4]}


	response = requests.get(url + '/reportes/calorias',  json=data, headers={'Authorization': token_usuario})
	print('test_get_reporte_calorias_deportes_erroneos')
	print(response.content.decode('utf8'))
	assert response.status_code == 400

#CODIGO DE TEST 106: CONSULTA REPORTES FECHA ERRONEA
def test_get_reporte_calorias_fecha_erronea():
	
	data = {'fecha_inicio':'2020-01-01',
			'fecha_fin':"asd",
			'deportes':[1,2,3,4]}


	response = requests.get(url + '/reportes/calorias',  json=data, headers={'Authorization': token_usuario})
	print('test_get_reporte_calorias_fecha_erronea')
	print(response.content.decode('utf8'))
	assert response.status_code == 400


#CODIGO DE TEST 110: REPORTE CON EMISION DE PARAMETROS PARA DISTANCIA
def test_get_reporte_distancia():
	
	
	data = {'fecha_inicio':'2020-01-01',
			'fecha_fin':'2020-06-02',
			'deportes':[1,2,3,4]}
	

	response = requests.get(url + '/reportes/distancia',  json=data, headers={'Authorization': token_usuario})
	print('test_get_reporte_distancia')
	print(response.content.decode('utf8'))
	assert response.status_code == 200 


# CODIGO DE TEST 111: REPORTE CON EMISION DE PARAMETROS PARA TIEMPO
def test_get_reporte_tiempo():
	
	data = {
		
		'fecha_inicio':'2020-01-01',
		'fecha_fin':'2020-06-02',
		'deportes':[1,2,3,4]
		
	}
	
	response = requests.get(url + '/reportes/tiempo', json = data, headers = {'Authorization':token_usuario})
	print('test_get_reporte_tiempo')
	print(response.content.decode('utf8'))
	assert response.status_code == 200


#CODIGO DE TEST 112: REPORTE CON EMISION DE PARAMETROS PARA CALORIAS
def test_get_reporte_calorias():
	data = {
		
		'fecha_inicio':'2020-01-01',
		'fecha_fin':'2020-06-02',
		'deportes':[1,2,3,4]
																			 
	}
	
	response = requests.get(url + '/reportes/calorias', json = data, headers = {'Authorization':token_usuario})
	print('test_get_reporte_calorias')
	print(response.content.decode('utf8'))
	assert response.status_code == 200

#CODIGO DE TEST 113: REPORTE CON EMISION DE PARAMETROS PARA VELOCIDAD
def test_get_reporte_velocidad():
	data = {
		
		'fecha_inicio':'2020-01-01',
		'fecha_fin':'2020-06-02',
		'deportes':[1,2,3,4]
																			 
	}
	
	response = requests.get(url + '/reportes/velocidad', json = data, headers = {'Authorization':token_usuario})
	print('test_get_reporte_velocidad')
	print(response.content.decode('utf8'))
	assert response.status_code == 200

#CODIGO DE TEST 130: REPORTE CON OMISION DE PARAMETROS PARA DISTANCIA
def test_get_reporte_distancia_omision_parametros():
  
	response = requests.get(url + '/reportes/distancia', headers={'Authorization': token_usuario})
	print('test_get_reporte_distancia')
	print(response.content.decode('utf8'))
	assert response.status_code == 200 


# CODIGO DE TEST 131: REPORTE CON OMISION DE PARAMETROS PARA TIEMPO
def test_get_reporte_tiempo_omision_parametros():
	
	response = requests.get(url + '/reportes/tiempo', headers = {'Authorization':token_usuario})
	print('test_get_reporte_tiempo')
	print(response.content.decode('utf8'))
	assert response.status_code == 200


#CODIGO DE TEST 132: REPORTE CON OMISION DE PARAMETROS PARA CALORIAS
def test_get_reporte_calorias_omision_parametros():
	
	response = requests.get(url + '/reportes/calorias', headers = {'Authorization':token_usuario})
	print('test_get_reporte_calorias')
	print(response.content.decode('utf8'))
	assert response.status_code == 200

#CODIGO DE TEST 133: REPORTE CON OMISION DE PARAMETROS PARA VELOCIDAD
def test_get_reporte_velocidad_omision_parametros():
	
	response = requests.get(url + '/reportes/velocidad', headers = {'Authorization':token_usuario})
	print('test_get_reporte_velocidad')
	print(response.content.decode('utf8'))
	assert response.status_code == 200

#CODIGO DE TEST 203_CONSULTA_REPORTES_RITMO_CARDIACO_CON_DEPORTE
def test_get_ritmo_cardiaco_deporte_1():

	data = {'fecha_inicio':'2020-01-01',
			'fecha_fin':'2020-06-30',
			'deportes':[1]}
	
	r = requests.get(url + '/reportes/ritmocardiaco', json=data, headers={'Authorization': token_usuario})
	print('test_get_ritmo_cardiaco_deporte_1')
	print(r.content.decode('utf8'))
	assert r.status_code == 200 #OK

# CODIGO DE TEST 204_CONSULTA_REPORTES_RITMO_CARDIACO_SIN_DEPORTE
def test_get_ritmo_cardiaco_deporte_2():


	data = {'fecha_inicio':'2020-01-01',
			'fecha_fin':'2020-06-30',
			'deportes':''}


	r = requests.get(url + '/reportes/ritmocardiaco', json=data, headers={'Authorization': token_usuario})
	print('test_get_ritmo_cardiaco_deporte_2')
	print(r.content.decode('utf8'))
	assert r.status_code == 200 #OK

#--------------------------------------Test Carga de Nuevos Entrenamientos--------------------------------------------

#carga nuevo entrenamiento happy path
def test_create_entrenamiento_happy_path():
	data={
"id_vinculo":"1111111111",
"calorias_consumidas":"918.0",
"cadencia":"100",
"distancia":"10000",
"rc_promedio":"21",
"tiempo_actividad":"54",
"pasos":"321",
"fecha":str(datetime.datetime.utcnow()),
"deporte_id":1
}
	response = requests.post(url + '/entrenamiento/', json = data, headers = {'Authorization':token_usuario})
	assert response.status_code == 200

# carga nuevo entrenamiento id_vinculo 
def test_create_entrenamiento_id_incorrecto():
	data={
"id_vinculo":"8888888888",
"calorias_consumidas":"918.0",
"cadencia":"100",
"distancia":"10000",
"rc_promedio":"21",
"tiempo_actividad":"54",
"pasos":"321",
"fecha":str(datetime.datetime.utcnow()),
"deporte_id":1
}
	response = requests.post(url + '/entrenamiento/', json = data, headers = {'Authorization':token_usuario})
	assert response.status_code == 401

#--------------------------------------Test Reportes Top10--------------------------------------------
  
# CODIGO DE TEST 205-1: SOLICITAR REPORTE TOP10 CON USUARIO OPERARIO
def test_top10():
	#primero hay que loguearse con el usuario que pueda realizar esta consulta (operario), para poder trabajar bien en el pedido.
	#a tener en cuenta que los token son temporales, al realizar el test en el futuro se debe de generar uno nuevo.

	r = requests.get(url + '/reportes/top10', headers={'Authorization': token_operario})
	assert r.status_code == 200
	print('test_top10')
	print (r.content.decode('utf8'))
	#anduvo, voy a probar con un usuario que seguramente falle.

# CODIGO DE TEST 205-2: SOLICITAR REPORTE TOP10 CON USUARIO NO OPERARIO
def test_top10_no_operario():
	r = requests.get(url + '/reportes/top10', headers={'Authorization': token_usuario})
	assert r.status_code == 401 #Falló por ende 401 por no ser tipo de usuario 'Operario'
	print('test_top10_no_operario')
	print (r.content.decode('utf8'))

# CODIGO DE TEST 205-3: SOLICITAR REPORTE TOP10 SIN HABERSE LOGUEADO
def test_top10_no_logueado():
	#En este caso al no estar logueado no puede acceder a esta peticion.
	r = r = requests.get(url + '/reportes/top10')
	assert r.status_code == 401
	print('test_top10_no_logueado')
	print (r.content.decode('utf8')) 


#--------------------------------------Test Reportes Globales--------------------------------------------

#CODIGO DE TEST 220: CONSULTA REPORTES DISTANCIA TOTAL RECORRIDA CORRECTA
def test_get_reporte_distanciatotalrecorrida():

	response = requests.get(url + '/reportes/distanciatotalrecorrida', headers = {'Authorization':token_operario})
	print('test_get_reporte_distanciatotalrecorrida')
	print(response.content.decode('utf8'))
	assert response.status_code == 200


# CODIGO DE TEST 202: CONSULTA REPORTES GLOBAL DEPORTE MENOS PRACTICADO
def test_deporte_menos_practicado():

	r = requests.get(url + '/reportes/deportemenospracticado', headers={'Authorization': token_operario})
	assert r.status_code == 200 #OK
	print('test_deporte_menos_practicado')
	print (r.content.decode('utf8'))

#--------------------------------------Test Registro de Usuarios--------------------------------------------

#CODIGO DE TEST 300: CREACION USUARIO OPERARIO 
def test_get_creacion_usuario_operario():
	
	data={
		"email":"operario@gmail.com",
		"nombre":"operario",
		"password":"1234",
		"apellido":"Menem",
		"sexo":"m",
		"estatura":180,
		"peso":70,
		"fecha_nacimiento":"1996-12-31",
		"rol":"operario",
		"locacion":1
		}

	response = requests.post(url + '/usuario/new_operario', json=data, headers = {'Authorization':token_admin})
	print('test_get_creacion_usuario_operario')

	assert response.status_code == 200

#CODIGO DE TEST 310: REGISTRO CON FORMATO INCORRECTO DE MAIL 
def test_registro_formato_mail():
	

	data = {
	'email':'esto.es-un#mail!invalido',
	'nombre':'Raul',
	'password':'Raul no sabe lo que es un email',
	'apellido':'Raul sin email',
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
	} 


	response = requests.post(url + '/usuario/registro',  json=data)
	print('test_registro_formato_mail')
	print(response.content.decode('utf8'))
	assert response.status_code == 400 #BAD REQUEST



#CODIGO DE TEST 311: REGISTRO CON EMAIL CORRECTO Y REGISTRO CON EMAIL REPETIDO 
def test_registro_mail_repetido():
	
	data1={ 
	'email':'raulahoratieneemail@gmail.com',
	'nombre':'Raul',
	'password':'dsfs4',
	'apellido':'Peron',
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
} 
	data2 = {
	'email':'raulahoratieneemail@gmail.com',
	'nombre':'Raul',
	'password':'dsfs4',
	'apellido':'Peron',
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
} 
	response1 = requests.post(url + '/usuario/registro',  json=data1)
	response2 = requests.post(url + '/usuario/registro',  json=data2 )
	print('test_registro_mail_repetido')
	#print(response.content.decode('utf8'))
	assert response1.status_code == 200
	assert response2.status_code == 400

#Funciona, cuando lo vuelvan a probar borren los datos de la bd o no va a pasar el test


# #CODIGO DE TEST 312: REGISTRO CON CAMPOS VACIOS
def test_registro_campos_vacios():
	


	#MAIL VACIO
	data1={ 
	'email':None,
	'nombre':'Raul',
	'password':'dsfs4',
	'apellido':'Peron',
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
} 


	#NOMBRE VACIO
	data2={ 
	'email':'raulahoratieneemail@gmail.com',
	'nombre':None,
	'password':'dsfs4',
	'apellido':'Peron',
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
} 

	#PASSWORD VACIA
	data3={ 
	'email':'raulahoratieneemail@gmail.com',
	'nombre':'Raul',
	'password':None,
	'apellido':'Peron',
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
} 

	#APELLIDO VACIO
	data4={ 
	'email':'raulahoratieneemail@gmail.com',
	'nombre':'Raul',
	'password':'dsfs4',
	'apellido':None,
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
} 

	#SEXO VACIO
	data5={ 
	'email':'raulahoratieneemail@gmail.com',
	'nombre':'Raul',
	'password':'dsfs4',
	'apellido':'Peron',
	'sexo':None,
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
} 

	#ESTATURA VACIA
	data6={ 
	'email':'raulahoratieneemail@gmail.com',
	'nombre':'Raul',
	'password':'dsfs4',
	'apellido':'Peron',
	'sexo':'-',
	'estatura':None,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
} 

	#PESO VACIO
	data7={ 
	'email':'raulahoratieneemail@gmail.com',
	'nombre':'Raul',
	'password':'dsfs4',
	'apellido':'Peron',
	'sexo':'-',
	'estatura':180,
	'peso':None,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':1
} 

	#FECHA_VACIA
	data8={ 
	'email':'raulahoratieneemail@gmail.com',
	'nombre':'Raul',
	'password':'dsfs4',
	'apellido':'Peron',
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':None,
	'locacion_id':1
} 

	#ID_VACIA
	data9={ 
	'email':'raulahoratieneemail@gmail.com',
	'nombre':'Raul',
	'password':'dsfs4',
	'apellido':'Peron',
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-08',
	'locacion_id':None
} 

	response1 = requests.post(url + '/usuario/registro',  json=data1, headers={'Authorization': token_usuario})
	response2 = requests.post(url + '/usuario/registro',  json=data2, headers={'Authorization': token_usuario})
	response3 = requests.post(url + '/usuario/registro',  json=data3, headers={'Authorization': token_usuario})
	response4 = requests.post(url + '/usuario/registro',  json=data4, headers={'Authorization': token_usuario})
	response5 = requests.post(url + '/usuario/registro',  json=data5, headers={'Authorization': token_usuario})
	response6 = requests.post(url + '/usuario/registro',  json=data6, headers={'Authorization': token_usuario})
	response7 = requests.post(url + '/usuario/registro',  json=data7, headers={'Authorization': token_usuario})
	response8 = requests.post(url + '/usuario/registro',  json=data8, headers={'Authorization': token_usuario})
	response9 = requests.post(url + '/usuario/registro',  json=data9, headers={'Authorization': token_usuario})

	print('test_registro_campos_vacios')


	responses = [response1, response2, response3, response4, response5, response6, response7, response8, response9]


	for x in responses:
		assert x.status_code == 400 #BAD REQUEST




#COODIGO DE TEST 313: REGISTRO CON FECHA INVALIDA
def test_registro_fecha_invalida():
	data =  {
	'email':'asd@gmail.com',
	'nombre':'carl',
	'password':'asd',
	'apellido':'mark',
	'sexo':'-',
	'estatura':180,
	'peso':321,
	'fecha_nacimiento':'1991-01-00',
	'locacion_id':1
} 
	response = requests.get(url + '/usuario/registro',  json=data)
	print('test_registro_fecha_invalida')
	print(response.content.decode('utf8'))
	assert response.status_code == 405 #CONFLICT

