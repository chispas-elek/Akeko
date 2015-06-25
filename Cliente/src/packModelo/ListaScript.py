# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class ListaScript(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios

    def cotejar_lista_s(self, p_lista_script):
        """
        Cotejamos la lista de scripts con otra lista de scripts para saber qué scripts NO
        están en la lista que le hemos pasado como parámetro de entrada
        :param p_lista_script: La lista a cotejar
        :return: Una lista que contiene los elementos que no existen en la nueva lista
        """
        # Verificamos las listas
        lista_elementos = []
        for elemento in self.lista:
            if not p_lista_script.existe(elemento):
                # No existe el script en la lista
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

    # todo definir método que transforme la lista en una diccionario para envitar por JSON
    # def deconstruir(self):
    # todo definir un método que transforme un diccionario en la lista y añada todo
    # def construir(self, p_lista_diccionario):