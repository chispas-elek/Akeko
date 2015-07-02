# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

from Cliente.src.packGestorSocket import ServerSender

from Cliente.src.packModelo import ListaHistorial, Historial

class Singleton(type):

    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance

class CHistorial(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_historial(self, p_id_usuario):
        """
        Carga el historial del usuario actual

        :param p_id_usuario: El identificador del usuario actual
        :return: El historial completo del usuario
        """
        lista_envio = []
        lista_envio.append({'metodo': 'obtener_historial'})
        lista_envio.append({'id_usuario': p_id_usuario})
        socket = ServerSender.ServerSender(lista_envio)
        resultado = socket.enviar_datos()
        # todo recuerda que con ésto solo obtienes las entradas con los identificadores, si quieres los datos tienes que realizar más llamadas
        # Por ejemplo, el nombre del TAG, el nombre del script, etc etc....
        return resultado

    def filtrar_historial(self, p_nombre_alumno, p_id_script,
                          p_fecha_ini, p_fecha_fin, p_lista_historial):
        """
        Realiza un filtrado del historial que se muestra en pantalla

        :param p_nombre_alumno: El nombre del alumno a filtrar
        :param p_id_script: El identificador del script
        :param p_fecha_ini: La fecha de inicio
        :param p_fecha_fin: La fecha Fin
        :param p_historial: El historial completo obtenido anteriormente desde "obtener_historial"
        :return: La lista del historial filtrada con todos los valores
        """
        historial_filtrado = []
        # todo hacer el filtrado del historial