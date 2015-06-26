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
from Servidor.src.packControladoras import GestorAlumno
from Servidor.src.packControladoras import GestorTagScript


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
                           'aplicar_cambios': self.aplicar_cambios,
                           'eliminar_tag_usuario': self.eliminar_tag_usuario,
                           'modificar_tag': self.modificar_tag,
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
        """
        Comprobamos si el usuario y contraseña son correctos

        :param p_data: El usuario y la contraseña
        :return: True o False dependiendo de si todo ha ido bien
        """
        gestor_usu = GestorUsuario.GestorUsuario()
        usuario = p_data[1]['usuario']
        contrasena = p_data[1]['contrasena']
        resultado = gestor_usu.obtener_credenciales(usuario, contrasena)
        return resultado

    def obtener_grupos(self, p_data):
        """
        Obtenemos los grupos de un usuario

        :param p_data: El identificador del usuario
        :return: Los grupos que tiene
        """
        gestor_grupo = GestorGrupo.GestorGrupo()
        id_usuario = p_data[1]['id_usuario']
        resultado = gestor_grupo.obtener_grupos(id_usuario)
        return resultado

    def obtener_alumnos(self, p_data):
        """
        Obtenemos la lista de alumnos de un grupo

        :param p_data: El identificador del grupò
        :return: La lista de alumnos del grupo
        """
        gestor_alumno = GestorAlumno.GestorAlumno()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_alumno.obtener_alumnos(id_grupo)
        return resultado

    def obtener_scripts(self, p_data):
        """
        Obtener la lista de los scripts aplicados en un grupo

        :param p_data: El identificador del grupo
        :return: La lista de los scripts actualmente aplicados
        """
        gestor_tag_script = GestorTagScript.GestorTagScript()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_tag_script.obtener_scripts(id_grupo)
        return resultado

    def obtener_tags(self, p_data):
        """
        Obtener la lista de los tags aplicados en un grupo

        :param p_data: El identificador del grupo
        :return: La lista de los tags actualmente aplicados
        """
        gestor_tag_script = GestorTagScript.GestorTagScript()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_tag_script.obtener_tags(id_grupo)
        return resultado

    def obtener_scripts_disponibles(self, p_data):
        """
        Obtener los scripts disponibles para un grupo

        :param p_data: El identificador del grupo
        :return: La lista de los scripts DISPONIBLES y No aplicados
        """
        gestor_tag_script = GestorTagScript.GestorTagScript()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_tag_script.obtener_scripts_disponibles(id_grupo)
        return resultado

    def obtener_tags_disponibles(self, p_data):
        """
        Obtener los tags disponibles para un grupo

        :param p_data: El identificador del grupo
        :return: La lista de los tags DISPONIBLES y No aplicados
        """
        gestor_tag_script = GestorTagScript.GestorTagScript()
        id_grupo = p_data[1]['id_grupo']
        resultado = gestor_tag_script.obtener_tags_disponibles(id_grupo)
        return resultado

    def obtener_tags_usuario(self, p_data):
        """
        Obtener los tags que posee un usuario. "Mis TAGS"

        :param p_data: El identificador del usuario
        :return: La lista de sus tags
        """
        gestor_tag_script = GestorTagScript.GestorTagScript()
        id_usuario = p_data[1]['id_usuario']
        resultado = gestor_tag_script.obtener_tags_usuario(id_usuario)
        return resultado

    def obtener_scripts_tag(self, p_data):
        """ Obtener los scripts que contiene un tag

        :param p_data: el identificador del tag
        :return:
        """
        gestor_tag_script = GestorTagScript.GestorTagScript()
        id_tag = p_data[1]['id_tag']
        resultado = gestor_tag_script.obtener_scripts_tag(id_tag)
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
        """
        Elimina un grupo seleccionado por el usuario

        Si algún alumno se queda huérfano(sin grupo alguno)
        sus datos serán eliminados del sistema.

        :param p_data: Contiene el identificador del usuario, del grupo y la lista de alumnos
        :return:
        """
        gestor_alumno = GestorAlumno.GestorAlumno()
        gestor_grupo = GestorGrupo.GestorGrupo()
        gestor_tag_script = GestorTagScript.GestorTagScript()
        id_usuario = p_data[1]['id_usuario']
        id_grupo = p_data[1]['id_grupo']
        lista_alumnos = p_data[1]['lista_alumnos']
        # Obtenemos los scripts que tiene el grupo
        # ¿Podria enviarse por el SOCKET?????
        lista_scripts = gestor_tag_script.obtener_scripts(id_grupo)
        lista_tags = gestor_tag_script.obtener_tags(id_grupo)
        # Por cada alumno, eliminamos el script
        for alumno in lista_alumnos:
            # Eliminamos el script
            # TODO falta implementar los métodos de eliminar script y acabar ésta parte
            # Eliminamos los TAGS
            # TODO falta implementar los métodos de eliminar tag y acabar ésta parte
            # Eliminamos al alumno
            rdo = gestor_alumno.borrar_alumno(alumno['Dni'])

        # Por último eliminamos el grupo del sistema.
        resultado = gestor_grupo.borrar_grupo(id_grupo)

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
        # todo habrá que cambiar el nombre de éste método a crear_tag_usuario
        gestor_tag_script = GestorTagScript.GestorTagScript()
        nombre_tag = p_data[1]['nombre_tag']
        id_usuario = p_data[1]['id_usuario']
        descripcion = p_data[1]['descripcion']
        lista_script = p_data[1]['lista_script']
        resultado = gestor_tag_script.anadir_tag(nombre_tag, id_usuario, descripcion, lista_script)
        return resultado

    def aplicar_cambios(self, p_data):
        """
        Aplica los cambios a una serie de alumnos que pertenecen a un grupo

        Dichos cambios son la adición o no de scripts y tags.

        :param p_data: Contiene los siguientes elementos:
                        -> id_usuario: El identificador del usuario
                        -> id_grupo: El identificador del grupo
                        -> lista_cambios_s: Una lista que contiene los cambios en los scripts que se realizarán
                        -> lista_cambios_t: Una lista que contiene los cambios en los tags que se realizarán.
                        -> lista_alumnos: La lista de los alumnos afectados
        :return:
        """
        gesto_tag_script = GestorTagScript.GestorTagScript()
        id_usuario = p_data[1]['id_usuario']
        id_grupo = p_data[1]['id_grupo']
        lista_cambios_s = p_data[1]['lista_cambios_s']
        lista_cambios_t = p_data[1]['lista_cambios_t']
        lista_alumnos = p_data[1]['lista_alumnos']
        # Por cada alumno realizamos la lista de cambios necesaria
        for alumno in lista_alumnos:
            # Modificamos los scripts
            for cambio_s in lista_cambios_s:
                if cambio_s['accion'] == 'anadir_script':
                    # añadimos script al alumno actual

                    # todo hay que modificar la relacion entre grupo y script para añadir éste nuevo script
                    pass
                else:
                    # Eliminamos script al alumno actual
                    # Mismo caso que arriba pero eliminando
                    pass
            # Modificamos los Tags
            for cambio_t in lista_cambios_t:
                if cambio_t['accion'] == 'anadir_tag':
                    # Añadimos el tag de la misma forma que con el script
                    # Recorremos la lista de los scrips que contiene el tag e insertamos.
                    # todo no se considera el tag introducido hasta que no estén todos sus scripts aplicados.
                    # todo hay que añadir éste nuevo tag en la lista de tag_scriot
                    pass
                else:
                    # Eliminamos el tag
                    # todo no se considera el tag eliminado hasta que no se borren todos los scripts
                    pass

    def eliminar_tag_usuario(self, p_data):
        """
        Elimina un Tag del usuario del sistema y se revocan de los alumnos afectados los scripts
        que hayan sido aplicados con anterioridad.

        :param p_data: Cotiene el identificador del TAG y del usuario
        :return: True o False dependiendo del éxito de la operación
        """
        # todo pensar cómo vas a constorlar las excepciones
        gestor_grupo = GestorGrupo.GestorGrupo()
        gesto_tag_script = GestorTagScript.GestorTagScript()
        gestor_alumno = GestorAlumno.GestorAlumno()
        id_tag = p_data[1]['id_tag']
        id_usuario = p_data[1]['id_usuario']
        lista_s = p_data[1]['lista_s']
        resultado = False
        actualibar_bd = False
        # obtenemos los grupso donde el tag está aplicado
        lista_grupo = gestor_grupo.obtener_grupos_tag(id_tag)
        # Meter ésto e un Try Catch?
        # En caso de que el for se complete bien, se cambia a True actualizar_bd
        for grupo in lista_grupo:
            #Obtenemos la lista de alumnos del grupo actual
            lista_alumno = gestor_alumno.obtener_alumnos(grupo['IdGrupo'])
            for alumno in lista_alumno:
                # Eliminamos los scripts de este TAG
                exito = gesto_tag_script.eliminar_tag(id_tag, alumno['Dni'], id_usuario, grupo['IdGrupo'])
                # Deberiamos meter exceptions en éste punto

        if actualibar_bd:
            # ha ido bien, vamos a elininar el TAG
            resultado = gesto_tag_script.borrar_tag(id_tag)

        return resultado

    def modificar_tag(self, p_data):
        """
        Modifica los scripts contenidos en un TAg por otros nuevos y se reaplican/eliminan los
        actuales

        :param p_data: Contiene los siguientes elementos:
                                    -> Id_Usuario: El identificador del usuario actual.
                                    -> Nombre_Tag: El nuevo nombre del Tag.
                                    -> Owner: El identificador del nuevo usuario
                                    -> Descripción: Una nueva descripción del TAG
                                    -> lista_cambios: La lista de los cambios a realizar.

        :return: True o False dependiendo del resultado de la actualización
        """
        gestor_tag_script = GestorTagScript.GestorTagScript()
        gestor_grupo = GestorGrupo.GestorGrupo()
        gestor_alumno = GestorAlumno.GestorAlumno()
        id_usuario = p_data[1]['id_usuario']
        nombre_tag = p_data[1]['nombre_tag']
        owner = p_data[1]['owner']
        descripcion = p_data[1]['descripcion']
        lista_cambios = p_data[1]['lista_cambios']
        # todo hacer ésta parte
        pass

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
