from StudentIO import Estudiante
from StudentIO import save
from StudentIO import read

listaEstudiantes=[]
estudiante=Estudiante("Alberto","Hernandez","27","mecatronica")
listaEstudiantes.append(estudiante)
estudiante=Estudiante("Luciana","Lopez","21","quimica")
listaEstudiantes.append(estudiante)
estudiante=Estudiante("Emilio","Peña","25","quimica")
listaEstudiantes.append(estudiante)
estudiante=Estudiante("Ana","Perez","23","sistemas")
listaEstudiantes.append(estudiante)
estudiante=Estudiante("Lorenzo","Gutierrez","20","mecatronica")
listaEstudiantes.append(estudiante)

for estudiante in listaEstudiantes:
    estudiante.show()
save(listaEstudiantes)
read()
