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


class CMisTags(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

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
        return resultado

    def obtener_scripts_tag(self, p_id_tag):
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_scripts_tag'})
        lista_envio.append({'id_tag': p_id_tag})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def anadir_modificar_tag(self, p_id_tag=None):
        """
        Decide si tiene que modificar o crear un nuevo TAG
        :param p_id_tag: El identificador del TAg. Por defecto vale None
        :return:
        """
        if p_id_tag is None:
            # Se pide crear un nuevo TAG
            pass
        else:
            # Se pide modificar un tag existente
            pass

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

    def modificar_tag(self, p_id_usuario, p_nombre_tag, p_lista_vieja_s,
                      p_lista_nueva_s, p_owner, p_descripcion):
        """
        Modifica los scripts de un Tag.

        :param p_id_usuario: El identificador de un usuario
        :param p_nombre_tag: El nuevo nombre del Tag
        :param p_lista_vieja_s: La lista antigua de scripts
        :param p_lista_nueva_s: La lista nueva de scripts
        :param p_owner: El nuevo owner del grupo (Propietario)
        :param p_descripcion: La nueva descripción del tag
        :return:
        """
        # Lo primero es crear una lista de cambios con los scripts
        lista_envio = []
        lista_cambios = self._crear_lista_cambios(p_lista_vieja_s, p_lista_nueva_s)
        lista_envio.append({'metodo': 'modificar_tag'})
        lista_envio.append({'id_usuario': p_id_usuario,
                            'nombre_tag': p_nombre_tag,
                            'owner': p_owner,
                            'descripcionn': p_descripcion,
                            'lista_cambios': lista_cambios
                            })
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        return resultado

    def eliminar_tag_usuario(self, p_tag, p_id_usuario):
        """
        Elimina el tag de un usuario del sistema

        :param p_id_tag: El identificador del Tag
        :param p_id_usuario: El identificador del usuario
        :return:
        """
        lista_envio = []
        lista_envio.append({'metodo': 'eliminar_tag'})
        # todo es una prueba, revisar si ésto funciona bien asi
        lista_envio.append({'id_tag': p_tag.Tag.id_tag,
                            'id_usuario': p_id_usuario,
                            'lista_s': p_tag.Tag.lista_s
                            })
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
            # Agregamos directamente la nueva lista
            for nueva in p_lista_nueva:
                lista_cambios.append({'accion': 'anadir_script',
                                      'id_script': nueva.id_script})
        return lista_cambios
