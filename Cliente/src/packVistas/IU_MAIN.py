# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox
from Cliente.src.packControladoras import CMain
import IU_CREAR_GRUPO, IU_CAMBIAR_NOMBRE_GRUPO, IU_GESTIONAR_SCRIPT, IU_MIS_TAGS, IU_HISTORIAL

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.cSelecionarGrupo = QtWidgets.QComboBox(self.centralwidget)
        self.cSelecionarGrupo.setObjectName("cSelecionarGrupo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cSelecionarGrupo)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.verticalLayout.addLayout(self.formLayout)
        self.tListaAlumnos = QtWidgets.QTableWidget(self.centralwidget)
        self.tListaAlumnos.setObjectName("tListaAlumnos")
        self.tListaAlumnos.setColumnCount(4)
        self.tListaAlumnos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tListaAlumnos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tListaAlumnos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tListaAlumnos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tListaAlumnos.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tListaAlumnos)
        self.lNumeroAlumnos = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lNumeroAlumnos.setFont(font)
        self.lNumeroAlumnos.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lNumeroAlumnos.setObjectName("lNumeroAlumnos")
        self.verticalLayout.addWidget(self.lNumeroAlumnos)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bGestionarScripts = QtWidgets.QPushButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/user-group-properties.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bGestionarScripts.setIcon(icon)
        self.bGestionarScripts.setObjectName("bGestionarScripts")
        self.horizontalLayout.addWidget(self.bGestionarScripts)
        self.bCambiarNombre = QtWidgets.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/configure-shortcuts.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCambiarNombre.setIcon(icon1)
        self.bCambiarNombre.setObjectName("bCambiarNombre")
        self.horizontalLayout.addWidget(self.bCambiarNombre)
        self.bEliminarGrupo = QtWidgets.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/edit-delete-shred.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bEliminarGrupo.setIcon(icon2)
        self.bEliminarGrupo.setObjectName("bEliminarGrupo")
        self.horizontalLayout.addWidget(self.bEliminarGrupo)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 29))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuHistorial = QtWidgets.QMenu(self.menubar)
        self.menuHistorial.setObjectName("menuHistorial")
        self.menuCerrar_sesi_n = QtWidgets.QMenu(self.menubar)
        self.menuCerrar_sesi_n.setObjectName("menuCerrar_sesi_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAnadirGrupo = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/resource-group-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnadirGrupo.setIcon(icon3)
        self.actionAnadirGrupo.setObjectName("actionAnadirGrupo")
        self.actionVerHistorial = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/cartesian-plot-four-axes.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVerHistorial.setIcon(icon4)
        self.actionVerHistorial.setObjectName("actionVerHistorial")
        self.actionCerrarSesion = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/application-exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCerrarSesion.setIcon(icon5)
        self.actionCerrarSesion.setObjectName("actionCerrarSesion")
        self.actionGestionar_Mis_Tags = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/milestone.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGestionar_Mis_Tags.setIcon(icon6)
        self.actionGestionar_Mis_Tags.setObjectName("actionGestionar_Mis_Tags")
        self.menuArchivo.addAction(self.actionAnadirGrupo)
        self.menuHistorial.addAction(self.actionGestionar_Mis_Tags)
        self.menuHistorial.addAction(self.actionVerHistorial)
        self.menuCerrar_sesi_n.addAction(self.actionCerrarSesion)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuHistorial.menuAction())
        self.menubar.addAction(self.menuCerrar_sesi_n.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pantalla Principal"))
        self.label.setText(_translate("MainWindow", "Seleccionar grupo:"))
        self.tListaAlumnos.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Tabla que contiene la información relativa al grupo que ha sido seleccionado actualmente.</p></body></html>"))
        item = self.tListaAlumnos.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tListaAlumnos.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tListaAlumnos.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Dni"))
        item = self.tListaAlumnos.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "E-Mail"))
        self.lNumeroAlumnos.setText(_translate("MainWindow", "Número de alumnos en el grupo: XXXX"))
        self.groupBox.setTitle(_translate("MainWindow", "Acciones del grupo"))
        self.bGestionarScripts.setText(_translate("MainWindow", "Gestionar scripts"))
        self.bCambiarNombre.setText(_translate("MainWindow", "Cambiar nombre"))
        self.bEliminarGrupo.setText(_translate("MainWindow", "Eliminar"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Ar&chivo"))
        self.menuHistorial.setTitle(_translate("MainWindow", "Herramie&ntas"))
        self.menuCerrar_sesi_n.setTitle(_translate("MainWindow", "&Cerrar sesión"))
        self.actionAnadirGrupo.setText(_translate("MainWindow", "&Añadir nuevo grupo"))
        self.actionVerHistorial.setText(_translate("MainWindow", "Ver historial de &cambios"))
        self.actionCerrarSesion.setText(_translate("MainWindow", "&Cerrar la sesión actual"))
        self.actionGestionar_Mis_Tags.setText(_translate("MainWindow", "Gestionar Mis &Tags"))

class Main(QtWidgets.QMainWindow):
    # Definimos el constructor de la clase principal
    def __init__(self, p_id_usuario, parent=None):
        # Llamamos al constructor de la clase padre
        super(Main, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        # Modificamos las propiedades de la tabla para que no pueda ser editable y solo se pueda seleccionar 1 fila
        self.ventana.tListaAlumnos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ventana.tListaAlumnos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ventana.tListaAlumnos.setSelectionMode(QAbstractItemView.SingleSelection)
        # Ajustamos la tabla para que haga un fit correcto con el espacio que tiene el layout.
        self.ventana.tListaAlumnos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Cargamos los datos que nos vienen de otras interfaces
        self.id_usuario = p_id_usuario
        print "Usuario logueado en el sistema con el identificador ", p_id_usuario

        # Cargamos la controladora del main
        self.controladora_main = CMain.CMain()

        # Declaramos la lista de grupos
        self.lista_grupos = None
        self.lista_alumnos_grupo = None

        # Deshabilitamos en un principio los botones de gestión de los grupos
        self.ventana.bGestionarScripts.setDisabled(True)
        self.ventana.bCambiarNombre.setDisabled(True)
        self.ventana.bEliminarGrupo.setDisabled(True)

        # Generamos el combobox y seleccionamos el item
        self.generar_combo_box()
        self.seleccionar_item()

        # Programamos los conectores de cada botón, lista, etc....
        # self.ventana.bLogin.clicked.connect(self.login)
        self.ventana.cSelecionarGrupo.currentIndexChanged.connect(self.seleccionar_item)
        self.ventana.actionAnadirGrupo.triggered.connect(self.crear_grupo)
        self.ventana.actionGestionar_Mis_Tags.triggered.connect(self.mis_tags)
        self.ventana.bCambiarNombre.clicked.connect(self.cambiar_nombre_grupo)
        self.ventana.bEliminarGrupo.clicked.connect(self.eliminar_grupo)
        self.ventana.bGestionarScripts.clicked.connect(self.gestionar_script)
        self.ventana.actionVerHistorial.triggered.connect(self.historial)

        # Iniciamos las variables de las nuevas ventanas
        self.window_gestionar_script = None
        self.window_cambiar_nombre_grupo = None
        self.window_eliminar_grupo = None
        self.window_crear_grupo = None
        self.window_mis_tags = None
        self.window_historial = None

    def crear_grupo(self):
        """
        Lanza la interfaz de creación de nuevo grupo, pasándole la lista actual de grupos y el identificador de usuario.

        :return:
        """
        if self.window_crear_grupo is None:
            self.window_crear_grupo = IU_CREAR_GRUPO.CrearGrupo(self, self.id_usuario, self.lista_grupos)
        self.window_crear_grupo.show()

    def mis_tags(self):
        """
        Inicializa la interfaz de mis tags, para que el usuario pueda crear sus tags personalizados.

        :return:
        """
        if self.window_mis_tags is None:
            self.window_mis_tags = IU_MIS_TAGS.MisTags(self.id_usuario)
        self.window_mis_tags.show()

    def eliminar_grupo(self):
        """
        Lanza la interfaz de interrogación para eliminar el grupo que está actualmente seleccionado

        :return:
        """
        # todo pensar en la limitación que haga que el botón funcione o no.
        id_grupo = self.ventana.cSelecionarGrupo.itemData(self.ventana.cSelecionarGrupo.currentIndex())

        # Generamos un QmeesageBox para gestionar la pregunta al usuario
        warm_box = QMessageBox()
        warm_box.setIcon(2)
        warm_box.setWindowTitle("Borrado de un grupo")
        warm_box.setText("¡¡Atención!!")
        warm_box.setInformativeText("¿Estás seguro que deseas eliminar el grupo?")
        warm_box.setDetailedText("Al eliminar un grupo, todos los scripts de los alumnos asociados al mismo son "
                                 "eliminados de forma automática. Es recomendable revisar bien a quién afecta el "
                                 "borrado del grupo.")
        # Creamos los botones de aceptar y cancelar.
        warm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        warm_box.setDefaultButton(QMessageBox.Cancel)
        # Ejectuamos la interfaz y recogemos el resultado de la decisión
        seleccion = warm_box.exec_()
        if seleccion == QMessageBox.Ok:
            # Si el usuario ha pulsado a aceptar, procedemos a borrar el grupo
            resultado = self.controladora_main.borrar_grupo(self.id_usuario, id_grupo, self.lista_alumnos_grupo)
            if resultado is True:
                # Mostramos un mensaje indicando que las cosas han ido bien.
                msg_box = QMessageBox()
                msg_box.setIcon(1)
                msg_box.setWindowTitle("Borraddo de un grupo")
                msg_box.setText("CORRECTO")
                msg_box.setInformativeText("El grupo ha sido borrado corretamente")
                msg_box.exec_()
                # Regeneramos el combo box.
                self.generar_combo_box()
                self.seleccionar_item()
            else:
                print "Existe algún error a la hora de borrar el alumno"
                msg_box_e = QMessageBox()
                msg_box_e.setIcon(3)
                msg_box_e.setWindowTitle("Borraddo de un grupo")
                msg_box_e.setText("ERROR")
                msg_box_e.setInformativeText("Ha ocurrido algún error a la hora de borrar el grupo. Inténtelo de nuevo.")
                msg_box_e.exec_()

    def seleccionar_item(self):
        """
        Cuando el usuario selecciona un elemento en el combobox. Ésta funnción se encarga de rellenar la lista de los
        alumnos del grupo.

        :return:
        """
        # Obtenemos el elemento actualmente seleccionado
        id_grupo = self.ventana.cSelecionarGrupo.itemData(self.ventana.cSelecionarGrupo.currentIndex())
        self.lista_alumnos_grupo = self.controladora_main.obtener_alumnos(id_grupo)
        numero_alumnos = self.lista_alumnos_grupo.obtener_tamano_lista()
        if numero_alumnos != 0:
            # Las cosas han ido bien, creamos la tabla
            self._generar_tabla()
        else:
            # Ha pasado algo a la hora de obtener los alumnos. Damos un error
            print "Error serio a la hora de obtener los alumnos de un Grupo"
            # todo limpiar la tabla de elementos

    def cambiar_nombre_grupo(self):
        """
        Dado el grupo actualmente seleccionado, cambiamos el nombre por uno nuevo.

        :return:
        """
        # Obtenemos el elemento actualmente seleccionado
        id_grupo = self.ventana.cSelecionarGrupo.itemData(self.ventana.cSelecionarGrupo.currentIndex())
        nombre_grupo = self.ventana.cSelecionarGrupo.currentText()
        # Pasar todos los datos a la nueva interfaz
        if self.window_cambiar_nombre_grupo is None:
                self.window_cambiar_nombre_grupo = IU_CAMBIAR_NOMBRE_GRUPO.CambiarNombreGrupo\
                    (self, id_grupo, nombre_grupo, self.lista_grupos)
        self.window_cambiar_nombre_grupo.show()


    def historial(self):
        """
        Muesta el historial del usuario actual para ver los cambios realizados

        """
        self.window_historial = IU_HISTORIAL.Historial(self.id_usuario)
        self.window_historial.show()

    def gestionar_script(self):
        """
        Gestiona los scripts que dispone el grupo actualmente seleccionado

        """
        # Obtenemos el elemento actualmente seleccionado
        id_grupo = self.ventana.cSelecionarGrupo.itemData(self.ventana.cSelecionarGrupo.currentIndex())
        # nombre_grupo = self.ventana.cSelecionarGrupo.currentText()
        self.window_gestionar_script = IU_GESTIONAR_SCRIPT.GestionarScript(self.id_usuario,
                                                                           self.lista_alumnos_grupo, id_grupo)
        self.window_gestionar_script.show()

    def _generar_tabla(self):
        """
        Genera una tabla a partir de una lista de alumnos del grupo actualmente selecccionado

        """
        # Bloquemos las señales y vaciamos la tabla
        self.ventana.tListaAlumnos.blockSignals(True)
        # self.ventana.tListaAlumnos.clear()
        # Rellenamos la tabla
        tamano_lista = self.lista_alumnos_grupo.obtener_tamano_lista()
        # El tamaño de los datos que me vienen
        self.ventana.tListaAlumnos.setRowCount(tamano_lista)
        for i in range(0, tamano_lista):
            # Rellenamos la tabla
            alumno = self.lista_alumnos_grupo.obtener_alumno(i)
            newitem = QTableWidgetItem(alumno.dni_a)
            self.ventana.tListaAlumnos.setItem(i, 0, newitem)
            newitem = QTableWidgetItem(alumno.nombre_a)
            self.ventana.tListaAlumnos.setItem(i, 1, newitem)
            newitem = QTableWidgetItem(alumno.apellido_a)
            self.ventana.tListaAlumnos.setItem(i, 2, newitem)
            newitem = QTableWidgetItem(alumno.email_a)
            self.ventana.tListaAlumnos.setItem(i, 3, newitem)
        # Liberamos las señales
        self.ventana.tListaAlumnos.blockSignals(False)
        # Actualizo el valor del label con el número de alumnos del grupo actual.
        self.ventana.lNumeroAlumnos.setText("Número de alumnos en el grupo: %s"
                                            % tamano_lista)

    def generar_combo_box(self):
        """
        Dada una lista de grupos, rellena el combo box con los datos necesarios

        """
        # Obtenemos la lista actual de los grupos
        self.lista_grupos = self.controladora_main.obtener_grupos(self.id_usuario)
        # Bloqueamos la señal del combo box y lo limpiamos
        self.ventana.cSelecionarGrupo.blockSignals(True)
        self.ventana.cSelecionarGrupo.clear()
        tamano_lista = self.lista_grupos.obtener_tamano_lista()
        if tamano_lista == 0:
            # El usuario no tiene grupos creados anteriormente
            self.ventana.cSelecionarGrupo.addItem("No hay grupos disponibles")
            # Deshabilitamos los botones de función de los grupos
            self.ventana.bGestionarScripts.setDisabled(True)
            self.ventana.bCambiarNombre.setDisabled(True)
            self.ventana.bEliminarGrupo.setDisabled(True)
        else:
            # Cargamos los datoss del combobox
            for i in range(0, tamano_lista):
                un_grupo = self.lista_grupos.obtener_grupo(i)
                self.ventana.cSelecionarGrupo.addItem(un_grupo.nombre_grupo, un_grupo.id_grupo)
            # Habilitamos los botones de función de grupos
            self.ventana.bGestionarScripts.setDisabled(False)
            self.ventana.bCambiarNombre.setDisabled(False)
            self.ventana.bEliminarGrupo.setDisabled(False)
        # Habilitamos el combobox y seleccionamos el primer grupo de la lista
        self.ventana.cSelecionarGrupo.setCurrentIndex(0)
        self.ventana.cSelecionarGrupo.blockSignals(False)
