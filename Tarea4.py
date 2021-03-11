import mongoengine as db
import datetime
# #Crear base de datos nombre test
db.connect('IECA', host='localhost', port=27017)
#clase del modelo, el api la interpreta para guardar los datos en sus campos
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


if __name__ == '__main__':
    # print('Base de datos IECA se ha creado.',db)
    # estudiante = Post(EstudianteID= '1',Nombre= 'Efra',Apellido= 'Alvarado',Edad= '25',Carrera= 'Mecatronica',Fecha= datetime.datetime.now)
    # estudiante.save()
    # estudiante = Post(EstudianteID= '2',Nombre= 'Alberto', Apellido= 'Hernandez', Edad= '27', Carrera='mecatronica',Fecha= datetime.datetime.now)
    # estudiante.save()
    # estudiante = Post(EstudianteID= '3',Nombre= 'Luciana', Apellido= 'Lopez', Edad= '21', Carrera='quimica',Fecha= datetime.datetime.now)
    # estudiante.save()
    # estudiante = Post(EstudianteID= '4',Nombre='Emilio', Apellido='Peña', Edad='25', Carrera='quimica',Fecha= datetime.datetime.now)
    # estudiante.save()
    # estudiante = Post(EstudianteID= '5',Nombre='Ana', Apellido='Perez', Edad='23', Carrera='sistemas',Fecha= datetime.datetime.now)
    # estudiante.save()
    # estudiante = Post(EstudianteID= '6',Nombre='Lorenzo', Apellido='Gutierrez', Edad='20', Carrera='mecatronica',Fecha= datetime.datetime.now)
    # estudiante.save()

# [PV] Hacia falta la indentacion
    print('\nBienvenido al menu de seleccion!')
    State =True
    while State:
        print('\nSeleccione un opcion'
              '   Actualizar estudiante = 0'
              '   Leer estudiantes = 1'
              '   Escribir estudiante = 2'
              '   Eliminar estudiante = 3'
              '   Borrar y Salir = 4')
        opciones = ['Actualizar', 'Leer', 'Escribir', 'Eliminar', 'Salir y eliminar base de datos']
        seleccion = int(input("Ingresa numero:"))
        tuseleccion = opciones[seleccion]
        print('\nHas elegido', tuseleccion)
        if seleccion==0:
            print('Seleccione ID del estudiante que desea actualizar:')
            seleccionest = int(input("Ingresa numero:"))
            estudiante = Post.objects(EstudianteID=seleccionest).first()
            print('\nTu seleccion es:', estudiante.to_json())
            print('Ingrese los nuevos valores para cada campo:')
            EstudianteIDtemp = int(input("Ingresa numero de ID:"))
            Nombretemp = str(input("Ingresa nuevo Nombre:"))
            Apellidotemp = str(input("Ingresa nuevo Apellido:"))
            Edadtemp = str(input("Ingresa nueva Edad:"))
            Carreratemp = str(input("Ingresa nueva Carrera:"))
            estudiante.update(EstudianteID=EstudianteIDtemp, Nombre=Nombretemp, Apellido=Apellidotemp, Edad=Edadtemp,
                              Carrera=Carreratemp, Fecha=datetime.datetime.now)
            estudiante = Post.objects(EstudianteID=EstudianteIDtemp).first()
            print('\nTus cambios:', estudiante.to_json())

        elif seleccion==1:
            estudiantes = []
            for estudiante in Post.objects():
                estudiantes.append(estudiante.to_json())
            print('Tus estudiantes:')
            for x in estudiantes:
                print(x)

        elif seleccion==2:
            print('Ingrese los nuevos valores para el nuevo estudiante:')
            EstudianteIDtemp = int(input("Ingresa numero de ID:"))
            Nombretemp = str(input("Ingresa nuevo Nombre:"))
            Apellidotemp = str(input("Ingresa nuevo Apellido:"))
            Edadtemp = str(input("Ingresa nueva Edad:"))
            Carreratemp = str(input("Ingresa nueva Carrera:"))
            estudiante = Post(EstudianteID=EstudianteIDtemp, Nombre=Nombretemp, Apellido=Apellidotemp, Edad=Edadtemp,
                              Carrera=Carreratemp, Fecha=datetime.datetime.now)
            estudiante.save()
            print('\nTu nuevo estudiante es:\n', estudiante.to_json())

        elif seleccion==3:
            print('Seleccione ID del estudiante que desea eliminar:')
            seleccionest = int(input("Ingresa numero:"))
            estudiante = Post.objects(EstudianteID=seleccionest).first()
            print('\nTu seleccion:', estudiante.to_json())
            estudiante.delete()
            print('Ha sido eliminado, documentos restantes:', Post.objects.count())

        elif seleccion==4:
            for estudiante in Post.objects():
                estudiante.delete()
            print('\nDocumentos restantes:', Post.objects.count())
            print('\nPrograma Finalizado, Gracias.')
            State=None
        else:
           print("\n Not Valid Choice Try again")
