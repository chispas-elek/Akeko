# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

"""
Server sender es una clase que tiene como objetivo crear un socket con los valores
del server ya establecidos y facilitar al usuario el envío de los datos a un servidor en particular.
En un princio la idea es obtener el destino del server mediante la conexión inicial que se leerá de
un archivo de configuración
"""

import json
import Decoder
import socket


class ServerSender(object):
    # Definimos dos constantes y encapsulamos en privativo.
    __SERVER_NAME = "localhost"
    __PORT = 13373

    def __init__(self, p_datos_enviar):
        # Creamos el Socket y le pasamos los parámetros básicos de conexión
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.datos_enviar = p_datos_enviar

    def enviar_datos(self, intento=0):
        if intento < 10:
            try:
                # Comprobamos si el servidor existe
                remote_ip = socket.gethostbyname(self.__SERVER_NAME)
                # Nos conectamos al servidor
                self.s.connect((remote_ip, self.__PORT))
                # Serializamos y enviamos
                self.s.send(json.dumps(self.datos_enviar))
                # Recibo la respuesta del servidor y la devuelvo
                result = Decoder.Decoder(self.s.recv(1024))
                # Correcto, cerramos y devolvemos.
                self.s.close()
                return result.decode_json()
            except socket.gaierror:
                # No se puede conectar al servidor. No gethostname.
                print "No se ha podido conectar al servidor. Intento: ", intento
                intento += 1
                self.enviar_datos(intento)
            except socket.error as msg:
                # Se ha producido un error con el socket
                print msg
                intento += 1
                self.enviar_datos(intento)
        else:
            # Después de 10 intentos no ha sido posible enviar el socket
            # Devolvemos un None para indicar el error.
            print "El envío del socket ha excedido el número de intentos"
            self.s.close()
            return None