# -*- encoding: utf-8 -*-

import sys
from os.path import dirname
from src.packGestorSocket import ServerReceiver

sys.path.append(dirname(__file__))

if __name__ == "__main__":

    PORT = 13373
    cert_path = "ssl/cacert.pem"
    key_path = "ssl/private/key.pem"

    config_server = ServerReceiver.ConfigServer(PORT, cert_path, key_path)
    config_server.iniciar_servidor()
