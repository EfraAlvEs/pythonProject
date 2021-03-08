# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(405, 432)
        self.groupBox_actualizar = QGroupBox(Dialog)
        self.groupBox_actualizar.setObjectName(u"groupBox_actualizar")
        self.groupBox_actualizar.setGeometry(QRect(10, 100, 381, 321))
        self.layoutWidget = QWidget(self.groupBox_actualizar)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 50, 351, 201))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.IDfind_lineEdit = QLineEdit(self.layoutWidget)
        self.IDfind_lineEdit.setObjectName(u"IDfind_lineEdit")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.IDfind_lineEdit)

        self.find_Button = QPushButton(self.layoutWidget)
        self.find_Button.setObjectName(u"find_Button")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.find_Button)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.ID_lineEdit = QLineEdit(self.layoutWidget)
        self.ID_lineEdit.setObjectName(u"ID_lineEdit")
        self.ID_lineEdit.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ID_lineEdit)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.nombre_lineEdit = QLineEdit(self.layoutWidget)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")
        self.nombre_lineEdit.setEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.nombre_lineEdit)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.apellido_lineEdit = QLineEdit(self.layoutWidget)
        self.apellido_lineEdit.setObjectName(u"apellido_lineEdit")
        self.apellido_lineEdit.setEnabled(False)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.apellido_lineEdit)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_6)

        self.edad_lineEdit = QLineEdit(self.layoutWidget)
        self.edad_lineEdit.setObjectName(u"edad_lineEdit")
        self.edad_lineEdit.setEnabled(False)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.edad_lineEdit)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_7)

        self.carrera_lineEdit = QLineEdit(self.layoutWidget)
        self.carrera_lineEdit.setObjectName(u"carrera_lineEdit")
        self.carrera_lineEdit.setEnabled(False)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.carrera_lineEdit)

        self.label_info = QLabel(self.groupBox_actualizar)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(20, 15, 341, 31))
        self.execute_Button = QPushButton(self.groupBox_actualizar)
        self.execute_Button.setObjectName(u"execute_Button")
        self.execute_Button.setEnabled(False)
        self.execute_Button.setGeometry(QRect(170, 260, 191, 51))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 381, 81))
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(19, 20, 351, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, 5)
        self.comboBox = QComboBox(self.horizontalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_actualizar.setTitle(QCoreApplication.translate("Dialog", u"Estudiantes", None))
        self.IDfind_lineEdit.setText("")
        self.find_Button.setText(QCoreApplication.translate("Dialog", u"Buscar", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Numero de ID:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Apellido:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Edad:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Carrera:", None))
        self.label_info.setText(QCoreApplication.translate("Dialog", u"Bienvenido", None))
        self.execute_Button.setText(QCoreApplication.translate("Dialog", u"Ejecutar", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Seleccion", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Seleccione Opcion", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Actualizar", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Leer", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Escribir", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"Eliminar", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"Salir", None))

    # retranslateUi

