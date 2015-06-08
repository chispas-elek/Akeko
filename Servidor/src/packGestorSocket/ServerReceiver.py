# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

"""
ServerReceiver es una clase de escucha de sockets, la cual recibe un Socket determinado con información caracterísitca
y manda la acción necesaria para usar los gestores necesarios y llamar a la BD.
"""

from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
import json
import socket
import Decoder
import ssl
from Servidor.src.packControladoras import GestorUsuario
from Servidor.src.packControladoras import GestorGrupo
from Servidor.src.packControladoras import GestorScript
from Servidor.src.packControladoras import GestorTag
from Servidor.src.packControladoras import GestorAlumno


class MySSLTCPServer(TCPServer):
    # Sobreescribimos TCPServer para admitir conexiones SSL
    def __init__(self,
                 server_address,
                 request_handler_class,
                 certfile,
                 keyfile,
                 ssl_version=ssl.PROTOCOL_TLSv1,
                 bind_and_activate=True):
        # Inicializamos la clase padre
        TCPServer.__init__(self, server_address, request_handler_class, bind_and_activate)
        self.certfile = certfile
        self.keyfile = keyfile
        self.ssl_version = ssl_version

    def get_request(self):
        # Sobreescribimos get_request de la clase padre para crear el socket
        newsocket, fromaddr = self.socket.accept()
        connstream = ssl.wrap_socket(newsocket,
                                     server_side=True,
                                     certfile=self.certfile,
                                     keyfile=self.keyfile,
                                     ssl_version=self.ssl_version)
        return connstream, fromaddr


class MySSLThreadingTCPServer(ThreadingMixIn, MySSLTCPServer):
    """
    Hereda de dos clases. Una permite conexiónes asícronas y la otra me permite sobreescribir
    los méotdos de TCPServer para crear el socket ssl de la parte servidor
    """
    pass


class ServerHandler(StreamRequestHandler):
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
                           'cambiar_nombre': self.cambiar_nombre,
                           'anadir_tag': self.anadir_tag,
                           'crear_grupo': self.crear_grupo,
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

    def crear_grupo(self, p_data):
        """
        Crear un nuevo grupo en el sistema
        :param p_data: El identificador del usuario, el nombre del grupo y
                        los alumnos asociados
        :return: True o False dependiendo si se ha creado correctamente
        """
        gestor_alumno = GestorAlumno.GestorAlumno()
        gestor_grupo = GestorGrupo.GestorGrupo()
        id_usuario = p_data[1]['id_usuario']
        nombre_grupo = p_data[1]['nombre_grupo']
        lista_alumnos = p_data[1]['lista_alumnos']
        lista_alumnos_nuevos = []
        puedo_insertar = True
        # Vamos a comprobar que los alumnos estén correctos
        for alumno in lista_alumnos:
            existe = gestor_alumno.buscar_alumno(alumno['Dni'])
            if existe is None:
                # El alumno no existe, añadimos la intención
                lista_alumnos_nuevos.append(alumno)
            else:
                # El alumno existe en el sistema, vamos a ver si sus datos
                # Son correctos
                try:
                    if alumno['Nombre'] != existe['Nombre'] or alumno['Apellido'] != existe['Apellido'] \
                            or alumno['Email'] != existe['Email']:
                        # Existe un error con los datos del alumno. Lanzamos excepción
                        raise ErrorAlumno(alumno['Dni'])
                except ErrorAlumno, e:
                    print e
                    puedo_insertar = False
                    break
        # Ahora comprobamos si podemos o no insertar datos
        if puedo_insertar:
            # Insertamos los nuevos alumnos en el sistema
            for alumno_nuevo in lista_alumnos_nuevos:
                gestor_alumno.anadir_alumno(alumno_nuevo['Dni'], alumno_nuevo['Nombre'],
                                              alumno_nuevo['Apellido'], alumno_nuevo['Email'])
            # Agregamos el nuevo grupo, con sus alumnos asociados
            # Si ésta función devuelve True es que las cosas han ido bien
            resultado = gestor_grupo.anadir_grupo(nombre_grupo, id_usuario, lista_alumnos)
        else:
            # Algo ha fallado y debemos retornar un error
            resultado = {'return': 'Los datos de un alumno no son corretos'}  # Especificar qué alumno por sus Dni

        return resultado

    def borrar_grupo(self, p_data):
        """ Elimina un grupo seleccionado por el usuario

        Si algún alumno se queda huérfano(sin grupo alguno)
        sus datos serán eliminados del sistema.

        :param p_data: Contiene el id del grupo y el usuario
        :return:
        """
        pass

    def cambiar_nombre(self, p_data):
        """
        Cambiamos el nombre de un grupo a otro diferente
        :param p_data: El identificador del grupo y el nueevo nombre
        :return: True o False dependiendo de si ha sido posible o no cambiar el nombre
        """
        gestor_grupo = GestorGrupo.GestorGrupo()
        id_grupo = p_data[1]['id_grupo']
        nombre_grupo = p_data[1]['nombre_gruo']
        resultado = gestor_grupo.cambiar_nombre(id_grupo, nombre_grupo)
        return resultado

    def anadir_tag(self, p_data):
        """
        Añade un nuevo Tag en el sistema
        :param p_data: Los datos necesarios para crear un TAG
        :return: True o False dependiendo del exito
        """
        gestor_tag = GestorTag.GestorTag()
        nombre_tag = p_data[1]['nombre_tag']
        id_usuario = p_data[1]['id_usuario']
        descripcion = p_data[1]['descripcion']
        lista_script = p_data[1]['lista_script']
        resultado = gestor_tag.anadir_tag(nombre_tag, id_usuario, descripcion, lista_script)
        return resultado


# Programamos los errores personalizados
class ErrorAlumno(Exception):
    def __init__(self, p_valor):
        self.valor = p_valor

    def __str__(self):
        return "Los datos del Alumno no son correcto. Dni: " + str(self.valor)

# Configuracion de los datos de escucha y ejecucion infinita del servidor.
if __name__ == "__main__":
    PORT = 13373
    try:
        # obtenemos la ip local de la máquina y ejecutamos el servidor en escucha.
        HOST = socket.gethostbyname(socket.gethostname())
        server = MySSLThreadingTCPServer((HOST, PORT), ServerHandler,
                                         "../../../ssl/cacert.pem",
                                         "../../../ssl/private/key.pem")
        # Se queda en ejecución infinita
        server.serve_forever()
    except socket.error:
        print "Ha ocurrido un error a la hora de obtener" \
              "la ip local del servidor"
        exit()
