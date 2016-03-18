# -*- coding: utf-8 -*-
__author__ = "Rubén Mulero"

# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QAbstractItemView, QHeaderView, QTableWidgetItem
from src.packModelo import Alumno, ListaAlumno, ListaGrupo
import IU_CREAR_GRUPO_NOMBRE, IU_CREAR_GRUPO_ANADIR_ALUMNO

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(950, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tOpenFile = QtWidgets.QToolButton(Form)
        self.tOpenFile.setObjectName("tOpenFile")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tOpenFile)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.tAlumnos = QtWidgets.QTableWidget(Form)
        self.tAlumnos.setObjectName("tAlumnos")
        self.tAlumnos.setColumnCount(4)
        self.tAlumnos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/document-edit-decrypt.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tAlumnos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/format-text-subscript.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tAlumnos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/format-text-superscript.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.tAlumnos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/mail-mark-read.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.tAlumnos.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.tAlumnos)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.bAnadir = QtWidgets.QPushButton(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bAnadir.setIcon(icon4)
        self.bAnadir.setObjectName("bAnadir")
        self.horizontalLayout.addWidget(self.bAnadir)
        self.bEliminar = QtWidgets.QPushButton(Form)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/list-remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bEliminar.setIcon(icon5)
        self.bEliminar.setObjectName("bEliminar")
        self.horizontalLayout.addWidget(self.bEliminar)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.bCrear = QtWidgets.QPushButton(Form)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/user-group-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCrear.setIcon(icon6)
        self.bCrear.setObjectName("bCrear")
        self.horizontalLayout_2.addWidget(self.bCrear)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.bCancelar = QtWidgets.QPushButton(Form)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("plasma-next-icons/Breeze/actions/toolbar/dialog-close.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bCancelar.setIcon(icon7)
        self.bCancelar.setObjectName("bCancelar")
        self.horizontalLayout_2.addWidget(self.bCancelar)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label.setBuddy(self.tOpenFile)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.tOpenFile, self.tAlumnos)
        Form.setTabOrder(self.tAlumnos, self.bAnadir)
        Form.setTabOrder(self.bAnadir, self.bEliminar)
        Form.setTabOrder(self.bEliminar, self.bCrear)
        Form.setTabOrder(self.bCrear, self.bCancelar)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crear Grupo"))
        self.label.setText(_translate("Form", "Importar &un fichero de alumnos(formato *.txt"))
        self.tOpenFile.setText(_translate("Form", "..."))
        item = self.tAlumnos.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Dni"))
        item = self.tAlumnos.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Nombre"))
        item = self.tAlumnos.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Apellidos"))
        item = self.tAlumnos.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Email"))
        self.bAnadir.setText(_translate("Form", "Añadir"))
        self.bEliminar.setText(_translate("Form", "Eliminar"))
        self.bCrear.setText(_translate("Form", "Crear"))
        self.bCancelar.setText(_translate("Form", "Cancelar"))

class CrearGrupo(QtWidgets.QWidget):
    # Definimos el constructor de la clase principal
    def __init__(self, p_iu_main, p_id_usuario, p_lista_grupos, parent=None):
        # Llamamos al constructor de la clase padre
        super(CrearGrupo, self).__init__(parent)
        self.el_parent = parent
        # Instancio la Interfaz
        self.ventana = Ui_Form()
        self.ventana.setupUi(self)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
        self.setWindowIcon(QtGui.QIcon('logo/Akeko_logo.png'))

        self.iu_main = p_iu_main

        # Generamos la lista de alumos como variable global.
        self.lista_alumnos = ListaAlumno.ListaAlumno()
        self.id_usuario = p_id_usuario
        self.lista_grupos = p_lista_grupos

        # Deshabilitar algunos botones inicialmente
        self.ventana.bCrear.setDisabled(True)
        self.ventana.bEliminar.setDisabled(True)

        # Modificamos las propiedades de la tabla para que no pueda ser editable y solo se pueda seleccionar 1 fila
        self.ventana.tAlumnos.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ventana.tAlumnos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ventana.tAlumnos.setSelectionMode(QAbstractItemView.SingleSelection)
        # Ajustamos la tabla para que haga un fit correcto con el espacio que tiene el layout.
        self.ventana.tAlumnos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Realizamos las conexiones de los botones
        self.ventana.tOpenFile.clicked.connect(self.cargar_fichero)
        self.ventana.bCrear.clicked.connect(self.crear_un_grupo)
        self.ventana.bCancelar.clicked.connect(self.close)
        self.ventana.bAnadir.clicked.connect(self.anadir_alumno)
        self.ventana.bEliminar.clicked.connect(self.eliminar_alumno)

        # Inicializamos las nuevas interfaces
        self.window_crear_grupo_nombre = None
        self.window_anadir_nuevo_alumno = None

        # Configuramos el bloque de ventanas
        self.quiero_cerrar = True

    def anadir_alumno(self):
        """
        Ésta función llama a la ventana que nos permite introducir los datos de un nuevo alumno.

        :return:
        """
        """
        if self.window_anadir_nuevo_alumno is None:
            self.window_anadir_nuevo_alumno = IU_CREAR_GRUPO_ANADIR_ALUMNO.CrearGrupoAnadirAlumno \
                (self, self.lista_alumnos)
        self.window_anadir_nuevo_alumno.show()
        """
        # Generamos una nueva ventana por vez.
        self.window_anadir_nuevo_alumno = IU_CREAR_GRUPO_ANADIR_ALUMNO.CrearGrupoAnadirAlumno(self, self.lista_alumnos)
        self.window_anadir_nuevo_alumno.show()

    def eliminar_alumno(self):
        """
        Elimina al alumno actualmente seleccionado en la talba

        :return:
        """
        alumno_seleccionado = self.ventana.tAlumnos.selectionModel().selectedRows()
        dni = None
        # Este for está preparado para procesar varias selecciones, en nuestro caso sólo hace 1
        for index in sorted(alumno_seleccionado):
            row = index.row()  # Se obtiene el número de la línea
            dni = index.sibling(row, 0).data()  # Se obtiene el dato de la columna 0 en éste caso el DNI.

        if dni is not None:
            el_alumno = self.lista_alumnos.exite_alumno(dni)
            if el_alumno is not None:
                # Hemos encontrado el alumno y lo eliminamos de la lista
                self.lista_alumnos.eliminar(el_alumno)
                print "Se ha eliminado al alumno %s" % el_alumno.nombre_a
                # Regeneramos la tabla
                self.generar_tabla()

    def cargar_fichero(self):
        """
        Abre un diálogo de carga y permite introducir un fichero con extensión *.txt
        La función comprueba si la nomemclatura del fichero es correcta e informa de cualquier fallo.

        :return:
        """
        filename = QFileDialog.getOpenFileName(
            # self.el_parent, 'Open File', '', 'Images (*.png *.xpm *.jpg)',
            self.el_parent, 'Importar alumnos', '', 'Archivo de texto (*.txt)',
            None, QFileDialog.DontUseNativeDialog)
        try:
            fichero = open(filename[0], 'r')
            try:
                for i, linea in enumerate(fichero, 1):
                    # Por cada línea cargamos los datos necesarios
                    datos_alumno = linea.split(":")
                    datos_alumno = map(lambda s: s.strip(), datos_alumno)
                    # todo hacer alguna acción más estricta para comprobar los datos
                    # Seria ampliar el IF haciendo uan comprobación de cada dato para justificar que se ajusta
                    # a las necesidades de la aplicación.
                    if len(datos_alumno) == 4:
                        # Los datos son correctos
                        un_alumno = Alumno.Alumno(datos_alumno[0], datos_alumno[1], datos_alumno[2], datos_alumno[3])
                        if self.lista_alumnos.exite_alumno(un_alumno.dni_a) is None:
                            print "Se añade al alumno %s" % un_alumno.nombre_a
                            self.lista_alumnos.anadir(un_alumno)
                        else:
                            # todo seria conveniente añadir éstos en otra lista para mostrar un mensaje de alumnos repetidos
                            print "El alumno ya estaba en la lista, no se añade"
                    else:
                        # El fichero no es correcto
                        raise ErrorMalformedSource(i)
                print "Se han cargado correctamente los datos de los alumnos"
                # Dada la lista de alumnos generamos la tabla
                self.generar_tabla()
            except ErrorMalformedSource, e:
                print e
            finally:
                fichero.close()
        except (IOError, OSError) as e:
            print "Ha ocurrido un error al abrir el archivo: "
            print e
            # Por lo que pueda suceder. Deshabilitamos el botón de crear grupo.
            self.ventana.bCrear.setDisabled(True)

    def crear_un_grupo(self):
        """
        Abre la interfaz del nonbre del grupo y se dispone a crearlo

        :return:
        """
        if self.window_crear_grupo_nombre is None:
            self.window_crear_grupo_nombre = IU_CREAR_GRUPO_NOMBRE.CrearGrupoNombre \
                (self, self.iu_main, self.id_usuario, self.lista_alumnos, self.lista_grupos)
        self.window_crear_grupo_nombre.show()

    def generar_tabla(self):
        # Bloquemos las señales y vaciamos la tabla
        self.ventana.tAlumnos.blockSignals(True)
        # self.ventana.tAlumnos.clear()
        # Rellenamos la tabla
        tamano_lista = self.lista_alumnos.obtener_tamano_lista()
        # El lengh de los datos que me vienen
        self.ventana.tAlumnos.setRowCount(tamano_lista)
        for i in range(0, tamano_lista):
            # Rellenamos la tabla
            alumno = self.lista_alumnos.obtener_alumno(i)
            newitem = QTableWidgetItem(alumno.dni_a)
            self.ventana.tAlumnos.setItem(i, 0, newitem)
            newitem = QTableWidgetItem(alumno.nombre_a)
            self.ventana.tAlumnos.setItem(i, 1, newitem)
            newitem = QTableWidgetItem(alumno.apellido_a)
            self.ventana.tAlumnos.setItem(i, 2, newitem)
            newitem = QTableWidgetItem(alumno.email_a)
            self.ventana.tAlumnos.setItem(i, 3, newitem)
        self.ventana.tAlumnos.blockSignals(False)
        # Si no existen elementos, deshabilito los botones de eliminar y crear grupo
        # En caso contrario los habilito para poder crear el grupo
        if tamano_lista == 0:
            # Deshabilitamos los botones
            self.ventana.bCrear.setDisabled(True)
            self.ventana.bEliminar.setDisabled(True)
        else:
            # Habilitamos los botones
            self.ventana.bCrear.setDisabled(False)
            self.ventana.bEliminar.setDisabled(False)

    def closeEvent(self, evnt):
        if self.quiero_cerrar:
            super(CrearGrupo, self).closeEvent(evnt)
        else:
            evnt.ignore()

# Excepciones de control personalizadas
class ErrorMalformedSource(Exception):
    def __init__(self, p_valor):
        self.valor = p_valor

    def __str__(self):
        return "El fichero contiene una entrada inválida en la línea: " + str(self.valor)
