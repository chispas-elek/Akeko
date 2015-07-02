# -*- encoding: utf-8 -*-

__author__ = 'Rubén Mulero'

import Grupo


class ListaGrupo(object):
    def __init__(self):
        self.lista = []

    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

    def buscar_nombre(self, p_nombre_grupo):
        """
        Busca si existe o no el nombre de un grupo
        :param p_nombre_grupo: El nombre del grupo
        :return: True o False
        """
        encontrado = False
        it = self._obtener_iterador()
        while not encontrado:
            try:
                grupo = it.next()
                if grupo.nombre_grupo == p_nombre_grupo:
                    # El nombre del grupo existe
                    encontrado = True
            except StopIteration:
                break
        return encontrado

    def _obtener_iterador(self):
        return iter(self.lista)

    def deconstruir(self):
        """
        Transformamos la lista en un array de diccionarios

        :return: Un array de diccionarios con los elementos de la lista
        """
        lista_dic = []
        for elemento in self.lista:
            lista_dic.append({'IdGrupo': elemento.id_grupo,
                              'NombreGrupo': elemento.nombre_grupo,
                              'FechaCreacion': elemento.f_creacion,
                              'IdUsuario': elemento.usuario})
        return lista_dic

    def construir(self, p_lista_diccionario):
        """
        Construimos la lista a partir de los datos que nos trae un diccionario
        :param p_lista_diccionario: Un diccionario con los datos
        :return:
        """
        for diccionario in p_lista_diccionario:
            un_grupo = Grupo.Grupo(diccionario['IdGrupo'], diccionario['NombreGrupo'],
                                   diccionario['FechaCreacion'], None, None, None,
                                   diccionario['IdUsuario'])

            self.lista.append(un_grupo)
