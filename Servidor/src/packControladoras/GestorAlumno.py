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

class GestorAlumno(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_alumnos(self, p_id_grupo):
        """
        Dado el idenficiador de un grupo, obtenemos los alumnos que lo contiene

        :param p_id_grupo: Identificador del grupo
        :return: La lista de los alumnos que compone el grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT Dni,Nombre,Apellido,Email
                    FROM Alumno WHERE Dni IN (
                    SELECT Dni FROM Alumno_Grupo WHERE IdGrupo=%s);""", p_id_grupo
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def anadir_alumno(self, p_dni, p_nombre, p_apellido, p_email):
        """
        Insertamos un nuevo alumno en la BD
        :param p_dni:
        :param p_nombre:
        :param p_apellido:
        :param p_email:
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """INSERT INTO Alumno(Dni,Nombre,Apellido,Email)
                    VALUES(%s,%s,%s,%s);""", (p_dni, p_nombre, p_apellido, p_email)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def borrar_alumno(self, p_dni):
        """
        Borar el alumno del sistema.
        :param p_dni: Dni del alumno
        :return:None
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Alumno WHERE Dni=%s;", p_dni
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def buscar_alumno(self, p_dni):
        """
        Busca la existencia de un alumno dado su dni
        :param p_dni: El Dni del alumno
        :return: -> None si no existen datos
                -> Datos de un alumno si éste existe
        """
        existe = None
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT * FROM Alumno WHERE Dni=%s;", p_dni
        respuesta_bd = bd.execute(consulta)
        if len(respuesta_bd) != 0:
            # El alumno eexiste en la BD
            existe = respuesta_bd
        return existe

