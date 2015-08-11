# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Cliente.src.packControladoras import CMisTags

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
        self.listEnElTag = QtWidgets.QListWidget(Form)
        self.listEnElTag.setObjectName("listEnElTag")
        self.gridLayout.addWidget(self.listEnElTag, 1, 0, 5, 1)
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
        self.lNombreTag = QtWidgets.QLineEdit(self.groupBox)
        self.lNombreTag.setMaxLength(20)
        self.lNombreTag.setObjectName("lNombreTag")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lNombreTag)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lDescripcion = QtWidgets.QLineEdit(self.groupBox)
        self.lDescripcion.setMaxLength(150)
        self.lDescripcion.setObjectName("lDescripcion")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lDescripcion)
        self.cOwner = QtWidgets.QComboBox(self.groupBox)
        self.cOwner.setObjectName("cOwner")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cOwner)
        self.label_7.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.lNombreTag.raise_()
        self.lDescripcion.raise_()
        self.cOwner.raise_()
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lNombreScript = QtWidgets.QLabel(self.groupBox_2)
        self.lNombreScript.setText("")
        self.lNombreScript.setObjectName("lNombreScript")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lNombreScript)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lDescripcionScript = QtWidgets.QLabel(self.groupBox_2)
        self.lDescripcionScript.setText("")
        self.lDescripcionScript.setObjectName("lDescripcionScript")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lDescripcionScript)
        self.verticalLayout.addWidget(self.groupBox_2)
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
        self.label_5.setBuddy(self.lNombreTag)
        self.label_7.setBuddy(self.cOwner)
        self.label.setBuddy(self.lDescripcion)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.listEnElTag, self.listDisponibles)
        Form.setTabOrder(self.listDisponibles, self.bAnadir)
        Form.setTabOrder(self.bAnadir, self.bEliminar)
        Form.setTabOrder(self.bEliminar, self.lNombreTag)
        Form.setTabOrder(self.lNombreTag, self.lDescripcion)
        Form.setTabOrder(self.lDescripcion, self.bAplicar)
        Form.setTabOrder(self.bAplicar, self.bCerrar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Gestionar Tag"))
        self.label_4.setText(_translate("Form", "Disponibles"))
        self.listEnElTag.setToolTip(_translate("Form", "Scripts dentro del Tag"))
        self.listEnElTag.setWhatsThis(_translate("Form", "Contiene los Scripts que están o estarán contenidos en le Tag. Si el Tag es nuevo, ésta lista vendrá por defecto vacía."))
        self.listDisponibles.setToolTip(_translate("Form", "Scripts disponibles para el Tag"))
        self.listDisponibles.setWhatsThis(_translate("Form", "Contiene los scripts disponibles para el Tag actual. Tanto si es para modificar uno como para crearlo. Desplazar éstos scripts al lado izquierdo para incluirlos en el Tag."))
        self.label_3.setText(_translate("Form", "En el tag"))
        self.bEliminar.setToolTip(_translate("Form", "Eliminar un Script del Tag."))
        self.bEliminar.setText(_translate("Form", "Eliminar"))
        self.bAnadir.setToolTip(_translate("Form", "Añadir un Script al Tag"))
        self.bAnadir.setText(_translate("Form", "Añadir"))
        self.groupBox.setTitle(_translate("Form", "Información Avanzada"))
        self.label_5.setText(_translate("Form", "&Nombre del &Tag:"))
        self.lNombreTag.setToolTip(_translate("Form", "Nombre del Tag a Introducir"))
        self.label_7.setText(_translate("Form", "Owner del &Tag:"))
        self.label.setText(_translate("Form", "&Descripción:"))
        self.lDescripcion.setToolTip(_translate("Form", "Descripción del Tag a introducir"))
        self.cOwner.setToolTip(_translate("Form", "Propietario del Tag. Por defecto, es el usuario que lo ha creado."))
        self.groupBox_2.setTitle(_translate("Form", "Información del Script"))
        self.label_2.setText(_translate("Form", "-Nombre Script:"))
        self.label_8.setText(_translate("Form", "-Descripción:"))
        self.bAplicar.setText(_translate("Form", "Aplicar"))
        self.bCerrar.setText(_translate("Form", "Cerrar"))

class GestionarTag(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_id_usuario, p_id_tag, parent=None):
        # todo, pensar en enviar el TAG completo, con toda la información.
        # Llamamos al constructor de la clase padre
        super(GestionarTag, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        # Parámetros adicionales para los listWidget
        self.ventana.listDisponibles.setSortingEnabled(True)
        self.ventana.listEnElTag.setSortingEnabled(True)

        self.id_usuario = p_id_usuario
        self.id_tag = p_id_tag
        self.controlador_mis_tags = CMisTags.CMisTags()

        # cagamos los datos de las listas
        self._cargar_datos()

        # Guardamos una copia de las listas actuales
        self.lista_disponble_previa = self.ventana.listDisponibles.findItems \
            ("*", QtCore.Qt.MatchWrap | QtCore.Qt.MatchWildcard)
        self.lista_en_el_tag_previa = self.ventana.listEnElTag.findItems \
            ("*", QtCore.Qt.MatchWrap | QtCore.Qt.MatchWildcard)

        # Conectamos los botones
        self.ventana.bCerrar.clicked.connect(self.close)
        self.ventana.bAnadir.clicked.connect(self.anadir_un_elemento)
        self.ventana.bEliminar.clicked.connect(self.eliminar_un_elemento)
        self.ventana.bAplicar.clicked.connect(self.aplicar_cambios)
        self.ventana.listDisponibles.clicked.connect(self.imprimir_info_disponible)
        self.ventana.listEnElTag.clicked.connect(self.imprimir_info_en_tag)

    def _cargar_datos(self):
        """
        Cargamos los datos de las listas para poder saber qué está aplicado actualmente o no

        :return:
        """
        # Cargamos las listas
        # Lock de las tablas
        self.ventana.listEnElTag.blockSignals(True)
        self.ventana.listEnElTag.clear()
        self.ventana.listDisponibles.blockSignals(True)
        self.ventana.listDisponibles.clear()
        # Obtenemos los Scripts que hay en el TAG
        if self.id_tag != -1:
            scripts_en_el_tag = self.controlador_mis_tags.obtener_scripts_tag(self.id_tag)
            scripts_en_el_tag.cargar_lista_script(self.ventana.listEnElTag)
        scripts_disponibles = self.controlador_mis_tags.obtener_scripts_no_en_tag(self.id_tag)
        scripts_disponibles.cargar_lista_script(self.ventana.listDisponibles)
        # Libreamos las señales
        self.ventana.listEnElTag.blockSignals(False)
        self.ventana.listDisponibles.blockSignals(False)

        if self.id_tag != -1:
            # Cargar el combobox
            # todo cargar el combobox con los usuarios

            # Obtener los datos relativos al TAG
            pass


    def anadir_un_elemento(self):
        """
        Añade un Elemento a la lista de En el tag

        :return:
        """
        # Obtenemos la posición de la lista del scripts pulsado
        posicion_selec = self.ventana.listDisponibles.currentRow()
        if posicion_selec != -1:
            # Obtenemos el item y lo eliminamos de la lista de forma automática
            item_selec = self.ventana.listDisponibles.takeItem(posicion_selec)
            # Cambia el color de las letras del item.
            item_selec.setForeground(QtGui.QColor(102, 204, 0))
            self.ventana.listEnElTag.addItem(item_selec)
        else:
            print "No se ha seleccionado nada"
            msg_box_e = QMessageBox()
            msg_box_e.setIcon(1)
            msg_box_e.setWindowTitle("Información selección script/tag")
            msg_box_e.setText("INFORMACIÓN")
            msg_box_e.setInformativeText("No has seleccionado ningún script/tag. Recuerda seleccionar primero uno")
            msg_box_e.exec_()

    def eliminar_un_elemento(self):
        """
        Eliminamos un elemento de la lista en el tag

        :return:
        """
        # Obtenemos la posición de la lista del scripts pulsado
        posicion_selec = self.ventana.listEnElTag.currentRow()
        if posicion_selec != -1:
            # Obtenemos el item y lo eliminamos de la lista de forma automática
            item_selec = self.ventana.listEnElTag.takeItem(posicion_selec)
            # Cambia el color de las letras del item.
            item_selec.setForeground(QtGui.QColor(204, 0, 0))
            self.ventana.listDisponibles.addItem(item_selec)
        else:
            print "No se ha seleccionado nada"
            msg_box_e = QMessageBox()
            msg_box_e.setIcon(1)
            msg_box_e.setWindowTitle("Información selección script/tag")
            msg_box_e.setText("INFORMACIÓN")
            msg_box_e.setInformativeText("No has seleccionado ningún script/tag. Recuerda seleccionar primero uno")
            msg_box_e.exec_()

    def imprimir_info_disponible(self):
        # Obtener los datos del item
        item_seleccionado = self.ventana.listDisponibles.currentItem()
        # Obtenemos el objeto que contiene el item
        item_seleccionado_datos = item_seleccionado.data(QtCore.Qt.UserRole)
        script = item_seleccionado_datos[1]
        self.ventana.lNombreScript.setText(script.nombre_s)
        self.ventana.lDescripcionScript.setText(script.descripcion)

    def imprimir_info_en_tag(self):
        # Obtener los datos del item
        item_seleccionado = self.ventana.listEnElTag.currentItem()
        # Obtenemos el objeto que contiene el item
        item_seleccionado_datos = item_seleccionado.data(QtCore.Qt.UserRole)
        script = item_seleccionado_datos[1]
        self.ventana.lNombreScript.setText(script.nombre_s)
        self.ventana.lDescripcionScript.setText(script.descripcion)

    def aplicar_cambios(self):
        """
        Aplica los cambios realizados

        :return:
        """
        pass