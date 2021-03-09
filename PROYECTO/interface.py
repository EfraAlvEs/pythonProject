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
        Dialog.resize(407, 409)
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 100, 381, 191))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 341, 111))
        self.formLayout_3 = QFormLayout(self.layoutWidget)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(10)
        self.formLayout_3.setVerticalSpacing(13)
        self.formLayout_3.setContentsMargins(10, 10, 10, 10)
        self.correo_label = QLabel(self.layoutWidget)
        self.correo_label.setObjectName(u"correo_label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.correo_label)

        self.contrasena_label = QLabel(self.layoutWidget)
        self.contrasena_label.setObjectName(u"contrasena_label")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.contrasena_label)

        self.nombre_label = QLabel(self.layoutWidget)
        self.nombre_label.setObjectName(u"nombre_label")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.nombre_label)

        self.correo_lineEdit = QLineEdit(self.layoutWidget)
        self.correo_lineEdit.setObjectName(u"correo_lineEdit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.correo_lineEdit)

        self.contrasena_lineEdit = QLineEdit(self.layoutWidget)
        self.contrasena_lineEdit.setObjectName(u"contrasena_lineEdit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.contrasena_lineEdit)

        self.nombre_lineEdit = QLineEdit(self.layoutWidget)
        self.nombre_lineEdit.setObjectName(u"nombre_lineEdit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.nombre_lineEdit)

        self.enviarEstudiante_Button = QPushButton(self.groupBox_2)
        self.enviarEstudiante_Button.setObjectName(u"enviarEstudiante_Button")
        self.enviarEstudiante_Button.setGeometry(QRect(60, 140, 268, 41))
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(10, 300, 381, 71))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 20, 341, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.enviarArchivo_Button = QPushButton(self.horizontalLayoutWidget_2)
        self.enviarArchivo_Button.setObjectName(u"enviarArchivo_Button")

        self.horizontalLayout.addWidget(self.enviarArchivo_Button)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 381, 81))
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 20, 361, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 5, 10, 5)
        self.connect_Button = QPushButton(self.horizontalLayoutWidget)
        self.connect_Button.setObjectName(u"connect_Button")

        self.horizontalLayout_2.addWidget(self.connect_Button)

        self.serverIP_line = QLineEdit(self.horizontalLayoutWidget)
        self.serverIP_line.setObjectName(u"serverIP_line")
        self.serverIP_line.setEnabled(True)
        self.serverIP_line.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.serverIP_line)

        self.serverPort_line = QLineEdit(self.horizontalLayoutWidget)
        self.serverPort_line.setObjectName(u"serverPort_line")
        self.serverPort_line.setEnabled(True)
        self.serverPort_line.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.serverPort_line)

        self.disconnect_Button = QPushButton(self.horizontalLayoutWidget)
        self.disconnect_Button.setObjectName(u"disconnect_Button")
        self.disconnect_Button.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.disconnect_Button)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Estudiantes", None))
        self.correo_label.setText(QCoreApplication.translate("Dialog", u"Correo:", None))
        self.contrasena_label.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a:", None))
        self.nombre_label.setText(QCoreApplication.translate("Dialog", u"Nombre:", None))
        self.correo_lineEdit.setText(QCoreApplication.translate("Dialog", u"eg-alvarado@hotmail.com", None))
        self.contrasena_lineEdit.setText(QCoreApplication.translate("Dialog", u"glkgjl76587", None))
        self.nombre_lineEdit.setText(QCoreApplication.translate("Dialog", u"Efrain Alvarado", None))
        self.enviarEstudiante_Button.setText(QCoreApplication.translate("Dialog", u"Enviar Estudiante", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"Archivo", None))
        self.enviarArchivo_Button.setText(QCoreApplication.translate("Dialog", u"Enviar Archivo", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Servidor", None))
        self.connect_Button.setText(QCoreApplication.translate("Dialog", u"Conectar", None))
        self.serverIP_line.setText(QCoreApplication.translate("Dialog", u"3.16.226.150", None))
        self.serverPort_line.setText(QCoreApplication.translate("Dialog", u"9997", None))
        self.disconnect_Button.setText(QCoreApplication.translate("Dialog", u"Desconectar", None))
    # retranslateUi

