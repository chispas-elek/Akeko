# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IU_CAMBIAR_NOMBRE_GRUPO.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Cliente.src.packControladoras import CMain
import re

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(556, 330)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lNuevoNombreGrupo = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lNuevoNombreGrupo.setFont(font)
        self.lNuevoNombreGrupo.setAlignment(QtCore.Qt.AlignCenter)
        self.lNuevoNombreGrupo.setObjectName("lNuevoNombreGrupo")
        self.verticalLayout.addWidget(self.lNuevoNombreGrupo)
        spacerItem1 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lNombreGrupo = QtWidgets.QLineEdit(Dialog)
        self.lNombreGrupo.setMaxLength(25)
        self.lNombreGrupo.setAlignment(QtCore.Qt.AlignCenter)
        self.lNombreGrupo.setObjectName("lNombreGrupo")
        self.horizontalLayout_2.addWidget(self.lNombreGrupo)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.bCambiarNombre = QtWidgets.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/edit-rename.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCambiarNombre.setIcon(icon)
        self.bCambiarNombre.setObjectName("bCambiarNombre")
        self.horizontalLayout.addWidget(self.bCambiarNombre)
        spacerItem6 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.bCancelar = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/edit-delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCancelar.setIcon(icon1)
        self.bCancelar.setObjectName("bCancelar")
        self.horizontalLayout.addWidget(self.bCancelar)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.lNombreGrupo)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cambiar Nombre Grupo"))
        self.label.setText(_translate("Dialog", "Por favor, define &un nombre válido para:"))
        self.lNuevoNombreGrupo.setText(_translate("Dialog", "...."))
        self.bCambiarNombre.setText(_translate("Dialog", "Cambiar Nombre"))
        self.bCancelar.setText(_translate("Dialog", "Cancelar"))

class CambiarNombreGrupo(QtWidgets.QDialog):
    # Definimos el constructor de la clase principal
    def __init__(self, p_iu_main, p_id_grupo, p_nombre_grupo_actual, p_lista_grupos, parent=None):
        # Llamamos al constructor de la clase padre
        super(CambiarNombreGrupo, self).__init__(parent)
        self.el_parent = parent
        # Instancio la Interfaz
        self.ventana = Ui_Dialog()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        self.iu_main = p_iu_main
        self.id_grupo = p_id_grupo
        self.lista_grupos = p_lista_grupos

        self.ventana.lNuevoNombreGrupo.setText(p_nombre_grupo_actual)

        # Configuramos las acciones de los botones
        self.ventana.bCancelar.clicked.connect(self.close)
        self.ventana.bCambiarNombre.clicked.connect(self.cambiar_nombre_grupo)

    def cambiar_nombre_grupo(self):
        # Obtenemos le nombre del grupoo y lo validamos
        nombre_grupo = self.ventana.lNombreGrupo.text()
        if nombre_grupo == self.iu_main.ventana.cSelecionarGrupo.currentText():
            # Los nombre de los grupos coinciden. Error
            warm_box = QMessageBox()
            warm_box.setIcon(2)
            warm_box.setWindowTitle("Cambiar Nombre Grupo")
            warm_box.setText("ATENCIÓN")
            warm_box.setInformativeText("Has introducido el mismo nombre del grupo.")
            warm_box.exec_()
        elif nombre_grupo == "":
            error_box_blank = QMessageBox()
            error_box_blank.setIcon(3)
            error_box_blank.setWindowTitle("Cambiar Nombre Grupo")
            error_box_blank.setText("ERROR")
            error_box_blank.setInformativeText("Introduce al menos un nombre para el grupo.")
            error_box_blank.exec_()
        else:
            if self.__mascara_filtrado(nombre_grupo):
                # El nombre del grupo no existe por lo que podemos insertar los datos en la BD
                controladora_main = CMain.CMain()
                resultado = controladora_main.cambiar_nombre(self.id_grupo, nombre_grupo, self.lista_grupos)
                # Si el resultado es correcto, mostramos una pantalla de confirmación. y cerramoas la interfaz anterior.
                print "Resultado de la operación es %s" % resultado
                if resultado is True:
                    # Las cosas han ido como deberian.
                    info_box = QMessageBox()
                    info_box.setIcon(1)
                    info_box.setWindowTitle("Cambiar Nombre Grupo")
                    info_box.setText("CORRECTO")
                    info_box.setInformativeText("Nombre del grupo cambiado correctamente.")
                    info_box.exec_()
                    self.iu_main.generar_combo_box()
                    self.close()
                else:
                    print "El nombre del grupo no se ha actualizado"
                    error_box = QMessageBox()
                    error_box.setIcon(3)
                    error_box.setWindowTitle("Cambiar Nombre Grupo")
                    error_box.setText("ERROR")
                    error_box.setInformativeText("El nombre del grupo no se ha podido actualizar de manera correcta.")
                    error_box.setDetailedText("El nombre del grupo no se ha podido actualizar de manera correcta. "
                                                 "Ésto puede ser debido a que se ha introducido un nombre que ya existia "
                                                 "con anteriorirdad o que ha habido algún error de conexión con el servidor.")
                    error_box.exec_()
            else:
                print "Los caracteres del grupo introducidos son inválidos"
                warm_box_2 = QMessageBox()
                warm_box_2.setIcon(2)
                warm_box_2.setWindowTitle("Cambiar Nombre Grupo")
                warm_box_2.setText("ADVERTENCIA")
                warm_box_2.setInformativeText("Los caracteres introducidos para el nuevo grupo, no son correctos.")
                warm_box_2.exec_()

    def __mascara_filtrado(self, p_texto):
        """
        Filtra los valores de entrada para permitir sólo letras y números

        :param p_texto: El texto a comprobar
        :return: True si la cadeno de texto contiene a-z, A-Z, 0-9
                False si la cadena de texto contiene espacios o caracteres extraños
        """
        patron = re.compile("[a-zA-Z\d]*$")
        return patron.match(p_texto)
