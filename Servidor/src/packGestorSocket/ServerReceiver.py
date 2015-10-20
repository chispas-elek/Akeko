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
import time
from Servidor.src.packControladoras import GestorUsuario
from Servidor.src.packControladoras import GestorGrupo
from Servidor.src.packControladoras import GestorAlumno
from Servidor.src.packControladoras import GestorTagScript
from Servidor.src.packControladoras import GestorHistorial


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
            reciv = Decoder.Decoder(self.request.recv(4096).strip())
            data = reciv.decode_json()
            # Programamos el diccionario para elegir las acciones a realizar.
            operaciones = {'iniciar_sesion': self.iniciar_sesion,
                           'obtener_todos_los_propietarios': self.obtener_todos_los_propietarios,
                           'obtener_grupos': self.obtener_grupos,
                           'obtener_alumnos': self.obtener_alumnos,
                           'obtener_scripts': self.obtener_scripts,
                           'obtener_tags': self.obtener_tags,
                           'obtener_scripts_disponibles': self.obtener_scripts_disponibles,
                           'obtener_tags_disponibles': self.obtener_tags_disponibles,
                           'obtener_tags_usuario': self.obtener_tags_usuario,
                           'obtener_scripts_tag': self.obtener_scripts_tag,
                           'obtener_scripts_no_en_tag': self.obtener_scripts_no_en_tag,
                           'borrar_grupo': self.borrar_grupo,
                           'cambiar_nombre': self.cambiar_nombre,
                           'crear_tag_usuario': self.crear_tag_usuario,
                           'crear_grupo': self.crear_grupo,
                           'aplicar_cambios': self.aplicar_cambios,
                           'eliminar_tag_usuario': self.eliminar_tag_usuario,
                           'modificar_tag': self.modificar_tag,
                           'obtener_historial': self.obtener_historial,
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

    def obtener_todos_los_propietarios(self, p_data):
        """
        Obtiene todos los usuarios potenciales para poder heredar un Tag por parte del usuario actual

        :param p_data: El identificador del usuario actual
        :return:
        """
        gestor_usu = GestorUsuario.GestorUsuario()
        id_usuario = p_data[1]['id_usuario']
        resultado = gestor_usu.obtener_todos_los_propietarios(id_usuario)
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
        id_usuario = p_data[1]['id_usuario']
        resultado = gestor_tag_script.obtener_tags_disponibles(id_grupo, id_usuario)
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

    def obtener_scripts_no_en_tag(self, p_data):
        """
        Obtiene los scripts que NO contiene un TAG

        :param p_data: El identificador del tag
        :return:
        """
        gestor_tag_script = GestorTagScript.GestorTagScript()
        id_tag = p_data[1]['id_tag']
        resultado = gestor_tag_script.obtener_scripts_no_en_tag(id_tag)
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
        gestor_historial = GestorHistorial.GestorHistorial()
        id_usuario = p_data[1]['id_usuario']
        nombre_grupo = p_data[1]['nombre_grupo']
        lista_alumnos = p_data[1]['lista_alumnos']
        lista_alumnos_nuevos = []
        puedo_insertar = True
        resultado = False
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
                    if alumno['Nombre'] != existe[0]['Nombre'] or alumno['Apellido'] != existe[0]['Apellido'] \
                            or alumno['Email'] != existe[0]['Email']:
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
            grupo_nuevo = gestor_grupo.anadir_grupo(nombre_grupo, id_usuario, lista_alumnos)
            if grupo_nuevo:
                # El grupo se ha creado correctamente. Añadimos el registro en el historial
                resultado = gestor_historial.anadir_historial_grupo(id_usuario, nombre_grupo,
                                                                    True, "Se ha añadido un nuevo grupo.")

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
        :return: True -> Si el grupo se ha borrado correctamente
                False -> Si algo ha sucedido durante el borrado del grupo
        """
        gestor_alumno = GestorAlumno.GestorAlumno()
        gestor_grupo = GestorGrupo.GestorGrupo()
        gestor_tag_script = GestorTagScript.GestorTagScript()
        gestor_historial = GestorHistorial.GestorHistorial()
        id_usuario = p_data[1]['id_usuario']
        id_grupo = p_data[1]['id_grupo']
        lista_alumnos = p_data[1]['lista_alumnos']
        # Obtenemos los scripts que tiene el grupo
        lista_scripts = gestor_tag_script.obtener_scripts(id_grupo)
        lista_tags = gestor_tag_script.obtener_tags(id_grupo)
        resultado = True

        # Por cada alumno, eliminamos el script
        for alumno in lista_alumnos:
            # Eliminamos el script
            for script in lista_scripts:
                elim_script = gestor_tag_script.eliminar_script(script['IdScript'], alumno['Dni'], id_usuario, id_grupo)
                if elim_script:
                    # Se ha eliminado el tag del alumno actual, insertamos la acción en el historial
                    gestor_historial.anadir_historial_script(script['IdScript'], alumno['Nombre'], alumno['Apellido'],
                                                             id_usuario, id_grupo, False, 'Borrado de grupo')
                else:
                    # Algo ha pasado, paramos
                    resultado = False
                    break
            # Eliminamos los TAGS
            for tag in lista_tags:
                elim_tag = gestor_tag_script.eliminar_tag(tag['IdTag'], alumno['Dni'], id_usuario, id_grupo)
                if elim_tag:
                    # Se ha eliminado el tag del alumno actual, insertamos la acción en el historial
                    gestor_historial.anadir_historial_tag(tag['IdTag'], alumno['Nombre'], alumno['Apellido'],
                                                          id_usuario, id_grupo, False, 'Borrado de grupo')
                else:
                    # Algo ha pasado, paramos
                    resultado = False
                    break

        # Éste time sleep ayuda a que el código se ejecute de manera correcta sin que los scripts de bash interfieran.
        time.sleep(0.1)
        # Por último eliminamos el grupo del sistema.
        if resultado:
            datos_grupo = gestor_grupo.obtener_un_grupo(id_grupo)
            resultado_borrar_grupo = gestor_grupo.borrar_grupo(id_grupo)
            if resultado_borrar_grupo:
                # Insertamos en el historial lo sucediddo

                resultado = gestor_historial.anadir_historial_grupo(id_usuario, datos_grupo[0]['NombreGrupo'], False,
                                                                    "Se ha eliminado un grupo.")
                # Comprobamos si algún alumno se ha quedado sin grupo y lo eliminamos del sistema
                for alumno2 in lista_alumnos:
                    rdo = gestor_alumno.borrar_alumno(alumno2['Dni'])
                    # todo sería conveniente hacer algo en caso de que ésto falle.
            else:
                # Algo ha pasado a la hora de borrar el grupo.
                resultado = False

        return resultado

    def cambiar_nombre(self, p_data):
        """
        Cambiamos el nombre de un grupo a otro diferente
        :param p_data: El identificador del grupo y el nueevo nombre
        :return: True o False dependiendo de si ha sido posible o no cambiar el nombre
        """
        gestor_grupo = GestorGrupo.GestorGrupo()
        id_grupo = p_data[1]['id_grupo']
        nombre_grupo = p_data[1]['nombre_grupo']
        resultado = gestor_grupo.cambiar_nombre(id_grupo, nombre_grupo)
        return resultado

    def crear_tag_usuario(self, p_data):
        """
        Añade un nuevo Tag en el sistema

        :param p_data: Los datos necesarios para crear un TAG
        :return: True o False dependiendo del exito
        """
        resultado = False
        gestor_tag_script = GestorTagScript.GestorTagScript()
        gestor_historial = GestorHistorial.GestorHistorial()
        nombre_tag = p_data[1]['nombre_tag']
        id_usuario = p_data[1]['id_usuario']
        descripcion = p_data[1]['descripcion']
        lista_script = p_data[1]['lista_script']
        resultado_creacion = gestor_tag_script.crear_tag_usuario(nombre_tag, id_usuario, descripcion, lista_script)
        if resultado_creacion is True:
            # Insertamos en el historial la creación del TAG
            resultado = gestor_historial.anadir_historia_gestion_tag(nombre_tag, id_usuario, True,
                                                                     'Se ha creado un nuevo Tag')
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
        :return: True -> Si todo se ha aplicado sin problemas
                False -> Si algo no ha ido bien
        """
        resultado = False
        gesto_tag_script = GestorTagScript.GestorTagScript()
        gestor_historial = GestorHistorial.GestorHistorial()
        id_usuario = p_data[1]['id_usuario']
        id_grupo = p_data[1]['id_grupo']
        lista_cambios_s = p_data[1]['lista_cambios_s']
        lista_cambios_t = p_data[1]['lista_cambios_t']
        lista_alumnos = p_data[1]['lista_alumnos']

        if lista_cambios_s or lista_cambios_t:
            # Lo primero que vamos a hacer, es recorrer la lista de cambios de los Scripts.
            # Aplicando cada script 1 a 1 a cada alumno.
            for cambio_s in lista_cambios_s:
                # Vamos a recorrer cada alumno, aplicando o eliminando el script actual
                if cambio_s['accion'] == 'anadir_script':
                    # Se le añade el script actual a los alumnos
                    aplicado_s = False
                    for alumno in lista_alumnos:
                        aplicado_s = gesto_tag_script.aplicar_script(cambio_s['id_script'], alumno['Dni'], id_usuario,
                                                                     id_grupo)
                        if aplicado_s:
                            historial_registrado_s = gestor_historial.anadir_historial_script(cambio_s['id_script'],
                                                                                              alumno['Nombre'],
                                                                                              alumno['Apellido'],
                                                                                              id_usuario, id_grupo, True,
                                                                                              'Se ha añadido un Script')
                            if historial_registrado_s is not True:
                                aplicado_s = False
                                break
                        else:
                            # Algo no ha ido bien
                            break
                    if aplicado_s:
                        # El script se ha aplicado a todos los alumnos añado la relación entre grupo y scriot
                        grupo_aplicado_s = gesto_tag_script.anadir_script_al_grupo(id_grupo, cambio_s['id_script'])
                        if grupo_aplicado_s:
                            # Se ha resgistrado correctamente. Añadimos el historial
                            resultado = True
                        else:
                            # Ha ocurrido un error serio. Paramos la ejecución.
                            resultado = False
                            break
                    else:
                        # Algo serio ha ocurrido a la hora de aplicar los scrips.
                        resultado = False
                        break
                else:
                    # Se elimina el script actual a los alumnos
                    eliminado_s = False
                    for alumno in lista_alumnos:
                        eliminado_s = gesto_tag_script.eliminar_script(cambio_s['id_script'], alumno['Dni'], id_usuario,
                                                                       id_grupo)
                        if eliminado_s:
                            historial_registrado_s = gestor_historial.anadir_historial_script(cambio_s['id_script'],
                                                                                              alumno['Nombre'],
                                                                                              alumno['Apellido'],
                                                                                              id_usuario, id_grupo,
                                                                                              False,
                                                                                              'Se ha borrado un Script')
                            if historial_registrado_s is not True:
                                # No se ha registrado bine el historial
                                eliminado_s = False
                        else:
                            # algo no ha ido bien
                            break
                    if eliminado_s:
                        # El script se ha aplicado a todos los alumnos añado la relación entre grupo y scriot
                        grupo_eliminado_s = gesto_tag_script.eliminar_script_al_grupo(id_grupo, cambio_s['id_script'])
                        if grupo_eliminado_s:
                            # Se ha resgistrado correctamente. Añadimos el historial
                            resultado = True
                        else:
                            # Ha ocurrido un error serio. Paramos la ejecución.
                            resultado = False
                            break
                    else:
                        # Algo serio ha ocurrido a la hora de aplicar los scrips.
                        resultado = False
                        break

            # Ahora vamos a proccesar la lista de Tags con todos los alumnos
            for cambio_t in lista_cambios_t:
                if cambio_t['accion'] == 'anadir_tag':
                    # Se le añade el tag actual a los alumnos
                    aplicado_t = False
                    for alumno in lista_alumnos:
                        aplicado_t = gesto_tag_script.aplicar_tag(cambio_t['id_tag'], alumno['Dni'], id_usuario, id_grupo)
                        if aplicado_t:
                            historial_registrado_t = gestor_historial.anadir_historial_tag(cambio_t['id_tag'],
                                                                                           alumno['Nombre'],
                                                                                           alumno['Apellido'], id_usuario,
                                                                                           id_grupo,
                                                                                           True, 'Se ha añadido un Tag')
                            if historial_registrado_t is not True:
                                aplicado_t = False
                                break
                    if aplicado_t:
                        # El tag se ha aplicado a todos los alumnos añado la relación entre grupo y tag
                        grupo_aplicado_t = gesto_tag_script.anadir_tag_al_grupo(id_grupo, cambio_t['id_tag'])
                        if grupo_aplicado_t:
                            # Se ha resgistrado correctamente.
                            resultado = True
                        else:
                            # Ha ocurrido un error serio. Paramos la ejecución.
                            resultado = False
                            break
                    else:
                        # Algo serio ha ocurrido a la hora de aplicar los tags.
                        resultado = False
                        break
                else:
                    # Se elimina el tag actual a los alumnos
                    eliminado_t = False
                    for alumno in lista_alumnos:
                        eliminado_t = gesto_tag_script.aplicar_tag(cambio_t['id_tag'], alumno['Dni'], id_usuario,
                                                                   id_grupo)
                        if eliminado_t:
                            historial_registrado_t = gestor_historial.anadir_historial_tag(cambio_t['id_tag'],
                                                                                           alumno['Nombre'],
                                                                                           alumno['Apellido'], id_usuario,
                                                                                           id_grupo,
                                                                                           False, 'Se ha eliminado un Tag')
                            if historial_registrado_t is not True:
                                eliminado_t = False
                                break

                    if eliminado_t:
                        # El tag se ha aplicado a todos los alumnos añado la relación entre grupo y tag
                        grupo_eliminado_t = gesto_tag_script.eliminar_tag_al_grupo(id_grupo, cambio_t['id_tag'])
                        if grupo_eliminado_t:
                            # Se ha resgistrado correctamente. Añadimos el historial
                            resultado = True
                        else:
                            # Ha ocurrido un error serio. Paramos la ejecución.
                            resultado = False
                            break
                    else:
                        # Algo serio ha ocurrido a la hora de aplicar los tags.
                        resultado = False
                        break
        else:
            # No hay cambios que hacer de ningún tipo. Algo no ha ido bien
            print "He recibido las listas de cambios vacías. Algo no ha ido bien."

        return resultado

    def eliminar_tag_usuario(self, p_data):
        """
        Elimina un Tag del usuario del sistema y se revocan de los alumnos afectados los scripts
        que hayan sido aplicados con anterioridad.

        :param p_data: Cotiene el identificador del TAG y del usuario
        :return: True o False dependiendo del éxito de la operación
        """
        gestor_grupo = GestorGrupo.GestorGrupo()
        gesto_tag_script = GestorTagScript.GestorTagScript()
        gestor_alumno = GestorAlumno.GestorAlumno()
        gestor_historial = GestorHistorial.GestorHistorial()
        id_tag = p_data[1]['id_tag']
        id_usuario = p_data[1]['id_usuario']
        resultado = False
        actualibar_bd = False
        # obtenemos los grupso donde el tag está aplicado
        lista_grupo = gestor_grupo.obtener_grupos_tag(id_tag)
        if len(lista_grupo) != 0:
            # Afecta a grupos. Eliminamos la relación
            for grupo in lista_grupo:
                # Obtenemos la lista de alumnos del grupo actual
                lista_alumno = gestor_alumno.obtener_alumnos(grupo['IdGrupo'])
                for alumno in lista_alumno:
                    # Eliminamos los scripts de este TAG
                    exito = gesto_tag_script.eliminar_tag(id_tag, alumno['Dni'], id_usuario, grupo['IdGrupo'])
                    if exito:
                        # Actualizamos el Historial con el borrado
                        actualizado = gestor_historial.anadir_historial_tag(id_tag, alumno['Nombre'],
                                                                            alumno['Apellido'],
                                                                            id_usuario, grupo['IdGrupo'], False,
                                                                            'Tag eliminado por el usuario')
                        if actualizado:
                            actualibar_bd = True
                        else:
                            # No se ha actualizado bien la base de datos
                            actualibar_bd = False
                            break
                    else:
                        # Algo malo ha pasado
                        actualibar_bd = False
                        break

            if actualibar_bd:
                # ha ido bien, vamos a elininar el TAG
                datos_tag = gesto_tag_script.obtener_info_tag(id_tag)
                borrar_tag = gesto_tag_script.borrar_tag(id_tag)
                if borrar_tag:
                    # Tag borrado OK. Insertamos en el historial
                    resultado = gestor_historial.anadir_historia_gestion_tag(datos_tag[0]['NombreTag'], id_usuario,
                                                                             False, 'Se ha eliminado un Tag')
        else:
            # No afecta a ningún Grupo. Eliminamos directamente
            # Obtenemos primero los datos del Tag antes de borrarlo para el historial
            datos_tag = gesto_tag_script.obtener_info_tag(id_tag)
            # todo algo pasa al borrar el tag, reviasar
            borrar_tag = gesto_tag_script.borrar_tag(id_tag)
            if borrar_tag:
                # Tag borrado OK. Insertamos en el historial
                resultado = gestor_historial.anadir_historia_gestion_tag(datos_tag[0]['NombreTag'], id_usuario,
                                                                         False, 'Se ha eliminado un Tag')
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
        gestor_historial = GestorHistorial.GestorHistorial()
        id_usuario = p_data[1]['id_usuario']
        id_tag = p_data[1]['id_tag']
        nombre_tag = p_data[1]['nombre_tag']
        owner = p_data[1]['owner']
        descripcion = p_data[1]['descripcion']
        lista_cambios = p_data[1]['lista_cambios']

        resultado = False
        # Lo primero, actualizar los datos referentes al TAG.
        exito = gestor_tag_script.modificar_tag(id_tag, nombre_tag, descripcion, owner)
        if exito:
            # Se han cambiado los datos de forma correcta
            # Comprobamos si se ha cambiado el owner
            if id_usuario is not owner:
                # Se ha cambiado de owner, deshabilitamos el TAg en todos los grupos del user actual
                lista_grupo = gestor_grupo.obtener_grupos_tag(id_tag)
                for grupo in lista_grupo:
                    # Obtenemos la lista de alumnos del grupo actual
                    lista_alumno = gestor_alumno.obtener_alumnos(grupo['IdGrupo'])
                    for alumno in lista_alumno:
                        # Eliminamos los scripts de este TAG
                        exito = gestor_tag_script.eliminar_tag(id_tag, alumno['Dni'], id_usuario, grupo['IdGrupo'])
                        if exito:
                            # Actualizar el Historial
                            actualizar_historial = gestor_historial.anadir_historial_tag(id_tag, alumno['Nombre'],
                                                                                         alumno['Apellido'], id_usuario,
                                                                                         grupo['IdGrupo'], False,
                                                                                         'Traspaso de Tag '
                                                                                         'a otro usuario.')
                            if actualizar_historial:
                                resultado = True
                            else:
                                resultado = False
                                break
                        else:
                            resultado = False
                            break
                    eliminado_ok = gestor_tag_script.eliminar_tag_al_grupo(grupo['IdGrupo'], id_tag)
                    print eliminado_ok
                # Si existen cambios en la lista, vamos a aplicarlos
                if len(lista_cambios):
                    resultado = gestor_tag_script.modificar_scripts_del_tag(id_tag, lista_cambios)

                else:
                    resultado = True
            else:
                # El usuario es el mismo, debemos reestructurar los cambios
                # Vamos a comprobar si tenemos cambios en la lista
                if len(lista_cambios) != 0:
                    # Hay cambios. Vamos a ver si afecta a algún grupo
                    lista_grupo = gestor_grupo.obtener_grupos_tag(id_tag)
                    if len(lista_grupo) != 0:
                        for cambio in lista_cambios:
                            if cambio['accion'] == 'borrar_script':
                                # Tenemos que borrar el Script
                                for grupo in lista_grupo:
                                    lista_alumnos_grupo = gestor_alumno.obtener_alumnos(grupo['IdGrupo'])
                                    # Los grupos siempre tienene minnimo un alumno. Recorremos
                                    for alumno in lista_alumnos_grupo:
                                        exito = gestor_tag_script.modificar_scripts_alumnos_de_un_grupo \
                                            (cambio['id_script'], alumno['Dni'], id_usuario,
                                             grupo['IdGrupo'], cambio['accion'])
                                        if exito:
                                            # Registro en Historial
                                            historial_ok = gestor_historial.anadir_historial_script \
                                                (cambio['id_script'], alumno['Nombre'], alumno['Apellido'],
                                                 id_usuario, grupo['IdGrupo'], False, "Modificar un Tag")

                                # Una vez procesados todos los Grupos se elimina la relación entre Tag y Scrip
                                eliminar_relacion = gestor_tag_script.eliminar_scrit_al_tag(id_tag, cambio['id_script'])
                                if eliminar_relacion:
                                    resultado = True
                                else:
                                    resultado = False
                                    break
                            else:
                                # Tenemos que añadir el TAg
                                for grupo in lista_grupo:
                                    # Primero comprobamos si el script ya estaba aplicado en el TAg
                                    existe_en_el_grupo = gestor_grupo.existe_script(grupo['IdGrupo'],
                                                                                    cambio['id_script'])

                                    if existe_en_el_grupo:
                                        # El Script actual ya existe en el TAg. Eliminaamos la relación entre grupo y Script
                                        gestor_tag_script.eliminar_script_al_grupo(grupo['IdGrupo'],
                                                                                   cambio['id_script'])
                                        # Se podría registrar la acción en el historial. Sólo opcional
                                    else:
                                        # El script actual no existe en el grupo. Lo aplicamos
                                        lista_alumnos_grupo = gestor_alumno.obtener_alumnos(grupo['IdGrupo'])
                                        # Los grupos siempre tienene minnimo un alumno. Recorremos
                                        for alumno in lista_alumnos_grupo:
                                            exito_a = gestor_tag_script.modificar_scripts_alumnos_de_un_grupo \
                                                (cambio['id_script'], alumno['Dni'], id_usuario,
                                                 grupo['IdGrupo'], cambio['accion'])
                                            if exito_a:
                                                # Registro en Historial
                                                historial_ok = gestor_historial.anadir_historial_script(
                                                    cambio['id_script'],
                                                    alumno['Nombre'], alumno['Apellido'], id_usuario, grupo['IdGrupo'],
                                                    True, "Modificar un Tag")
                                            else:
                                                # Algo ha ocurrido y no ha ido bien.
                                                break

                                # Una vez procesados todos los grupos se añade la relación entre Tag y Script
                                anadir_relacion = gestor_tag_script.anadir_script_al_tag(id_tag, cambio['id_script'])
                                if anadir_relacion:
                                    resultado = True
                                else:
                                    resultado = False
                                    break

                    else:
                        # Los cambios no afectan a ningún Grupo. Sólo cambiamos la relación de los Scripts
                        resultado = gestor_tag_script.modificar_scripts_del_tag(id_tag, lista_cambios)

                else:
                    # No hay cambios que hacer.
                    resultado = True


        else:
            # Raisemos exception
            pass

        # todo cambiar la nomeemclatura y hacer uso de éxito para devolver None en 1 caso especial.
        return resultado

    def obtener_historial(self, p_data):
        """
        Obtiene el historial del usuario actual

        :param p_data: Contiene el identificador del usuario
        :return: El historial completo del usuario
        """
        gestor_historial = GestorHistorial.GestorHistorial()
        id_usuario = p_data[1]['id_usuario']
        resultado = gestor_historial.obtener_historial(id_usuario)
        return resultado


# Programamos los errores personalizados
class ErrorAlumno(Exception):
    def __init__(self, p_valor):
        self.valor = p_valor

    def __str__(self):
        return "Los datos del Alumno no son correcto. Dni: " + str(self.valor)


# Configuracion de los datos de escucha y ejecucion infinita del servidor.
class ConfigServer(object):
    def __init__(self, p_PORT, p_cert, p_key):
        self._PORT = p_PORT
        self._cert = p_cert
        self._key = p_key

    def iniciar_servidor(self):
        try:
            # obtenemos la ip local de la máquina y ejecutamos el servidor en escucha.
            HOST = socket.gethostbyname(socket.gethostname())
            # server = MySSLThreadingTCPServer((HOST, self._PORT), ServerHandler,
            #                                 "../../../ssl/cacert.pem",
            #                                "../../../ssl/private/key.pem")
            server = MySSLThreadingTCPServer((HOST, self._PORT), ServerHandler,
                                             self._cert,
                                             self._key)

            # Si no ha saltado excepción es que el servidor se ha configurado
            # de manera correcta por lo que damos un feedback
            print ""
            print "El servidor esta en ejecución los datos de conexión son los siguientes:"
            print "======================================================================="
            print ""
            print "El HOST local del servidor es: %s" % HOST
            print "El PUERTO del servidor es: %s" % self._PORT
            print ""
            print "======================================================================="
            print ""
            # Se queda en ejecución infinita
            server.serve_forever()
        except socket.error:
            print "Ha ocurrido un error a la hora de obtener" \
                  "la ip local del servidor"
            exit()
