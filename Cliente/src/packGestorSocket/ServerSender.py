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
    __SERVER_NAME = '192.168.0.10'
    __PORT = 13373

    def __init__(self, p_datos_enviar):
        # Creamos el Socket y le pasamos los parámetros básicos de conexión
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # todo descomentar ésto para darle a los sockets un timeout
        s.settimeout(10)
        # Creamos el socket SSL y le indicamos el certificado
        self.ssl_sock = ssl.wrap_socket(s,
                                        ca_certs="ssl/cacert.pem",
                                        cert_reqs=ssl.CERT_REQUIRED,
                                        ssl_version=ssl.PROTOCOL_TLSv1)
        self.datos_enviar = p_datos_enviar

    # todo generar un parámetro optativo más para que ejecute la BETA en determinados casos puntuales
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
                result = Decoder.Decoder(self.ssl_sock.recv(8192))
                ##### BETA FUNCTION
                #result = Decoder.Decoder(self._recv_timeout(self.ssl_sock))
                # Correcto, cerramos y devolvemos.
                self.ssl_sock.close()
                return result.decode_json()
            except socket.error as msg:
                # Se ha producido un error con el socket
                print msg, " -- Intento número", intento
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

    def _recv_timeout(self, p_socket, timeout=0.4):
        """
        Consiste en un método que hace una espera para recibir los datagramas de los datos por TCP/IP

        La idea consiste en mantener la conexión abierta durante 4 segundos y reabrirla durante otros 4 segundos
        en caso de recibir nuevos datos.

        Si no se reciben datos en 4 segundos se da la transferencia por terminada y se une el resultado.

        :param p_socket: La instancia del Socket SSL
        :param timeout: El tiempo total que se le quiera dar de tinmeout
        :return:
        """
        # Hacer que el socket no espere a ver si aparecen o no datos.
        p_socket.setblocking(0)
        # total data es un array que recibirá todas las cadenas de datos
        total_data = []
        # Comienzo del temporizador
        begin = time.time()
        while 1:
            # Si tienes algo de datos y el tiempo se acaba, se termina el loop
            if total_data and time.time() - begin > timeout:
                break
            # Si no tiene nada de datos, esperamos un tiempo, el doble de lo marcado en la función.
            elif time.time() - begin > timeout * 1.2:
                break
            # Recibimos datos
            try:
                data = p_socket.recv(8192)
                if data:
                    total_data.append(data)
                    # Cambiamos el tiempo de comienzo
                    begin = time.time()
                else:
                    # Dormir para indicar un hueco.
                    time.sleep(0.1)
            except:
                pass

        # Juntar todas las partes y realizar un string.
        return ''.join(total_data)
