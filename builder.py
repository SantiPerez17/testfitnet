from fitnet.models import Locacion, Usuario, Entrenamiento, Deporte
from fitnet import db

db.create_all()
l = Locacion(provincia='BsAs', ciudad='Junin', cp='6000')
l1 = Locacion(provincia='BsAs', ciudad='Los toldos', cp='6010')
l2 = Locacion(provincia = 'BsAs', ciudad = 'Pergamino', cp = '2700')

d = Deporte(denominacion ='Correr')
d1 = Deporte(denominacion ='Caminar')
d2 = Deporte(denominacion = 'Futbol')
d3 = Deporte (denominacion = 'Basquet')

db.session.add(l)
db.session.add(l1)
db.session.add(l2)
db.session.add(d)
db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.commit()

u0 = Usuario(habilitado=True,
            fecha_registro='2020-04-01 22:47:20.770543',
            nombre='Operario',
            apellido='Menem',
            email='operario@gmail.com',
            password='sha256$oKzH6mjM$adbedde79ab58327af732bde8118c8a5d9933f21298ac8bda5d1cb97f82d7dfe',
            sexo='m',
            estatura='180',
            peso='70',
            fecha_nacimiento='1990-01-01',
            rol='operario',
            locacion_id=l.id

            )
operario = Usuario(habilitado=True,
            fecha_registro='2020-04-01 22:47:20.770543',
            nombre='Operario1',
            apellido='Menem',
            email='operario1@gmail.com',
            password='sha256$oKzH6mjM$adbedde79ab58327af732bde8118c8a5d9933f21298ac8bda5d1cb97f82d7dfe',
            sexo='m',
            estatura='180',
            peso='70',
            fecha_nacimiento='1990-01-01',
            rol='operario',
            locacion_id=l.id

            )
admin = Usuario(habilitado=True,
            fecha_registro='2020-04-01 22:47:20.770543',
            nombre='ADMIN',
            apellido='Dios',
            email='admin@gmail.com',
            password='sha256$oKzH6mjM$adbedde79ab58327af732bde8118c8a5d9933f21298ac8bda5d1cb97f82d7dfe',
            sexo='m',
            estatura='180',
            peso='70',
            fecha_nacimiento='1996-12-31',
            rol='admin',
            locacion_id=l.id

            )


u = Usuario(habilitado=True,
            fecha_registro='2020-01-13 22:47:20.770543',
            nombre='Jose',
            apellido='Gonzalez',
            email='jgonzales@gmail.com',
            password='sha256$oKzH6mjM$adbedde79ab58327af732bde8118c8a5d9933f21298ac8bda5d1cb97f82d7dfe',
            sexo='m',
            estatura='180',
            peso='70',
            fecha_nacimiento='1994-05-05',
            rol='usuario',
            locacion_id=l.id,
            id_vinculo=1111111111
            )
u = Usuario(habilitado=True,
            fecha_registro='2020-01-13 22:47:20.770543',
            nombre='sa',
            apellido='sa',
            email='sa@gmail.com',
            password='sha256$4cf6829aa93728e8f3c97df913fb1bfa95fe5810e2933a05943f8312a98d9cf2',
            sexo='m',
            estatura='180',
            peso='70',
            fecha_nacimiento='1994-05-05',
            rol='usuario',
            locacion_id=l.id

            )

db.session.add(u0)
db.session.add(admin)
db.session.add(operario)
db.session.add(u)
db.session.commit()

e = Entrenamiento(calorias_consumidas='250',
                  cadencia='45',
                  distancia='100',
                  rc_promedio='35.5',
                  tiempo_actividad='60',
                  pasos='4500',
                  fecha='2020-05-05',
                  usuario_id=u.id,
                  deporte_id=d.id
)

