
import unittest
from unittest.mock import Mock
from kata.ficheros import BorraFicheros


class BorraFicheroTest(unittest.TestCase):

    def setUp(self):
        self.fichero_repetido = Mock()
        self.fichero_repetido.nombre = "fichero_repetido"
        self.fichero_repetido.tamanyo = 100

        self.borrado = BorraFicheros()


    def test_when_hayDosFicherosConElMismoTamanyo_then_borrarUnFichero(self):
        directorio = Mock()
        directorio.ficheros = [self.fichero_repetido, self.fichero_repetido]

        # Codigo de prueba
        self.borrado.borra_ficheros_en(directorio)

        # Assert
        directorio.borrafichero.assert_called_with(self.fichero_repetido)


    def test_when_hayTresFicherosConElMismoTamanyo_then_borrarDosFicheros(self):
        directorio = Mock()
        directorio.ficheros = [self.fichero_repetido,  self.fichero_repetido, self.fichero_repetido]

        # Codigo de prueba
        self.borrado.borra_ficheros_en(directorio)

        # Assert
        directorio.borrafichero.assert_called_with(self.fichero_repetido)
        self.assertEqual(directorio.borrafichero.call_count, 2)


    # Esta prueba no me lleva a escrbir nuevo codigo
    def test_when_hayTresFicheros_y_dosConElMismoTamanyo_then_borrarUnFichero(self):
        fichero_no_repetido = Mock()
        fichero_no_repetido.nombre = "fichero_no_repetido"
        fichero_no_repetido.tamanyo = 50

        directorio = Mock()
        directorio.ficheros = [self.fichero_repetido,  fichero_no_repetido, self.fichero_repetido]

        # Codigo de prueba
        self.borrado.borra_ficheros_en(directorio)

        # Assert
        directorio.borrafichero.assert_called_with(self.fichero_repetido)


if __name__ == "__main__":
    unittest.main()