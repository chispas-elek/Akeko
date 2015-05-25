# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

import MySQLdb


class MySQLConnector(object):

    # Definimos un método de ejecución de consultas estático
    def execute(self, p_consulta):
        cur = self.conexion()
        result = cur.execute(p_consulta)
        cur.close()
        return result

    def conexion(self):
        db = MySQLdb.connect(host="localhost", # El host de la máquina
                             user="john", # El usuario de la BD
                             passwd="megajonhy", # la password de la BD
                             db="jonhydb") # el nombre de la base de datos a usar
        # Es necesario crear un objeto de tipo cursor
        # será indispenbale para hacer los execute necesarios.
        cursor = db.cursor()
        return cursor