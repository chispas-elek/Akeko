# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import collections
from Cliente.src.packGestorSocket import ServerSender
from Cliente.src.packModelo import ListaScript, ListaTag


class Singleton(type):
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance


class CMisTags(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_todos_los_usuarios(self):
        """
        Obtiene todos los usuarios del sistema para mostrarlos en el Propietario
        :return:
        """
        pass

    def obtener_tags_usuario(self, p_id_usuario):
        """
        Obtiene los tags del usuario en "MIS TAGS"

        :param p_id_usuario: El identificador del usuario
        :return: La lista que contiene los tags
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_tags_usuario'})
        lista_envio.append({'id_usuario': p_id_usuario})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        lista_tags = ListaTag.ListaTag()
        lista_tags.construir(resultado)
        return lista_tags

    def obtener_scripts_tag(self, p_id_tag):
        """
        Obtiene los Scripts que tiene un Tag

        :param p_id_tag: El identificador del TAG
        :return: La lista de scripts que contiene el TAG
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_scripts_tag'})
        lista_envio.append({'id_tag': p_id_tag})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        lista_scripts = ListaScript.ListaScript()
        lista_scripts.construir(resultado)
        return lista_scripts

    def obtener_scripts_no_en_tag(self, p_id_tag):
        """
        Obtiene la lista de scripts que NO contiene un TAG

        :param p_id_tag: El identificador del tag
        :return: La lista de scripts que NO contiene un tag
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_scripts_no_en_tag'})
        lista_envio.append({'id_tag': p_id_tag})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        lista_scripts = ListaScript.ListaScript()
        lista_scripts.construir(resultado)
        return lista_scripts

    def anadir_tag(self, p_nombre_tag, p_id_usuario, p_descripcion, p_lista_scrip):
        """
        Añadimos un nuevo Tag en el sistema

        :param p_nombre_tag: El nombre del tag a agregar
        :param p_id_usuario: El identificador del usuario
        :param p_descripcion: La descripción del tag
        :param p_lista_scrip: La lista que contiene los scripts
        :return:
        """
        # todo habrá que modificar el nombre del método a crear_tag_usuario
        lista_envio = []
        lista_envio.append({'metodo': 'anadir_tag'})
        lista_envio.append({'nombre_tag': p_nombre_tag,
                            'id_usuario': p_id_usuario,
                            'descripcion': p_descripcion,
                            'lista_script': p_lista_scrip
                            })
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def modificar_tag(self, p_id_usuario, p_id_tag, p_nombre_tag, p_lista_vieja_s,
                      p_lista_nueva_s, p_owner, p_descripcion):
        """
        Modifica los scripts de un Tag.

        :param p_id_usuario: El identificador de un usuario
        :param p_id_tag: El identificador del tag a modificar
        :param p_nombre_tag: El nuevo nombre del Tag
        :param p_lista_vieja_s: La lista antigua de scripts
        :param p_lista_nueva_s: La lista nueva de scripts
        :param p_owner: El nuevo owner del grupo (El identificador del nuevo propietario
        :param p_descripcion: La nueva descripción del tag
        :return:
        """
        # Lo primero es crear una lista de cambios con los scripts
        lista_envio = []
        # Primero comaramos si los scripts son iguales
        comparar = lambda x, y: collections.Counter(x) == collections.Counter(y)
        if comparar(p_lista_vieja_s, p_lista_nueva_s):
            # Las listas son iguales
            lista_cambios = None
        else:
            # La lista de scritps es distinta
            lista_cambios = self._crear_lista_cambios(p_lista_vieja_s, p_lista_nueva_s)

        lista_envio.append({'metodo': 'modificar_tag'})
        lista_envio.append({'id_usuario': p_id_usuario,
                            'id_tag': p_id_tag,
                            'nombre_tag': p_nombre_tag,
                            'owner': p_owner,
                            'descripcionn': p_descripcion,
                            'lista_cambios': lista_cambios
                            })

        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def eliminar_tag_usuario(self, p_id_tag, p_id_usuario):
        """
        Elimina el tag de un usuario del sistema

        :param p_id_tag: El identificador del Tag
        :param p_id_usuario: El identificador del usuario
        :return: True -> Si todo ha ido bien
                False -> Si algo no ha ido bien
        """
        lista_envio = []
        lista_envio.append({'metodo': 'eliminar_tag_usuario'})
        lista_envio.append({'id_tag': p_id_tag,
                            'id_usuario': p_id_usuario})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def _crear_lista_cambios(self, p_lista_vieja, p_lista_nueva):
        """
        Genera la lista de cambios para los scripts

        :param p_lista_vieja: La lista vieja de Scripts
        :param p_lista_nueva: La lista nueva de Scripts

        :return: La lista de cambios
        """
        lista_cambios = []
        if len(p_lista_vieja) != 0:
            # Primero cotejamos la lista vieja con la nueva para eliminar scripts
            lista_borrado = p_lista_vieja.cotejar_lista_s(p_lista_nueva)
            # Ahora cotejamos la lista nueva con la vieja para saber cuáles son los scripts nuevos
            lista_anadir = p_lista_nueva.cotejar_lista_s(p_lista_vieja)

            # Creamos la lista de cambios
            for borrado in lista_borrado:
                lista_cambios.append({'accion': 'borrar_script',
                                      'id_script': borrado.id_script})
            for anadir in lista_anadir:
                lista_cambios.append({'accion': 'anadir_script',
                                      'id_script': anadir.id_script})
        else:
            # Esto podria no producirse nunca.
            # Agregamos directamente la nueva lista
            for nueva in p_lista_nueva:
                lista_cambios.append({'accion': 'anadir_script',
                                      'id_script': nueva.id_script})
        return lista_cambios