e0 = Entrenamiento(calorias_consumidas='300',
                  cadencia='50',
                  distancia='200',
                  rc_promedio='45.5',
                  tiempo_actividad='75',
                  pasos='5500',
                  fecha='2020-05-15',
                  usuario_id=u.id,
                  deporte_id=d.id
)
e00 = Entrenamiento(calorias_consumidas='550',
                  cadencia='75',
                  distancia='1000',
                  rc_promedio='40.5',
                  tiempo_actividad='60',
                  pasos='6500',
                  fecha='2020-02-28',
                  usuario_id=u.id,
                  deporte_id=d1.id
)
e01 = Entrenamiento(calorias_consumidas='400',
                  cadencia='65',
                  distancia='500',
                  rc_promedio='37.5',
                  tiempo_actividad='90',
                  pasos='7500',
                  fecha='2020-02-25',
                  usuario_id=u.id,
                  deporte_id=d2.id
)
e02 = Entrenamiento(calorias_consumidas='200',
                  cadencia='35',
                  distancia='300',
                  rc_promedio='30.5',
                  tiempo_actividad='30',
                  pasos='2500',
                  fecha='2020-01-15',
                  usuario_id=u.id,
                  deporte_id=d1.id
)
e03 = Entrenamiento(calorias_consumidas='400',
                  cadencia='70',
                  distancia='1000',
                  rc_promedio='40.5',
                  tiempo_actividad='70',
                  pasos='6350',
                  fecha='2020-03-12',
                  usuario_id=u.id,
                  deporte_id=d3.id
)
e04 = Entrenamiento(calorias_consumidas='600',
                  cadencia='100',
                  distancia='1000',
                  rc_promedio='35.5',
                  tiempo_actividad='120',
                  pasos='8545',
                  fecha='2020-05-06',
                  usuario_id=u.id,
                  deporte_id=d.id
)
e05 = Entrenamiento(calorias_consumidas='250',
                  cadencia='105',
                  distancia='1500',
                  rc_promedio='45.5',
                  tiempo_actividad='150',
                  pasos='9500',
                  fecha='2020-05-07',
                  usuario_id=u.id,
                  deporte_id=d.id
)

e06 = Entrenamiento(calorias_consumidas='2500',
                  cadencia='120',
                  distancia='3000',
                  rc_promedio='40.5',
                  tiempo_actividad='180',
                  pasos='10500',
                  fecha='2020-03-31',
                  usuario_id=u.id,
                  deporte_id=d.id
)
e07 = Entrenamiento(calorias_consumidas='700',
                  cadencia='100',
                  distancia='3000',
                  rc_promedio='35.5',
                  tiempo_actividad='70',
                  pasos='9008',
                  fecha='2020-04-07',
                  usuario_id=u.id,
                  deporte_id=d2.id
)
e08 = Entrenamiento(calorias_consumidas='400',
                  cadencia='85',
                  distancia='1000',
                  rc_promedio='35.5',
                  tiempo_actividad='70',
                  pasos='10528',
                  fecha='2020-05-02',
                  usuario_id=u.id,
                  deporte_id=d3.id
)
e09 = Entrenamiento(calorias_consumidas='650',
                  cadencia='75',
                  distancia='2000',
                  rc_promedio='30.5',
                  tiempo_actividad='60',
                  pasos='9536',
                  fecha='2020-05-10',
                  usuario_id=u.id,
                  deporte_id=d3.id
)
db.session.add(e)
db.session.add(e0)
db.session.add(e00)
db.session.add(e01)
db.session.add(e02)
db.session.add(e03)
db.session.add(e04)
db.session.add(e05)
db.session.add(e06)
db.session.add(e07)
db.session.add(e08)
db.session.add(e09)
db.session.commit()


u1 = Usuario(habilitado=True,
            fecha_registro='2020-01-01 20:47:20.770543',
            nombre='Juan',
            apellido='Perez',
            email='fnraco@gmail.com',
            password='sha256$oKzH6mjM$adbedde79ab58327af732bde8118c8a5d9933f21298ac8bda5d1cb97f82d7dfe',
            sexo='m',
            estatura='170',
            peso='75',
            fecha_nacimiento='1996-08-19',
            rol='usuario',
            locacion_id=l1.id

            )

db.session.add(u1)
db.session.commit()

