# -*- encoding: utf-8 -*-

import PyQt5
from PyQt5 import QtWidgets
from sys import path, argv
from os.path import dirname, join
from src.packVistas import IU_LOGIN


# Añadimos el path de nuestra app
path.append(dirname(__file__))

# Código adicional para tener compatibilidad con Windows
dirname_windows = dirname(PyQt5.__file__)
plugin_path = join(dirname_windows, 'plugins', 'platforms')
QtWidgets.QApplication.addLibraryPath(plugin_path)

 # Se lanza la interface principal
if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = IU_LOGIN.Principal()
    myapp.show()
    exit(app.exec_())
