# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class Alumno(object):

    def __init__(self, p_dni_a, p_nombre_a, p_apellido_a, p_email_a):
        self.dni_a_a = p_dni_a
        self.nombre_a = p_nombre_a
        self.apellido_a = p_apellido_a
        self.email_a = p_email_a

    # Programamos los getters y los setters

    @property
    def dni_a(self):
        return self.__dni_a

    @dni_a.setter
    def dni_a(self, un_dni_a):
        self.__dni_a = un_dni_a

    @property
    def nombre_a(self):
        return self.__nombre_a

    @nombre_a.setter
    def nombre_a(self, un_nombre_a):
        self.__nombre_a = un_nombre_a

    @property
    def apellido_a(self):
        return self.__apellido_a

    @apellido_a.setter
    def apellido_a(self, un_apellido_a):
        self.__apellido_a = un_apellido_a

    @property
    def email_a(self):
        return self.__email_a

    @email_a.setter
    def email_a(self, un_email_a):
        self.__email_a = un_email_a
