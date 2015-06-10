# -*- encoding: utf-8 -*-
from Servidor.src.packGestorBD.MySQLConnector import MySQLConnector

__author__ = 'Rubén Mulero'

import subprocess as sub
import shlex
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

    def eliminar_script(self, p_id_script, p_id_alumno, p_id_usuario, p_id_grupo):
        """
        Dado un alumno, comrpueba si tiene un script aplicado por otros profesores y grupos.

        En caso de estar en otro grupo -> Elimina la intención.
        En caso de no estar en ninguno otro -> Elimina la intención y revoca el script
        :param p_id_script: El identificador del scriot
        :param p_id_alumno: El identificador del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo:  El identificador del grupo
        :return:
        """
        pass

    def apply_script(self, p_id_script, p_id_alumno):
        """
        Aplicamos un script
        :param p_id_script: El identificador del Script
        :param p_id_alumno: El identificador del alumno
        :return:
        """

        # Obtener el path del script(LLamaba BD o tipo de objeto)

        # Ejecutar el script enviando los datos del alumno
        p = sub.Popen(shlex.split('sh /home/administrador/ex11-7.generarlist.sh'),  stdout=sub.PIPE, stderr=sub.PIPE)
        salida, errores = p.communicate()
        if len(salida) != 0:
            print salida
        else:
            # Ha habido errores lanzamos una excepción
            print errores
        # Si las cosas han ido bien,a ctualizar los datos en la BD

a = GestorScript()
a.apply_script(3, 4)
