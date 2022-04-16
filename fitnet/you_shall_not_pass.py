import jwt
from flask import request,jsonify
from fitnet import app
from fitnet.models import Usuario
class Login_rol_required:
	def __init__(self, roles):
		self.roles=roles
		self.invalid_msg = {
				'message': 'Debe estar logueado para realizar esta operación.',
				'authenticated': False
			}
		self.expired_msg = {
				'message': 'token invalido',
				'authenticated': False
			}

	def __call__(self,f):
		def deco(*args,**kwargs):

			auth_headers = request.headers.get('Authorization', '').split()
			if len(auth_headers) != 2:
				return jsonify(self.invalid_msg), 401
			try:
				token = auth_headers[1]
				data = jwt.decode(token, app.config['SECRET_KEY'])
				user = Usuario.query.filter_by(email=data['email']).first()
				if not user:
					raise RuntimeError('usuario no encontrado')
				if user.rol not in self.roles:
					return jsonify(self.invalid_msg), 401

				return f(user, *args, **kwargs)
				

			except jwt.ExpiredSignatureError:
				return jsonify(self.expired_msg), 401 
			except (jwt.InvalidTokenError) :
				return jsonify(self.invalid_msg), 401
			except Exception as e:
				return jsonify(str(e)), 400
		deco.__name__ = f.__name__


		return deco

#                                  ....
#                                .'' .'''
#.                             .'   :
#\\                          .:    :
# \\                        _:    :       ..----.._
#  \\                    .:::.....:::.. .'         ''.
#   \\                 .'  #-. .-######'     #        '.
#    \\                 '.##'/ ' ################       :
#     \\                  #####################         :
#      \\               ..##.-.#### .''''###'.._        :
#       \\             :--:########:            '.    .' :
#        \\..__...--.. :--:#######.'   '.         '.     :
#        :     :  : : '':'-:'':'::        .         '.  .'
#        '---'''..: :    ':    '..'''.      '.        :'
#           \\  :: : :     '      ''''''.     '.      .:
#            \\ ::  : :     '            '.      '      :
#             \\::   : :           ....' ..:       '     '.
#              \\::  : :    .....####\\ .~~.:.             :
#               \\':.:.:.:'#########.===. ~ |.'-.   . '''.. :
#                \\    .'  ########## \ \ _.' '. '-.       '''.
#                :\\  :     ########   \ \      '.  '-.        :
#               :  \\'    '   #### :    \ \      :.    '-.      :
#              :  .'\\   :'  :     :     \ \       :      '-.    :
#             : .'  .\\  '  :      :     :\ \       :        '.   :
#             ::   :  \\'  :.      :     : \ \      :          '. :
#             ::. :    \\  : :      :    ;  \ \     :           '.:
#              : ':    '\\ :  :     :     :  \:\     :        ..'
#                 :    ' \\ :        :     ;  \|      :   .'''
#                 '.   '  \\:                         :.''
#                  .:..... \\:       :            ..''
#                 '._____|'.\\......'''''''.:..'''
#                            \\