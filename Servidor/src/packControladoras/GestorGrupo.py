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

class GestorGrupo(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_grupos(self, p_id_usuario):
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdGrupo,NombreGrupo FROM Grupo WHERE IdUsuario=%s", p_id_usuario
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_alumnos(self, p_id_grupo):
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT Dni,Nombre,Apellido,Email
                    FROM Alumno WHERE Dni IN (
                    SELECT Dni FROM Alumno_Grupo WHERE IdGrupo=%s);""", p_id_grupo
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd
