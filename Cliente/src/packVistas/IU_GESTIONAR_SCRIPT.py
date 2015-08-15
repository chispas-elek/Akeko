# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Cliente.src.packControladoras import CGestionarScript
from Cliente.src.packModelo import ListaScript, ListaTag
import collections


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
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lScripsTag = QtWidgets.QLabel(self.groupBox)
        self.lScripsTag.setText("")
        self.lScripsTag.setObjectName("lScripsTag")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lScripsTag)
        self.lNombre.raise_()
        self.label_7.raise_()
        self.lDescripcion.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.lScripsTag.raise_()
        self.verticalLayout.addWidget(self.groupBox)
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
        self.listAplicados.setToolTip(_translate("Form", "Scripts aplicados en el grupo o que se desean aplicar."))
        self.listAplicados.setWhatsThis(_translate("Form",
                                                   "En ésta lista se muestran los Scripts/Tags que se desean aplicar al grupo. Los Tags son representados por una estrella mientras que los Scripts son representados con una almohadilla."))
        self.listDisponibles.setToolTip(_translate("Form", "Scripts disponibles para el usuario."))
        self.listDisponibles.setWhatsThis(_translate("Form",
                                                     "En ésta lista, se contienen todos los Scripts/Tags que posee el usuario para poder insertar en el grupo. Los Tags y los scripts son diferenciados por dos iconos. Un Tag contiene una estrella de favorito mientras un Script contiene una almohadilla."))
        self.label_3.setText(_translate("Form", "Aplicados"))
        self.bEliminar.setToolTip(_translate("Form", "Eliminar un elemento del grupo"))
        self.bEliminar.setText(_translate("Form", "Eliminar"))
        self.bAnadir.setToolTip(_translate("Form", "Añadir un elemento al grupo"))
        self.bAnadir.setText(_translate("Form", "Añadir"))
        self.groupBox.setTitle(_translate("Form", "Información Avanzada"))
        self.label_5.setToolTip(_translate("Form", "Nombre del elemento seleccionado"))
        self.label_5.setText(_translate("Form", "- Nombre:"))
        self.label_7.setToolTip(_translate("Form", "Descripción del elemento seleccionado."))
        self.label_7.setWhatsThis(_translate("Form",
                                             "Todo Script y Tag vienen asociados a una descripción que indican qué hacen exáctamente."))
        self.label_7.setText(_translate("Form", "- Descripción:"))
        self.label.setToolTip(_translate("Form", "Muestra los scripts que contiene un Tag."))
        self.label.setWhatsThis(_translate("Form",
                                           "Si se pulsa sobre un Tag. Ésta lista se rellenará mostrando qué scripts forman el Tag seleccionado. Si se pulsa un Script no ocurrirá nada."))
        self.label.setText(_translate("Form", "-Scrips del Tag:"))
        self.bAplicar.setToolTip(_translate("Form", "Aplica los cambios deseados"))
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
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        # Parámetros adicionales para los listWidget
        self.ventana.listDisponibles.setSortingEnabled(True)
        self.ventana.listAplicados.setSortingEnabled(True)

        # Inicialización de los datos necesarrios
        self.id_usuario = p_id_usuario
        self.lista_alumnos = p_lista_alumnos
        self.id_grupo = p_id_grupo
        self.scripts_aplicados = None
        self.tags_aplicados = None
        self.scripts_disponibles = None
        self.tags_disponibles = None

        self.controlador_gestionar_script = CGestionarScript.CGestionarScript()

        # Cargamos los datos de las listas
        self._cargar_datos()
        # Guardamos una copia de los elementos que contienen las listas de forma original para observar cambios
        self.lista_disponibles_previa = self.ventana.listDisponibles.findItems \
            ("*", QtCore.Qt.MatchWrap | QtCore.Qt.MatchWildcard)
        self.lista_aplicados_previa = self.ventana.listAplicados.findItems \
            ("*", QtCore.Qt.MatchWrap | QtCore.Qt.MatchWildcard)

        # Programamos los botones
        self.ventana.bCerrar.clicked.connect(self.close)
        self.ventana.bAnadir.clicked.connect(self.anadir_un_elemento)
        self.ventana.bEliminar.clicked.connect(self.eliminar_un_elemento)
        self.ventana.listDisponibles.clicked.connect(self.imprimir_info_disponible)
        self.ventana.listAplicados.clicked.connect(self.imprimir_info_aplicado)
        self.ventana.bAplicar.clicked.connect(self.aplicar_cambios)

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
        self.scripts_aplicados = self.controlador_gestionar_script.obtener_scripts(self.id_grupo)
        self.tags_aplicados = self.controlador_gestionar_script.obtener_tags(self.id_grupo)
        self.scripts_disponibles = self.controlador_gestionar_script.obtener_scripts_disponibles(self.id_grupo)
        self.tags_disponibles = self.controlador_gestionar_script.obtener_tags_disponibles(self.id_grupo, self.id_usuario)
        # Una ve obtenidos todos los datos, rellenamos las tablas
        # Primero vamos a rellenear los tags
        self.tags_disponibles.cargar_lista_tag(self.ventana.listDisponibles)
        self.tags_aplicados.cargar_lista_tag(self.ventana.listAplicados)
        # Ahora rellenamos los scripts disponibles
        self.scripts_disponibles.cargar_lista_script(self.ventana.listDisponibles)
        self.scripts_aplicados.cargar_lista_script(self.ventana.listAplicados)
        # Libreamos las señales
        self.ventana.listAplicados.blockSignals(False)
        self.ventana.listDisponibles.blockSignals(False)

    def anadir_un_elemento(self):
        """
        Añade un elemento de la lista de Disponibles, a la lista de Aplicados

        :return:
        """
        # Obtenemos la posición de la lista del scripts pulsado
        posicion_selec = self.ventana.listDisponibles.currentRow()
        if posicion_selec != -1:
            # Obtenemos el item y lo eliminamos de la lista de forma automática
            item_selec = self.ventana.listDisponibles.takeItem(posicion_selec)
            # Cambia el color de las letras del item.
            item_selec.setForeground(QtGui.QColor(102, 204, 0))
            self.ventana.listAplicados.addItem(item_selec)
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
        Eliminamos un elemento de la lista de Disponibles

        :return:
        """
        # Obtenemos la posición de la lista del scripts pulsado
        posicion_selec = self.ventana.listAplicados.currentRow()
        if posicion_selec != -1:
            # Obtenemos el item y lo eliminamos de la lista de forma automática
            item_selec = self.ventana.listAplicados.takeItem(posicion_selec)
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
        """
        Al pulsar sobre un Tag o un script. Rellena la información relativa sobre éste.

        :return:
        """
        # Obtener los datos del item
        item_seleccionado = self.ventana.listDisponibles.currentItem()
        self._mostrar_informacion(item_seleccionado)

    def imprimir_info_aplicado(self):
        """
        Al pulsar sobre un Tag o un script. Rellena la información relativa sobre éste.

        :return:
        """
        item_seleccionado = self.ventana.listAplicados.currentItem()
        self._mostrar_informacion(item_seleccionado)

    def _mostrar_informacion(self, p_item_seleccionado):
        # Obtenemos el objeto que contiene el item
        item_seleccionado_datos = p_item_seleccionado.data(QtCore.Qt.UserRole)
        # Miramos que tipo de objeto es.
        if item_seleccionado_datos[0] == "tag":
            tag = item_seleccionado_datos[1]
            self.ventana.lNombre.setText(tag.nombre_tag)
            self.ventana.lDescripcion.setText(tag.descripcion)
            # Obtenemos los scripts que pertenecen al TAG
            lista_scripts_tag_seleccionado = self.controlador_gestionar_script.obtener_scripts_tag(tag.id_tag)
            # Emviamos el elemento y seteamos los valores
            lista_scripts_tag_seleccionado.imprimir_elementos_iu(self.ventana.lScripsTag)
        else:
            script = item_seleccionado_datos[1]
            self.ventana.lNombre.setText(script.nombre_s)
            self.ventana.lDescripcion.setText(script.descripcion)
            self.ventana.lScripsTag.setText(" ---- ")

    def aplicar_cambios(self):
        """
        Aplica los scrips/tags que el usuario haya seleccionado. Agregando los que estén en la lista de aplicados y
        eliminando los que estén en la lista de disponibles.

        :return:
        """
        # Mostramos una ventana preguntando si desea o no hacer la acción
        warm_box = QMessageBox()
        warm_box.setIcon(2)
        warm_box.setWindowTitle("Aplicar cambios")
        warm_box.setText("¡¡Atención!!")
        warm_box.setInformativeText("¿Estás seguro de querer aplicar los cambios realizados?")
        warm_box.setDetailedText("Al pulsar aceptar, el sistema eliminará los scripts que haya puesto en la columna "
                                 "de disponibles y agregará como nuevos scripts aquellos que haya dejado en la "
                                 "columna de aplicados.")
        # Creamos los botones de aceptar y cancelar.
        warm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        warm_box.setDefaultButton(QMessageBox.Cancel)
        # Ejectuamos la interfaz y recogemos el resultado de la decisión
        seleccion = warm_box.exec_()
        if seleccion == QMessageBox.Ok:
            # Vamos a obtener los elementos actuales que existan en ambos QWidetList y los vamos a comprara
            # Con los anteriores
            comparar = lambda x, y: collections.Counter(x) == collections.Counter(y)
            lista_disponibles_actual = self.ventana.listDisponibles.findItems \
                ("*", QtCore.Qt.MatchWrap | QtCore.Qt.MatchWildcard)
            lista_aplicados_actual = self.ventana.listAplicados.findItems \
                ("*", QtCore.Qt.MatchWrap | QtCore.Qt.MatchWildcard)
            if comparar(lista_disponibles_actual, self.lista_disponibles_previa) is not True and \
                            comparar(lista_aplicados_actual, self.lista_aplicados_previa) is not True:
                # Las listas son diferentes, por lo que ha habido cambios. Llamamos al controlador
                print "Listas distintas, llamamos al controlador"
                resultado = self.controlador_gestionar_script.aplicar_cambios(self.id_usuario, self.id_grupo,
                                                                              self.lista_alumnos,
                                                                              self.lista_disponibles_previa,
                                                                              lista_disponibles_actual,
                                                                              self.lista_aplicados_previa,
                                                                              lista_aplicados_actual)
                if resultado:
                    # las cosas han ido bien, podemos mostrar una ventana
                    msg_box = QMessageBox()
                    msg_box.setIcon(1)
                    msg_box.setWindowTitle("Aplicar cambios")
                    msg_box.setText("CORRECTO")
                    msg_box.setInformativeText("Los cambios se han aplicado correctamente en el sistema")
                    msg_box.exec_()
                    self.close()
                else:
                    # Algo ha pasado, reproducimos el error
                    error_box = QMessageBox()
                    error_box.setIcon(3)
                    error_box.setWindowTitle("Aplicar cambios")
                    error_box.setText("ERROR")
                    error_box.setInformativeText("Ha ocurrido algún problema a la hora de aplicar los cambios. "
                                                 "Por favor, reinténtalo de nuevo.")
                    error_box.exec_()
            else:
                # Las listas son iguales y el usuario no ha movido ningún elemento
                info_box = QMessageBox()
                info_box.setIcon(1)
                info_box.setWindowTitle("Aplicar cambios")
                info_box.setText("INFORMACIÓN")
                info_box.setInformativeText("Parece que no has hecho ningún cambio. "
                                            "Haz primero cambios antes de aplicar")
                info_box.exec_()
