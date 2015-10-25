# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Cliente.src.packControladoras import CMisTags
from Cliente.src.packVistas import IU_GESTIONAR_TAG

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listTagsUsuario = QtWidgets.QListWidget(self.centralwidget)
        self.listTagsUsuario.setObjectName("listTagsUsuario")
        self.verticalLayout.addWidget(self.listTagsUsuario)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.bModificar_tag = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/configure-shortcuts.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bModificar_tag.setIcon(icon)
        self.bModificar_tag.setObjectName("bModificar_tag")
        self.horizontalLayout_2.addWidget(self.bModificar_tag)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.bEliminar_tag = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bEliminar_tag.setIcon(icon1)
        self.bEliminar_tag.setObjectName("bEliminar_tag")
        self.horizontalLayout_2.addWidget(self.bEliminar_tag)
        spacerItem2 = QtWidgets.QSpacerItem(90, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lNombreTag = QtWidgets.QLabel(self.groupBox)
        self.lNombreTag.setText("")
        self.lNombreTag.setObjectName("lNombreTag")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lNombreTag)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lScripts = QtWidgets.QLabel(self.groupBox)
        self.lScripts.setText("")
        self.lScripts.setObjectName("lScripts")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lScripts)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lFecha = QtWidgets.QLabel(self.groupBox)
        self.lFecha.setText("")
        self.lFecha.setObjectName("lFecha")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lFecha)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lDescripcion = QtWidgets.QLabel(self.groupBox)
        self.lDescripcion.setText("")
        self.lDescripcion.setObjectName("lDescripcion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lDescripcion)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.bCerrar = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/dialog-close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCerrar.setIcon(icon2)
        self.bCerrar.setObjectName("bCerrar")
        self.horizontalLayout.addWidget(self.bCerrar)
        spacerItem6 = QtWidgets.QSpacerItem(170, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 29))
        self.menubar.setObjectName("menubar")
        self.menuNuevo = QtWidgets.QMenu(self.menubar)
        self.menuNuevo.setObjectName("menuNuevo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCrear_tag = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCrear_tag.setIcon(icon3)
        self.actionCrear_tag.setObjectName("actionCrear_tag")
        self.actionEditar_Tag = QtWidgets.QAction(MainWindow)
        self.actionEditar_Tag.setObjectName("actionEditar_Tag")
        self.menuNuevo.addAction(self.actionCrear_tag)
        self.menubar.addAction(self.menuNuevo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mis Tags"))
        MainWindow.setWhatsThis(_translate("MainWindow", "Ésta interfaz permite el manejo de los Tags personalizados del usuario. Desde aquí se pondrán crear, modificar y eliminar los Tags.\n"
"\n"
"Los Tags son agrupaciones de Scripts que permiten introducir de una vez una serie de Scripts determinados. Es una buena forma de ahorrar tiempo, cuando se tiene en mente qué Scripts se quieren añadir a un grupo determinado."))
        self.listTagsUsuario.setToolTip(_translate("MainWindow", "Listado de Tags del usuario"))
        self.listTagsUsuario.setWhatsThis(_translate("MainWindow", "En ésta lista se visualizan los Tags que tiene el usuario creado actualmente. La estrella indica que es un tag para ayudar a la futura identificación en otras áreas de la aplicación.\n"
"\n"
"Al pulsar un elemento, se habilitarán los botones de Modificar y Eliminar Tag para poder hacer operaciones sobre éstos.\n"
"\n"
"Si se desea crear un nuevo Tag, se debe haccer uso del menu \"Nuevo\""))
        self.bModificar_tag.setToolTip(_translate("MainWindow", "Modificar el Tag seleccionado"))
        self.bModificar_tag.setText(_translate("MainWindow", "&Modificar Tag"))
        self.bEliminar_tag.setToolTip(_translate("MainWindow", "Eliminar el Tag seleccionado"))
        self.bEliminar_tag.setText(_translate("MainWindow", "&Eliminar Tag"))
        self.groupBox.setToolTip(_translate("MainWindow", "Información avanzada del Tag actualmente seleccionado."))
        self.groupBox.setWhatsThis(_translate("MainWindow", "Contiene la información relacionada sobre el Tag que está seleccionado actualmente. Dicha información consiste en:\n"
"\n"
"--> Nombre Tag: El nombre del Tag\n"
"--> Scripts: Qué Scripts conforman el tag actualmente seleccionado. (Vista rápida)\n"
"--> Fecha Creación: La fecha de creación del Tag. (NO DE SUS FUTURAS MODIFICACIONES)"))
        self.groupBox.setTitle(_translate("MainWindow", "Información Avanzada"))
        self.label.setText(_translate("MainWindow", "- Nombre Tag:"))
        self.label_3.setText(_translate("MainWindow", "- Scripts:"))
        self.label_5.setText(_translate("MainWindow", "- Fecha Creación:"))
        self.label_2.setText(_translate("MainWindow", "Descripción"))
        self.bCerrar.setText(_translate("MainWindow", "Cerrar"))
        self.menuNuevo.setTitle(_translate("MainWindow", "&Nuevo"))
        self.actionCrear_tag.setText(_translate("MainWindow", "&Crear Tag"))
        self.actionEditar_Tag.setText(_translate("MainWindow", "&Editar Tag"))

class MisTags(QtWidgets.QMainWindow):
    # Definimos el constructor de la clase principal
    def __init__(self, p_id_usuario, parent=None):
        # Llamamos al constructor de la clase padre
        super(MisTags, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        self.id_usuario = p_id_usuario
        self.controlador_mis_tags = CMisTags.CMisTags()

        # Cargamos la lista de datos
        self.cargar_datos()

        # Deshabilitar algunos botones inicialmente
        self.ventana.bModificar_tag.setDisabled(True)
        self.ventana.bEliminar_tag.setDisabled(True)

        # Creamos las ventanas
        self.window_crear_tag = None
        self.window_modificar_tag = None

        # Programamos las conexiones
        self.ventana.bCerrar.clicked.connect(self.close)
        self.ventana.actionCrear_tag.triggered.connect(self.crear_tag)
        self.ventana.listTagsUsuario.clicked.connect(self.imprimir_informacion)
        self.ventana.listTagsUsuario.currentRowChanged.connect(self.habilitar_botones)
        self.ventana.bModificar_tag.clicked.connect(self.modificar_tag)
        self.ventana.bEliminar_tag.clicked.connect(self.borrar_tag)

    def cargar_datos(self):
        # Bloqueamos señales y limpiamos
        self.ventana.listTagsUsuario.blockSignals(True)
        self.ventana.listTagsUsuario.clear()

        # Obtenemos la lista de los scripts y cargamos la interfaz
        lista_tags = self.controlador_mis_tags.obtener_tags_usuario(self.id_usuario)
        lista_tags.cargar_lista_tag(self.ventana.listTagsUsuario)

        # Libreamos las señales
        self.ventana.listTagsUsuario.blockSignals(False)

        # Limpiamos la ventana de información
        self.ventana.lNombreTag.setText("")
        self.ventana.lFecha.setText("")
        self.ventana.lDescripcion.setText("")
        self.ventana.lScripts.setText("")

    def imprimir_informacion(self):
        """
        Imprime la informaicón del Tag seleccionado

        :return:
        """
        # Obtener los datos del item
        item_seleccionado = self.ventana.listTagsUsuario.currentItem()
        item_seleccionado_datos = item_seleccionado.data(QtCore.Qt.UserRole)
        tag = item_seleccionado_datos[1]
        self.ventana.lNombreTag.setText(tag.nombre_tag)
        self.ventana.lFecha.setText(tag.f_creacion)
        self.ventana.lDescripcion.setText(tag.descripcion)
        # Obtenemos los scripts que pertenecen al TAG
        lista_scripts_tag_seleccionado = self.controlador_mis_tags.obtener_scripts_tag(tag.id_tag)
        # Emviamos el elemento y seteamos los valores
        lista_scripts_tag_seleccionado.imprimir_elementos_iu(self.ventana.lScripts)

    def habilitar_botones(self):
        # Habilitamos los botones para poder manipular el TAG
        self.ventana.bModificar_tag.setDisabled(False)
        self.ventana.bEliminar_tag.setDisabled(False)

    def crear_tag(self):
        """
        Abre la ventana para poder realizar la creación de un TAG

        :return:
        """
        self.window_crear_tag = IU_GESTIONAR_TAG.GestionarTag(self.id_usuario, None, self)
        self.window_crear_tag.show()

    def modificar_tag(self):
        """
        ABre la ventana para poder realizar la modificación de un TAG

        :return:
        """
        # Obtener los datos del item
        item_seleccionado = self.ventana.listTagsUsuario.currentItem()
        if item_seleccionado is not None:
            item_seleccionado_datos = item_seleccionado.data(QtCore.Qt.UserRole)
            tag = item_seleccionado_datos[1]
            self.window_modificar_tag = IU_GESTIONAR_TAG.GestionarTag(self.id_usuario, tag, self)
            self.window_modificar_tag.show()
        else:
            warm_box_modif = QMessageBox()
            warm_box_modif.setIcon(2)
            warm_box_modif.setWindowTitle("Mis Tags")
            warm_box_modif.setText("ADVERTENCIA")
            warm_box_modif.setInformativeText("Selecciona al menos un Tag antes de intentar modificar algo.")
            warm_box_modif.exec_()

    def borrar_tag(self):
        """
        Dado un tag seleccionado. Borra el Tag del sistema y elimina el tag de los grupos donde haya sido aplicado

        :return:
        """
        # Mostramos advertencia al usuario
        # Generamos un QmeesageBox para gestionar la pregunta al usuario
        warm_box = QMessageBox()
        warm_box.setIcon(2)
        warm_box.setWindowTitle("Borrado de un tag")
        warm_box.setText("¡¡Atención!!")
        warm_box.setInformativeText("¿Estás seguro que deseas eliminar el tag?")
        warm_box.setDetailedText("Al eliminar un Tag no sólo éste será borrado del sistema. Si no que además "
                                 "todos los grupos en le que se haya aplicado el Tag estarán afectados por dicho "
                                 "borrado. El resultado será que los scripts aplicados por los Tags implicados serán "
                                 "removados automáticamente.")
        # Creamos los botones de aceptar y cancelar.
        warm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        warm_box.setDefaultButton(QMessageBox.Cancel)
        # Ejectuamos la interfaz y recogemos el resultado de la decisión
        seleccion = warm_box.exec_()
        if seleccion == QMessageBox.Ok:
            # Obtener los datos del item
            # todo solvertar pequeño error al eliminar un tag
            item_seleccionado = self.ventana.listTagsUsuario.currentItem()
            if item_seleccionado is not None:
                item_seleccionado_datos = item_seleccionado.data(QtCore.Qt.UserRole)
                tag = item_seleccionado_datos[1]
                resultado = self.controlador_mis_tags.eliminar_tag_usuario(tag.id_tag, self.id_usuario)
                if resultado:
                    # El Tag se ha eliminado de forma exitosa
                    info_box = QMessageBox()
                    info_box.setIcon(1)
                    info_box.setWindowTitle("Borrado de un tag")
                    info_box.setText("CORRECTO")
                    info_box.setInformativeText("El Tag se ha borrado satisfactoriamente")
                    info_box.exec_()
                    self.cargar_datos()
                else:
                    # Ha ocurrido algún error
                    error_box = QMessageBox()
                    error_box.setIcon(3)
                    error_box.setWindowTitle("Borrado de un tag")
                    error_box.setText("Error")
                    error_box.setInformativeText("Algo ha pasado al eliminar el Tag")
                    error_box.exec_()
            else:
                warm_box_borrar = QMessageBox()
                warm_box_borrar.setIcon(2)
                warm_box_borrar.setWindowTitle("Mis Tags")
                warm_box_borrar.setText("ADVERTENCIA")
                warm_box_borrar.setInformativeText("Selecciona al menos un Tag antes de intentar modificar algo.")
                warm_box_borrar.exec_()