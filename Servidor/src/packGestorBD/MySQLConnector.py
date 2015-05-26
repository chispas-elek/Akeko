# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import MySQLdb


class MySQLConnector(object):

    # Definimos un método de ejecución de consultas estático
    def execute(self, p_consulta):
        devolver = None
        database = self.conexion
        if database is not None:
            cur = database.cursor()
            # Si nos conectamos correctamente, ejecutamos Consulta
            try:
                result = cur.execute(p_consulta)
                # Cerramos el cursor y la conexión a la BD
                cur.close
                database.close()
                devolver = result
            except MySQLdb.Error, e:
                try:
                    print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
                except IndexError:
                    print "MySQL Error: %s" % str(e)
        return devolver

    def conexion(self):
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
