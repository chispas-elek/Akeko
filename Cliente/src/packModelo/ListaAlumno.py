# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import Alumno


class ListaAlumno(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios
    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

    def _obtener_iterador(self):
        return iter(self.lista)

    def deconstruir(self):
        """
        Transformamos la lista en un array de diccionarios
        :return: Un array de diccionarios con los elementos de la lista
        """
        lista_dic = []
        for elemento in self.lista:
            lista_dic.append({'Dni': elemento.dni_a,
                              'Nombre': elemento.nombre_a,
                              'Apellido': elemento.apellido_a,
                              'Email': elemento.email_a})
        return lista_dic

    def construir(self, p_lista_diccionario):
        """
        Construimos la lista a partir de los datos que nos trae un diccionario
        :param p_lista_diccionario: Un diccionario con los datos
        :return:
        """
        for diccionario in p_lista_diccionario:
            un_alumno = Alumno.Alumno(diccionario['Dni'], diccionario['Nombre'],
                                      diccionario['Apellido'], diccionario['Email'])
            self.lista.append(un_alumno)
