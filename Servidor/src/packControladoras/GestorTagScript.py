# -*- encoding: utf-8 -*-

__author__ = 'Rubén Mulero'

import subprocess as sub
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
        consulta = """SELECT IdScript,NombreScript,Descripcion FROM Script
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
        consulta = """SELECT IdScript,NombreScript,Descripcion FROM Script
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
        consulta = """SELECT IdScript,NombreScript,Descripcion FROM Script
                    WHERE IdScript IN (SELECT IdScript FROM Tag_Script WHERE IdTag=%s)
                    AND Activo=%s;""", (p_id_tag, True)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def obtener_scripts_no_en_tag(self, p_id_tag):
        """
        Obtiene los scritps que NO estan incluidos en un TAG

        :param p_id_tag: El identificador de un tag
        :return: La lista de los scripts que no están incluidos en un TAG
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdScript,NombreScript,Descripcion FROM Script
                    WHERE IdScript NOT IN (SELECT IdScript FROM Tag_Script WHERE IdTag=%s)
                    AND Activo=%s;""", (p_id_tag, True)
        respuesta_bd = bd.execute(consulta)
        return respuesta_bd

    def aplicar_script(self, p_id_script, p_dni, p_id_usuario, p_id_grupo):
        """
        Dado un script, llama a añadir intencion

        :param p_id_script: El identificador del scriot
        :param p_dni: El Dni del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo:  El identificador del grupo
        :return: True -> Si el script se ha aplicado correctamente al alumno del grupo seleecionado
                False -> Si algo no ha ido bien
        """
        exito = False
        # Añadimos la intención en la BD
        actualizar_datos = self._anadir_intencion(p_id_script, p_dni, p_id_usuario, p_id_grupo)
        if actualizar_datos:
            # La intención del script se ha registrado correctamente
            exito = True
        else:
            # Ha existido algun error serio a la hora de intentar añadir la intención
            # O ejecutar el script. Revisar qué ha sucedido
            # Añadir exception
            pass

        return exito

    def eliminar_script(self, p_id_script, p_dni, p_id_usuario, p_id_grupo):
        """
        Dado un script, llama a eliminar intencion.

        :param p_id_script: El identificador del scriot
        :param p_dni: El Dni del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo:  El identificador del grupo
        :return:
        """
        exito = False
        # Elimino la intención de la BD
        actualizar_datos = self._eliminar_intencion(p_id_script, p_dni, p_id_usuario, p_id_grupo)
        if actualizar_datos:
            exito = True
        else:
            # Error garrafal, añadir alguna excepcion en éste punto
            pass

        return exito

    def anadir_script_al_grupo(self, p_id_grupo, p_id_script):
        """
        Añade la relación entre Grupo y Script. Cuando un script se ha aplicado a todos los alumnos de un grupo

        :param p_id_gruo:
        :param p_id_script:
        :return:
        """
        exito = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "INSERT INTO Script_Grupo(IdGrupo,IdScript) VALUES (%s,%s);", (p_id_grupo, p_id_script)
        respuesta_bd = bd.execute(consulta)
        if respuesta_bd == 1:
            exito = True

        return exito

    def eliminar_script_al_grupo(self, p_id_grupo, p_id_script):
        """
        Elimina la relación entre Grupo y Script. Cuando un script se ha eliminado a todos los alumnos de un Grupo

        :param p_id_grupo:
        :param p_id_script:
        :return: True o False dependiendo del éxito de la operación
        """
        exito = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Script_Grupo WHERE IdGrupo=%s AND IdScript=%s;", (p_id_grupo, p_id_script)
        respuesta_bd = bd.execute(consulta)
        if respuesta_bd == 1:
            exito = True

        return exito

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
            # todo podriamos intentar verificar que al menos el script exista.
            # El script ya ha sido añadido asi que simplemente añado la intención
            consulta_2 = """INSERT INTO Aplicacion(IdScript,Dni,IdUsuario,IdGrupo) VALUES
                        (%s,%s,%s,%s);
                        """, (p_id_script, p_dni, p_id_usuario, p_id_grupo)
            respuesta_bd_2 = bd.execute(consulta_2)
            if respuesta_bd_2:
                actualizar_bd = True
        else:
            # Es la primera vez que se añade éste script a éste alumno, lo aplicamos
            resultado = self._execute_script(p_id_script, p_dni, True)
            if resultado:
                # El script se ha aplicado bien inserto la intención
                consulta_3 = """INSERT INTO Aplicacion(IdScript,Dni,IdUsuario,IdGrupo) VALUES
                        (%s,%s,%s,%s);
                        """, (p_id_script, p_dni, p_id_usuario, p_id_grupo)
                respuesta_bd_3 = bd.execute(consulta_3)
                if respuesta_bd_3:
                    actualizar_bd = True
            else:
                # Por alguna razón, el script ya no existe en la BD y no se puede aplicar correctamente
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
            resultado = self._execute_script(p_id_script, p_dni, False)
            if resultado:
                # Al alumno se le ha revocado el script que tenia aplicado
                actualizar_bd = True
            else:
                # Ha ocurrido un error garrafal, raiseo exception y controlo la salida
                pass
        return actualizar_bd

    def exite_intencion(self, p_id_script, p_dni, p_id_usuario, p_id_grupo):
        """
        Comprobamos si existe o no una intención en la BD dado varios datos

        :param p_id_script: El identificador del script
        :param p_dni: El Dni del usuario
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :return: True o False dependiendo de si existo o no la intención
        """
        existe = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdScript FROM Aplicacion WHERE IdScript=%s AND Dni=%s AND IdUsuario=%s AND IdGrupo=%s", (
            p_id_script, p_dni, p_id_usuario, p_id_grupo)
        respuesta_bd = bd.execute(consulta)
        if len(respuesta_bd) != 0:
            existe = True

        return existe

    # el parámetro de entrada de los argumentos decidirá la acción.
    def _execute_script(self, p_id_script, p_dni, p_accion):
        """
        Aplicamos un script
        :param p_id_script: El identificador del Script
        :param p_dni: El Dni del alumno
        :param p_accion: True -> Ejecuta el Script añadiendo datos
                        False -> Ejecuta el Script eliminando datos
        :return: True o False dependiendo del éxito de la aplicación del script
        """
        correcto = False
        # Comprobar si la suma de verificación SHA-1 es correcta y en caso positivo continuar
        bd = MySQLConnector.MySQLConnector()
        consulta_1 = "SELECT Ruta,SHA FROM Script WHERE IdScript=%s;", (p_id_script,)
        respuesta_bd = bd.execute(consulta_1)
        if len(respuesta_bd) != 0:
            consulta_2 = "SELECT Email FROM Alumno WHERE Dni=%s;", (p_dni,)
            respuesta_bd_2 = bd.execute(consulta_2)
            if len(respuesta_bd_2) != 0:
                # Obtenemos el nombre de usuario del mail para usarlo como identificador en los servicios
                ident_alumno = respuesta_bd_2[0]['Email'].split("@")[0]
                # Obtenemos la Ruta del script
                p = sub.Popen(("shasum", respuesta_bd[0]['Ruta']), stdout=sub.PIPE, stderr=sub.PIPE)
                salidas_sha, errores_sha = p.communicate()
                if len(salidas_sha) != 0:
                    # Comprobamos los SHA de la BD con el del archivo
                    salidas = salidas_sha.split()
                    if respuesta_bd[0]['SHA'] == salidas[0]:
                        # Los SHA coinciden, podemos ejecutar el script
                        p = sub.Popen(("/bin/bash", respuesta_bd[0]['Ruta'], ident_alumno, str(p_accion)),
                                      stdout=sub.PIPE, stderr=sub.PIPE)
                        salidas, errores = p.communicate()
                        if len(salidas) != 0 and len(errores) == 0:
                            print salidas
                            salidas = salidas.split('\n', 2)
                            if salidas[0] == "borrado":
                                # Se ha hecho una eliminación
                                correcto = self._enviar_mail(respuesta_bd_2[0]['Email'], p_descripcion=salidas[1])
                            else:
                                # El script se ha aplicado correctamente. Por lo tanto, enviaremos un mail con los cambios
                                # hacemos un slipt del usuario y contraseña que nos deevuelve el script
                                correcto = self._enviar_mail(respuesta_bd_2[0]['Email'], salidas[0], salidas[1],
                                                             salidas[2])
                        else:
                            # El script no se ha podido aplicar bien, raise exception
                            print errores
                    else:
                        # Error, los SHA NO son iguales. Raise exception
                        print "El SHA no coincide con el de la BD"
                else:
                    # Error garrafal, raiseamos exception
                    print errores_sha

        return correcto

    def _enviar_mail(self, p_email_alumno, p_ident_alumno=None, p_contrasena=None, p_descripcion=None):
        """
        Contienen el texto que va a representar el cuerpo del Mail a enviar.

        :param p_ident_alumno: Identificador del alumno (Login)
        :param p_contrasena: Contraseña del alumno
        :param p_email_alumno: El mail del alumno a enviar
        :param p_descripcion: Descripción del script.
        :return: True o False dependiendo de si se ha enviado correctamente el mail
        """
        enviado = False
        if p_ident_alumno is None:
            # Se ha eliminado un alumno
            el_texto = """
                        Hola.

                        El acceso a tu usuario en: %s ha sido eliminado.

                        Ya no podrás loguearte más haciendo uso de tu usuario y contraseña.

                        Un saludo.


                        PD: Éste mail ha sido enviado de manera automática, por favor, no responda a ésta dirección.

                        """ % p_descripcion
        else:
            # Se ha añadido un alumno
            el_texto = """
                        Hola.

                        Se ha generado un acceso en: %s

                        Tus datos para poder acceder a éste servicio, son los siguientes:

                        --> Usuario: %s
                        --> Contraseña: %s

                        Un saludo.


                        PD: Éste mail ha sido enviado de manera automática, por favor, no responda a ésta dirección.

                        """ % (p_descripcion, p_ident_alumno, p_contrasena)

        # Enviamos el mail
        p = sub.Popen(("/bin/bash", "./scripts/sent_mail.sh", el_texto, "elektro108@gmail.com"),
                      stdout=sub.PIPE, stderr=sub.PIPE)
        salidas_mail, errores_mail = p.communicate()
        if salidas_mail == "ok\n" and len(errores_mail) == 0:
            # Send OK
            enviado = True

        return enviado

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
        consulta = """SELECT IdTag,NombreTag,Descripcion,FechaCreacion,IdUsuario FROM Tag
                    WHERE IdTag IN (SELECT IdTag FROM Tag_Grupo WHERE IdGrupo=%s);
                    """, (p_id_grupo,)
        respuesta_bd = bd.execute(consulta)
        respuesta_bd_f_formateada = self._formatear_hora(respuesta_bd)
        return respuesta_bd_f_formateada

    def obtener_tags_disponibles(self, p_id_grupo, p_id_usuario):
        """
        Obtenemos los tags que aún no han sido aplicados en un grupo
        :param p_id_grupo: El identificador de un grupo
        :return: Los tags que aún no han sido aplicados en un grupo
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = """SELECT IdTag,NombreTag,Descripcion,FechaCreacion,IdUsuario FROM Tag
                    WHERE IdTag NOT IN (SELECT IdTag FROM Tag_Grupo WHERE IdGrupo=%s) AND IdUsuario=%s;
                    """, (p_id_grupo, p_id_usuario)
        respuesta_bd = bd.execute(consulta)
        respuesta_bd_f_formateada = self._formatear_hora(respuesta_bd)
        return respuesta_bd_f_formateada

    def obtener_tags_usuario(self, p_id_usuario):
        """
        Obtenemos los tags que ha creado un usuario en el sistema
        :param p_id_usuario: El identificador del usuario
        :return: Los tags que tiene el usuario
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT IdTag,NombreTag,Descripcion,FechaCreacion,IdUsuario FROM Tag WHERE IdUsuario=%s;", \
                   (p_id_usuario,)
        respuesta_bd = bd.execute(consulta)
        respuesta_bd_f_formateada = self._formatear_hora(respuesta_bd)
        return respuesta_bd_f_formateada

    def crear_tag_usuario(self, p_nombre_tag, p_id_usuario, p_descripcion, p_lista_scrip):
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
        consulta1 = "SELECT IdTag FROM Tag WHERE NombreTag=%s", (p_nombre_tag,)
        respuesta_bd_1 = bd.execute(consulta1)
        if len(respuesta_bd_1) == 0:
            # No existe el nombre en la BD, procedeemos a insertar el TAG
            consulta2 = "INSERT INTO Tag(NombreTag,Descripcion,IdUsuario) VALUES(%s,%s,%s);", \
                        (p_nombre_tag, p_descripcion, p_id_usuario)
            respuesta_bd_2 = bd.execute(consulta2)
            if respuesta_bd_2 == 1:
                # Se ha insertado el tag correctamente, añadimos los Scripts
                # Obtenemos le identificador que se le ha asociado a nuestro nuevo TAG
                consulta3 = "SELECT IdTag FROM Tag WHERE NombreTag=%s", (p_nombre_tag,)
                respuesta_bd_3 = bd.execute(consulta3)
                # Recorremos la lista de script y vamos insertado uno a uno en la BD
                for script in p_lista_scrip:
                    consulta4 = "INSERT INTO Tag_Script(IdTag,IdScript) VALUES(%s,%s);", \
                                (int(respuesta_bd_3[0]['IdTag']), int(script['IdScript']))
                    bd.execute(consulta4)
                exito = True
        return exito

    def aplicar_tag(self, p_id_tag, p_dni, p_id_usuario, p_id_grupo):
        """
        Dado un tag, llama a añadir intencion y actualiza la tablas de Tag-Grupo e
        Historial para dejar patente que a un alumno se le ha agregado unn nuevo tag.

        :param p_id_tag: El identificador del Tag
        :param p_dni: El identificador del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :return: True -> Si todos los scripts se han insertado correctamente
                False -> Algo no ha ido bien durante la aplicación del Tag
        """
        exito = False
        # Dado el tag, tenemos que obtener sus scripts asociados
        lista_scripts_ya_aplicados = []
        lista_scripts = self.obtener_scripts_tag(p_id_tag)
        bd = MySQLConnector.MySQLConnector()
        for script in lista_scripts:
            # Antes de añadir el Tag, vamos a ver si el grupo tenía ya un Script previamente aplicado que
            # pertenezca al grupo.
            consulta = "SELECT IdScript from Script_Grupo Where IdScript=%s AND IdGrupo=%s", (script['IdScript'],
                                                                                              p_id_grupo)
            resultado_bd = bd.execute(consulta)
            if len(resultado_bd) != 0:
                # El script que pertenece a ésta lista ya había sido añadido con anterioridad
                exito = True
                pass
            else:
                actualizar_datos = self._anadir_intencion(script['IdScript'], p_dni, p_id_usuario, p_id_grupo)
                if actualizar_datos:
                    exito = True
                else:
                    # Ha existido algun error serio a la hora de intentar añadir la intención
                    # O ejecutar el script. Revisar qué ha sucedido
                    # Añadir exception
                    exito = False
                    break
        return exito

    def eliminar_tag(self, p_id_tag, p_dni, p_id_usuario, p_id_grupo):
        """
        Dado un tag, llama a eliminar intención y actualiza las tablas de Tag-Grupo e
        Historial para dejar patente que un alumno se le ha eliminado un Tag.

        :param p_id_tag: El identificador del Tag
        :param p_dni: El identificador del alumno
        :param p_id_usuario: El identificador del usuario
        :param p_id_grupo: El identificador del grupo
        :return:
        """
        exito = False
        # Obtenemos los scripts asociados al tag
        lista_scripts = self.obtener_scripts_tag(p_id_tag)
        for script in lista_scripts:
            actualizar_datos = self._eliminar_intencion(script['IdScript'], p_dni, p_id_usuario, p_id_grupo)
            if actualizar_datos:
                exito = True
            else:
                # Algo serio ha pasado, paramos la acción
                exito = False
                break
        return exito

    def anadir_tag_al_grupo(self, p_id_grupo, p_id_tag):
        """
        Añade la relación entre Tag_Grupo para dejar patente que a todos los alumnos se le han agregado el TAG

        :param p_id_grupo:
        :param p_id_tag:
        :return:
        """
        exito = False
        exito_s = False
        bd = MySQLConnector.MySQLConnector()
        ## Antes de añadir la intención, vamos a eliminar los posibles Script residuales.
        # Obtenemos los tags del grupo actual
        lista_script = self.obtener_scripts_tag(p_id_tag)
        for script in lista_script:
            consulta_s = "SELECT IdScript from Script_Grupo Where IdScript=%s AND IdGrupo=%s", (script['IdScript'],
                                                                                                p_id_grupo)
            repuesta_s = bd.execute(consulta_s)
            if len(repuesta_s):
                # Este Script ya había sido aplicado. Vamos a eliminar la relación con el grupo
                exito_s = self.eliminar_script_al_grupo(p_id_grupo, script['IdScript'])
                if not exito_s:
                    break
        if exito_s:
            consulta = "INSERT INTO Tag_Grupo(IdGrupo,IdTag) VALUES (%s,%s);", (p_id_grupo, p_id_tag)
            respuesta_bd = bd.execute(consulta)
            if respuesta_bd == 1:
                # Las inserciones han ido correctamente bien.
                exito = True

        return exito

    def eliminar_tag_al_grupo(self, p_id_grupo, p_id_tag):
        """
        Elimina la relación entre Tag_Grupo para dejar patente que a todos los alumnos se le han eliminado el TAG

        :param p_id_grupo:
        :param p_id_tag:

        :return:
        """
        exito = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Tag_Grupo WHERE IdGrupo=%s AND IdTag=%s;", (p_id_grupo, p_id_tag)
        respuesta_bd = bd.execute(consulta)
        if respuesta_bd == 1:
            # Las inserciones han ido correctamente bien.
            exito = True

        return exito

    def borrar_tag(self, p_id_tag):
        """
        Borra un Tag del sistema.

        :param p_id_tag: El identificador del TAG
        :return: True o False dependiendo del éxito de la operación
        """
        resultado = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Tag WHERE IdTag=%s;", (p_id_tag, )
        respuesta_bd = bd.execute(consulta)
        if respuesta_bd != 0:
            resultado = True

        return resultado


    def modificar_scripts_del_tag(self, p_id_tag, p_lista_cambios):
        """
        Dada una lista de cambios. Se modifican los scripts que tenga un Tag.

        :param p_id_tag:
        :param p_lista_cambios:

        :return: True -> Todos los cambios han sido correctos
                False -> Algo no ha ido como deberia.
        """
        exito = False
        bd = MySQLConnector.MySQLConnector()
        # Recorremos la lista
        for cambio in p_lista_cambios:
            if cambio['accion'] == 'borrar_script':
                # Eliminamos la relación
                consulta_1 = "DELETE FROM Tag_Script WHERE IdTag=%s AND IdScript=%s;", (p_id_tag, cambio['id_script'])
                resultado_bd_1 = bd.execute(consulta_1)
                if resultado_bd_1 == 1:
                    exito = True
                else:
                    # Algo no ha ido bien
                    exito = False
                    break
            else:
                # Vamos a añadir un Script al TAg
                consulta_2 = "INSERT INTO Tag_Script(IdTag,IdScript) VALUES (%s,%s);", (p_id_tag, cambio['id_script'])
                resultado_bd_2 = bd.execute(consulta_2)
                if resultado_bd_2 == 1:
                    exito = True
                else:
                    exito = False
                    break

        return exito

    def anadir_script_al_tag(self, p_id_tag, p_id_script):
        """
        Añade la relación entre un Tag y un Script

        :param p_id_tag:
        :param p_id_script:
        :return:
        """
        exito = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "INSERT INTO Tag_Script(IdTag,IdScript) VALUES (%s,%s);", (p_id_tag, p_id_script)
        resultado_bd = bd.execute(consulta)
        if resultado_bd == 1:
            exito = True

        return exito

    def eliminar_scrit_al_tag(self, p_id_tag, p_id_script):
        """
        Elimina la relación entre un Tag y un Script

        :return:
        """
        exito = False
        bd = MySQLConnector.MySQLConnector()
        consulta = "DELETE FROM Tag_Script WHERE IdTag=%s AND IdScript=%s;", (p_id_tag, p_id_script)
        resultado_bd = bd.execute(consulta)
        if resultado_bd == 1:
            exito = True

        return exito

    def modificar_tag(self, p_id_tag, p_nombre_tag, p_descripcion, p_owner):
        """
        Cambia los datos de un tag

        :param p_id_tag: El identificador del tag
        :param p_nombre_tag: El nuevo nombre del tag
        :param p_descripcion: La nueva descripción del tag
        :param p_owner: El identificador del nuevo usuario del TAG
        :return: True o False indicando el cambio satisfactorio
        """
        exito = False
        # Comprobamos que le nombre del tag no exista en la BD
        bd = MySQLConnector.MySQLConnector()
        consulta_1 = "SELECT IdTag FROM Tag WHERE NombreTag=%s AND IdUsuario=%s", (p_nombre_tag, p_owner)
        respuesta_bd_1 = bd.execute(consulta_1)
        if len(respuesta_bd_1) != 0:
            if int(respuesta_bd_1[0]['IdTag']) == p_id_tag:
                # El nombre del tag no se ha querido actualziar
                consulta_2 = "UPDATE Tag SET NombreTag=%s,Descripcion=%s,IdUsuario=%s WHERE IdTag=%s;", \
                             (p_nombre_tag, p_descripcion, p_owner, p_id_tag)
                respuesta_bd_2 = bd.execute(consulta_2)
                print respuesta_bd_2
                exito = True
            else:
                # YA existe el nombre del TAG
                # Excep
                pass
        else:
            # No existe el Tag asi que podemos actualizar sin miedo
            consulta_3 = "UPDATE Tag SET NombreTag=%s,Descripcion=%s,IdUsuario=%s WHERE IdTag=%s;", \
                         (p_nombre_tag, p_descripcion, p_owner, p_id_tag)
            respuesta_bd_3 = bd.execute(consulta_3)
            if respuesta_bd_3 == 1:
                # todo ejecutar Script de envío de correo electronico con mensaje al nuevo usuario
                # Debemos obtener el mail del nuevo usuario y enviarle la informacion
                exito = True

        return exito

    def modificar_scripts_alumnos_de_un_grupo(self, p_id_script, p_dni, p_id_usuario, p_id_grupo, p_accion):
        """
        Dada una accicón determinada, la función comprueba si se quiere añadir o eliminar un script en el TAg y realiza
        los cambios pertinentes.

        :param p_id_script:
        :param p_dni:
        :param p_id_usuario:
        :param p_id_grupo:
        :param p_accion:
        :return:
        """
        resultado = False
        if p_accion == 'borrar_script':
            actualizar_datos = self._eliminar_intencion(p_id_script, p_dni, p_id_usuario, p_id_grupo)
            if actualizar_datos:
                resultado = True
            else:
                # Error garrafal, añadir alguna excepcion en éste punto
                pass
        else:
            # Se añade un nuevo script al Tag, vamos a mirar si ya estaba aplicado.
            exite = self.exite_intencion(p_id_script, p_dni, p_id_usuario, p_id_grupo)
            if not exite:
                # Si el script no existe, simplemente añadimos intención y lo agregamos a la tabla de Script_tag
                actualizar_datos = self._anadir_intencion(p_id_script, p_dni, p_id_usuario, p_id_grupo)
                if actualizar_datos:
                    resultado = True
                else:
                    # Error garrafal
                    pass
            else:
                # Ha ocurrido algún error extraño porque la intención no deberia de existir al ser llamado éste método.
                pass
        return resultado


    def obtener_info_tag(self, p_id_tag):
        """
        Obtiene los datos relativos a un tag dado su identificador

        :param p_id_tag: El identificador del Tag
        :return: Los datos relativos al tag
        """
        bd = MySQLConnector.MySQLConnector()
        consulta = "SELECT NombreTag,Descripcion,FechaCreacion From Tag where IdTag=%s;", (p_id_tag, )
        respuesta_bd_1 = bd.execute(consulta)
        return respuesta_bd_1


    def _formatear_hora(self, p_list_dict_valores):
        """
        La base de datos devuelve los datos en formato datetime. El cual es incompatible con JSON ya que pide Strings
        o ints. Para evitar problemas, con ésta función vamos a transformar el valor datetime en un String en un formato
        europeo

        :param p_dict_valores: La lista que contiene los diciconarios con los valores de la BD

        :return: El dicionario de datos enviados con la fechas formateadas.
        """
        for valor in p_list_dict_valores:
            fecha_de_la_bd = valor['FechaCreacion']
            fecha_formateada = fecha_de_la_bd.strftime("%H:%M:%S %d-%m-%Y")
            valor['FechaCreacion'] = fecha_formateada

        return p_list_dict_valores


class Solitario(object):
    # For other purposes. Code reserved

    def testing(self):
        correcto = False
        # p = sub.Popen(shlex.split('sh /home/administrador/ex11-7.generarlist.sh'),  stdout=sub.PIPE, stderr=sub.PIPE)
        ruta = '/home/administrador/ex11-7.generarlist.sh'
        p = sub.Popen(('sh', ruta), stdout=sub.PIPE, stderr=sub.PIPE)
        salidas, errores = p.communicate()
        if len(salidas) != 0:
            print salidas
        else:
            # Ha habido errores lanzamos una excepción
            print errores
        return correcto
