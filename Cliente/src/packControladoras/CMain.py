# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from Cliente.src.packGestorSocket import ServerSender

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class CMain(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_grupos(self, p_id_usuario):
        # Preparamos los datos y los enviamos.
        lista_envio = []
        # Cabecera de envío para saber que método hay que ejecutar en el server
        lista_envio.append({'metodo': 'obtener_grupos'})
        # Los datos asociados
        lista_envio.append({'id_usuario': p_id_usuario})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def obtener_alumnos(self, p_id_grupo):
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_alumnos'})
        lista_envio.append({'id_grupo': p_id_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def borrar_grupo(self, p_id_usuario, p_id_grupo, p_lista_alumno):
        """
        Borra un grupo del sistema y por cada alumno que compone el grupo
        el sistema revoca todos los scripts y Tags que tuvieran aplicados.


        Además, si por alguna razón algún alumno se queda huérfano el programa
        lo elimina del sistema

        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :param p_lista_alumno: La lista de los alumnos que componen el grupo
        :return:
        """
        # todo reconvertir las listas a tipos de datos usando las funciones propias de las listas.
        lista_envio = []
        lista_envio.append({'metodo': 'borrar_grupo'})
        lista_envio.append({'id_usuario': p_id_usuario, 'id_grupo': p_id_grupo,
                            'lista_alumnos': p_lista_alumno})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def cambiar_nombre(self, p_id_grupo, p_nombre_grupo):
        lista_envio = []
        lista_envio.append({'metodo': 'cambiar_nombre'})
        lista_envio.append({'id_grupo': p_id_grupo, 'nombre_grupo': p_nombre_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

