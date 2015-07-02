# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import Script


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

    def deconstruir(self):
        """
        Transformamos la lista en un array de diccionarios
        :return: Un array de diccionarios con los elementos de la lista
        """
        lista_dic = []
        for elemento in self.lista:
            lista_dic.append({'IdScript': elemento.id_script,
                              'NombreS': elemento.nombre_s,
                              'Descripcion': elemento.descripcion,
                              'Activo': elemento.activo,
                              'Ruta': elemento.ruta,
                              })
        return lista_dic

    def construir(self, p_lista_diccionario):
        """
        Construimos la lista a partir de los datos que nos trae un diccionario
        :param p_lista_diccionario: Un diccionario con los datos
        :return:
        """
        for diccionario in p_lista_diccionario:
            un_script = Script.Script(diccionario['IdScript'], diccionario['NombreS'],
                                            diccionario['Descripcion'], diccionario['Activo'],
                                            diccionario['Ruta'])
            self.lista.append(un_script)
