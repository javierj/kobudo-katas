import os

class BorraFicheros(object):
    def _esFicheroRepetido(self, fichero):
        return fichero.tamanyo in self.ficheros_leidos

    def _nuevoFicheroEncontrado(self, fichero):
        self.ficheros_leidos[fichero.tamanyo] = fichero

    def borra_ficheros_en(self, directorio):
        self.ficheros_leidos = dict()
        for fichero in directorio.ficheros:
            if self._esFicheroRepetido(fichero):
                directorio.borrafichero(fichero)
            else:
                self._nuevoFicheroEncontrado(fichero)


class Directorio:
    def __init__(self, path =""):
        self.ficheros = list()
        self.path = path
        for fichero in os.listdir(path):
            self.ficheros.append(Fichero(fichero, os.path.getsize(self._rutacompleta(fichero))))

    def _rutacompleta(self, fichero):
        return self.path+"/" + str(fichero)

    def borrafichero(self, fichero):
        os.remove(self.path+"/" + fichero.nombre)


class Fichero:
    def __init__(self, nombre="", tamanyo = 0):
        self.nombre = nombre
        self.tamanyo = tamanyo
