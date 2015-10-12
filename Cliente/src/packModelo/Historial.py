# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class Historial(object):

    def __init__(self, p_id_historial, p_nombre_script, p_nombre_tag, p_nombre_alumno,
                 p_apellido, p_nombre_grupo, p_fecha_creacion_h, p_id_usuario, p_accion, p_informacion):


        self.id_historial = p_id_historial
        if p_nombre_script is None:
            self.nombre_script = "--"
        else:
            self.nombre_script = p_nombre_script
        if p_nombre_tag is None:
            self.nombre_tag = "--"
        else:
            self.nombre_tag = p_nombre_tag
        if p_nombre_alumno is None and p_apellido is None:
            self.nombre_alumno = "--"
            self.apellido = ""
        else:
            self.nombre_alumno = p_nombre_alumno
            self.apellido = p_apellido
        if p_nombre_grupo is None:
            self.nombre_grupo = "--"
        else:
            self.nombre_grupo = p_nombre_grupo
        self.fecha_creacion_h = p_fecha_creacion_h
        self.id_usuario = p_id_usuario
        self.accion = p_accion
        self.informacion = p_informacion

    # Seteamos los Getters y los Setters

    @property
    def id_historial(self):
        return self.__id_historial

    @id_historial.setter
    def id_historial(self, un_id_historial):
        self.__id_historial = un_id_historial

    @property
    def nombre_script(self):
        return self.__nombre_script

    @nombre_script.setter
    def nombre_script(self, un_nombre_script):
        self.__nombre_script = un_nombre_script

    @property
    def nombre_tag(self):
        return self.__nombre_tag

    @nombre_tag.setter
    def nombre_tag(self, un_nombre_tag):
        self.__nombre_tag = un_nombre_tag

    @property
    def nombre_alumno(self):
        return self.__nombre_alumno

    @nombre_alumno.setter
    def nombre_alumno(self, un_nombre_alumno):
        self.__nombre_alumno = un_nombre_alumno

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, un_apellido):
        self.__apellido = un_apellido

    @property
    def nombre_grupo(self):
        return self.__nombre_grupo

    @nombre_grupo.setter
    def nombre_grupo(self, un_nombre_grupo):
        self.__nombre_grupo = un_nombre_grupo

    @property
    def fecha_creacion_h(self):
        return self.__fecha_creacion_h

    @fecha_creacion_h.setter
    def fecha_creacion_h(self, una_fecha_creacion_h):
        self.__fecha_creacion_h = una_fecha_creacion_h

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, un_id_usuario):
        self.__id_usuario = un_id_usuario

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
