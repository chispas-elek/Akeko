# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import Historial
import unicodedata
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtGui


class ListaHistorial(object):
    def __init__(self):
        self.lista = []

    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

    def filtrar_lista(self):
        pass

    def deconstruir(self):
        """
        Transformamos la lista en un array de diccionarios
        :return: Un array de diccionarios con los elementos de la lista
        """
        lista_dic = []
        for elemento in self.lista:
            lista_dic.append({'IdHist': elemento.id_historial,
                              'NombreScript': elemento.nombre_script,
                              'NombreTag': elemento.nombre_tag,
                              'NombreAlumno': elemento.nombre_alumno,
                              'Apellido': elemento.apellido,
                              'NombreGrupo': elemento.nombre_grupo,
                              'Fecha': elemento.fecha_creacion_h,
                              'IdUsuario': elemento.id_usuario,
                              'Accion': elemento.accion,
                              'Informacion': elemento.informacion
                              })
        return lista_dic

    def construir(self, p_lista_diccionario):
        """
        Construimos la lista a partir de los datos que nos trae un diccionario
        :param p_lista_diccionario: Un diccionario con los datos
        :return:
        """
        for diccionario in p_lista_diccionario:
            un_historial = Historial.Historial(diccionario['IdHist'], diccionario['NombreScript'],
                                               diccionario['NombreTag'], diccionario['NombreAlumno'],
                                               diccionario['Apellido'], diccionario['NombreGrupo'],
                                               diccionario['Fecha'], diccionario['IdUsuario'],
                                               diccionario['Accion'], diccionario['Informacion'])
            self.lista.append(un_historial)

    def generar_tabla(self, p_table_widged):
        """
        Genera una tabla con las entradas de la lista del historial

        :param p_table_widged: La tabla perteneciente a la interfaz
        :return:
        """
        p_table_widged.setRowCount(len(self.lista))
        for i in range(0, len(self.lista)):
            # Rellenamos la tabla
            historial = self.lista[i]
            newitem = QTableWidgetItem(historial.nombre_script)
            p_table_widged.setItem(i, 0, newitem)
            newitem = QTableWidgetItem(historial.nombre_tag)
            p_table_widged.setItem(i, 1, newitem)
            newitem = QTableWidgetItem(historial.nombre_alumno + " " + historial.apellido)
            p_table_widged.setItem(i, 2, newitem)
            newitem = QTableWidgetItem(historial.nombre_grupo)
            p_table_widged.setItem(i, 3, newitem)
            if historial.accion == 1:
                # Añadir
                newitem_anadir = QTableWidgetItem("Añadir")
                newitem_anadir.setIcon(QtGui.QIcon("/home/administrador/PycharmProjects/Akeko/Cliente/src/packVistas"
                                                   "/plasma-next-icons/Breeze/actions/toolbar/list-add.svg"))
                p_table_widged.setItem(i, 4, newitem_anadir)
            else:
                # Eliminar
                newitem_eliminar = QTableWidgetItem("Eliminar")
                newitem_eliminar.setIcon(QtGui.QIcon("/home/administrador/PycharmProjects/Akeko/Cliente/src/packVistas"
                                                     "/plasma-next-icons/Breeze/actions/toolbar/edit-delete.svg"))
                p_table_widged.setItem(i, 4, newitem_eliminar)

            newitem = QTableWidgetItem(historial.informacion)
            p_table_widged.setItem(i, 5, newitem)
            newitem = QTableWidgetItem(historial.fecha_creacion_h)
            p_table_widged.setItem(i, 6, newitem)

    def realizar_filtrado(self, p_criterio, p_busqueda, p_fecha_inicio, p_fecha_fin):
        """
        Dada una lista determinada. Recorre la lista actual y captura los elementos que tengan que ver con el criterio
        deseado

        :param p_lista_filtrar: La lista a querer filtrar
        :param p_criterio: El tipo de criterio escogido
        :param p_busqueda: La búsuqeda que se desea realizar

        :return: Una lista que contiene los objetos de los elementos que considere que coinciden con la búsqueda y el
                criterio establecido
        """
        # Haremos un mapeo y filtraremos de la lista los elementos necesarios
        lista_filtrada = []
        # normalizamos la búsqueda a str
        busqueda_normalizada = unicodedata.normalize('NFKD', p_busqueda).encode('ascii', 'ignore')
        # Seleccionamos el filtrado en base al criterior pedido
        # Realizamos un filtrado haciendo una función avanzada en una sola línea que itera la lista de elementos
        # y por cada elemento realiza una condición IF que pide si la búsqueda del usuario se encuentra en el elemento
        # actual. ---> Búsqueda usuario IN elemento_actual
        if p_criterio == 'nombre_alumno':
            print "Filtrado por nombre"
            lista_filtrada = [elemento for elemento in self.lista if busqueda_normalizada in elemento.nombre_alumno]
        elif p_criterio == 'apellido':
            print "Filtrado por apellido"
            lista_filtrada = [elemento for elemento in self.lista if busqueda_normalizada in elemento.apellido]
        elif p_criterio == 'nombre_grupo':
            print "Filtrado por grupo"
            lista_filtrada = [elemento for elemento in self.lista if busqueda_normalizada in elemento.nombre_grupo]
        elif p_criterio == 'nombre_script':
            print "Filtrado por Script"
            lista_filtrada = [elemento for elemento in self.lista if busqueda_normalizada in elemento.nombre_script]
        elif p_criterio == 'nombre_tag':
            print "Filtrado por Tag"
            lista_filtrada = [elemento for elemento in self.lista if busqueda_normalizada in elemento.nombre_tag]
        else:
            print "Error Garrafal"

        # Una vez filtrado por el criterio. Vamos a filtrar por la fecha establecida
        # Transformamos el tipo de objeto a uno entendible por Python
        fecha_inicio_python = p_fecha_inicio.toPyDate()
        fecha_fin_python = p_fecha_fin.toPyDate()

        # Realizamos el filtrado necesario
        # Hemos usado el mismo método de filtrado que antes. Pero poniendo como condición que el elmeento esté entre
        # las dos fechas
        # Fecha_inicio <= EL DATO <= Fecha_fin
        lista_filtrada_final = [elemento for elemento in lista_filtrada if fecha_inicio_python.strftime(
            "%d/%m/%Y") <= elemento.fecha_creacion_h <= fecha_fin_python.strftime("%d/%m/%Y")]

        return lista_filtrada_final
