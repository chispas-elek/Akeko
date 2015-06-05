# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class ListaGrupo(object):

    def __init__(self):
        self.lista = []

    def anadir(self, p_elemento):
        self.lista.append(p_elemento)

    def buscar_nombre(self, p_nombre_grupo):
        """
        Busca si existe o no el nombre de un grupo
        :param p_nombre_grupo:
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
