# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

"""
MySQLConnector es una clase que facilita la conexión y envío de comandos SQL a la base de datos.
Ésta programada para pedir datos en forma de Diccionarios en caso de recibir una sentencia SELECT o
realizar un COMMIT si la sentencia es un INSERT, UPDATE o DELETE.

Si por alguna razón, ocurre algún error serio. El escript fuerza un rollback para dejar la BD en un estado estable.

"""


import MySQLdb


class MySQLConnector(object):

    def __init__(self):
        pass

    def execute(self, p_consulta):
        devolver = None
        database = self.__conexion()
        if database is not None:
            # Creamos un cursor para obtener los datos en forma de diccionarios
            cur = database.cursor(MySQLdb.cursors.DictCursor)
            # Si nos conectamos correctamente, ejecutamos Consulta
            try:
                if type(p_consulta) == tuple:
                    # Es una tupla con datos, llamada combinada
                    devolver = cur.execute(*p_consulta)
                    # Si la consulta es un SELECT obtenemos todos los datos
                    # Si es UPDATE o DELETE hacemos un commit.
                    if p_consulta[0].upper().startswith('SELECT'):
                        devolver = cur.fetchall()
                    else:
                        database.commit()
                else:
                    # Es un simple String de datos. LLamada sencilla
                    devolver = cur.execute(p_consulta)
                    if p_consulta.upper().startswith('SELECT'):
                        devolver = cur.fetchall()
                    else:
                        database.commit()
            except MySQLdb.Error, e:
                try:
                    print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
                except IndexError:
                    print "MySQL Error: %s" % str(e)
                finally:
                    if database:
                        database.rollback()
            finally:
                # Cerramos el cursor y la conexión a la BD
                if database:
                    cur.close()
                    database.close()

        return devolver

    def __conexion(self):
        try:
            # Nos conectamos a la BD
            db = MySQLdb.connect(host="localhost",  # El host de la máquina
                                 user="akeko",  # El usuario de la BD
                                 passwd="akekohola123",  # la password de la BD
                                 db="AkekoProject")  # el nombre de la base de datos a usar
            return db
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)
            finally:
                # En caso de fallo, devolvemos nada
                return None
