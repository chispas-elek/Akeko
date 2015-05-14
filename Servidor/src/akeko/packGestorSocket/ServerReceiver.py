# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import SocketServer
import json
import Decoder

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True


class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    # Gestiona las conexiones que recibe de cada cliente y elige lo que debe hacer.
    def handle(self):
        try:
            reciv = Decoder.Decoder(self.request.recv(1024).strip())
            data = reciv.decode_json()
            # A partir de éste punto elegimos qué se debe de hacer.

            print "Hay que llamar a la clase %s" % data[0]
            for i in range(1, len(data)):
                # Creamos un objeto de tipo persona y lo imprimimos.
                print "Hey"
                # una_persona = Persona.Persona(data[i]['nombre'], data[i]['apellido'])
                # print una_persona.ImprimirDatos()
            # send some 'ok' back

            self.request.sendall(json.dumps({'return':'ok'}))
        except Exception, e:
            print "Exception al recibir el mensaje del cliente: ", e
            self.request.sendall(json.dumps({'return':'fail'}))


# Configuracion de los datos de escucha y ejecucion infinita del servidor.
if __name__ == "__main__":
    HOST, PORT = '127.0.0.1', 13373
    server = MyTCPServer((HOST, PORT), MyTCPServerHandler)
    server.serve_forever()