# -*- coding: utf-8 -*-
__author__ = "Rubén Mulero"

# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QHeaderView, QMessageBox, QTableWidgetItem
from src.packControladoras import CHistorial
import datetime

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(1200, 800)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tHistorial = QtWidgets.QTableWidget(Form)
        self.tHistorial.setObjectName("tHistorial")
        self.tHistorial.setColumnCount(7)
        self.tHistorial.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/irc-operator.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tHistorial.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/get-hot-new-stuff.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tHistorial.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/im-user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.tHistorial.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/user-group-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tHistorial.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/checkbox.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.tHistorial.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/documentinfo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.tHistorial.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/view-calendar-day.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.tHistorial.setHorizontalHeaderItem(6, item)
        self.verticalLayout_2.addWidget(self.tHistorial)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(Form)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lBuscar = QtWidgets.QLineEdit(self.groupBox)
        self.lBuscar.setMaxLength(200)
        self.lBuscar.setClearButtonEnabled(True)
        self.lBuscar.setObjectName("lBuscar")
        self.horizontalLayout_2.addWidget(self.lBuscar)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cTipoFiltro = QtWidgets.QComboBox(self.groupBox)
        self.cTipoFiltro.setObjectName("cTipoFiltro")
        self.horizontalLayout_2.addWidget(self.cTipoFiltro)
        spacerItem3 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.dateInicio = QtWidgets.QDateEdit(self.groupBox)
        self.dateInicio.setCalendarPopup(True)
        self.dateInicio.setObjectName("dateInicio")
        self.horizontalLayout_3.addWidget(self.dateInicio)
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.dateFin = QtWidgets.QDateEdit(self.groupBox)
        self.dateFin.setCalendarPopup(True)
        self.dateFin.setObjectName("dateFin")
        self.horizontalLayout_3.addWidget(self.dateFin)
        spacerItem7 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(650, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.bFiltrar = QtWidgets.QPushButton(self.groupBox)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/view-filter.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bFiltrar.setIcon(icon7)
        self.bFiltrar.setObjectName("bFiltrar")
        self.horizontalLayout_4.addWidget(self.bFiltrar)
        spacerItem10 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.bLimpiarF = QtWidgets.QPushButton(self.groupBox)
        self.bLimpiarF.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/edit-undo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bLimpiarF.setIcon(icon8)
        self.bLimpiarF.setObjectName("bLimpiarF")
        self.horizontalLayout_4.addWidget(self.bLimpiarF)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem12 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem13)
        self.bCerrar = QtWidgets.QPushButton(Form)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/window-close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCerrar.setIcon(icon9)
        self.bCerrar.setObjectName("bCerrar")
        self.horizontalLayout.addWidget(self.bCerrar)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem14)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lBuscar, self.cTipoFiltro)
        Form.setTabOrder(self.cTipoFiltro, self.bFiltrar)
        Form.setTabOrder(self.bFiltrar, self.bLimpiarF)
        Form.setTabOrder(self.bLimpiarF, self.bCerrar)
        Form.setTabOrder(self.bCerrar, self.tHistorial)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Historial"))
        self.tHistorial.setWhatsThis(_translate("Form", "En ésta tabla se muestran todos los cambios que han sufrito los alumnos de cada grupo dependiendo de las decisiones que haya seleccionado el usuario actual Cada columna representa una serie de datos para que el usuario pueda saber qué acciones ha realizado exáctamente y el porqué de cada cambio. La tabla tiene los siguientes elementos:\n"
"\n"
"-> Script: Indica el script utilizado. Si está en blanco es porque ha sido usado un Tag en su lugar.\n"
"-> Tag: Indica el tag utilizado. Si está en blanc es porque ha sido usado un Script en su lugar.\n"
"-> Alumno: El nombre y apellidos del alumno afectado por el Script/Tag utilizados.\n"
"-> Grupo: El grupo por el cual pertenece el alumno.\n"
"-> Acción: La acción realizada. Puede ser añadir un Script/Tag, o eliminar.\n"
"-> Información: Muestra un texto que razona el porqué de la acción realizada.\n"
"-> Fecha: La fecha que registra la acción que se ha realizado."))
        item = self.tHistorial.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Script"))
        item = self.tHistorial.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Tag"))
        item = self.tHistorial.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Alumno"))
        item = self.tHistorial.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Grupo"))
        item = self.tHistorial.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Acción"))
        item = self.tHistorial.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Información"))
        item = self.tHistorial.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Fecha"))
        self.groupBox.setTitle(_translate("Form", "Opciones de filtrado avanzado"))
        self.label.setText(_translate("Form", "Buscar"))
        self.lBuscar.setToolTip(_translate("Form", "Introdce un texto de búsqueda."))
        self.lBuscar.setWhatsThis(_translate("Form", "En éste campo se introduce las palabas claves que conforman el criterior de búsqueda a realizar. Es imperativo seleccionar en el desplegable continuo qué tipo de criterior se quiere aplicar"))
        self.label_2.setText(_translate("Form", "Filtrar"))
        self.cTipoFiltro.setToolTip(_translate("Form", "Selecciona un filtro determinado."))
        self.label_5.setText(_translate("Form", "Elegir fecha de filtrado:"))
        self.label_3.setText(_translate("Form", "Desde:"))
        self.dateInicio.setToolTip(_translate("Form", "Fecha de inicio de la consulta"))
        self.dateInicio.setWhatsThis(_translate("Form", "Selecciona una fecha de inicio para iniciar la consulta. Por defecto obtendrá la fecha actual del sistema.\n"
"\n"
"Al pulsar sobre el desplegable se obtendrá un calendario que simplicifará el proceso para elegir la fecha. También se puede introducir la fecha de manera manual."))
        self.label_4.setText(_translate("Form", "Hasta:"))
        self.dateFin.setToolTip(_translate("Form", "Fecha de fin de la consulta"))
        self.dateFin.setWhatsThis(_translate("Form", "Selecciona una fecha de fin para iniciar la consulta. Por defecto obtendrá la fecha actual del sistema.\n"
"\n"
"Al pulsar sobre el desplegable se obtendrá un calendario que simplicifará el proceso para elegir la fecha. También se puede introducir la fecha de manera manual."))
        self.bFiltrar.setToolTip(_translate("Form", "Filtrar los parámetros deseados."))
        self.bFiltrar.setWhatsThis(_translate("Form", "Permite aplicar todos los filtros seleccionados por el usuario. Al pulsar éste botón el sistema actualizará la tabla superior mostrando únicamente aquellos resultados que  coincidan con los criterios de búsqueda que haya seleccionado."))
        self.bFiltrar.setText(_translate("Form", "Filtrar"))
        self.bLimpiarF.setToolTip(_translate("Form", "Limpiar todos los filtros aplicados"))
        self.bLimpiarF.setWhatsThis(_translate("Form", "Limpia todos los campos de filtros que el usuario haya modificado y actualiza la tabla superior mostrando todas las entradas existentes.\n"
"\n"
"Éste botón sólo se habilita si se detecta que existe un filtro aplicado."))
        self.bLimpiarF.setText(_translate("Form", "Limpiar Filtros"))
        self.bCerrar.setText(_translate("Form", "Cerrar"))

