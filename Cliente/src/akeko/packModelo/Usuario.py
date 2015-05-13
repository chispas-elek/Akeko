# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'


class Usuario(object):

    def __init__(self, p_id_usuario, p_usuario, p_contrasena, p_email, p_nombre, p_apellido, p_dni, p_f_alta):
        self.id_usuario = p_id_usuario
        self.usuario = p_usuario
        self.contrasena = p_contrasena
        self.email = p_email
        self.nombre = p_nombre
        self.apellido = p_apellido
        self.dni = p_dni
        self.f_alta = p_f_alta

    # Programamos los getters y los setters

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, un_id_usuario):
        self.__id_usuario = un_id_usuario

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, un_usuario):
        self.__usuario == un_usuario

    @property
    def contrasena(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, una_contrasena):
        self.__contrasena = una_contrasena

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, un_email):
        self.__email = un_email

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
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, un_dni):
        self.__dni = un_dni

    @property
    def f_alta(self):
        return self.__f_alta

    @f_alta.setter
    def f_alta(self, una_f_alta):
        self.__f_alta = una_f_alta