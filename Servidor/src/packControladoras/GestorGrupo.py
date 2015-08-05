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
        consulta = "SELECT IdGrupo,NombreGrupo,IdUsuario FROM Grupo WHERE IdUsuario=%s;", (p_id_usuario, )
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
        consulta2 = "SELECT IdGrupo FROM Grupo WHERE NombreGrupo=%s;", (p_nombre_grupo, )
        respuesta_bd_2 = bd.execute(consulta2)
        id_grupo = int(respuesta_bd_2[0]['IdGrupo'])
        respuesta_bd_3 = 0
        # Insertamos la relación entre alumno y grupo
        for alumno in p_lista_alumnos:
            consulta3 = "INSERT INTO Alumno_Grupo(IdGrupo,Dni) VALUES(%s,%s);", \
                        (id_grupo, alumno['Dni'])
            respuesta_bd_3 = bd.execute(consulta3)
            if respuesta_bd_3 == 0:
                # todo, deberiamos hacer una excepción en éste punto, indicando un fallo en la inserción.
                break
        if respuesta_bd == 1 and len(respuesta_bd_2) != 0 and respuesta_bd_3 == 1:
            # Los dos inserts han devuelvo 1 por lo que se han realizado correctamente y el SELECT devolvio datos
            # Como han ido bien las cosas. Damos por éxito la operación.
            devolver = True
        return devolver

    def borrar_grupo(self, p_id_grupo):
        """
        Borra un grupo del sistema dado su identificador
        :param p_id_grupo:
        :return: Resultado de la BD
        """
        resultado = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Grupo WHERE IdGrupo=%s", (p_id_grupo, )
        respuesta_bd = bd.execute(consulta)
        if respuesta_bd == 1:
            resultado = True

        return resultado

    def cambiar_nombre(self, p_id_grupo, p_nombre_grupo):
        """
        Cambiamos el nombre de un grupo si es posible
        :param p_id_grupo: El identificador del grupo
        :param p_nombre_grupo: EL nuevo nombre del grupo
        :return: True o False dependiendo del cambio exitoso
        """
        bd = MySQLConnector.MySQLConnector()
        exito = False
        consulta2 = "UPDATE Grupo SET NombreGrupo=%s WHERE IdGrupo=%s", (p_nombre_grupo, p_id_grupo)
        respuesta_bd_2 = bd.execute(consulta2)
        # Comprobamos el éxito de la actualización
        if respuesta_bd_2 == 1:
            exito = True

        return exito

    def obtener_grupos_tag(self, p_id_tag):
        """
        Dado el identificador de un tag, obtenemos la información de los grupos en los que ha sido aplicado

        :param p_id_tag: El identificador de un tag
        :return: La lista de los grupos donde está aplicado dicho Tag.
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdGrupo,NombreGrupo,FechaCreacion,IdUsuario FROM Grupo WHERE IdGrupo IN (
                    SELECT IdGrupo FROM Tag_Grupo WHERE IdTag=%s);""""", (p_id_tag, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd
