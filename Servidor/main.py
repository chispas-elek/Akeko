# -*- encoding: utf-8 -*-

import sys
from os.path import dirname
from src.packGestorSocket import ServerReceiver

sys.path.append(dirname(__file__))

if __name__ == "__main__":
    config_server = ServerReceiver.ConfigServer()
    config_server.iniciar_servidor()
