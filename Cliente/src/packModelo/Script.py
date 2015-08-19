# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class Script(object):

    def __init__(self, p_id_script, p_nombre_s, p_descripcion, p_activo, p_ruta):
        self.id_script = p_id_script
        self.nombre_s = p_nombre_s
        self.descripcion = p_descripcion
        self.activo = p_activo
        self.ruta = p_ruta

    # Programamos los getters y los setters

    @property
    def id_script(self):
        return self.__id_script

    @id_script.setter
    def id_script(self, un_id_script):
        self.__id_script = un_id_script

    @property
    def nombre_s(self):
        return self.__nombre_s

    @nombre_s.setter
    def nombre_s(self, un_nombre_s):
        self.__nombre_s = un_nombre_s

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, una_descripcion):
        self.__descripcion = una_descripcion

    @property
    def activo(self):
        return self.__activo

    @activo.setter
    def activo(self, un_activo):
        self.__activo = un_activo

    @property
    def ruta(self):
        return self.__ruta

    @ruta.setter
    def ruta(self, una_ruta):
        self.__ruta = una_ruta