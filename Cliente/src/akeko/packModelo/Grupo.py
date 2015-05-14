# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class Grupo(object):
    ############################################# Algunos de éstos parámetro sobran. Reviar bien.
    def __init__(self, p_id_grupo, p_nombre_grupo, p_f_creacion,
                p_lista_s, p_lista_t, p_lista_a, p_usuario):
        self.id_grupo = p_id_grupo
        self.nombre_grupo = p_nombre_grupo
        self.f_creacion = p_f_creacion
        self.lista_s = p_lista_s
        self.lista_t = p_lista_t
        self.lista_a = p_lista_a
        self.usuario = p_usuario

    # Getters y Setters

    @property
    def id_grupo(self):
        return self.__id_grupo

    @id_grupo.setter
    def id_grupo(self, un_id_grupo):
        self.__id_grupo = un_id_grupo

    @property
    def nombre_grupo(self):
        return self.__nombre_grupo

    @nombre_grupo.setter
    def nombre_grupo(self, un_nombre_grupo):
        self.__nombre_grupo = un_nombre_grupo

    @property
    def f_creacion(self):
        return self.__f_creacion

    @f_creacion.setter
    def f_creacion(self, una_f_creacion):
        self.__f_creacion = una_f_creacion

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, un_usuario):
        self.__usuario = un_usuario