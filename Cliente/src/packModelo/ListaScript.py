# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import Script
from PyQt5 import QtGui, QtWidgets, QtCore

class ListaScript(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios

    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

    def obtener_tamano_lista(self):
        """
        Obtiene el tamaño de la lista

        :return: El número de elementos que tiene la lista
        """

        return len(self.lista)

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
        encontrado = False
        it = self._obtener_iterador()
        while not encontrado:
            try:
                script = it.next()
                if p_elemento.id_script == script.id_script:
                    encontrado = True
            except StopIteration:
                break
        return encontrado

    def cargar_lista_script(self, p_iu_list_item):
        """
        Se encarga de cargar en un elemento list de QT los nombres del Tag para mostrarlos en la interfaz

        :param p_iu_list_item: El objeto de list_aplicados o list_disponibles a rellenar
        :return:
        """
        for elemento in self.lista:
            # item_script = QtWidgets.QListWidgetItem()
            item_script = ListWidgetItem()
            item_script.setData(QtCore.Qt.UserRole, QtCore.QVariant(("script", elemento)))
            item_script.setIcon(QtGui.QIcon("plasma-next-icons/Breeze/actions/toolbar/irc-operator.svg"))
            item_script.setText(elemento.nombre_s)
            p_iu_list_item.addItem(item_script)

    def imprimir_elementos_iu(self, p_label):
        """
        Ésta función sirve para poder cargar los Scritps que pertenecen a un TAG e imprimirlos en la interfaz
        que sea necesaria

        :param p_label:
        :return:
        """
        imprimir = ""
        for elemento in self.lista:
           imprimir = imprimir + elemento.nombre_s + " -- "

        p_label.setText(imprimir)

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
            un_script = Script.Script(diccionario['IdScript'], diccionario['NombreScript'],
                                            diccionario['Descripcion'], None, None)
            self.lista.append(un_script)


# Reimplemento la clase de WidgetItem para que ponga los Scripts por debajo de los tags
# y los ordene de forma alfabética.

class ListWidgetItem(QtWidgets.QListWidgetItem):
    def __lt__(self, other):
        other_datos = other.data(QtCore.Qt.UserRole)
        if other_datos[0] == "tag":
            return False
        else:
            return self.text() < other.text()
