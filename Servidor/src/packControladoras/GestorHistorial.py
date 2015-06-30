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


class GestorHistorial(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_historial(self, p_id_usuario):
        """
        Obtiene el historial dado el usuario

        :param p_id_usuario: El identificador del usuario
        :return: El historial completo de dicho usuario
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT * FROM Historial WHERE IdUsuario=%s", p_id_usuario
        respuesta_bd = bd.execute(consulta)

        return respuesta_bd
