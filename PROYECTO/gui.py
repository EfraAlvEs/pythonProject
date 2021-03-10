import socket
import pickle
import sys
from interface import *
from estudiante import Estudiante

class Dialog(QMainWindow):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # bloquear grupos
        self.ui.groupBox_2.setEnabled(False)
        self.ui.groupBox_3.setEnabled(False)

        # funciones servidor
        self.ui.connect_Button.clicked.connect(self.botonConectar)
        self.ui.disconnect_Button.clicked.connect(self.botonDesconectar)

        # funciones enviar
        self.ui.enviarEstudiante_Button.clicked.connect(self.bontonEnviarEstudiantePresionado)
        self.ui.enviarArchivo_Button.clicked.connect(self.bontonEnviarArchivoPresionado)


    def botonConectar(self):
        self.s = socket.socket()
        self.s.connect((self.ui.serverIP_line.text(),int(self.ui.serverPort_line.text())))
        # bloquear botone conectar y habilitar desconectar
        self.ui.connect_Button.setEnabled(False)
        self.ui.disconnect_Button.setEnabled(True)
        self.ui.serverIP_line.setEnabled(False)
        self.ui.serverPort_line.setEnabled(False)
        # habilitar grupo estudiante
        self.ui.groupBox_2.setEnabled(True)
        # reset estudiante group
        # self.ui.nombre_lineEdit.clear()
        # self.ui.contrasena_lineEdit.clear()
        # self.ui.correo_lineEdit.clear()
        self.ui.enviarEstudiante_Button.setText('Enviar Estudiante')
        self.ui.enviarArchivo_Button.setText('Enviar Archivo')

    def botonDesconectar(self):
        self.s.close()
        # bloquear botone desconectar y habilitar conectar
        self.ui.connect_Button.setEnabled(True)
        self.ui.disconnect_Button.setEnabled(False)
        self.ui.serverIP_line.setEnabled(True)
        self.ui.serverPort_line.setEnabled(True)

    def bontonEnviarEstudiantePresionado(self):
        print('Se ha presionado boton enviar estudiante')
        # copiar datos y serializar
        estudiante = Estudiante(self.ui.nombre_lineEdit.text(),self.ui.correo_lineEdit.text(), self.ui.contrasena_lineEdit.text())
        estudiante_seriado = pickle.dumps(estudiante)
        # enviar objeto serializado e imprimir retorno en boton
        self.s.send(estudiante_seriado)
        res = self.s.recv(1024)
        self.ui.enviarEstudiante_Button.setText(res.decode())
        # Bloquear grupo y desbloquear 3
        self.ui.groupBox_2.setEnabled(False)
        self.ui.groupBox_3.setEnabled(True)

    def bontonEnviarArchivoPresionado(self):
        print('Se ha presionado boton enviar archivo')
        file = open('PROYECTO.zip', 'rb')
        zip_serializado = pickle.dumps(file.read())

        self.s.send(b'INI')
        res = self.s.recv(1024)
        print(res.decode())

        continuar = True
        inicio = 0
        while continuar:
            chunk =  zip_serializado[inicio:inicio + 1024]
            if not chunk:
                    continuar = False
                    continue
            self.s.send(chunk)
            res = self.s.recv(1024)
            print(res.decode())
            inicio += 1024

        self.s.send(b'FIN')
        res = self.s.recv(1024)
        print(res.decode())

        res = self.s.recv(1024)
        print(res.decode())

        self.ui.groupBox_3.setEnabled(False)
        self.ui.enviarArchivo_Button.setText(res.decode())

    def bontonDesconectarPresionado(self):
        print('Se ha presionado boton desconectar')

if __name__=='__main__':
    app = QApplication(sys.argv)
    # window=QMainWindow()
    window = Dialog()
    window.show()
    sys.exit(app.exec_())