# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Cliente.src.packControladoras import CMisTags
from Cliente.src.packModelo import ListaScript
import re


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
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/arrow-right.svg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.bEliminar.setIcon(icon)
        self.bEliminar.setObjectName("bEliminar")
        self.gridLayout.addWidget(self.bEliminar, 4, 2, 1, 1)
        self.bAnadir = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/arrow-left.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
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
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/dialog-ok-apply.svg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAplicar.setIcon(icon2)
        self.bAplicar.setObjectName("bAplicar")
        self.horizontalLayout.addWidget(self.bAplicar)
        spacerItem3 = QtWidgets.QSpacerItem(35, 35, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bCerrar = QtWidgets.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/window-close.svg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
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
        self.listEnElTag.setWhatsThis(_translate("Form",
                                                 "Contiene los Scripts que están o estarán contenidos en le Tag. Si el Tag es nuevo, ésta lista vendrá por defecto vacía."))
        self.listDisponibles.setToolTip(_translate("Form", "Scripts disponibles para el Tag"))
        self.listDisponibles.setWhatsThis(_translate("Form",
                                                     "Contiene los scripts disponibles para el Tag actual. Tanto si es para modificar uno como para crearlo. Desplazar éstos scripts al lado izquierdo para incluirlos en el Tag."))
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
    def __init__(self, p_id_usuario, p_tag, p_iu_mis_tags, parent=None):
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
        self.tag = p_tag
        self.controlador_mis_tags = CMisTags.CMisTags()
        self.iu_mis_tags = p_iu_mis_tags

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
        if self.tag is not None:
            # Estamos modificando un TAg
            scripts_en_el_tag = self.controlador_mis_tags.obtener_scripts_tag(self.tag.id_tag)
            scripts_en_el_tag.cargar_lista_script(self.ventana.listEnElTag)
            scripts_disponibles = self.controlador_mis_tags.obtener_scripts_no_en_tag(self.tag.id_tag)
            scripts_disponibles.cargar_lista_script(self.ventana.listDisponibles)
            self.ventana.lNombreTag.setText(self.tag.nombre_tag)
            self.ventana.lDescripcion.setText(self.tag.descripcion)

        else:
            scripts_disponibles = self.controlador_mis_tags.obtener_scripts_no_en_tag(-1)
            scripts_disponibles.cargar_lista_script(self.ventana.listDisponibles)
        # Libreamos las señales
        self.ventana.listEnElTag.blockSignals(False)
        self.ventana.listDisponibles.blockSignals(False)

        # Cargamos el comboBox dependiendo de la situación.
        # Bloque de señales
        self.ventana.cOwner.blockSignals(True)
        self.ventana.cOwner.clear()

        if self.tag is not None:
            # Estamos modificando un tag Existente por lo que vamos a cargar a todos los profesores
            # Primero añadimos al usuario acutal
            self.ventana.cOwner.addItem("Yo. Usuario actual", self.id_usuario)
            lista_usuarios = self.controlador_mis_tags.obtener_todos_los_propietarios(self.id_usuario)
            if len(lista_usuarios) != 0:
                for usuario in lista_usuarios:
                    self.ventana.cOwner.addItem(usuario['Nombre'] + " " + usuario['Apellido'], usuario['IdUsuario'])
        else:
            # Esttamos creando un nuevo TAg, el único owner será el propio profesor.
            # Pasamos
            pass

        # Por último libero el Cbombox
        self.ventana.cOwner.blockSignals(False)

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
        question_box = QMessageBox()
        question_box.setIcon(2)
        question_box.setWindowTitle("Aplicar cambios")
        question_box.setText("¡¡Atención!!")
        question_box.setInformativeText("¿Estás seguro que deseas aplicar los siguientes cambios?")
        question_box.setDetailedText("Recuerda revisar correctamente todos los datos. Si estás modificando un script "
                                     "ten en cuenta si lo estás o no donando. Una vez realizada la donación no podrás "
                                     "volver a usar más éste script. Revisa de forma cautelosa todos los datos antes "
                                     "de proceder.")
        # Creamos los botones de aceptar y cancelar.
        question_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        question_box.setDefaultButton(QMessageBox.Cancel)
        # Ejectuamos la interfaz y recogemos el resultado de la decisión
        seleccion = question_box.exec_()
        if seleccion == QMessageBox.Ok:
            if self.tag is None:
                # Si el TAG es NONE es que queremos crear un nuevo TAG
                # Obtenemeos las listas actuales
                lista_en_el_tag_actual = self.ventana.listEnElTag.findItems \
                    ("*", QtCore.Qt.MatchWrap | QtCore.Qt.MatchWildcard)
                if len(lista_en_el_tag_actual) != 0:
                    lista_scripts_nuevo_tag = ListaScript.ListaScript()
                    # Por cada elemento, extraemos el Script y lo incluimos en la lista

                    for item in lista_en_el_tag_actual:
                        item_data = item.data(QtCore.Qt.UserRole)
                        script = item_data[1]
                        lista_scripts_nuevo_tag.anadir(script)
                    # Tenemeos que aplicar las máscaras de filtrado para saber si los datos están bien introducidos
                    if self._mascara_filtrado(self.ventana.lNombreTag.text()):
                        # El Nombre del tag es correcto
                        if len(self.ventana.lDescripcion.text()) != 0:
                            # Contiene al menos alguna descripcción
                            # LLamamos a la función
                            exito = self.controlador_mis_tags.crear_tag_usuario(self.ventana.lNombreTag.text(),
                                                                                self.id_usuario,
                                                                                self.ventana.lDescripcion.text(),
                                                                                lista_scripts_nuevo_tag)
                            if exito:
                                # Se ha creado el Tag correctamente.
                                info_box = QMessageBox()
                                info_box.setIcon(1)
                                info_box.setWindowTitle("Crear Nuevo Tag")
                                info_box.setText("CORRECTO")
                                info_box.setInformativeText("Se ha creado el Tag correctamente en el sistema")
                                info_box.exec_()
                                self.iu_mis_tags.cargar_datos()
                                self.close()
                            else:
                                # Ha ocurido un error
                                error_box = QMessageBox()
                                error_box.setIcon(3)
                                error_box.setWindowTitle("Crear Nuevo Tag")
                                error_box.setText("ERROR")
                                error_box.setInformativeText("Ha ocurrido algún error a la hora de crear un Tag. "
                                                             "Revisa que no hayas intentado crear un Tag con el mismo "
                                                             "nombre de alguno creado con anterioridad")
                                error_box.exec_()
                        else:
                            print "No ha introducido nada en la descripción"
                            warm_box_2 = QMessageBox()
                            warm_box_2.setIcon(2)
                            warm_box_2.setWindowTitle("Crear Nuevo Tag")
                            warm_box_2.setText("¡Atención!")
                            warm_box_2.setInformativeText("Introduce al menos una descripción.")
                            warm_box_2.exec_()
                    else:
                        print "Nome del Tag incorrecto"
                        warm_box = QMessageBox()
                        warm_box.setIcon(2)
                        warm_box.setWindowTitle("Crear Nuevo Tag")
                        warm_box.setText("¡Atención!")
                        warm_box.setInformativeText("Los datos introducidos para el nombre del Tag no son válidos")
                        warm_box.exec_()
                else:
                    # El usuaio no ha introducido ningún Script
                    info_box_2 = QMessageBox()
                    info_box_2.setIcon(1)
                    info_box_2.setWindowTitle("Crear Nuevo Tag")
                    info_box_2.setText("INFORMACIÓN")
                    info_box_2.setInformativeText("Antes de crear un Tag, al menos introduce un Script en él.")
                    info_box_2.exec_()

            else:
                # Queremos modificar uno existente
                # Obtenemos la lsita de scripts actuales
                lista_en_el_tag_actual = self.ventana.listEnElTag.findItems \
                    ("*", QtCore.Qt.MatchWrap | QtCore.Qt.MatchWildcard)
                lista_disponible_actual = self.ventana.listDisponibles.findItems \
                    ("*", QtCore.Qt.MatchWrap | QtCore.Qt.MatchWildcard)
                if len(lista_en_el_tag_actual) != 0:
                    # El nuevo Tag contiene elementos nuevos
                    if self._mascara_filtrado(self.ventana.lNombreTag.text()):
                        # El Nombre del tag es correcto
                        if len(self.ventana.lDescripcion.text()) != 0:
                            # Contiene al menos alguna descripcción
                            # LLamamos a la función
                            owner = self.ventana.cOwner.itemData(self.ventana.cOwner.currentIndex())

                            exito = self.controlador_mis_tags.modificar_tag(self.id_usuario, self.tag.id_tag,
                                                                            self.ventana.lNombreTag.text(), owner,
                                                                            self.ventana.lDescripcion.text(),
                                                                            self.lista_disponble_previa,
                                                                            lista_disponible_actual,
                                                                            self.lista_en_el_tag_previa,
                                                                            lista_en_el_tag_actual)

                            if exito:
                                # Se ha Modificado correctamente
                                info_box = QMessageBox()
                                info_box.setIcon(1)
                                info_box.setWindowTitle("Modificar Tag actual")
                                info_box.setText("CORRECTO")
                                info_box.setInformativeText("Se ha modificado el Tag correctamente en el sistema")
                                info_box.exec_()
                                self.iu_mis_tags.cargar_datos()
                                self.close()
                            else:
                                # Ha ocurido un error
                                error_box = QMessageBox()
                                error_box.setIcon(3)
                                error_box.setWindowTitle("Modificar Tag actual")
                                error_box.setText("ERROR")
                                error_box.setInformativeText("Ha ocurrido algún error a la hora de modificar un Tag. "
                                                             "Revisa que no hayas intentado crear un Tag con el mismo "
                                                             "nombre de alguno creado con anterioridad")
                                error_box.exec_()
                        else:
                            print "No ha introducido nada en la descripción"
                            warm_box_2 = QMessageBox()
                            warm_box_2.setIcon(2)
                            warm_box_2.setWindowTitle("Modificar Tag actual")
                            warm_box_2.setText("¡Atención!")
                            warm_box_2.setInformativeText("Introduce al menos una descripción.")
                            warm_box_2.exec_()
                    else:
                        print "Nome del Tag incorrecto"
                        warm_box = QMessageBox()
                        warm_box.setIcon(2)
                        warm_box.setWindowTitle("Modificar Tag actual")
                        warm_box.setText("¡Atención!")
                        warm_box.setInformativeText("Los datos introducidos para el nombre del Tag no son válidos")
                        warm_box.exec_()
                else:
                    error_box_2 = QMessageBox()
                    error_box_2.setIcon(3)
                    error_box_2.setWindowTitle("Modificar Tag actual")
                    error_box_2.setText("ERROR")
                    error_box_2.setInformativeText("No dejar el Tag sin scripts. "
                                                   "Debes dejar al Tag con al menos un script.")
                    error_box_2.exec_()

    def _mascara_filtrado(self, p_texto):
        """
        Filtra los valores de entrada para permitir sólo letras y números

        :param p_texto: El texto a comprobar
        :return: True si la cadeno de texto contiene a-z, A-Z, 0-9
                False si la cadena de texto contiene espacios o caracteres extraños
        """
        patron = re.compile("[a-zA-Z\d]*$")
        return patron.match(p_texto)
