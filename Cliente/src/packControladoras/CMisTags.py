# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import collections
from Cliente.src.packGestorSocket import ServerSender
from Cliente.src.packModelo import ListaScript, ListaTag
from PyQt5 import QtCore


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

    def obtener_todos_los_propietarios(self, p_id_usuario):
        """
        Obtiene todos los usuarios del sistema para mostrarlos en el Propietario

        :param p_id_usuario: El identificador del usuario actual
        :return:
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_todos_los_propietarios'})
        lista_envio.append({'id_usuario': p_id_usuario})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

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

    def crear_tag_usuario(self, p_nombre_tag, p_id_usuario, p_descripcion, p_lista_scrip):
        """
        Añadimos un nuevo Tag en el sistema

        :param p_nombre_tag: El nombre del tag a agregar
        :param p_id_usuario: El identificador del usuario
        :param p_descripcion: La descripción del tag
        :param p_lista_scrip: La lista que contiene los scripts
        :return:
        """
        lista_envio = []
        lista_envio.append({'metodo': 'crear_tag_usuario'})
        lista_envio.append({'nombre_tag': p_nombre_tag,
                            'id_usuario': p_id_usuario,
                            'descripcion': p_descripcion,
                            'lista_script': p_lista_scrip.deconstruir()
                            })
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def modificar_tag(self, p_id_usuario, p_id_tag, p_nombre_tag, p_owner, p_descripcion, p_lista_disponible_previa,
                        p_lista_disponible_actual, p_lista_en_el_tag_previa, p_lista_en_el_tag_actual):
        """
        Modifica los scripts que tiene actualmente el TAG y los aplica/elimina en los grupos afectados por el mismo.


        :param p_id_usuario: El identidicador del usuario
        :param p_id_tag: El identificador del TAg
        :param p_nombre_tag: El nombre del Tag
        :param p_owner: El propietario del Tag
        :param p_descripcion: La descripcción del Tag
        :param p_lista_disponible_previa: La lista de scripts disponibles previa
        :param p_lista_disponible_actual: La lista de scripts disponibles actual
        :param p_lista_en_el_tag_previa: La lista de scripts en el tag previa
        :param p_lista_en_el_tag_actual: La lista de scripts en el tag actual
        :return:
        """
        # inicializamos la lista de envío y de cambios
        lista_envio = []
        lista_cambios = []

        # Los tags deben contener a la fuerzaz minimo un script, por ello debemos recorrerlos SIEMPRE.
        # Se puede dar el caso que un usuario sólo busque moddificar los datos del TAG, en vez de otra cosa

        # Verificamos si debemos AÑADIR algun Script
        self._crear_lista_cambios(lista_cambios, p_lista_disponible_previa, p_lista_en_el_tag_actual, True)
        # Verificamos si debeoms ELIMINAR algún Script
        self._crear_lista_cambios(lista_cambios, p_lista_disponible_actual, p_lista_en_el_tag_previa, False)

        # todo merece la pena ponerse a comprobar datos para verificar si hace falta enviar al server?

        lista_envio.append({'metodo': 'modificar_tag'})
        lista_envio.append({'id_usuario': p_id_usuario,
                            'id_tag': p_id_tag,
                            'nombre_tag': p_nombre_tag,
                            'owner': p_owner,
                            'descripcion': p_descripcion,
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

    def _crear_lista_cambios(self, p_lista_cambios, p_lista_disponible, p_lista_en_el_tag, p_accion):
        """
        Crea la lista de cambios para el TAg actual.

        :param p_lista_cambios: La lista que contendrá los cambios
        :param p_lista_disponible: La lista de scripts disponibles. Puede ser la vieja o la nueva
        :param p_lista_en_el_tag:  La lista de scripts aplicados en el tag
        :param p_accion: True --> Vamos a mirar que scripts se añaden
                        False --> Vamos a mirar que scripts de borran

        :return: La lista de cambios deseada.
        """

        if p_accion:
            # Vamos a comprobar que tenemos que AÑADIR
            # Recorremos la lista vieja de disponibles y miramos qué elementos han pasado a la nueva lista de aplicados
            for item in p_lista_disponible:
                item_aplicado_encontrado = False
                i = 0
                while i < len(p_lista_en_el_tag) and item_aplicado_encontrado is not True:
                    elemento = p_lista_en_el_tag[i]
                    if elemento is item:
                        # El elemento se encuentra en la nueva lista
                        elemento_data = elemento.data(QtCore.Qt.UserRole)
                        p_lista_cambios.append({'accion': 'anadir_script',
                                                     'id_script': elemento_data[1].id_script})
                        item_aplicado_encontrado = True
                    i += 1
        else:
            # Vamos a comprobar que tenemos que BORRAR
            for item_2 in p_lista_en_el_tag:
                item_disponible_encontrado = False
                j = 0
                while j < len(p_lista_disponible) and item_disponible_encontrado is not True:
                    elemento_2 = p_lista_disponible[j]
                    if elemento_2 is item_2:
                        # El elemento se encuentra en la nueva lista
                        elemento_2_data = elemento_2.data(QtCore.Qt.UserRole)
                        p_lista_cambios.append({'accion': 'borrar_script',
                                                        'id_script': elemento_2_data[1].id_script})
                        item_disponible_encontrado = True
                    j += 1