class Historial(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_id_usuario, parent=None):
        # Llamamos al constructor de la clase padre
        super(Historial, self).__init__(parent)

        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        # Modificamos las propiedades de la tabla para que no pueda ser editable y solo se pueda seleccionar 1 fila
        self.ventana.tHistorial.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ventana.tHistorial.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ventana.tHistorial.setSelectionMode(QAbstractItemView.SingleSelection)
        # Ajustamos la tabla para que haga un fit correcto con el espacio que tiene el layout.
        self.ventana.tHistorial.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Inicializar variables
        self.controladora_historial = CHistorial.CHistorial()
        self.id_usuario = p_id_usuario
        self.lista_historial = None

        # Configurar calendarios
        self._configurar_calendarios()

        # Cargamos la tabla
        self._generar_tabla()

        # Cargamos el combobox
        self._cargar_combo_box()

        # Conectar botones
        self.ventana.bCerrar.clicked.connect(self.close)
        self.ventana.bLimpiarF.clicked.connect(self.limpiar_filtros)
        self.ventana.bFiltrar.clicked.connect(self.aplicar_filtro)


    def _configurar_calendarios(self):
        """
        Obtiene el año actual y configura los calendarios para mostrar el inicio y final de año

        :return:
        """
        # Obtenemos la fecha actual
        fecha_actual = datetime.datetime.now()

        # Configuro el tipo de fecha a mostrar
        self.ventana.dateInicio.setDisplayFormat("dd/MM/yyyy")
        self.ventana.dateFin.setDisplayFormat("dd/MM/yyyy")

        # Configuramos los datetimes con la fecha del dia actual
        self.ventana.dateInicio.setDate(fecha_actual)
        self.ventana.dateFin.setDate(fecha_actual)

    def _generar_tabla(self):
        """
        Genera una tabla a partir de las entradas existentes en el historial

        """
        # Bloquemos las señales y vaciamos la tabla
        self.ventana.tHistorial.blockSignals(True)
        # self.ventana.tHistorial.clear()
        # Modificar y setear el HEADER de la tabla.

        if self.lista_historial is None:
            self.lista_historial = self.controladora_historial.obtener_historial(self.id_usuario)
        self.lista_historial.generar_tabla(self.ventana.tHistorial)

        # Liberamos las señales
        self.ventana.tHistorial.blockSignals(False)

    def _generar_tabla_filtrada(self, p_lista_filtrada):
        """
        La lista que nos genera la función de filtrado. Es una lista que contiene objetos de tipo historial.
        Por ello. La generación de la tabla de filtrado es algo diferente y se debe hacer en éste punto.

        :param p_lista_filtrada: La lista que contiene los elementos de historial ya filtrada
        :return:
        """

        # Bloquemos las señales y vaciamos la tabla
        self.ventana.tHistorial.blockSignals(True)

        # Cargamos la tabla
        self.ventana.tHistorial.setRowCount(len(p_lista_filtrada))
        for i in range(0, len(p_lista_filtrada)):
            # Rellenamos la tabla
            historial = p_lista_filtrada[i]
            newitem = QTableWidgetItem(historial.nombre_script)
            self.ventana.tHistorial.setItem(i, 0, newitem)
            newitem = QTableWidgetItem(historial.nombre_tag)
            self.ventana.tHistorial.setItem(i, 1, newitem)
            newitem = QTableWidgetItem(historial.nombre_alumno + " " + historial.apellido)
            self.ventana.tHistorial.setItem(i, 2, newitem)
            newitem = QTableWidgetItem(historial.nombre_grupo)
            self.ventana.tHistorial.setItem(i, 3, newitem)
            if historial.accion == 1:
                # Añadir
                newitem_anadir = QTableWidgetItem("Añadir")
                newitem_anadir.setIcon(QtGui.QIcon("plasma-next-icons/Breeze/actions/toolbar/list-add.svg"))
                self.ventana.tHistorial.setItem(i, 4, newitem_anadir)
            else:
                # Eliminar
                newitem_eliminar = QTableWidgetItem("Eliminar")
                newitem_eliminar.setIcon(QtGui.QIcon("plasma-next-icons/Breeze/actions/toolbar/edit-delete.svg"))
                self.ventana.tHistorial.setItem(i, 4, newitem_eliminar)

            newitem = QTableWidgetItem(historial.informacion)
            self.ventana.tHistorial.setItem(i, 5, newitem)
            newitem = QTableWidgetItem(historial.fecha_creacion_h)
            self.ventana.tHistorial.setItem(i, 6, newitem)

        # Liberamos las señales
        self.ventana.tHistorial.blockSignals(False)

    def _cargar_combo_box(self):
        """
        Carga el comboBox con los criterios de búsqueda deseados

        :return:
        """
        # Bloqueamos la señal del combo box y lo limpiamos
        self.ventana.cTipoFiltro.blockSignals(True)
        self.ventana.cTipoFiltro.clear()

        # Añadimos los criterios deseados
        self.ventana.cTipoFiltro.addItem("Nombre alumno", "nombre_alumno")
        self.ventana.cTipoFiltro.addItem("Apellido alumno", "apellido")
        self.ventana.cTipoFiltro.addItem("Grupo", "nombre_grupo")
        self.ventana.cTipoFiltro.addItem("Script", "nombre_script")
        self.ventana.cTipoFiltro.addItem("Tag", "nombre_tag")
        # self.ventana.cTipoFiltro.addItem("Acción", "accion")
        # Habilitamos el combobox y seleccionamos el primer criterio de la lista
        self.ventana.cTipoFiltro.setCurrentIndex(0)
        self.ventana.cTipoFiltro.blockSignals(False)


    def limpiar_filtros(self):
        """
        Limpia los filtros existentes y deshabilita el botón de filtrado


        :return:
        """
        # Limpiamos el buscador de datos
        self.ventana.lBuscar.setText("")
        # Ponemos el combo box a 0
        self.ventana.cTipoFiltro.setCurrentIndex(0)
        # Recargamos la fecha
        self._configurar_calendarios()
        # Recargamos la tabla inicial
        self._generar_tabla()
        # Deshabilitar el botón
        self.ventana.bLimpiarF.setEnabled(False)

    def aplicar_filtro(self):
        """
        Aplica los filtros deseados por el usuario

        :return:
        """
        # Comprobar que existan datos al menos
        if self.ventana.lBuscar.text() != "":
            # Contiene datos
            # Vamos a comprobar que al menos las fechas tengan sentido
            if self.ventana.dateInicio.date() < self.ventana.dateFin.date() or self.ventana.dateInicio.date() == self.ventana.dateFin.date():
                print "Todo correcto"
                # vamos a obtener el criterior de búsqueda
                criterio = self.ventana.cTipoFiltro.itemData(self.ventana.cTipoFiltro.currentIndex())
                # Hacemos la llamada para generar una nueva lista
                lista_historial_filtrada = self.lista_historial.realizar_filtrado(criterio, self.ventana.lBuscar.text(),
                                                                                  self.ventana.dateInicio.date(),
                                                                                  self.ventana.dateFin.date())
                # Ponemos la nueva lista en la tabla
                self._generar_tabla_filtrada(lista_historial_filtrada)
                # Habilitamos el botón de limpiar filtros
                self.ventana.bLimpiarF.setEnabled(True)

            elif self.ventana.dateInicio.date() > self.ventana.dateFin.date():
                troll_box = QMessageBox()
                troll_box.setIcon(2)
                troll_box.setWindowTitle("u MAD?????¿¿¿¿")
                troll_box.setText("U 4r3 tr1y1ng t0 tr4ll m3??????")
                troll_box.setInformativeText("¯\_(ツ)_/¯                      Shit happens? ")
                troll_box.exec_()

        else:
            warm_box = QMessageBox()
            warm_box.setIcon(2)
            warm_box.setWindowTitle("Filtrado aviso")
            warm_box.setText("¡Atención!")
            warm_box.setInformativeText("Introduce al menos un dato para la búsqueda")
            warm_box.exec_()
