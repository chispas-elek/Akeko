# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IU_GESTIONAR_SCRIPT.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Cliente.src.packControladoras import CGestionarScript

from sys import argv

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(872, 686)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        self.listAplicados = QtWidgets.QListWidget(Form)
        self.listAplicados.setObjectName("listAplicados")
        self.gridLayout.addWidget(self.listAplicados, 1, 0, 5, 1)
        self.listDisponibles = QtWidgets.QListWidget(Form)
        self.listDisponibles.setObjectName("listDisponibles")
        self.gridLayout.addWidget(self.listDisponibles, 1, 4, 5, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.bEliminar = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/arrow-right.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bEliminar.setIcon(icon)
        self.bEliminar.setObjectName("bEliminar")
        self.gridLayout.addWidget(self.bEliminar, 4, 2, 1, 1)
        self.bAnadir = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/arrow-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAnadir.setIcon(icon1)
        self.bAnadir.setObjectName("bAnadir")
        self.gridLayout.addWidget(self.bAnadir, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lNombre = QtWidgets.QLabel(self.groupBox)
        self.lNombre.setText("")
        self.lNombre.setObjectName("lNombre")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lNombre)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lDescripcion = QtWidgets.QLabel(self.groupBox)
        self.lDescripcion.setText("")
        self.lDescripcion.setObjectName("lDescripcion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lDescripcion)
        self.lNombre.raise_()
        self.label_7.raise_()
        self.lDescripcion.raise_()
        self.label_5.raise_()
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bAplicar = QtWidgets.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/dialog-ok-apply.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAplicar.setIcon(icon2)
        self.bAplicar.setObjectName("bAplicar")
        self.horizontalLayout.addWidget(self.bAplicar)
        spacerItem3 = QtWidgets.QSpacerItem(35, 35, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bCerrar = QtWidgets.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/window-close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCerrar.setIcon(icon3)
        self.bCerrar.setObjectName("bCerrar")
        self.horizontalLayout.addWidget(self.bCerrar)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.listAplicados, self.listDisponibles)
        Form.setTabOrder(self.listDisponibles, self.bAnadir)
        Form.setTabOrder(self.bAnadir, self.bEliminar)
        Form.setTabOrder(self.bEliminar, self.bAplicar)
        Form.setTabOrder(self.bAplicar, self.bCerrar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestionar Script"))
        self.label_4.setText(_translate("Form", "Disponibles"))
        self.label_3.setText(_translate("Form", "Aplicados"))
        self.bEliminar.setText(_translate("Form", "Eliminar"))
        self.bAnadir.setText(_translate("Form", "Añadir"))
        self.groupBox.setTitle(_translate("Form", "Información Avanzada"))
        self.label_5.setText(_translate("Form", "- Nombre:"))
        self.label_7.setText(_translate("Form", "- Descripción:"))
        self.bAplicar.setText(_translate("Form", "Aplicar"))
        self.bCerrar.setText(_translate("Form", "Cerrar"))

class GestionarScript(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_id_usuario, p_lista_alumnos, p_id_grupo, parent=None):
        # Llamamos al constructor de la clase padre
        super(GestionarScript, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)

        self.id_usuario = p_id_usuario
        self.lista_alumnos = p_lista_alumnos
        self.id_grupo = p_id_grupo

        self.gestionar_script = CGestionarScript.CGestionarScript()

        # Cargamos los datos de las listas
        self._cargar_datos()

        # Programamos los botones
        self.ventana.bCerrar.clicked.connect(self.close)

    def _cargar_datos(self):
        """
        Se encarga de obtener los datos relativos a la disponibilidad de los Scripts/Tags y los carga en las listas

        :return:
        """
        # Lock de las tablas
        self.ventana.listAplicados.blockSignals(True)
        self.ventana.listAplicados.clear()
        self.ventana.listDisponibles.blockSignals(True)
        self.ventana.listDisponibles.clear()

        # Obteemos los datos necesarios
        scripts_aplicados = self.gestionar_script.obtener_scripts(self.id_grupo)
        tags_aplicados = self.gestionar_script.obtener_tags(self.id_grupo)
        scripts_disponibles = self.gestionar_script.obtener_scripts_disponibles(self.id_grupo)
        tags_disponibles = self.gestionar_script.obtener_tags_disponibles(self.id_grupo)
        # Una ve obtenidos todos los dstos, rellenamos las tablas
        print scripts_disponibles
        print tags_disponibles




        # Libreamos las señales
        self.ventana.listAplicados.blockSignals(False)
        self.ventana.listDisponibles.blockSignals(False)
