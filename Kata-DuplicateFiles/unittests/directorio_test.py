import unittest
import tempfile
import os
from kata.ficheros import Directorio, Fichero

class DirectorioTest(unittest.TestCase):
    """
    Utiliza las herramientas paracrear directorios temporales del
    paquete tempfile
    """

    def setUp(self):
        self.nombre_fichero = "tmp"

    def creaDirectorio(self, nombre_directorio_temporal):
        directorio = Directorio(nombre_directorio_temporal)
        return directorio

    def creaFichero(self, nombre_directorio_temporal):
        f = open(nombre_directorio_temporal + "/" + self.nombre_fichero, "w")
        f.write("a")
        f.close()

    def creaDirectorioConUnFichero(self, tmp_dir):
        self.creaFichero(tmp_dir)
        directorio = self.creaDirectorio(tmp_dir)
        return directorio



    def test_ficheros_en_directorio_vacio_son_cero(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            directorio = self.creaDirectorio(tmp_dir)
            self.assertEqual(len(directorio.ficheros), 0)


    def test_ficheros_en_directorio_con_un_fichero_es_uno(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            directorio = self.creaDirectorioConUnFichero(tmp_dir)
            self.assertEqual(len(directorio.ficheros), 1)


    def test_cuando_borro_un_fichero_el_numero_de_ficheros_es_uno_menos(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            directorio = self.creaDirectorioConUnFichero(tmp_dir)

            directorio.borrafichero(Fichero(self.nombre_fichero))

            self.assertEqual(0, len(os.listdir(tmp_dir)))


    def test_cuando_recupero_un_fichero_tengo_su_nombre(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            directorio = self.creaDirectorioConUnFichero(tmp_dir)

            primer_fichero = directorio.ficheros[0]

            self.assertEqual(self.nombre_fichero, primer_fichero.nombre)


    def test_cuando_recupero_un_fichero_tengo_su_tamanyo(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            directorio = self.creaDirectorioConUnFichero(tmp_dir)
            primer_fichero = directorio.ficheros[0]

            self.assertEqual(1, primer_fichero.tamanyo)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()