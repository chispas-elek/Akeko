# -*- encoding: utf-8 -*-
__author__ = 'Rubén Mulero'

"""
Cuando usamos la clase Json y hacemos uso del método loads() nos surge un problema.
Dicho problema se trata que los datos se transforman en unicode y por ende todos los elementos
terminan con un prefijo u' (por ejemplo u'Persona, u'Manolo....).
Para evitar ésto, se ha creado un diccionario que hace que el loads no termine poniendo esa molesta u'
"""


import json


class Decoder(object):

    def __init__(self, p_datos):
        self.datos = p_datos

    def decode_json(self):
        # Ejecutamos json loads y le indicamos un decoder específico usándo object_hook
        obj = json.loads(self.datos, object_hook=self._decode_dict)
        return obj

    # Los siguientes  dos métodos son los decoders

    def _decode_list(self, data):
        rv = []
        for item in data:
            if isinstance(item, unicode):
                item = item.encode('utf-8')
            elif isinstance(item, list):
                item = self._decode_list(item)
            elif isinstance(item, dict):
                item = self._decode_dict(item)
            rv.append(item)
        return rv

    def _decode_dict(self, data):
        rv = {}
        for key, value in data.iteritems():
            if isinstance(key, unicode):
                key = key.encode('utf-8')
            if isinstance(value, unicode):
                value = value.encode('utf-8')
            elif isinstance(value, list):
                value = self._decode_list(value)
            elif isinstance(value, dict):
                value = self._decode_dict(value)
            rv[key] = value
        return rv