# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import Alumno


class ListaAlumno(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios
    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

    def eliminar(self, p_elemento):
        self.lista.remove(p_elemento)

    def _obtener_iterador(self):
        return iter(self.lista)

    def obtener_alumno(self, p_n_pos):
        """
        Dada una posición, obtiere el alumno

        :param p_n_pos: El número de la posición en la lista
        :return: Tipo de dato Alumno asociado a la posición pedida
        """
        return self.lista[p_n_pos]

    def obtener_tamano_lista(self):
        """
        Obtiene el tamaño de la lista

        :return: El número de elementos que tiene la lista
        """

        return len(self.lista)

    def exite_alumno(self, p_un_dni):
        """
        Comprueba si dentro de la lista existe un alumno basado en su DNI

        :param p_un_dni: El dni de un alumno
        :return: None si no existe un alumno, o un alumno en caso de existir.
        """
        alumno_encontrado = None
        encontrado = False
        it = self._obtener_iterador()
        while not encontrado:
            try:
                alumno = it.next()
                if p_un_dni == alumno.dni_a:
                    # El alumno existe
                    alumno_encontrado = alumno
                    encontrado = True
            except StopIteration:
                break
        return alumno_encontrado

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
