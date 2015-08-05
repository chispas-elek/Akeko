# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IU_LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from sys import argv
from Cliente.src.packControladoras import CLogin
import re
import IU_MAIN

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 260)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lEditContrasena = QtWidgets.QLineEdit(self.centralwidget)
        self.lEditContrasena.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoPredictiveText)
        self.lEditContrasena.setMaxLength(45)
        self.lEditContrasena.setObjectName("lEditContrasena")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lEditContrasena)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lEditUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.lEditUsuario.setMinimumSize(QtCore.QSize(50, 0))
        self.lEditUsuario.setMaxLength(45)
        self.lEditUsuario.setObjectName("lEditUsuario")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lEditUsuario)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.gridLayout.addLayout(self.formLayout, 0, 1, 1, 1)
        self.bLogin = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/document-encrypted.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bLogin.setIcon(icon)
        self.bLogin.setObjectName("bLogin")
        self.gridLayout.addWidget(self.bLogin, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 29))
        self.menubar.setObjectName("menubar")
        self.menuHerramientas = QtWidgets.QMenu(self.menubar)
        self.menuHerramientas.setObjectName("menuHerramientas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpciones = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/configure-shortcuts.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpciones.setIcon(icon1)
        self.actionOpciones.setObjectName("actionOpciones")
        self.menuHerramientas.addAction(self.actionOpciones)
        self.menubar.addAction(self.menuHerramientas.menuAction())
        self.label_2.setBuddy(self.lEditContrasena)
        self.label.setBuddy(self.lEditUsuario)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lEditUsuario, self.lEditContrasena)
        MainWindow.setTabOrder(self.lEditContrasena, self.bLogin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.lEditContrasena.setToolTip(_translate("MainWindow", "<html><head/><body><p>Contraseña de usuario del sistema</p></body></html>"))
        self.lEditContrasena.setWhatsThis(_translate("MainWindow", "Se ingresa el nombre de usuario del sistema. Para tener uno, por favor, contacta con el administrador."))
        self.label_2.setToolTip(_translate("MainWindow", "Contraseña del usuario"))
        self.label_2.setText(_translate("MainWindow", "Contrase&ña:"))
        self.lEditUsuario.setToolTip(_translate("MainWindow", "<html><head/><body><p>Nombre de usuario del sistema</p></body></html>"))
        self.lEditUsuario.setWhatsThis(_translate("MainWindow", "Se ingresa el nombre de usuario del sistema. Para tener uno, por favor, contacta con el administrador."))
        self.label.setToolTip(_translate("MainWindow", "Nombre de usuario."))
        self.label.setText(_translate("MainWindow", "&Usuario: "))
        self.bLogin.setToolTip(_translate("MainWindow", "<html><head/><body><p>Acceder al sistema</p></body></html>"))
        self.bLogin.setText(_translate("MainWindow", "Login"))
        self.menuHerramientas.setTitle(_translate("MainWindow", "Herramie&ntas"))
        self.actionOpciones.setText(_translate("MainWindow", "&Opciones"))

class Principal(QtWidgets.QMainWindow):
    # Definimos el constructor de la clase principal
    def __init__(self, parent=None):
        # Llamamos al constructor de la clase padre
        super(Principal, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)

        # Programamos los conectores de cada botón, lista, etc....
        self.ventana.bLogin.clicked.connect(self.login)
        # Configuramos las máscaras de entrada

        # todo descomentar ésto para que la contraseña no sea visible
        # self.ventana.lEditContrasena.setEchoMode(QLineEdit.Password)

        # Iniciamos las variables de las nuevas ventanas
        self.window_main = None
        self.window_error_login_user_pass_incorrect = None
        self.window_error_malformed_data = None
        self.window_error_unable_connect = None

    def login(self):
        """
        Lee los valores de usuario y contraseña y valida la identificación del usuario

        :return:
        """
        usuario = self.ventana.lEditUsuario.text()
        contrasena = self.ventana.lEditContrasena.text()
        if len(usuario) == 0 or len(contrasena) == 0:
            # Faltan datos, mostramos error
            print "Los datos son incorrectos"
            msg_box_w = QMessageBox()
            msg_box_w.setIcon(2)
            msg_box_w.setWindowTitle("Login Aviso")
            msg_box_w.setText("¡Atención!")
            msg_box_w.setInformativeText("Introduce un usuario y una contraseña. Revisa los datos.")
            msg_box_w.exec_()
        else:
            # Tenemos un posible usuario y contraseña válidos, vamos a validarlos
            if self.__mascara_filtrado(usuario) and self.__mascara_filtrado(contrasena):
                controladora_login = CLogin.CLogin()
                resultado = controladora_login.iniciar_sesion(usuario, contrasena)
                if resultado is not None and resultado != 'fail':
                    # Cargamos la interfaz principal del sistema y cerramos la actual.
                    print "Login correcto, cargamos interfaz principal."
                    if self.window_main is None:
                        self.window_main = IU_MAIN.Main(resultado)
                    self.window_main.show()
                    self.close()
                elif resultado == 'fail':
                    # Exception en la BD del servidor remoto
                    print "Error garrafal en la BD"
                else:
                    # Usuario y contraseña incorrectos.
                    print "Error, Usuario y contraseña mal introducida."
                    msg_box_e = QMessageBox()
                    msg_box_e.setIcon(3)
                    msg_box_e.setWindowTitle("Login Error")
                    msg_box_e.setText("ERROR")
                    msg_box_e.setInformativeText("El usuario y contraseña introducidos no son correctos.")
                    msg_box_e.exec_()
            else:
                print "Los caracteres introducidos son incorrectos"
                msg_box_w_2 = QMessageBox()
                msg_box_w_2.setIcon(2)
                msg_box_w_2.setWindowTitle("Login Aviso")
                msg_box_w_2.setText("¡Atención!")
                msg_box_w_2.setInformativeText("Los datos introducidos tienen muy poco sentido.")
                msg_box_w_2.exec_()

    def __mascara_filtrado(self, p_texto):
        """
        Filtra los valores de entrada para permitir sólo letras y números

        :param p_texto: El texto a comprobar
        :return: True si la cadeno de texto contiene a-z, A-Z, 0-9
                False si la cadena de texto contiene espacios o caracteres extraños
        """
        patron = re.compile("[a-zA-Z\d]*$")
        return patron.match(p_texto)

 # Se lanza la interface principal
if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    myapp = Principal()
    myapp.show()
    exit(app.exec_())