e1 = Entrenamiento(calorias_consumidas='200',
                  cadencia='40',
                  distancia='75',
                  rc_promedio='35.5',
                  tiempo_actividad='50',
                  pasos='3500',
                  fecha='2020-04-09',
                  usuario_id=u1.id,
                  deporte_id=d1.id
)
e10 = Entrenamiento(calorias_consumidas='550',
                  cadencia='75',
                  distancia='1000',
                  rc_promedio='40.5',
                  tiempo_actividad='60',
                  pasos='6500',
                  fecha='2020-02-23',
                  usuario_id=u1.id,
                  deporte_id=d3.id
)

e11 = Entrenamiento(calorias_consumidas='800',
                  cadencia='75',
                  distancia='2500',
                  rc_promedio='37.5',
                  tiempo_actividad='100',
                  pasos='8500',
                  fecha='2020-02-13',
                  usuario_id=u1.id,
                  deporte_id=d.id
)
e12 = Entrenamiento(calorias_consumidas='700',
                  cadencia='85',
                  distancia='2000',
                  rc_promedio='38.5',
                  tiempo_actividad='50',
                  pasos='4500',
                  fecha='2020-01-27',
                  usuario_id=u1.id,
                  deporte_id=d1.id
)
e13 = Entrenamiento(calorias_consumidas='445',
                  cadencia='70',
                  distancia='1200',
                  rc_promedio='43.5',
                  tiempo_actividad='95',
                  pasos='6350',
                  fecha='2020-04-12',
                  usuario_id=u1.id,
                  deporte_id=d3.id
)
e14 = Entrenamiento(calorias_consumidas='600',
                  cadencia='100',
                  distancia='1000',
                  rc_promedio='35.5',
                  tiempo_actividad='120',
                  pasos='8545',
                  fecha='2020-05-16',
                  usuario_id=u1.id,
                  deporte_id=d1.id
)
e15 = Entrenamiento(calorias_consumidas='250',
                  cadencia='105',
                  distancia='1500',
                  rc_promedio='45.5',
                  tiempo_actividad='95',
                  pasos='9500',
                  fecha='2020-03-27',
                  usuario_id=u1.id,
                  deporte_id=d2.id
)

e16 = Entrenamiento(calorias_consumidas='2500',
                  cadencia='120',
                  distancia='4000',
                  rc_promedio='40.5',
                  tiempo_actividad='85',
                  pasos='10500',
                  fecha='2020-03-31',
                  usuario_id=u1.id,
                  deporte_id=d2.id
)
e17 = Entrenamiento(calorias_consumidas='700',
                  cadencia='100',
                  distancia='3000',
                  rc_promedio='35.5',
                  tiempo_actividad='70',
                  pasos='9208',
                  fecha='2020-04-07',
                  usuario_id=u1.id,
                  deporte_id=d2.id
)
e18 = Entrenamiento(calorias_consumidas='400',
                  cadencia='85',
                  distancia='3250',
                  rc_promedio='35.5',
                  tiempo_actividad='150',
                  pasos='9550',
                  fecha='2020-02-25',
                  usuario_id=u1.id,
                  deporte_id=d.id
)
e19 = Entrenamiento(calorias_consumidas='650',
                  cadencia='75',
                  distancia='2000',
                  rc_promedio='30.5',
                  tiempo_actividad='60',
                  pasos='9536',
                  fecha='2020-05-10',
                  usuario_id=u1.id,
                  deporte_id=d3.id
)


db.session.add(e1)
db.session.add(e10)
db.session.add(e11)
db.session.add(e12)
db.session.add(e13)
db.session.add(e14)
db.session.add(e15)
db.session.add(e16)
db.session.add(e17)
db.session.add(e18)
db.session.add(e19)
db.session.commit()

u2 = Usuario(habilitado=True,
            fecha_registro='2020-01-20 20:47:20.770543',
            nombre='Maria',
            apellido='Lopez',
            email='marialopez@gmail.com',
            password='sha256$oKzH6mjM$adbedde79ab58327af732bde8118c8a5d9933f21298ac8bda5d1cb97f82d7dfe',
            sexo='f',
            estatura='171',
            peso='68',
            fecha_nacimiento='1995-04-07',
            rol='usuario',
            locacion_id=l2.id

            )

