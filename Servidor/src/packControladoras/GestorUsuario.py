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

class GestorUsuario(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_credenciales(self, p_usuario, p_contrasena):
        """
        Obtiene las credenciales de acceso de un usuario
        :param p_usuario: El usuario
        :param p_contrasena: Su contraseña
        :return: Devuelve el IdUsuario en cuestión si los datos son correctos o None si no lo son.
        """
        id_usuario = None
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdUsuario FROM Usuario WHERE Usuario=%s AND Contrasena=%s;", (p_usuario, p_contrasena)
        # Comprobamos el valor de la consulta
        respuesta_bd = bd.execute(consulta)
        if len(respuesta_bd) != 0:
            # El usuario y contraseña son correctos
            id_usuario = int(respuesta_bd[0]['IdUsuario'])
        return id_usuario

    def obtener_todos_los_propietarios(self, p_id_usuario):
        """
        Obtiene todos los propietarios disponibles para que puedan recibir un posible Tag por parte del usuario actual
        del sistema

        :param p_id_usuario: El identificador del usuario actual
        :return: La lista de los usuarios que no poseen el Tag a heredar.
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdUsuario,Nombre,Apellido FROM Usuario WHERE NOT IdUsuario=%s", (p_id_usuario, )
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd