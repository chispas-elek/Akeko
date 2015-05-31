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
        """
        Obtenemos los tags que tiene aplicados un grupo.
        :param p_id_grupo: El identificador del grupo
        :return: Los datos relativos a cada tag que posee el grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdTag,NombreTag,Descripcion,FechaCreacion FROM Tag
                    WHERE IdTag IN (SELECT IdTag FROM Tag_Grupo WHERE IdGrupo=%s);
                    """, p_id_grupo
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_tags_disponibles(self, p_id_grupo):
        """
        Obtenemos los tags que aún no han sido aplicados en un grupo
        :param p_id_grupo: El identificador de un grupo
        :return: Los tags que aún no han sido aplicados en un grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdTag,NombreTag,Descripcion,FechaCreacion FROM Tag
                    WHERE IdTag NOT IN (SELECT IdTag FROM Tag_Grupo WHERE IdGrupo=%s);
                    """, p_id_grupo
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_tags_usuario(self, p_id_usuario):
        """
        Obtenemos los tags que ha creado un usuario en el sistema
        :param p_id_usuario: El identificador del usuario
        :return: Los tags que tiene el usuario
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdTag,NombreTag,Descripcion,FechaCreacion FROM Tag WHERE IdUsuario=%s;", p_id_usuario
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd
