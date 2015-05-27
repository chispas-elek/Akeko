# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import MySQLdb


class MySQLConnector(object):

    def __init__(self):
        pass

    # Definimos un método de ejecución de consultas estático
    def execute(self, p_consulta):
        devolver = None
        database = self.__conexion()
        if database is not None:
            cur = database.cursor()
            # Si nos conectamos correctamente, ejecutamos Consulta
            try:
                cur.execute(*p_consulta)
                devolver = cur.fetchall()
                # Cerramos el cursor y la conexión a la BD
                # Hacemos commit y cerramos los cursores y la BD
                database.commit()
                cur.close()
                database.close()
            except MySQLdb.Error, e:
                try:
                    print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
                except IndexError:
                    print "MySQL Error: %s" % str(e)
        return devolver

    def __conexion(self):
        try:
            # Nos conectamos a la BD
            db = MySQLdb.connect(host="localhost",  # El host de la máquina
                                 user="akeko",  # El usuario de la BD
                                 passwd="akekohola123",  # la password de la BD
                                 db="AkekoProject")  # el nombre de la base de datos a usar
            # Es necesario crear un objeto de tipo cursor
            # será indispenbale para hacer los execute necesarios.
            return db
        except MySQLdb.Error, e:
            try:
                print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
            except IndexError:
                print "MySQL Error: %s" % str(e)
        # En caso de fallo, devolvemos nada
        return None
