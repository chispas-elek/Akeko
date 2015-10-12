# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

"""
En éste gestor se engloban las acciones de escritura en el historial del sistema. Aquí se registran los eventos que se
produzcan, debido a las acciones de un usuario.

"""

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
        consulta = "SELECT * FROM Historial WHERE IdUsuario=%s ORDER BY Fecha desc;", (p_id_usuario, )
        respuesta_bd = bd.execute(consulta)

        return self._formatear_hora(respuesta_bd)

    def anadir_historial_script(self, p_id_script, p_nombre_alumno, p_apellido,
                                p_id_usuario, p_id_grupo, p_accion, p_info):
        """
        Añade en la base de datos una entrada referente a la aplicación o eliminación
        exitosa de un script a un alumno en un grupo

        :param p_id_script: El identificador del script aplicado
        :param p_nombre_alumno: El nombre del alumno a introducir
        :param p_apellido: El apellido del alumno a introducir
        :param p_id_usuario: El identificador del usuario.
        :param p_id_grupo: El identificador del grupo
        :param p_accion: La acción ha realizar. True Añadir, False eliminar.
        :param p_info: La información relativa. El porque se añade la entrada.
        :return: True -> Si todo ha ido bien
                False -> Si algo ha ido mal
        """
        respuesta = False
        bd = MySQLConnector.MySQLConnector()
        # Obtenemos los nombres a partir de los Identificadores que hemnos recibido
        consulta_1 = "SELECT NombreScript FROM Script WHERE IdScript=%s", (p_id_script,)
        respuesta_bd_1 = bd.execute(consulta_1)
        consulta_2 = "SELECT NombreGrupo FROM Grupo WHERE IdGrupo=%s", (p_id_grupo,)
        respuesta_bd_2 = bd.execute(consulta_2)
        if len(respuesta_bd_1) != 0 and len(respuesta_bd_2) != 0:
            # Tenemos datos, vamos a obtenerlos y a insertar en el historial lo sucedido
            nombre_script = respuesta_bd_1[0]['NombreScript']
            nombre_grupo = respuesta_bd_2[0]['NombreGrupo']
            consulta_3 = """INSERT INTO Historial(NombreScript,NombreAlumno,Apellido,NombreGrupo,
                                IdUsuario,Accion,Informacion)
                                VALUES(%s,%s,%s,%s,%s,%s,%s);
                                """, (nombre_script, p_nombre_alumno,
                                      p_apellido, nombre_grupo, p_id_usuario, p_accion, p_info)
            respuesta_bd_3 = bd.execute(consulta_3)
            if respuesta_bd_3 == 1:
                # ok
                respuesta = True

        return respuesta

    def anadir_historial_tag(self, p_id_tag, p_nombre_alumno, p_apellido, p_id_usuario, p_id_grupo, p_accion, p_info):
        """
        Añade en la base de datos una entrada referente a la aplicación o eliminación
        exitosa de un script en un alumno en un grupo

        :param p_id_tag: El identificador del tag aplicado
        :param p_nombre_alumno: El nombre del alumno
        :param p_apellido: El apellido del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :param p_accion: La acción ha realizar. True Añadir, False eliminar.
        :param p_info: La información relativa.
        :return: True -> Si todo ha ido bien
                False -> Si algo ha ido mal.
        """
        respuesta = False
        bd = MySQLConnector.MySQLConnector()
        # Obtenemos los nombres a partir de los Identificadores que hemnos recibido
        consulta_1 = "SELECT NombreTag FROM Tag WHERE IdTag=%s", (p_id_tag,)
        respuesta_bd_1 = bd.execute(consulta_1)
        consulta_2 = "SELECT NombreGrupo FROM Grupo WHERE IdGrupo=%s", (p_id_grupo,)
        respuesta_bd_2 = bd.execute(consulta_2)
        if len(respuesta_bd_1) != 0 and len(respuesta_bd_2) != 0:
            # Tenemos datos, vamos a obtenerlos y a insertar en el historial lo sucedido
            nombre_tag = respuesta_bd_1[0]['NombreTag']
            nombre_grupo = respuesta_bd_2[0]['NombreGrupo']
            consulta_3 = """INSERT INTO Historial(NombreTag,NombreAlumno,Apellido,NombreGrupo,
                                IdUsuario,Accion,Informacion)
                                VALUES(%s,%s,%s,%s,%s,%s,%s);
                                """, (nombre_tag, p_nombre_alumno,
                                      p_apellido, nombre_grupo, p_id_usuario, p_accion, p_info)
            respuesta_bd_3 = bd.execute(consulta_3)
            if respuesta_bd_3 == 1:
                # ok
                respuesta = True

        return respuesta

    def anadir_historial_grupo(self, p_id_usuario, p_nombre_grupo, p_accion, p_info):
        """
        Añade a la base de datos una entrada referente a la adición o no de un grupo en el sistema

        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :param p_accion: La acción a realizar
        :param p_info: La información
        :return: True -> Si todo ha ido bien
                False -> Si algo ha ido mal
        """
        respuesta = False
        bd = MySQLConnector.MySQLConnector()
        # Tenemos datos, vamos a insertar en el historial
        consulta_2 = "INSERT INTO Historial(NombreScript,NombreTag,NombreAlumno,Apellido,NombreGrupo,IdUsuario,Accion," \
                   "Informacion) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);", \
                   ("", "", "", "", p_nombre_grupo, p_id_usuario, p_accion, p_info)
        respuesta_bd_2 = bd.execute(consulta_2)
        if respuesta_bd_2 == 1:
            # ok
            respuesta = True

        return respuesta

    def anadir_historia_gestion_tag(self, p_nombre_tag, p_id_usuario, p_accion, p_info):
        """
        Ésta función registra todos los datos relacionados con agregar, modificar o eliminar un targ en el sistema

        :param p_nombre_tag: El nombre del Tag
        :param p_id_usuario: El identificador de un usuario
        :param p_accion: La acción a realizar
        :param p_info: La información asociada
        :return: True -> Si se ha introducido bien todos los datos
                False -> Si algo ha ocurrido.
        """
        exito = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "INSERT INTO Historial(NombreScript,NombreTag,NombreAlumno,Apellido,NombreGrupo,IdUsuario,Accion," \
                   "Informacion) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);", \
                   (None, p_nombre_tag, None, None, None, p_id_usuario, p_accion, p_info)
        respuesta_bd = bd.execute(consulta)
        if respuesta_bd == 1:
            exito = True
        return exito


    def _formatear_hora(self, p_list_dict_valores):
        """
        La base de datos devuelve los datos en formato datetime. El cual es incompatible con JSON ya que pide Strings
        o ints. Para evitar problemas, con ésta función vamos a transformar el valor datetime en un String en un formato
        europeo

        :param p_dict_valores: La lista que contiene los diciconarios con los valores de la BD

        :return: El dicionario de datos enviados con la fechas formateadas.
        """
        for valor in p_list_dict_valores:
            fecha_de_la_bd = valor['Fecha']
            fecha_formateada = fecha_de_la_bd.strftime("%d/%m/%Y")
            valor['Fecha'] = fecha_formateada

        return p_list_dict_valores