# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


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


class CGestionarScript(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_scripts(self, p_id_grupo):
        """
        Obtenemos la lista de los scripts aplicados en el grupo

        :param p_id_grupo: El identificador del grupo
        :return: La lista con los scripts aplicados
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_scripts'})
        lista_envio.append({'id_grupo': p_id_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        lista_script = ListaScript.ListaScript()
        lista_script.construir(resultado)
        return lista_script

    def obtener_tags(self, p_id_grupo):
        """
        Obtenemos la lista de Tags aplicados en el grupo

        :param p_id_grupo: El identificador del grupo
        :return: La lista con los tags aplicados
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_tags'})
        lista_envio.append({'id_grupo': p_id_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        lista_tag = ListaTag.ListaTag()
        lista_tag.construir(resultado)
        return lista_tag

    def obtener_scripts_disponibles(self, p_id_grupo):
        """
        Obtenemos la lista de scripts que estén disponibles para el grupo

        :param p_id_grupo: El identificador del grupo
        :return: La lista con los scripts disponibles
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_scripts_disponibles'})
        lista_envio.append({'id_grupo': p_id_grupo})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        lista_script_dispo = ListaScript.ListaScript()
        lista_script_dispo.construir(resultado)
        return lista_script_dispo

    def obtener_tags_disponibles(self, p_id_grupo, p_id_usuario):
        """
        Obtenemos la lista de Tags disponibles para el grupo

        :param p_id_grupo: El identificador del grupo
        :param p_id_usuario: El identificador del usuario
        :return: La lista con los tags disponibles
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_tags_disponibles'})
        lista_envio.append({'id_grupo': p_id_grupo,
                            'id_usuario': p_id_usuario
                            })
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        lista_tag_dispo = ListaTag.ListaTag()
        lista_tag_dispo.construir(resultado)
        return lista_tag_dispo

    def obtener_scripts_tag(self, p_id_tag):
        """
        Dado el identificador de un TAg. Obtiene la lista de Scripts que Posee

        :param p_id_tag:
        :return:
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_scripts_tag'})
        lista_envio.append({'id_tag': p_id_tag})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        lista_scripts_tag = ListaScript.ListaScript()
        lista_scripts_tag.construir(resultado)
        return lista_scripts_tag

    def aplicar_cambios(self, p_id_usuario, p_id_grupo, p_lista_alumnos,
                        p_lista_disponibles_previa, p_lista_disponibles_actual,
                        p_lista_aplicados_previa, p_lista_aplicados_actual):

        lista_envio = []
        # Lo primero es crear dos listas de elementos que contengan los tags y los scripts
        lista_cambios_s = []
        lista_cambios_t = []
        # Vamos a realizar un filtrado de los scripts aplicados para eliminar redundancias
        lista_aplicados_filtrada = self._filtrar_scripts(p_lista_aplicados_actual)
        if lista_aplicados_filtrada is not None:
            # La lista se ha filtrado correctament
            # Vamos a comprobar qué script se han agregado
            self._crear_lista_cambios(lista_cambios_s, lista_cambios_t, p_lista_disponibles_actual,
                                      p_lista_aplicados_previa, False)
            self._crear_lista_cambios(lista_cambios_s, lista_cambios_t, p_lista_disponibles_previa,
                                      lista_aplicados_filtrada, True)
            # Si alguna de las listas tiene cambios, enviamos al servidor.
            if lista_cambios_s or lista_cambios_t:
                # Preparamos el envio de los datos
                lista_envio.append({'metodo': 'aplicar_cambios'})
                lista_envio.append({'id_usuario': p_id_usuario,
                                    'id_grupo': p_id_grupo,
                                    'lista_cambios_s': lista_cambios_s,
                                    'lista_cambios_t': lista_cambios_t,
                                    'lista_alumnos': p_lista_alumnos.deconstruir()})
                socket = ServerSender.ServerSender(lista_envio)
                resultado = socket.enviar_datos()
            else:
                print "Las listas no contienen cambios. Se habrán filtrado Scripts en algún Tag."
                resultado = True
        else:
            # Tenemos que devolver a la interfaz un dato para que  muestre un error de que hay 2 o más TAGS que tienen
            # Los mismos scripts por apicar y que ésto, no es deseable.
            resultado = None

        return resultado

    def _filtrar_scripts(self, p_lista_aplicados):
        """
        Ésta función separa los scripts y los tags en dos valores distintos y comprueba que no existan redundancias.
        Una redundancia es la existencia de un script, que ya está contenido en un TAG.

        :param p_lista_aplicados:
        :return: una lista con los scripts redundantes eliminados
                en caso de error se devueve None
        """
        lista_aplicados = p_lista_aplicados
        lista_filtrada = []
        fallo = False
        i = 0
        while i < len(lista_aplicados) and fallo is not True:
            item = lista_aplicados[i]
            item_data = item.data(QtCore.Qt.UserRole)
            if item_data[0] == "tag":
                # Tenemos un TAg, vamos a obtener sus TAGS y comprobar si existen en los demás elementos
                tag = item_data[1]
                lista_scripts_del_tag = self.obtener_scripts_tag(tag.id_tag)
                if len(lista_filtrada) != 0:
                    anadir = False
                    for filtrado in lista_filtrada:
                        filtrado_data = filtrado.data(QtCore.Qt.UserRole)
                        if filtrado_data[0] == "tag":
                            # Hay un Tag, Vamos a comprobar si son compatibles
                            otro_tag = filtrado_data[1]
                            lista_scripts_del_otro_tag = self.obtener_scripts_tag(otro_tag.id_tag)
                            resultado = lista_scripts_del_otro_tag.cotejar_lista_s(lista_scripts_del_tag)
                            if len(resultado) == lista_scripts_del_otro_tag.obtener_tamano_lista():
                                # No hay problema, no se repiten scripts
                                anadir = True
                            else:
                                print "El nuevo tag tiene scripts que ya contiene el que está en la lista de filtados"
                                lista_filtrada = None
                                fallo = True
                                break
                        else:
                            # Es imposible darse el caso que haya scripts, pero se deja programado por si acaso
                            otro_script = filtrado_data[1]
                            resultado = lista_scripts_del_tag.existe(otro_script)
                            if resultado:
                                # Elimino el script
                                lista_filtrada.remove(filtrado)
                            # El tag siempre va a tener preferencia sobre el Scipt
                            anadir = True
                    if anadir:
                        lista_filtrada.append(item)
                else:
                    # La lista de filtrado, está vacía, inserto directamente
                    lista_filtrada.append(item)

            else:
                # El item es un script. Comprobamos si éste es compatible con los TAGS que haya
                if len(lista_filtrada) != 0:
                    # Vamos a comprobar si los elementos son TAGS. En caso afirmativo comprobaremos si el script
                    # Es compatible
                    script = item_data[1]
                    resultado = False
                    j = 0
                    while j < len(lista_filtrada) and resultado is not True:
                        filtrado_2 = lista_filtrada[j]
                        filtrado_2_data = filtrado_2.data(QtCore.Qt.UserRole)
                        if filtrado_2_data[0] == "tag":
                            # Hay un tag, comprobamos compatiblidad
                            otro_tag = filtrado_2_data[1]
                            lista_scripts_del_otro_tag = self.obtener_scripts_tag(otro_tag.id_tag)
                            resultado = lista_scripts_del_otro_tag.existe(script)
                        else:
                            # Ya no existen más TAGS, no tiene sentido seguir recorriendo la lista
                            break
                        j += 1
                    if not resultado:
                        # Si resultado se ha mantenido False, es que el script no se encuentra en ningún TAG
                        # Podemos insertarlo
                        lista_filtrada.append(item)
                else:
                    # La lista de filtrados está vacía, insertamos el scrippt directamente
                    lista_filtrada.append(item)

            i += 1

        return lista_filtrada

    def _crear_lista_cambios(self, p_lista_cambios_s, p_lista_cambios_t, p_lista_disponible, p_lista_aplicado, p_accion):
        """
        Dada la acción emitida. Comprobaremos la lista disponible antigua, con la lista de aplicados nueva en busca
        de tags/scripts a agregar. O comprobaremos la lista antigua de aplicados con la lista nueva de disponibles
        en busca de tags/scripts a eliminar

        :param p_lista_cambios_s: La lista de cambios de los scripts
        :param p_lista_cambios_t: La lista de cambios de los tags
        :param p_lista_disponible: La lista diponibles, puede ser antigua o nueva
        :param p_lista_aplicado: La lista de aplicados, puede ser antigua o nueva
        :param p_accion: True para Mirar que añadir
                        False para mirar que eliminar.
        :return:
        """

        if p_accion:
            # Vamos a comprobar que tenemos que AÑADIR
            # Recorremos la lista vieja de disponibles y miramos qué elementos han pasado a la nueva lista de aplicados
            for item in p_lista_disponible:
                item_aplicado_encontrado = False
                i = 0
                while i < len(p_lista_aplicado) and item_aplicado_encontrado is not True:
                    elemento = p_lista_aplicado[i]
                    if elemento is item:
                        # El elemento se encuentra en la nueva lista
                        elemento_data = elemento.data(QtCore.Qt.UserRole)
                        if elemento_data[0] == "tag":
                            # El elemento es un tag
                            p_lista_cambios_t.append({'accion': 'anadir_tag',
                                                      'id_tag': elemento_data[1].id_tag})
                        else:
                            # El elemento es un script
                            p_lista_cambios_s.append({'accion': 'anadir_script',
                                                     'id_script': elemento_data[1].id_script})
                        item_aplicado_encontrado = True
                    i += 1
        else:
            # Vamos a comprobar que tenemos que BORRAR
            for item_2 in p_lista_aplicado:
                item_disponible_encontrado = False
                j = 0
                while j < len(p_lista_disponible) and item_disponible_encontrado is not True:
                    elemento_2 = p_lista_disponible[j]
                    if elemento_2 is item_2:
                        # El elemento se encuentra en la nueva lista
                        elemento_2_data = elemento_2.data(QtCore.Qt.UserRole)
                        if elemento_2_data[0] == "tag":
                            # El elemento es un tag
                            p_lista_cambios_t.append({'accion': 'borrar_tag',
                                                        'id_tag': elemento_2_data[1].id_tag})
                        else:
                            # El elemento es un script
                            p_lista_cambios_s.append({'accion': 'borrar_script',
                                                        'id_script': elemento_2_data[1].id_script})
                        item_disponible_encontrado = True
                    j += 1
