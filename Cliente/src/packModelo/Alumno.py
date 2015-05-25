# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class Alumno(object):

    def __init__(self, p_dni, p_nombre, p_apellido, p_email):
        self.dni = p_dni
        self.nombre = p_nombre
        self.apellido = p_apellido
        self.email = p_email

    # Programamos los getters y los setters

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, un_dni):
        self.__dni = un_dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, un_nombre):
        self.__nombre = un_nombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, un_apellido):
        self.__apellido = un_apellido

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, un_email):
        self.__email = un_email