db.session.add(u2)
db.session.commit()

e2 = Entrenamiento(calorias_consumidas='500',
                  cadencia='50',
                  distancia='1000',
                  rc_promedio='36.5',
                  tiempo_actividad='70',
                  pasos='3500',
                  fecha='2020-04-19',
                  usuario_id=u2.id,
                  deporte_id=d1.id
)
e20 = Entrenamiento(calorias_consumidas='643',
                  cadencia='65',
                  distancia='2000',
                  rc_promedio='40.5',
                  tiempo_actividad='70',
                  pasos='7500',
                  fecha='2020-02-28',
                  usuario_id=u2.id,
                  deporte_id=d3.id
)

e21 = Entrenamiento(calorias_consumidas='800',
                  cadencia='65',
                  distancia='2540',
                  rc_promedio='38.5',
                  tiempo_actividad='120',
                  pasos='8500',
                  fecha='2020-01-23',
                  usuario_id=u2.id,
                  deporte_id=d.id
)
e22 = Entrenamiento(calorias_consumidas='720',
                  cadencia='85',
                  distancia='3000',
                  rc_promedio='38.5',
                  tiempo_actividad='60',
                  pasos='5547',
                  fecha='2020-01-27',
                  usuario_id=u2.id,
                  deporte_id=d1.id
)
e23 = Entrenamiento(calorias_consumidas='445',
                  cadencia='70',
                  distancia='1200',
                  rc_promedio='43.5',
                  tiempo_actividad='95',
                  pasos='6350',
                  fecha='2020-05-09',
                  usuario_id=u2.id,
                  deporte_id=d3.id
)
e24 = Entrenamiento(calorias_consumidas='600',
                  cadencia='100',
                  distancia='1000',
                  rc_promedio='35.5',
                  tiempo_actividad='120',
                  pasos='8545',
                  fecha='2020-03-26',
                  usuario_id=u2.id,
                  deporte_id=d1.id
)
e25 = Entrenamiento(calorias_consumidas='250',
                  cadencia='105',
                  distancia='1500',
                  rc_promedio='45.5',
                  tiempo_actividad='95',
                  pasos='9500',
                  fecha='2020-03-27',
                  usuario_id=u2.id,
                  deporte_id=d1.id
)

e26 = Entrenamiento(calorias_consumidas='800',
                  cadencia='100',
                  distancia='4000',
                  rc_promedio='40.5',
                  tiempo_actividad='85',
                  pasos='7500',
                  fecha='2020-03-02',
                  usuario_id=u2.id,
                  deporte_id=d2.id
)
e27 = Entrenamiento(calorias_consumidas='674',
                  cadencia='100',
                  distancia='3852',
                  rc_promedio='35.5',
                  tiempo_actividad='73',
                  pasos='9298',
                  fecha='2020-02-27',
                  usuario_id=u2.id,
                  deporte_id=d2.id
)
e28 = Entrenamiento(calorias_consumidas='400',
                  cadencia='85',
                  distancia='3250',
                  rc_promedio='35.5',
                  tiempo_actividad='150',
                  pasos='9550',
                  fecha='2020-02-02',
                  usuario_id=u2.id,
                  deporte_id=d.id
)
e29 = Entrenamiento(calorias_consumidas='650',
                  cadencia='75',
                  distancia='2000',
                  rc_promedio='30.5',
                  tiempo_actividad='50',
                  pasos='9760',
                  fecha='2020-05-16',
                  usuario_id=u2.id,
                  deporte_id=d3.id
)


db.session.add(e2)
db.session.add(e20)
db.session.add(e21)
db.session.add(e22)
db.session.add(e23)
db.session.add(e24)
db.session.add(e25)
db.session.add(e26)
db.session.add(e27)
db.session.add(e28)
db.session.add(e29)

db.session.commit()