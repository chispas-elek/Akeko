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

class CGestionarScript(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_scripts(self, p_id_grupo):
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_scripts'})
        lista_envio.append({'id_grupo': p_id_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def obtener_tags(self, p_id_grupo):
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_tags'})
        lista_envio.append({'id_grupo': p_id_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def obtener_scripts_disponibles(self, p_id_grupo):
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_scripts_disponibles'})
        lista_envio.append({'id_grupo': p_id_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def obtener_tags_disponibles(self, p_id_grupo):
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_tags_disponibles'})
        lista_envio.append({'id_grupo': p_id_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def aplicar_cambios(self, p_id_usuario, p_id_grupo,
                        p_lista_nueva_s, p_lista_vieja_s,
                        p_lista_nueva_t, p_lista_vieja_t,
                        p_lista_alumnos):
        """
        Aplica los nuevos cambios de scripts y Tags en un grupo seleccionado

        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :param p_lista_nueva_s: La lista con los nuevos scripts
        :param p_lista_vieja_s: La lista anterior de scripts
        :param p_lista_nueva_t: La nueva lista de Tags
        :param p_lista_vieja_t: La lista anterior de Tags
        :param p_lista_alumnos: La lista que contiene los alumnos del grupo
        :return:
        """
        # Vamos a crear un diccionario de cambios que va a ser enviada
        lista_cambios = []
        # Primero vamos a comprobar la lista de Scripts
        lista_cambios.append(self._crear_lista_cambios_scripts(p_lista_vieja_s, p_lista_vieja_s))
        # A continuación vamos a comprobar la lista de los Tags

    def _crear_lista_cambios_scripts(self, p_lista_vieja_s, p_lista_nueva_s):
        """
        Genera la lista de cambios para los scripts
        :param p_lista_vieja_s: La lista vieja de Scripts
        :param p_lista_nueva_s: La lista nueva de Scripts
        :return:
        """
        lista_cambios_s = []
        if len(p_lista_vieja_s) != 0:
            # Primero cotejamos la lista vieja con la nueva para eliminar scripts
            lista_borrado = p_lista_vieja_s(p_lista_nueva_s)
            # Ahora cotejamos la lista nueva con la vieja para saber cuáles son los scripts nuevos
            lista_anadir = p_lista_nueva_s(p_lista_vieja_s)
            # Creamos la lista de cambios
            for borrado in lista_borrado:
                lista_cambios_s.append({'borrar_script': borrado['IdScript']})
            for anadir in lista_anadir:
                lista_cambios_s.append({'anadir_script': anadir['IdScript']})
        else:
            # Agregamos directamente la nueva lista
            for nueva_s in p_lista_nueva_s:
                lista_cambios_s.append({'anadir_script': nueva_s['IdScript']})
        return lista_cambios_s
