# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class ListaAlumno(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios
    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

    def _obtener_iterador(self):
        return iter(self.lista)

    def convertir_a_dict(self, p_lista_alumno):
        # todo seria interesante poder convertir una lista en un diccionario con un sólo método
        pass
