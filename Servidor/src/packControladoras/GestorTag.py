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

class GestorTag(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_tagss(self, p_id_grupo):
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdTag,NombreTag,Descripcion,Fecha FROM Tag
                    WHERE  IdTag IN (SELECT IdTag FROM Tag_Grupo WHERE IdGrupo=%s);
                    """, p_id_grupo
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd