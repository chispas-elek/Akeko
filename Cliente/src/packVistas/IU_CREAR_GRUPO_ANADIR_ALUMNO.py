# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IU_CREAR_GRUPO_ANADIR_ALUMNO.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Cliente.src.packModelo import Alumno
import re

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(569, 310)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lDni = QtWidgets.QLineEdit(Form)
        self.lDni.setMaxLength(10)
        self.lDni.setObjectName("lDni")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lDni)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lNombre = QtWidgets.QLineEdit(Form)
        self.lNombre.setMaxLength(45)
        self.lNombre.setObjectName("lNombre")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lNombre)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lApellidos = QtWidgets.QLineEdit(Form)
        self.lApellidos.setMaxLength(45)
        self.lApellidos.setObjectName("lApellidos")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lApellidos)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lEmail = QtWidgets.QLineEdit(Form)
        self.lEmail.setMaxLength(45)
        self.lEmail.setObjectName("lEmail")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lEmail)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bAnadirAlumno = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-add-user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAnadirAlumno.setIcon(icon)
        self.bAnadirAlumno.setObjectName("bAnadirAlumno")
        self.horizontalLayout.addWidget(self.bAnadirAlumno)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.bCancelar = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/dialog-close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCancelar.setIcon(icon1)
        self.bCancelar.setObjectName("bCancelar")
        self.horizontalLayout.addWidget(self.bCancelar)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.lDni)
        self.label_2.setBuddy(self.lNombre)
        self.label_3.setBuddy(self.lApellidos)
        self.label_4.setBuddy(self.lEmail)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Añadir un alumno"))
        self.label.setText(_translate("Form", "&Dni*:"))
        self.lDni.setToolTip(_translate("Form", "Dni del alumno"))
        self.lDni.setWhatsThis(_translate("Form", "El número de identificación personal (DNI) del alumno a añadir."))
        self.label_2.setText(_translate("Form", "&Nombre*:"))
        self.lNombre.setToolTip(_translate("Form", "Nombre del alumno"))
        self.lNombre.setWhatsThis(_translate("Form", "El nombre del Alumno"))
        self.label_3.setText(_translate("Form", "Ape&llidos*:"))
        self.lApellidos.setToolTip(_translate("Form", "Apellidos del alumno"))
        self.lApellidos.setWhatsThis(_translate("Form", "Los dos apellidos del alumno."))
        self.label_4.setText(_translate("Form", "Email*:"))
        self.lEmail.setToolTip(_translate("Form", "Email del alumno"))
        self.lEmail.setWhatsThis(_translate("Form", "El email que posee el alumno en la universidad por el cual le serán enviado los correos."))
        self.bAnadirAlumno.setToolTip(_translate("Form", "Añadir alumno al nuevo grupo"))
        self.bAnadirAlumno.setWhatsThis(_translate("Form", "Añade el alumno a la lista de creación del grupo. ¡OJO! Si el alumno ya existe NO se agregará"))
        self.bAnadirAlumno.setText(_translate("Form", "Añadir alumno"))
        self.bCancelar.setToolTip(_translate("Form", "Cancelar acción"))
        self.bCancelar.setWhatsThis(_translate("Form", "Cancela la acción, se perderán todos los datos"))
        self.bCancelar.setText(_translate("Form", "Cancelar"))

class CrearGrupoAnadirAlumno(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_iu_crear_grupo, p_lista_alumnos, parent=None):
        # Llamamos al constructor de la clase padre
        super(CrearGrupoAnadirAlumno, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        self.iu_crear_grupo = p_iu_crear_grupo
        self.lista_alumnos = p_lista_alumnos

        # Conectamos los botones
        self.ventana.bCancelar.clicked.connect(self.close)
        self.ventana.bAnadirAlumno.clicked.connect(self.anadir_nuevo_alumno)

        # Configuramos el bloqueo de ventanas
        self.quiero_cerrar = True
        self.iu_crear_grupo.quiero_cerrar = False

    def anadir_nuevo_alumno(self):
        # primero comprobamos que los datos estén correctos
        resultado = self._mascara_filtrado_datos()
        if resultado is True:
            # Agregamos el nuevo alumno
            nuevo_alumno = Alumno.Alumno(str(self.ventana.lDni.text()), str(self.ventana.lNombre.text()),
                                         str(self.ventana.lApellidos.text()), str(self.ventana.lEmail.text()))
            # Aqui ejectuamos el existe alumno y añadimos o no
            if self.lista_alumnos.exite_alumno(nuevo_alumno.dni_a) is None:
                print "Se añade al alumno %s" % nuevo_alumno.nombre_a
                info_box = QMessageBox()
                info_box.setIcon(1)
                info_box.setWindowTitle("Añadir un alumno")
                info_box.setText("Información")
                info_box.setInformativeText("El alumno ha sido añadido de manera satisfactoria.")
                info_box.exec_()
                self.lista_alumnos.anadir(nuevo_alumno)
                self.iu_crear_grupo.generar_tabla()
                self.close()
            else:
                print "El alumno ya estaba en la lista, no se añade"
                warm_box_2 = QMessageBox()
                warm_box_2.setIcon(2)
                warm_box_2.setWindowTitle("Añadir un alumno")
                warm_box_2.setText("¡Atención!")
                warm_box_2.setInformativeText("Ya existe otro alumno con el mismo Dni.")
                warm_box_2.exec_()

        else:
            # Alguno de los datos no ha sido correctamente introducidos.
            warm_box = QMessageBox()
            warm_box.setIcon(2)
            warm_box.setWindowTitle("Añadir un alumno")
            warm_box.setText("¡Atención!")
            warm_box.setInformativeText(resultado)
            warm_box.exec_()

    def _mascara_filtrado_datos(self):
        """
        Revisa que los datos introducidos por el usuario son correctos.

        :return: True si todo ha ido bien
                Un texto de error si algo no ha salido bien
        """
        # todo conseguir que acepte cadenas de Strings con acentuaciones mirar en meterlo dentro de STR
        # Comprobamos el Dni
        patron_dni = re.compile("\d{8}[A-Z]$")
        if patron_dni.match(self.ventana.lDni.text()) and self.ventana.lDni.text() != "":
            print "dni ok"
            # Comprobamos el nombre
            patron_nombre = re.compile("[a-zA-Z]*$")
            if patron_nombre.match(self.ventana.lNombre.text()) and self.ventana.lNombre.text() != "":
                print "Nombre ok"
                patron_apellido = re.compile("[a-zA-Z]*\s[a-zA-Z]*$")
                if patron_apellido.match(self.ventana.lApellidos.text()) and self.ventana.lApellidos.text() != "":
                    print "apellido ok"
                    patron = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
                    if patron.match(self.ventana.lEmail.text()) and self.ventana.lEmail.text() != "":
                        print "ALL OK"
                        resultado = True
                    else:
                        resultado = "Mail incorrecto"
                else:
                    resultado = "Apellido incorrecto"
            else:
                resultado = "Nombre incorrecto"
        else:
            resultado = "Dni incorrecto"

        return resultado

    def closeEvent(self, evnt):
        if self.quiero_cerrar:
            # Quitamos el bloqueo de cerrado de la anterior interfaz y cerramos
            self.iu_crear_grupo.quiero_cerrar = True
            super(CrearGrupoAnadirAlumno, self).closeEvent(evnt)
        else:
            evnt.ignore()
