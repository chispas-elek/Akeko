# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from Servidor.src.packGestorBD import MySQLConnector

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class GestorUsuario(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_credenciales(self, p_usuario, p_contrasena):
        """
        Obtiene las credenciales de acceso de un usuario
        :param p_usuario: El usuario
        :param p_contrasena: Su contraseña
        :return: True o False dependiendo de si las credenciales introducidas son correctas.
        """
        existe = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdUsuario FROM Usuario WHERE Usuario=%s AND Contrasena=%s;", (p_usuario, p_contrasena)
        # Comprobamos el valor de la consulta
        respuesta_bd = bd.execute(consulta)
        if len(respuesta_bd) != 0:
            # El usuario y contraseña son correctos
            existe = True
        return existe
