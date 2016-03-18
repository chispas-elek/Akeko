# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

"""
Ésto es una MAE usándo el patrón Singleton para python.
Python tiene muchas formas de hacer que una clase se instancie de forma única.
En éste caso, se ha usado la instanciación por Metaclase.
"""

from src.packGestorSocket import ServerSender

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class CLogin(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.
    
    def iniciar_sesion(self, p_usuario, p_contrasena):
        """
        Comprueba las credenciales del usuario

        :param p_usuario: El usuario del sistema
        :param p_contrasena: La contraseña del usuario
        :return: None -> Si los datos no están correctamente introducidos
                fail -> Si ha ocurrido un error serio en la BD
                id_usuario -> Identificador del usuario si todo ha ido bien.
        """
        # Preparamos los datos y los enviamos.
        lista_envio = []
        # Cabecera de envío para saber que método hay que ejecutar en el server
        lista_envio.append({'metodo': 'iniciar_sesion'})
        # Los datos asociados
        lista_envio.append({'usuario': p_usuario, 'contrasena': p_contrasena})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        if resultado == {'return': 'fail'}:
            resultado = 'fail'
        return resultado
