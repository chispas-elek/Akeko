# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


import Historial

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
                              'IdScript': elemento.id_script,
                              'IdTag': elemento.id_tag,
                              'Dni': elemento.dni,
                              'IdUsuario': elemento.id_usuario,
                              'IdGrupo': elemento.id_grupo,
                              'Fecha': elemento.fecha_crea,
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
            un_historial = Historial.Historial(diccionario['IdHist'], diccionario['IdScript'],
                                            diccionario['IdTag'], diccionario['Dni'],
                                            diccionario['IdUsuario'], diccionario['IdGrupo'],
                                            diccionario['Fecha'], diccionario['Accion'],
                                            diccionario['Informacion'])
            self.lista.append(un_historial)
