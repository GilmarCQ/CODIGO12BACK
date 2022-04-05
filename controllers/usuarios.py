import os

from flask_restful import Resource, request
from dtos.registro_dto import RegistroDTO, UsuarioResponseDto, LoginDTO
from dtos.usuario_dto import ResetPasswordRequestDTO
from models.usuarios import Usuario
from config import conexion, sendgrid
# from sendgrid.helpers.mail import Email, To, Content, Mail
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ
from cryptography.fernet import Fernet
from datetime import timedelta, datetime
import json


class RegistroController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = RegistroDTO().load(body)
            nuevoUsuario = Usuario(**data)
            nuevoUsuario.encriptar_pwd()
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()
            respuesta = UsuarioResponseDto().dump(nuevoUsuario)
            return {
                       'message': 'Usuario registrado correctamente',
                       'content': respuesta
                   }, 201
        except Exception as e:
            return {
                       'message': 'Error al registrar el usuario.',
                       'content': e.args
                   }, 400


class LoginController(Resource):
    def post(self):
        body = request.get_json()
        try:
            data = LoginDTO().load(body)
            return {
                'message': 'Bienvenido'
            }
        except Exception as e:
            return {
                'message': 'Credenciales Incorrectas',
                'content': e.args
            }


class ResetPasswordController(Resource):
    def post(self):
        body = request.get_json()
        mensaje = MIMEMultipart()
        email_emisor = environ.get('EMAIL_EMISOR')
        email_password = environ.get('EMAIL_PASSWORD')
        try:
            data = ResetPasswordRequestDTO().load(body)
            usuarioEncontrado = conexion.session.query(Usuario).filter_by(correo=data.get('correo')).first()
            if usuarioEncontrado is not None:
                texto = 'Hola este es un mensaje de recuperacion de correo'
                mensaje['Subject'] = 'Reiniciar contraseña de App Monedero'

                # Encriptacion de informacion
                fernet = Fernet(environ.get('FERNET_SECRET_KEY'))
                mensaje_secreto = {
                    'fecha_caducidad': str(datetime.now()+timedelta(hours=1)),
                    'id_usuario': usuarioEncontrado.id
                }
                mensaje_secreto_str = json.dumps(mensaje_secreto)
                mensaje_encriptado = fernet.encrypt(bytes(mensaje_secreto_str, 'utf-8'))

                # print(mensaje_encriptado.decode('utf-8'))
                # print(mensaje_encriptado)

                # Fin de la encriptacion
                html = open('./email-templates/forgot-password.html').read().format(usuarioEncontrado.nombre,
                                        environ.get('URL_FRONT') + '/reset-password?token='+mensaje_encriptado.decode('utf-8'))
                #   cuando se quiere agregar un html, como texto de mensaje, este debe ir despues del texto ya que
                #   primero tratara de enviar el ultimo y si no lo logra enviara el primero
                # mensaje.attach(MIMEText(texto, 'plain'))
                mensaje.attach(MIMEText(html, 'html'))
                # gmail     >   smtp.gmail.com | 587
                # outlook   >   outlook.office365.com | 587
                # iclooud   >   smtp.mail.me.com | 587
                # yahoo     >   smtp.mail.yahoo.com | 587
                # servidor, puerto
                emisorSMTP = SMTP('smtp.gmail.com', 587)
                emisorSMTP.starttls()
                # se realiza el login del correo
                emisorSMTP.login(email_emisor, email_password)
                emisorSMTP.sendmail(
                    from_addr=email_emisor,
                    to_addrs=usuarioEncontrado.correo,
                    msg=mensaje.as_string()
                )
                # finaliza la sesion de mi correo
                emisorSMTP.quit()
            return {
                'message': 'Correo enviado exitosamente.'
            }

        except Exception as e:
            return {
                'message': 'Error al intentar resetear el password',
                'content': e.args
            }

# try:
#     data = ResetPasswordRequestDTO().load(body)
#     usuarioEncontrado = conexion.session.query(Usuario).filter_by(correo=data.get('correo')).first()
#     if usuarioEncontrado is not None:
#         # usar los correos verificados en sendgrid
#         from_email = Email('gacampanaq@gmail.com')
#         to_email = To(usuarioEncontrado.correo)
#         subject = 'Reinicia tu contraseña'
#         content = Content('text/plain',
#                           'Hola has solicitado el reinicion de tu contraseña, haz click en el siguiente '
#                           'link para cambiar, sino haz sido tu ignora este mensaje:.....')
#         mail = Mail(from_email, to_email, subject, content)
#         correo_enviado = sendgrid.client.mail.send.post(request_body=mail.get())
#         # estado de respuesta del correo
#         print(correo_enviado.status_code)
#         # el cuerpo de la respuesta del correo
#         print(correo_enviado.body)
#         # las cabeceras de la respuesta del correo
#         print(correo_enviado.headers)
#     return {
#         'message': 'Correo enviado exitosamente.'
#     }
# except Exception as e:
#     return {
#         'message': 'Error al intentar resetear el password',
#         'content': e.args
#     }
