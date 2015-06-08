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
        """
        Obtenemos los grupos que tiene un usuario logueado

        :param p_id_usuario: El identificador del uusairo
        :return: La lista de los grupos que contiene el usuario
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdGrupo,NombreGrupo FROM Grupo WHERE IdUsuario=%s", p_id_usuario
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def anadir_grupo(self, p_nombre_grupo, p_id_usuario, p_lista_alumnos):
        """
        Creamos un nuevo grupo en el sistema
        :param p_nombre_grupo: El nombre del grupo
        :param p_id_usuario: El identificador del usuario
        :param p_lista_alumnos: La lista de alumnos que va a contener el nuevo grupo
        :return: True o False dependiendo si la operación ha sido un éxito
        """
        devolver = False
        bd = MySQLConnector.MySQLConnector()
        consulta1 = "INSERT INTO Grupo(NombreGrupo,IdUsuario) VALUES(%s,%s);", (p_nombre_grupo, p_id_usuario)
        respuesta_bd = bd.execute(consulta1)
        # Obtenemos el identificador del grupo
        consulta2 = "SELECT IdGrupo FROM Grupo WHERE NombreGrupo=%s;", p_nombre_grupo
        respuesta_bd_2 = bd.execute(consulta2)
        # Insertamos la relación entre alumno y grupo
        for alumno in p_lista_alumnos:
            consulta3 = "INSERT INTO Alumno_Grupo(Dni,IdGrupo) VALUES(%s,%s);", \
                        (alumno['Dni', respuesta_bd_2['IdGrupo']])
            respuesta_bd_3 = bd.execute(consulta3)
        if len(respuesta_bd) != 0 and len(respuesta_bd_2) != 0 and len(respuesta_bd_3) != 0:
            # Todo ha ido bien
            devolver = True
        return devolver

    def borrar_grupo(self, p_id_grupo):
        """
        Borra un grupo del sistema dado su identificador
        :param p_id_grupo:
        :return:
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Grupo WHERE IdGrupo=%s", p_id_grupo
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def cambiar_nombre(self, p_id_grupo, p_nombre_grupo):
        """
        Cambiamos el nombre de un grupo si es posible
        :param p_id_grupo: El identificador del grupo
        :param p_nombre_grupo: EL nuevo nombre del grupo
        :return: True o False dependiendo del cambio exitoso
        """
        bd = MySQLConnector.MySQLConnector()
        exito = False
        # Primero vamos a comprobar si el nombre ya existe en la BD
        consulta1 = "SELECT IdGrupo FROM Grupo WHERE NombreGrupo=%s", p_nombre_grupo
        respuesta_bd_1 = bd.execute(consulta1)
        if len(respuesta_bd_1) == 0:
            # No existe ninguna entrada en la BD con dicho nombre
            # Cambiamos el nombre sin problemas
            consulta2 = "UPDATE Grupo SET NombreGrupo=%s WHERE IdGrupo=%s", (p_nombre_grupo, p_id_grupo)
            respuesta_bd_2 = bd.execute(consulta2)
            # todo comprobar si el update devuelve 1
            if respuesta_bd_2 == 1:
                exito = True
        return exito
