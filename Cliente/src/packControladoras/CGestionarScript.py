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
                        p_lista_vieja_s, p_lista_nueva_s,
                        p_lista_vieja_t, p_lista_nueva_t,
                        p_lista_alumnos):
        """
        Aplica los nuevos cambios de scripts y Tags en un grupo seleccionado

        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :param p_lista_vieja_s: La lista anterior de scripts
        :param p_lista_nueva_s: La lista con los nuevos scripts
        :param p_lista_nueva_t: La nueva lista de Tags
        :param p_lista_vieja_t: La lista anterior de Tags
        :param p_lista_alumnos: La lista que contiene los alumnos del grupo
        :return:
        """
        lista_envio = []
        # Vamos a crear un diccionario de cambios que va a ser enviada
        lista_cambios_s = []
        lista_cambios_t = []
        # Primero vamos a crear la lista de cambios de los scripts
        lista_cambios_s.append(self._crear_lista_cambios(p_lista_vieja_s, p_lista_nueva_s, True))
        # A continuación repetimos para los TAGS
        lista_cambios_t.append(self._crear_lista_cambios(p_lista_vieja_t, p_lista_nueva_t, False))
        # Creamos el diccionario y enviamos los datos por socket
        lista_envio.append({'metodo': 'aplicar_cambios'})
        lista_envio.append({'id_usuario': p_id_usuario})
        lista_envio.append({'id_grupo': p_id_grupo})
        lista_envio.append({'lista_cambios_s': lista_cambios_s})
        lista_envio.append({'lista_cambios_t': lista_cambios_t})
        # todo habría que reconvertir ésta lista a un diccionario?
        lista_envio.append({'lista_alumnos': p_lista_alumnos})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def _crear_lista_cambios(self, p_lista_vieja, p_lista_nueva, p_es_script):
        """
        Genera la lista de cambios para los scripts

        :param p_lista_vieja: La lista vieja de Scripts
        :param p_lista_nueva: La lista nueva de Scripts
        :param p_es_script: True si es para crear una lista de cambios de scripts
                            False si es para crear una lista de cambios de TAGS
        :return: La lista de cambios
        """
        lista_cambios = []
        if len(p_lista_vieja) != 0:
            # Primero cotejamos la lista vieja con la nueva para eliminar scripts
            lista_borrado = p_lista_vieja(p_lista_nueva)
            # Ahora cotejamos la lista nueva con la vieja para saber cuáles son los scripts nuevos
            lista_anadir = p_lista_nueva(p_lista_vieja)
            # Creamos la lista de cambios
            for borrado in lista_borrado:
                if p_es_script:
                    lista_cambios.append({'accion': 'borrar_script',
                                          'IdScript': borrado['IdScript']})
                else:
                    lista_cambios.append({'accion': 'borrar_tag',
                                          'IdTag': borrado['IdTag']})
            for anadir in lista_anadir:
                if p_es_script:
                    lista_cambios.append({'accion': 'anadir_script',
                                          'IdScript': anadir['IdScript']})
                else:
                    lista_cambios.append({'acccion': 'anadir_tag',
                                          'IdTag': anadir['IdTag']})
        else:
            # Agregamos directamente la nueva lista
            for nueva in p_lista_nueva:
                if p_es_script:
                    lista_cambios.append({'accion': 'anadir_script',
                                          'IdScript': nueva['IdScript']})
                else:
                    lista_cambios.append({'accion': 'anadir_tag',
                                          'IdTag': nueva['IdTag']})
        return lista_cambios
