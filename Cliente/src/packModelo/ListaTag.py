# -*- encoding: utf-8 -*-
from Cliente.src.packModelo import Tag

__author__ = 'Rubén Mulero'

import Cliente.src.packModelo.Tag

class ListaTag(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios

    def cotejar_lista_t(self, p_lista_tag):
        """
        Cotejamos la lista de los Tags con otra lista para saber que TAGS NO están en la lista
        que hemos pasado como parámetro de entrada.

        :param p_lista_tag: La lista a cotejar.
        :return: Una lista que contiene los elementos que no existen en la nueva lista
        """
        # Verificamos las listas
        lista_elementos = []
        for elemento in self.lista:
            if not p_lista_tag.existe(elemento):
                # No existe el tag en la lista
                lista_elementos.append(elemento)
        return lista_elementos

    def _obtener_iterador(self):
        return iter(self.lista)

    def existe(self, p_elemento):
        """
        Comprueba si existe un elemento en la lista

        :param p_elemento: El elementoa  comprobar
        :return: True o False dependiendo si la lista contiene o no el elemento
        """
        if p_elemento in self.lista:
            return True
        else:
            return False

    def filtrado_script(self, p_lista_s):
        """
        Elimina los scripts redundantes que ya puedan estar incluidos en los TAGS

        :param p_lista_s: La lista de scripts
        :return: Una lista de scripts con los scripts redundantes eliminados
        """
        scripts_filtrados = p_lista_s

        for elemento in self.lista:
            sus_scripts_elemento = elemento.lista_s
            # Cotejamos la lista de scripts con la lista de scripts del TAG y filtramos
            scripts_filtrados = scripts_filtrados.cotejar_lista_s(sus_scripts_elemento)

        return scripts_filtrados

    # todo definir método que transforme la lista en una diccionario para envitar por JSON
    # def deconstruir(self):
    # todo definir un método que transforme un diccionario en la lista y añada todo
    # def construir(self, p_lista_diccionario):