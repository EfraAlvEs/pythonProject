import sys
import json
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from interface import *
import mongoengine as db
import datetime
#clase del modelo, el api la interpreta para guardar los datos en sus campos
db.connect('IECA', host='localhost', port=27017)
class Post(db.Document):
    EstudianteID = db.IntField()
    Nombre = db.StringField(required=True, max_length=50)
    Apellido = db.StringField(required=True, max_length=50)
    Edad = db.StringField(required=True, max_length=50)
    Carrera = db.StringField(required=True, max_length=50)
    Fecha = db.DateTimeField(default=datetime.datetime.now)
    def to_json(self):
        return {
            "EstudianteID": self.EstudianteID,
            "Nombre": self.Nombre,
            "Apellido": self.Apellido,
            "Edad": self.Edad,
            "Carrera": self.Carrera,
            "Fecha": self.Fecha,
            "MemoriaID": str(self.pk)
        }
estudiante = Post(EstudianteID='1', Nombre='Efra', Apellido='Alvarado', Edad='25', Carrera='Mecatronica', Fecha=datetime.datetime.now)
estudiante.save()
estudiante = Post(EstudianteID= '2',Nombre= 'Alberto', Apellido= 'Hernandez', Edad= '27', Carrera='mecatronica',Fecha= datetime.datetime.now)
estudiante.save()
estudiante = Post(EstudianteID= '3',Nombre= 'Luciana', Apellido= 'Lopez', Edad= '21', Carrera='quimica',Fecha= datetime.datetime.now)
estudiante.save()
estudiante = Post(EstudianteID= '4',Nombre='Emilio', Apellido='Peña', Edad='25', Carrera='quimica',Fecha= datetime.datetime.now)
estudiante.save()
estudiante = Post(EstudianteID= '5',Nombre='Ana', Apellido='Perez', Edad='23', Carrera='sistemas',Fecha= datetime.datetime.now)
estudiante.save()
estudiante = Post(EstudianteID= '6',Nombre='Lorenzo', Apellido='Gutierrez', Edad='20', Carrera='mecatronica',Fecha= datetime.datetime.now)
estudiante.save()
class Dialog (QMainWindow):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.groupBox_actualizar.setEnabled(False)
        self.ui.ID_lineEdit.setEnabled(False)
        self.ui.nombre_lineEdit.setEnabled(False)
        self.ui.apellido_lineEdit.setEnabled(False)
        self.ui.edad_lineEdit.setEnabled(False)
        self.ui.carrera_lineEdit.setEnabled(False)
        self.ui.execute_Button.setEnabled(False)

        self.ui.comboBox.activated.connect(self.cambioDeSeleccion)
        self.ui.find_Button.clicked.connect(self.buscarEstudiante)
        self.ui.execute_Button.clicked.connect(self.ejecutarFuncion)

        self.estudiante = Post.objects

        self.seleccion = None

        self.resetText()
        self.lockText()
        self.unlockText()

    def lockText(self):
        self.ui.ID_lineEdit.setEnabled(False)
        self.ui.nombre_lineEdit.setEnabled(False)
        self.ui.apellido_lineEdit.setEnabled(False)
        self.ui.edad_lineEdit.setEnabled(False)
        self.ui.carrera_lineEdit.setEnabled(False)
        self.ui.execute_Button.setEnabled(False)

    def unlockText(self):
        self.ui.ID_lineEdit.setEnabled(True)
        self.ui.nombre_lineEdit.setEnabled(True)
        self.ui.apellido_lineEdit.setEnabled(True)
        self.ui.edad_lineEdit.setEnabled(True)
        self.ui.carrera_lineEdit.setEnabled(True)
        self.ui.execute_Button.setEnabled(True)

    def resetText(self):
        self.ui.IDfind_lineEdit.clear()
        self.ui.ID_lineEdit.clear()
        self.ui.nombre_lineEdit.clear()
        self.ui.apellido_lineEdit.clear()
        self.ui.edad_lineEdit.clear()
        self.ui.carrera_lineEdit.clear()

    def cambioDeSeleccion(self):
        self.seleccion = self.ui.comboBox.currentIndex()
        self.resetText()
        self.lockText()
        self.ui.groupBox_actualizar.setEnabled(True)
        print('seleccion',self.seleccion)

        if(self.seleccion == 1):
            self.ui.label_info.setText('Actualizar. Ingrese ID del estudiante y presione boton buscar')

        elif (self.seleccion==2):
            self.ui.label_info.setText('Leer. Ingrese ID del estudiante y presione boton buscar')

        elif (self.seleccion==3):
            self.ui.IDfind_lineEdit.setEnabled(False)
            self.ui.find_Button.setEnabled(False)
            self.unlockText()
            self.ui.label_info.setText('Escribir. Ingrese datos y presione boton para guardar')

        elif (self.seleccion==4):
            self.ui.label_info.setText('Eliminar. Ingrese ID del estudiante y presione boton buscar')

        elif (self.seleccion==5):
            self.ui.label_info.setText('Eliminar. Ingrese ID del estudiante y presione boton buscar')


        else:
            self.ui.label_info.setText('Seleccione una opcion')
            self.ui.groupBox_actualizar.setEnabled(False)
            self.resetText()

    def buscarEstudiante(self):
        self.estudiante = Post.objects(EstudianteID=int(self.ui.IDfind_lineEdit.text())).first()

        if (self.seleccion==1):
            self.unlockText()
            self.ui.label_info.setText('Ingrese los cambios y presione boton ejecutar')

        if (self.seleccion==2):
            self.ui.label_info.setText('Seleccione otra opcion o busque otro estudiante')

        if (self.seleccion==4):
            self.ui.label_info.setText('Confirme los datos y presione boton ejecutar para eliminar')
            self.ui.execute_Button.setEnabled(True)

        self.resetText()
        self.ui.nombre_lineEdit.insert((json.dumps(self.estudiante['Nombre'], sort_keys=True, indent=4)).replace("\"", ""))
        self.ui.ID_lineEdit.insert((json.dumps(self.estudiante['EstudianteID'], sort_keys=True, indent=4)).replace("\"", ""))
        self.ui.apellido_lineEdit.insert((json.dumps(self.estudiante['Apellido'], sort_keys=True, indent=4)).replace("\"", ""))
        self.ui.edad_lineEdit.insert((json.dumps(self.estudiante['Edad'], sort_keys=True, indent=4)).replace("\"", ""))
        self.ui.carrera_lineEdit.insert((json.dumps(self.estudiante['Carrera'], sort_keys=True, indent=4)).replace("\"", ""))

    def ejecutarFuncion(self):
        if (self.seleccion==1):
            self.estudiante.update(EstudianteID=self.ui.ID_lineEdit.text(), Nombre=self.ui.nombre_lineEdit.text(),
                                   Apellido=self.ui.apellido_lineEdit.text(), Edad=self.ui.edad_lineEdit.text(),
                                   Carrera=self.ui.carrera_lineEdit.text(), Fecha=datetime.datetime.now)
            self.ui.label_info.setText('Los cambios han sido aplicados')
            self.ui.groupBox_actualizar.setEnabled(False)
            self.ui.comboBox.setCurrentIndex(0)
            self.resetText()

        # [PV] Validar que el ID no exista
        elif (self.seleccion==3):
            self.estudiante = Post(EstudianteID=self.ui.ID_lineEdit.text(), Nombre=self.ui.nombre_lineEdit.text(),
                                   Apellido=self.ui.apellido_lineEdit.text(), Edad=self.ui.edad_lineEdit.text(),
                                   Carrera=self.ui.carrera_lineEdit.text(), Fecha=datetime.datetime.now)
            self.estudiante.save()
            self.ui.label_info.setText('El estudiante se ha agregado correctamente')
            self.ui.groupBox_actualizar.setEnabled(False)
            self.ui.comboBox.setCurrentIndex(0)
            self.ui.IDfind_lineEdit.setEnabled(True)
            self.ui.find_Button.setEnabled(True)
            self.resetText()

        elif(self.seleccion==4):
            self.estudiante.delete()
            self.ui.label_info.setText('Estudiante eliminado satisfactoriamente')
            self.ui.groupBox_actualizar.setEnabled(False)
            self.ui.comboBox.setCurrentIndex(0)
            self.resetText()

if __name__=='__main__':
    def iniciarInterface():
        app = QApplication(sys.argv)
        window = Dialog()
        window.show()
        sys.exit(app.exec_())
iniciarInterface()
