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

class GestorScript(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_scripts(self, p_id_grupo):
        """
        Obtiene los scripts que contiene un grupo
        :param p_id_grupo: El identificador del grupo
        :return: La lista de scripts que contiene el grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdScript,NombreS,Descripcion FROM Script
                    WHERE IdScript IN (SELECT IdScript FROM Script_Grupo WHERE IdGrupo=%s)
                    AND Activo=%s;""", (p_id_grupo, True)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_scripts_disponibles(self, p_id_grupo):
        """
        Obtiene los scripts que no han sido aplicados en un grupo
        :param p_id_grupo: EL identificador del grupo
        :return: La lista de scripts NO aplicados en un grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta= """SELECT IdScript,NombreS,Descripcion FROM Script
                    WHERE IdScript NOT IN (SELECT IdScript FROM Script_Grupo WHERE IdGrupo=%s)
                    AND Activo=%s;""", (p_id_grupo, True)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_scripts_tag(self, p_id_tag):
        """
        Obtiene los scripts que contiene un TAG
        :param p_id_tag: Identificador del tag
        :return: La lista de scripts que contiene un TAG
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdScript,NombreS,Descripcion FROM Script
                    WHERE IdScript IN (SELECT IdScript FROM TAG_Script WHERE IdTag=%s)
                    AND Activo=%s;""", (p_id_tag, True)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd