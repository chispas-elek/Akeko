# -*- encoding: utf-8 -*-

__author__ = 'Rubén Mulero'


from PyQt5 import QtGui, QtWidgets, QtCore
import Tag

class ListaTag(object):

    def __init__(self):
        self.lista = []

    # Definición de los métodos necesarios

    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

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
        encontrado = False
        it = self._obtener_iterador()
        while not encontrado:
            try:
                tag = it.next()
                if p_elemento.id_tag == tag.id_tag:
                    encontrado = True
            except StopIteration:
                break
        return encontrado

    def filtrado_script(self, p_c_gestionar_script, p_lista_s):
        """
        Elimina los scripts redundantes que ya puedan estar incluidos en los TAGS

        :param p_lista_s: La lista de scripts
        :return: Una lista de scripts con los scripts redundantes eliminados
        """
        scripts_filtrados = p_lista_s
        for elemento in self.lista:
            sus_scripts_elemento = p_c_gestionar_script.obtener_scripts_tag(elemento.id_tag)
            # Cotejamos la lista de scripts con la lista de scripts del TAG y filtramos
            scripts_filtrados = scripts_filtrados.cotejar_lista_s(sus_scripts_elemento)

        return scripts_filtrados

    def cargar_lista_tag(self, p_iu_list_item):
        """
        Se encarga de cargar en un elemento list de QT los nombres del Tag para mostrarlos en la interfaz

        :param p_item_tag El item del tag a introducir
        :param p_iu_list_item: El objeto de list_aplicados o list_disponibles a rellenar
        :return:
        """
        for elemento in self.lista:
            # item_tag = QtWidgets.QListWidgetItem()
            item_tag = ListWidgetItem()
            item_tag.setData(QtCore.Qt.UserRole, QtCore.QVariant(("tag", elemento)))
            item_tag.setIcon(QtGui.QIcon("plasma-next-icons/Breeze/actions/toolbar/get-hot-new-stuff.svg"))
            item_tag.setText(elemento.nombre_tag)
            p_iu_list_item.addItem(item_tag)

    def deconstruir(self):
        """
        Transformamos la lista en un array de diccionarios
        :return: Un array de diccionarios con los elementos de la lista
        """
        lista_dic = []
        for elemento in self.lista:
            lista_dic.append({'IdTag': elemento.id_tag,
                              'NombreTag': elemento.nombre_tag,
                              'Descripcion': elemento.descripcion,
                              'FechaCreacion': elemento.f_creacion,
                              'IdUsuario': elemento.usuario
                              # Necesito meter también la lista de los scripts?
                              })
        return lista_dic

    def construir(self, p_lista_diccionario):
        """
        Construimos la lista a partir de los datos que nos trae un diccionario
        :param p_lista_diccionario: Un diccionario con los datos
        :return:
        """
        for diccionario in p_lista_diccionario:
            un_tag = Tag.Tag(diccionario['IdTag'], diccionario['NombreTag'],
                            diccionario['Descripcion'], diccionario['FechaCreacion'],
                            diccionario['IdUsuario'], None)
            self.lista.append(un_tag)


# Reimplemento la clase ListWidgetItem para que ponga los Tags por encima de los Scripts
# Ordenados de forma alfabética

class ListWidgetItem(QtWidgets.QListWidgetItem):
    def __lt__(self, other):
        other_datos = other.data(QtCore.Qt.UserRole)
        if other_datos[0] == "script":
            return True
        else:
            return self.text() < other.text()
