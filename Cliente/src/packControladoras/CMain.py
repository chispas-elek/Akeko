# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from src.packGestorSocket import ServerSender
from src.packModelo import ListaGrupo, ListaAlumno

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
        lista_grupo = ListaGrupo.ListaGrupo()
        lista_grupo.construir(resultado)
        return lista_grupo

    def obtener_alumnos(self, p_id_grupo):
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_alumnos'})
        lista_envio.append({'id_grupo': p_id_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        lista_alumno = ListaAlumno.ListaAlumno()
        lista_alumno.construir(resultado)
        return lista_alumno

    def borrar_grupo(self, p_id_usuario, p_id_grupo, p_lista_alumno):
        """
        Borra un grupo del sistema y por cada alumno que compone el grupo
        el sistema revoca todos los scripts y Tags que tuvieran aplicados.


        Además, si por alguna razón algún alumno se queda huérfano el programa
        lo elimina del sistema

        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :param p_lista_alumno: La lista de los alumnos que componen el grupo

        :return: True -> Si el grupo se ha eliminado de forma correcta del sistema
                False -> Si ha existido algún problema durante el borrado
        """
        lista_envio = []
        lista_envio.append({'metodo': 'borrar_grupo'})
        lista_envio.append({'id_usuario': p_id_usuario, 'id_grupo': p_id_grupo,
                            'lista_alumnos': p_lista_alumno.deconstruir()})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def cambiar_nombre(self, p_id_grupo, p_nombre_grupo, p_lista_grupos):
        """
        Cambia el nombre del grupo actual y avisa en caso de que el nombre del grupo ya exista en el sistema

        :param p_id_grupo:
        :param p_nombre_grupo:
        :param p_lista_grupos:
        :return: None -> El nombre del grupo ya existe en el sistema
                False -> Algo ha sucedido en la BD y no se ha actualizado todo bien
                True -> Todo ha ido bien
        """
        resultado = None
        ya_existe = p_lista_grupos.buscar_nombre(p_nombre_grupo)
        if ya_existe is not True:
            lista_envio = []
            lista_envio.append({'metodo': 'cambiar_nombre'})
            lista_envio.append({'id_grupo': p_id_grupo, 'nombre_grupo': p_nombre_grupo})
            socket = ServerSender.ServerSender(lista_envio)
            resultado = socket.enviar_datos()
        else:
            # El nombre del grupo existe. Devolvemos None para indicar Error
            print "El nombre del grupo ya existe"
        return resultado