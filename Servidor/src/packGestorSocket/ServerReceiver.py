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
from Servidor.src.packControladoras import GestorGrupo
from Servidor.src.packControladoras import GestorScript
from Servidor.src.packControladoras import GestorTag
from Servidor.src.packControladoras import GestorAlumno

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True


class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    # Gestiona las conexiones que recibe de cada cliente y elige lo que debe hacer.
    def handle(self):
        try:
            reciv = Decoder.Decoder(self.request.recv(1024).strip())
            data = reciv.decode_json()
            # Programamos el diccionario para elegir las acciones a realizar.
            operaciones = {'iniciar_sesion': self.iniciar_sesion,
                           'obtener_grupos': self.obtener_grupos,
                           'obtener_alumnos': self.obtener_alumnos,
                           'obtener_scripts': self.obtener_scripts,
                           'obtener_tags': self.obtener_tags,
                           'obtener_scripts_disponibles': self.obtener_scripts_disponibles,
                           'obtener_tags_disponibles': self.obtener_tags_disponibles,
                           'obtener_tags_usuario': self.obtener_tags_usuario,
                           'obtener_scripts_tag': self.obtener_scripts_tag,
                           'borrar_grupo': self.borrar_grupo,
                           }

            print "Hay que llamar a al gestor %s" % data[0]['metodo']
            # operaciones[seleccion](datos_entrada_del_metodo_elegido)
            resultado_operacion = operaciones[data[0]['metodo']](data)
            # devolvemos el resultado obtenido al cliente
            self.request.sendall(json.dumps(resultado_operacion))

            # send some 'ok' back
            # self.request.sendall(json.dumps({'return':'ok'}))
        except Exception, e:
            print "Exception al recibir el mensaje del cliente: ", e
            self.request.sendall(json.dumps({'return': 'fail'}))

    # Definimos los métodos para ejecutar cada necesidad recibida por el socket.

    def iniciar_sesion(self, p_data):
        # Comprobamos si el usuario y contraseña son correctos
        gestor_usu = GestorUsuario.GestorUsuario()
        usuario = p_data[1]['usuario']
        contrasena = p_data[1]['contrasena']
        resultado = gestor_usu.obtener_credenciales(usuario, contrasena)
        return resultado

    def obtener_grupos(self, p_data):
        # Obtenemos los grupos de un usuario
        gestor_grupo = GestorGrupo.GestorGrupo()
        id_usuario = p_data[1]['id_usuario']
        resultado = gestor_grupo.obtener_grupos(id_usuario)
        return resultado

    def obtener_alumnos(self, p_data):
        # Obtenemos la lista de alumnos de un grupo
        gestor_alumno = GestorAlumno.GestorAlumno()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_alumno.obtener_alumnos(id_grupo)
        return resultado

    def obtener_scripts(self, p_data):
        # Obtener la lista de los scripts aplicados en un grupo
        gestor_script = GestorScript.GestorScript()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_script.obtener_scripts(id_grupo)
        return resultado

    def obtener_tags(self, p_data):
        # Obtener la lista de los tags aplicados en un grupo
        gestor_tag = GestorTag.GestorTag()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_tag.obtener_tagss(id_grupo)
        return resultado

    def obtener_scripts_disponibles(self, p_data):
        # Obtener los scripts disponibles para un grupo
        gestor_script = GestorScript.GestorScript()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_script.obtener_scripts_disponibles(id_grupo)
        return resultado

    def obtener_tags_disponibles(self, p_data):
        # Obtener los tags disponibles para un grupo
        gestor_tag = GestorTag.GestorTag()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_tag.obtener_tags_disponibles(id_grupo)
        return resultado

    def obtener_tags_usuario(self, p_data):
        # Obtener los tags que posee un usuario. "Mis TAGS"
        gestor_tag = GestorTag.GestorTag()
        id_usuario = p_data[1]['id_usuario']
        resultado = gestor_tag.obtener_tags_usuario(id_usuario)
        return resultado

    def obtener_scripts_tag(self, p_data):
        """ Obtener los scripts que contiene un tag

        :param p_data: el identificador del tag
        :return:
        """
        gestor_script = GestorScript.GestorScript()
        id_tag = p_data[1]['id_tag']
        resultado = gestor_script.obtener_scripts_tag(id_tag)
        return resultado

    def borrar_grupo(self, p_data):
        """ Elimina un grupo seleccionado por el usuario

        Si algún alumno se queda huérfano(sin grupo alguno)
        sus datos serán eliminados del sistema.

        :param p_data: Contiene el id del grupo y el usuario
        :return:
        """
        pass

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
