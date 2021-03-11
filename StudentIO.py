try:
    import cPickle as pickle
except ImportError:
    import pickle

class Estudiante(object):
    def __init__(self, _nombre, _apellido, _edad, _carrera):
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad= _edad
        self.carrera= _carrera
    def show(self):
        print(self.nombre,self.apellido,self.edad,self.carrera)

def save(list):
    file_to_store = open("database.db", "wb")
    pickle.dump(list, file_to_store)
    file_to_store.close()

# def save(list):
#     file_to_store = open("database.db", "wb")
#     pickle.dump(list, file_to_store)
#     file_to_store.close()

# [PV] Usando un nombre como parametro se puede buscar uobjeto especifico
def read():
    file_to_read = open("database.db", "rb")
    loaded_object = pickle.load(file_to_read)
    file_to_read.close()
    # print(loaded_object)

    # [PV] Imprimir los objetos de la lista
    print('\n')
    for estudiante in loaded_object:
        print(estudiante.nombre, estudiante.apellido, estudiante.edad, estudiante.carrera)

