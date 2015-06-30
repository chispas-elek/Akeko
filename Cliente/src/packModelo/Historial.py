# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class Historial(object):

    def __init__(self, p_id_historial, p_id_script, p_id_tag, p_dni,
                 p_id_usuario, p_id_grupo, p_fecha_crea, p_accion, p_informacion):

        self.id_historial = p_id_historial
        self.id_script = p_id_script
        self.id_tag = p_id_tag
        self.dni = p_dni
        self.id_usuario = p_id_usuario
        self.id_grupo = p_id_grupo
        self.fecha_crea = p_fecha_crea
        self.accion = p_accion
        self.informacion = p_informacion

    # getters y setters

    @property
    def id_historial(self):
         return self.__id_historial

    @id_historial.setter
    def id_historial(self, un_id_historial):
         self.__id_historial = un_id_historial

    @property
    def id_script(self):
        return self.__id_script

    @id_script.setter
    def id_script(self, un_id_scrit):
        self.__id_script = un_id_scrit

    @property
    def id_tag(self):
        return self.__id_tag

    @id_tag.setter
    def id_tag(self, un_id_tag):
        self.__id_tag = un_id_tag

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, un_dni):
        self.__dni = un_dni

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, un_id_usuario):
        self.__id_usuario = un_id_usuario

    @property
    def id_grupo(self):
        return self.__id_grupo

    @id_grupo.setter
    def id_grupo(self, un_id_grupo):
        self.__id_grupo = un_id_grupo

    @property
    def fecha_crea(self):
        return self.__fecha_crea

    @fecha_crea.setter
    def fecha_crea(self, una_fecha_crea):
        self.__fecha_crea = una_fecha_crea

    @property
    def accion(self):
        return self.__accion

    @accion.setter
    def accion(self, una_accion):
        self.__accion = una_accion

    @property
    def informacion(self):
        return self.__informacion

    @informacion.setter
    def informacion(self, una_informacion):
        self.__informacion = una_informacion

