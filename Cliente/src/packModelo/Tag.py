# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class Tag(object):

    def __init__(self, p_id_tag, p_nombre_tag, p_descripcion, p_f_creacion, p_usuario, p_lista_s):
        self.id_tag = p_id_tag
        self.nombre_tag = p_nombre_tag
        self.descripcion = p_descripcion
        self.f_creacion = p_f_creacion
        self.usuario = p_usuario
        self.lista_s = p_lista_s

    # Getters y Setters

    @property
    def id_tag(self):
        return self.__id_tag

    @id_tag.setter
    def id_tag(self, un_id_tag):
        self.__id_tag = un_id_tag

    @property
    def nombre_tag(self):
        return self.__nombre_tag

    @nombre_tag.setter
    def nombre_tag(self, un_nombre_tag):
        self.__nombre_tag = un_nombre_tag

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, una_descripcion):
        self.__descripcion = una_descripcion

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