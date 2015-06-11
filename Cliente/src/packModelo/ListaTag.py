# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class ListaTag(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios

    def cotejar_lista(self, p_lista_tag):
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

