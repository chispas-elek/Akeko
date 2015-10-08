# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

"""
Server sender es una clase que tiene como objetivo crear un socket con los valores
del server ya establecidos y facilitar al usuario el envío de los datos a un servidor en particular.
En un princio la idea es obtener el destino del server mediante la conexión inicial que se leerá de
un archivo de configuración
"""

import json
import socket
import Decoder
import time
import ssl


class ServerSender(object):
    # Definimos dos constantes y marcamos como internas
    # todo Definir un archivo para cambiar el valor del server name
    #__SERVER_NAME = 'chispas-rpi.no-ip.biz'
    __SERVER_NAME = '10.90.67.28'
    __PORT = 13373

    def __init__(self, p_datos_enviar):
        # Creamos el Socket y le pasamos los parámetros básicos de conexión
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # todo descomentar ésto para darle a los sockets un timeout
        #s.settimeout(10)
        # Creamos el socket SSL y le indicamos el certificado
        self.ssl_sock = ssl.wrap_socket(s,
                                        ca_certs="ssl/cacert.pem",
                                        cert_reqs=ssl.CERT_REQUIRED,
                                        ssl_version=ssl.PROTOCOL_TLSv1)
        self.datos_enviar = p_datos_enviar

    def enviar_datos(self, intento=0):
        if intento < 10:
            try:
                # Comprobamos si el servidor existe
                remote_ip = socket.gethostbyname(self.__SERVER_NAME)
                # Nos conectamos al servidor
                self.ssl_sock.connect((remote_ip, self.__PORT))
                # Serializamos y enviamos
                self.ssl_sock.send(json.dumps(self.datos_enviar))
                # Recibo la respuesta del servidor y la devuelvo
                result = Decoder.Decoder(self.ssl_sock.recv(4096))
                # Correcto, cerramos y devolvemos.
                self.ssl_sock.close()
                return result.decode_json()
            except socket.error as msg:
                # Se ha producido un error con el socket
                print msg, "Intento número", intento
                # Cerramos el socket y creamos uno nuevo
                self.ssl_sock.close()
                self.__init__(self.datos_enviar)
                intento += 1
                time.sleep(5)
                self.enviar_datos(intento)
        else:
            # Después de 10 intentos no ha sido posible enviar el socket
            # Devolvemos un None para indicar el error.
            print "El envío del socket ha excedido el número de intentos"
            self.ssl_sock.close()
            return None
