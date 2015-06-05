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

    def anadir_tag(self, p_nombre_tag, p_id_usuario, p_descripcion, p_lista_scrip):
        """
        Añadimos un nuevo tag en el sistema
        :param p_nombre_tag: El nombre del Tag
        :param p_id_usuario: El identificador del usuario
        :param p_descripcion: La descripción del Tag
        :param p_lista_scrip: La lista de los scripts que se tiene que asociar
        :return: True o False dependiendo si se ha insertado el tag corretamente
        """
        # Primero se comprueba si el nombre del tag ya existe en el sistema.
        bd = MySQLConnector.MySQLConnector()
        exito = False
        consulta1 = "SELECT IdTag FROM Tag WHERE NombreTag=%s", p_nombre_tag
        respuesta_bd_1 = bd.execute(consulta1)
        if len(respuesta_bd_1) == 0:
            # No existe el nombre en la BD, procedeemos a insertar el TAG
            consulta2 = "INSERT INTO Tag(NombreTag,Descripcion,IdUsuario) VALUES(%s,%s,%s);", \
                        (p_nombre_tag, p_descripcion, p_id_usuario)
            respuesta_bd_2 = bd.execute(consulta2)
            if respuesta_bd_2 == 1:
                # Se ha insertado el tag correctamente, añadimos los Scripts
                # Obtenemos le identificador que se le ha asociado a nuestro nuevo TAG
                consulta3 = "SELECT IdTag FROM Tag WHERE NombreTag=%s", p_nombre_tag
                respuesta_bd_3 = bd.execute(consulta3)
                # Recorremos la lista de script y vamos insertado uno a uno en la BD
                for script in p_lista_scrip:
                    consulta4 = "INSERT INTO Tag_Script(IdTag,IdScript) VALUES(%s,%s);", \
                                (respuesta_bd_3['IdTag'], script)
                    bd.execute(consulta4)
                exito = True
        return exito
