# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class ListaTag(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios

    def _obtener_iterador(self):
        return iter(self.lista)