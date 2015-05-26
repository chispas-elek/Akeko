# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

"""
ServerReceiver es una clase de escucha de sockets, la cual recibe un Socket determinado con información caracterísitca
y manda la acción necesaria para usar los gestores necesarios y llamar a la BD.
"""

import SocketServer
import json
import socket
import Decoder
from Servidor.src.packControladoras import GestorUsuario

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True


class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    # Gestiona las conexiones que recibe de cada cliente y elige lo que debe hacer.
    def handle(self):
        try:
            reciv = Decoder.Decoder(self.request.recv(1024).strip())
            data = reciv.decode_json()
            # Programamos el diccionario para elegir las acciones a realizar.
            # TODO hacer métodos personalizados basados en las acciones que se van a realizar
            # TODO y que Gestores van a ser necesarios.
            operaciones = {'iniciar_sesion': self.iniciar_sesion,
                           'GestorTag': 'NombreMetodo2',
                           'GestorScript': 'NombreMetodo3',
                           'GestorUsuario': 'NombreMetodo4',
                           'GestorGrupo': 'NombreMetodo5',
                           }

            print "Hay que llamar a al gestor %s" % data[0]['clase']
            # operaciones[seleccion](datos_entrada_del_metodo_elegido)
            resultado_operacion = operaciones[data[0]['metodo']](data)
            # devolvemos el resultado obtenido al cliente
            # self.request.sendall(json.dumps(resultado_operacion))

            """
            for i in range(1, len(data)):
                # Creamos un objeto de tipo persona y lo imprimimos.
                print "Hey"
                # una_persona = Persona.Persona(data[i]['nombre'], data[i]['apellido'])
                # print una_persona.ImprimirDatos()
            """
            # send some 'ok' back
            self.request.sendall(json.dumps({'return':'ok'}))
        except Exception, e:
            print "Exception al recibir el mensaje del cliente: ", e
            self.request.sendall(json.dumps({'return':'fail'}))

    # Definimos los métodos para ejecutar cada necesidad recibida por el socket.

    def iniciar_sesion(self, p_data):
        # Comprobamos si el usuario y contraseña son correctos
        gestor_usu = GestorUsuario.GestorUsuario()
        usuario = p_data[1]['usuario']
        contrasena = p_data[1]['contrasena']
        resultado = gestor_usu.obtener_credenciales(usuario, contrasena)
        return resultado


# Configuracion de los datos de escucha y ejecucion infinita del servidor.
if __name__ == "__main__":
    PORT = 13373
    try:
        # obtenemos la ip local de la máquina y ejecutamos el servidor en escucha.
        HOST = socket.gethostbyname(socket.gethostname())
        server = MyTCPServer((HOST, PORT), MyTCPServerHandler)
        server.serve_forever()
    except socket.error:
        print "Ha ocurrido un error a la hora de obtener" \
              "la ip local del servidor"
        exit()
