# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class ListaAlumno(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios
    def anadir(self, p_elemento):
        self.lista.append(p_elemento)
