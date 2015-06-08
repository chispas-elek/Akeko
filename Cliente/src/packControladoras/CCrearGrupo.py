# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from Cliente.src.packGestorSocket import ServerSender
from Cliente.src.packModelo import Alumno, ListaAlumno, ListaGrupo

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class CCrearGrupo(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def crear_grupo(self, p_id_usuario, p_nombre_grupo, p_lista_alumnos, p_lista_grupos):
        """
        Creamos un nuevo grupo en el sistema.
        Es importante saber que a la hora de crear un grupo se darán de alta aquellos
        alumnos que NO ESTEN REGISTRADOS todavía en el sistema.

        Los alumnos que ya estén registrados en el sistema(han sido agregados en otro grupo)
        no será necesario registrarlos de nuevo. Por ello éste método se encargará de subsanar
        esa condición particular.



        :param p_id_usuario: El identificador del usuario
        :param p_nombre_grupo: El nombre del grupo dado por el usuairo
        :param p_lista_alumnos: El diccionario que contiene los alumnos del nuevo grupo
        :return: None -> Si el grupo ya existe en el sistema
                0 -> Si existe un error en la BD a la hora de insertar el grupo
                1 -> Si todo ha ido bien
        """
        resultado = None
        # Primero comprobamos que el nombre no exista en mis grupos.
        ya_existe = p_lista_grupos.buscar_nombre(p_nombre_grupo)
        if ya_existe is not True:
            # El nombre del grupo no existe por lo que podemos proceder
            lista_envio = []
            lista_envio.append({'metodo': 'crear_grupo'})
            lista_envio.append({'id_usuario': p_id_usuario,
                                'nombre_grupo': p_nombre_grupo,
                                'lista_alumnos': p_lista_alumnos # Comprobar si enviar un tipo de dato da problemas
                                                                  # Puede ser necesario convertir ésto en un dict.
                                })
            socket = ServerSender.ServerSender(lista_envio)
            resultado = socket.enviar_datos()
        else:
            # El nombre del grupo existe. Devolvemos None para indicar Error
            print "El nombre del grupo ya existe"
        return resultado
