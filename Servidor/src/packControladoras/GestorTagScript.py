# -*- encoding: utf-8 -*-

__author__ = 'Rubén Mulero'

import subprocess as sub
import shlex
from Servidor.src.packGestorBD import MySQLConnector


class Singleton(type):
    def __init__(cls, name, bases, dct):
        cls.__instance = None
        type.__init__(cls, name, bases, dct)

    def __call__(cls, *args, **kw):
        if cls.__instance is None:
            cls.__instance = type.__call__(cls, *args, **kw)
        return cls.__instance


class GestorTagScript(object):
    __metaclass__ = Singleton
    # Hemos creado el patrón de la MAE
    # Definimos el código que deseamos en la clase.

    def obtener_scripts(self, p_id_grupo):
        """
        Obtiene los scripts que contiene un grupo
        :param p_id_grupo: El identificador del grupo
        :return: La lista de scripts que contiene el grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdScript,NombreS,Descripcion FROM Script
                    WHERE IdScript IN (SELECT IdScript FROM Script_Grupo WHERE IdGrupo=%s)
                    AND Activo=%s;""", (p_id_grupo, True)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_scripts_disponibles(self, p_id_grupo):
        """
        Obtiene los scripts que no han sido aplicados en un grupo
        :param p_id_grupo: EL identificador del grupo
        :return: La lista de scripts NO aplicados en un grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdScript,NombreS,Descripcion FROM Script
                    WHERE IdScript NOT IN (SELECT IdScript FROM Script_Grupo WHERE IdGrupo=%s)
                    AND Activo=%s;""", (p_id_grupo, True)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_scripts_tag(self, p_id_tag):
        """
        Obtiene los scripts que contiene un TAG
        :param p_id_tag: Identificador del tag
        :return: La lista de scripts que contiene un TAG
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdScript,NombreS,Descripcion FROM Script
                    WHERE IdScript IN (SELECT IdScript FROM TAG_Script WHERE IdTag=%s)
                    AND Activo=%s;""", (p_id_tag, True)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def aplicar_script(self, p_id_script, p_dni, p_id_usuario, p_id_grupo):
        """
        Dado un script, llama a añadir intencion y actualiza la tablas de Script-Grupo e
        Historial para dejar patente que a un alumno se le ha agregado unn nuevo scrit.

        :param p_id_script: El identificador del scriot
        :param p_dni: El Dni del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo:  El identificador del grupo
        :return:
        """
        # Añadimos la intención en la BD
        actualizar_datos = self._anadir_intencion(p_id_script, p_dni, p_id_usuario, p_id_grupo)
        if actualizar_datos:
            # La intención del script se ha registrado correctamente
            bd = MySQLConnector.MySQLConnector()
            consulta_1 = "INSERT INTO Script_Grupo(IdGrupo,IdScipt) VALUES (%s,%s);", (p_id_grupo, p_id_script)
            respuesta_bd_1 = bd.execute(consulta_1)
            # Insertamos el Historial de lo sucedido
            consulta_2 = """INSERT INTO Historial VALUES(IdScript,Dni,IdUsuario,IdGrupo,Accion,Informacion)
                        VALUES(%s,%s,%s,%s,'anadir','Se ha anadido un script');
                        """, (p_id_script, p_dni, p_id_usuario, p_id_grupo)
            respuesta_bd_2 = bd.execute(consulta_2)
            # Comprobar que las 2 respuesta sean correctas y enviar la operación que se ha realizado.
        else:
            # Ha existido algun error serio a la hora de intentar añadir la intención
            # O ejecutar el script. Revisar qué ha sucedido
            # Añadir exception
            pass

    def eliminar_script(self, p_id_script, p_dni, p_id_usuario, p_id_grupo):
        """
        Dado un script, llama a eliminar intencion y actualizar las tablas de Script-Grupo e
        Historial para dejar patente que un alumno se le ha quitado un script.

        :param p_id_script: El identificador del scriot
        :param p_dni: El Dni del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo:  El identificador del grupo
        :return:
        """
        # Elimino la intención de la BD
        actualizar_datos = self._eliminar_intencion(p_id_script, p_dni, p_id_usuario, p_id_grupo)
        if actualizar_datos:
            # Se ha eliminado correctamente la intención
            bd = MySQLConnector.MySQLConnector()
            consulta_1 = "DELETE FROM Script_Grupo WHERE IdGrupo=%s, IdScript=%s;", (p_id_grupo, p_id_script)
            respuesta_bd_1 = bd.execute(consulta_1)
            # Insertamos en el Historial los datos
            consulta_2 = """INSERT INTO Historial VALUES(IdScript,Dni,IdUsuario,IdGrupo,Accion,Informacion)
                        VALUES(%s,%s,%s,%s,'borrar','Se ha borrado un script');
                        """, (p_id_script, p_dni, p_id_usuario, p_id_grupo)
            respuesta_bd_2 = bd.execute(consulta_2)
            # Comprobar que las 2 respuestas hayan salido bien
        else:
            # Error garrafal, añadir alguna excepcion en éste punto
            pass

    def _anadir_intencion(self, p_id_script, p_dni, p_id_usuario, p_id_grupo):
        """
        Dado un Alumno, añadimos la intención de un script y aplicamos en la BD si es necesario

        En caso de estar en otro grupo -> Añade la intención.
        En caso de no estar en ninguno otro -> Añade la intención y aplicar el script

        :param p_id_script: El identificador del scriot
        :param p_dni: El Dni del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo:  El identificador del grupo
        :return: True o False indicando que se ha insertado correctamente la intención.
        """
        actualizar_bd = False
        # Vamos a buscar si éste alumno tiene intenciones sobre el script a aplicar
        bd = MySQLConnector.MySQLConnector()
        consulta_1 = "SELECT IdScript FROM Aplicacion WHERE IdScript=%s AND Dni=%s;", (p_id_script, p_dni)
        respuesta_bd = bd.execute(consulta_1)
        if len(respuesta_bd) != 0:
            # El script ya ha sido añadido asi que simplemente añado la intención
            consulta_2 = """INSERT INTO Aplicacion(IdScript,Dni,IdUsuario,IdGrupo) VALUES
                        (%s,%s,%s,%s);
                        """, (p_id_script, p_dni, p_id_usuario, p_id_grupo)
            respuesta_bd_2 = bd.execute(consulta_2)
            if respuesta_bd_2:
                actualizar_bd = True
        else:
            # Es la primera vez que se añade éste script a éste alumno, lo aplicamos
            resultado = self._execute_script(p_id_script, p_dni)
            if resultado:
                # El script se ha aplicado bien inserto la intención
                consulta_3 = """INSERT INTO Aplicacion(IdScript,Dni,IdUsuario,IdGrupo) VALUES
                        (%s,%s,%s,%s);
                        """, (p_id_script, p_dni, p_id_usuario, p_id_grupo)
                respuesta_bd_3 = bd.execute(consulta_3)
                if respuesta_bd_3:
                    actualizar_bd = True
            else:
                # Error garrafal raiseo excepción
                pass

        return actualizar_bd

    def _eliminar_intencion(self, p_id_script, p_dni, p_id_usuario, p_id_grupo):
        """
        Dado un alumno, comrpueba si tiene un script aplicado por otros profesores y grupos.

        En caso de estar en otro grupo -> Elimina la intención.
        En caso de no estar en ninguno otro -> Elimina la intención y revoca el script

        :param p_id_script: El identificador del scriot
        :param p_dni: El Dni del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo:  El identificador del grupo
        :return: True o False indicando si se ha eliminado correctamente la intención
        """
        actualizar_bd = False
        # Eliminamos directamente la intención de la BD
        bd = MySQLConnector.MySQLConnector()
        consulta_1 = "DELETE FROM Aplicacion WHERE IdScript=%s AND Dni=%s " \
                     "AND IdUsuario=%s AND IdGrupo=%s;", (p_id_script, p_dni, p_id_usuario, p_id_grupo)
        respuesta_bd_1 = bd.execute(consulta_1)
        # Tenemos que comprobar si hay más intenciones sobre ese script
        consulta_2 = "SELECT IdScript FROM Aplicacion WHERE IdScript=%s AND Dni=%s;", (p_id_script, p_dni)
        respuesta_bd_2 = bd.execute(consulta_2)
        if len(respuesta_bd_2) != 0:
            # Aún hay más valores
            if respuesta_bd_1:
                actualizar_bd = True
        else:
            # Ya no queda más intenciones por lo que debemos eliminar el script
            resultado = self._execute_script(p_id_script, p_dni)
            if resultado:
                # Al alumno se le ha revocado el script que tenia aplicado
                actualizar_bd = True
            else:
                # Ha ocurrido un error garrafal, raiseo exception y controlo la salida
                pass
        return actualizar_bd

    # todo, vamos a hacer que ésta clase ejecute el script tanto para borrar como para añadir
    # el parámetro de entrada de los argumentos decidirá la acción.
    def _execute_script(self, p_id_script, p_dni, *args):
        """
        Aplicamos un script
        :param p_id_script: El identificador del Script
        :param p_dni: El Dni del alumno
        :return: True o False dependiendo del éxito de la aplicación del script
        """
        correcto = False
        # Comprobar si la suma de verificación SHA-1 es correcta y en caso positivo continuar
        bd = MySQLConnector.MySQLConnector()
        consulta_1 = "SELECT Ruta,SHA FROM Script WHERE IdScript=%s;", p_id_script
        respuesta_bd = bd.execute(consulta_1)
        if len(respuesta_bd) != 0:
            # Obtenemos la Ruta del script
            p = sub.Popen(('shasum', respuesta_bd['Ruta']), stdout=sub.PIPE, stderr=sub.PIPE)
            salidas_sha, errores_sha = p.communicate()
            if len(salidas_sha) != 0:
                # Comprobamos los SHA de la BD con el del archivo
                if respuesta_bd['Ruta'] is salidas_sha:
                    # Los SHA coinciden, podemos ejecutar el script
                    p = sub.Popen(('sh', respuesta_bd['Ruta'], p_dni),
                                  stdout=sub.PIPE, stderr=sub.PIPE)
                    salidas, errores = p.communicate()
                    if len(salidas) != 0:
                        print salidas
                        correcto = True
                    else:
                        # El script no se ha podido aplicar bien, raise exception
                        print errores
                else:
                    # Error, los SHA NO son iguales. Raise exception
                    pass
            else:
                # Error garrafal, raiseamos exception
                print errores_sha

        return correcto

    ##################################################
    ##################################################
    # Aquí van los métodos relacionados con los TAGS
    ##################################################
    ##################################################

    def obtener_tags(self, p_id_grupo):
        """
        Obtenemos los tags que tiene aplicados un grupo.
        :param p_id_grupo: El identificador del grupo
        :return: Los datos relativos a cada tag que posee el grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdTag,NombreTag,Descripcion,FechaCreacion FROM Tag
                    WHERE IdTag IN (SELECT IdTag FROM Tag_Grupo WHERE IdGrupo=%s);
                    """, p_id_grupo
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_tags_disponibles(self, p_id_grupo):
        """
        Obtenemos los tags que aún no han sido aplicados en un grupo
        :param p_id_grupo: El identificador de un grupo
        :return: Los tags que aún no han sido aplicados en un grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdTag,NombreTag,Descripcion,FechaCreacion FROM Tag
                    WHERE IdTag NOT IN (SELECT IdTag FROM Tag_Grupo WHERE IdGrupo=%s);
                    """, p_id_grupo
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_tags_usuario(self, p_id_usuario):
        """
        Obtenemos los tags que ha creado un usuario en el sistema
        :param p_id_usuario: El identificador del usuario
        :return: Los tags que tiene el usuario
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdTag,NombreTag,Descripcion,FechaCreacion FROM Tag WHERE IdUsuario=%s;", p_id_usuario
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def anadir_tag(self, p_nombre_tag, p_id_usuario, p_descripcion, p_lista_scrip):
        """
        Añadimos un nuevo tag en el sistema
        :param p_nombre_tag: El nombre del Tag
        :param p_id_usuario: El identificador del usuario
        :param p_descripcion: La descripción del Tag
        :param p_lista_scrip: La lista de los scripts que se tiene que asociar
        :return: True o False dependiendo si se ha insertado el tag corretamente
        """
        # Primero se comprueba si el nombre del tag ya existe en el sistema.
        bd = MySQLConnector.MySQLConnector()
        exito = False
        consulta1 = "SELECT IdTag FROM Tag WHERE NombreTag=%s", p_nombre_tag
        respuesta_bd_1 = bd.execute(consulta1)
        if len(respuesta_bd_1) == 0:
            # No existe el nombre en la BD, procedeemos a insertar el TAG
            consulta2 = "INSERT INTO Tag(NombreTag,Descripcion,IdUsuario) VALUES(%s,%s,%s);", \
                        (p_nombre_tag, p_descripcion, p_id_usuario)
            respuesta_bd_2 = bd.execute(consulta2)
            if respuesta_bd_2 == 1:
                # Se ha insertado el tag correctamente, añadimos los Scripts
                # Obtenemos le identificador que se le ha asociado a nuestro nuevo TAG
                consulta3 = "SELECT IdTag FROM Tag WHERE NombreTag=%s", p_nombre_tag
                respuesta_bd_3 = bd.execute(consulta3)
                # Recorremos la lista de script y vamos insertado uno a uno en la BD
                for script in p_lista_scrip:
                    consulta4 = "INSERT INTO Tag_Script(IdTag,IdScript) VALUES(%s,%s);", \
                                (respuesta_bd_3['IdTag'], script)
                    bd.execute(consulta4)
                exito = True
        return exito

    def eliminar_tag_usuario(self, p_id_tag, p_id_usuario):
        """
        Eliminamos un Tag del sistema y revocamos los scripts aplicados a todos los alumnos por éste TAG
        :param p_id_tag: El identificador del TAG
        :param p_id_usuario: El identificador del usuario
        :return:
        """
        # TODO Se eliminan los scripts de TODOS los alumnos afectados por el y se elimina del sistema
        bd = MySQLConnector.MySQLConnector()

    def aplicar_tag(self, p_id_tag, p_dni, p_id_usuario, p_id_grupo):
        """
        Dado un tag, llama a añadir intencion y actualiza la tablas de Tag-Grupo e
        Historial para dejar patente que a un alumno se le ha agregado unn nuevo tag.

        :param p_id_tag: El identificador del Tag
        :param p_dni: El identificador del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :return:
        """
        # Dado el tag, tenemos que obtener sus scripts asociados
        lista_scripts = self.obtener_scripts_tag(p_id_tag)
        for script in lista_scripts:
            actualizar_datos = self._anadir_intencion(script['IdScript'], p_dni, p_id_usuario, p_id_grupo)
            if actualizar_datos:
                # La intención del script se ha registrado correctamente
                bd = MySQLConnector.MySQLConnector()
                consulta_1 = "INSERT INTO Tag_Grupo(IdGrupo,IdTag) VALUES (%s,%s);", (p_id_grupo, p_id_tag)
                respuesta_bd_1 = bd.execute(consulta_1)
                # Insertamos el Historial de lo sucedido
                consulta_2 = """INSERT INTO Historial VALUES(IdTag,Dni,IdUsuario,IdGrupo,Accion,Informacion)
                                VALUES(%s,%s,%s,%s,'anadir','Se ha anadido un tag');
                                """, (p_id_tag, p_dni, p_id_usuario, p_id_grupo)
                respuesta_bd_2 = bd.execute(consulta_2)

            else:
                # Ha existido algun error serio a la hora de intentar añadir la intención
                # O ejecutar el script. Revisar qué ha sucedido
                # Añadir exception
                pass

# For other purposes. Code reserved

"""


    def testing(self):
        correcto = False
        # p = sub.Popen(shlex.split('sh /home/administrador/ex11-7.generarlist.sh'),  stdout=sub.PIPE, stderr=sub.PIPE)
        ruta = '/home/administrador/ex11-7.generarlist.sh'
        p = sub.Popen(('sh', ruta),  stdout=sub.PIPE, stderr=sub.PIPE)
        salidas, errores = p.communicate()
        if len(salidas) != 0:
            print salidas
        else:
            # Ha habido errores lanzamos una excepción
            print errores
        return correcto

"""
