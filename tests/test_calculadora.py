import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    # --- Operaciones basicas ---
    def test_sumar(self):
        self.assertEqual(self.calc.sumar(2, 3), 5)

    def test_restar(self):
        self.assertEqual(self.calc.restar(10, 4), 6)

    def test_multiplicar(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)

    def test_dividir_entre_cero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    # --- es_par ---
    def test_es_par_true(self):
        self.assertTrue(self.calc.es_par(4))

    # --- Pruebas adicionales ---
    def test_potencia_positiva(self):
        self.assertEqual(self.calc.potencia(2, 3), 8)

    def test_potencia_negativa(self):
        with self.assertRaises(ValueError):
            self.calc.potencia(5, -1)

    def test_es_par_impar(self):
        self.assertFalse(self.calc.es_par(7))

    def test_factorial_positivo(self):
        self.assertEqual(self.calc.factorial(5), 120)

    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

    def test_promedio_valido(self):
        self.assertEqual(self.calc.promedio([10, 20, 30]), 20)

    def test_promedio_vacio(self):
        with self.assertRaises(ValueError):
            self.calc.promedio([])

    def test_maximo_valido(self):
        self.assertEqual(self.calc.maximo([3, 7, 1, 9]), 9)

    def test_maximo_vacio(self):
        with self.assertRaises(ValueError):
            self.calc.maximo([])

    def test_clasificar_nota(self):
        self.assertEqual(self.calc.clasificar_nota(19), "Excelente")
        self.assertEqual(self.calc.clasificar_nota(16), "Bueno")
        self.assertEqual(self.calc.clasificar_nota(12), "Aprobado")
        self.assertEqual(self.calc.clasificar_nota(5), "Desaprobado")

    def test_clasificar_nota_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            self.calc.clasificar_nota(-1)
        with self.assertRaises(ValueError):
            self.calc.clasificar_nota(21)

if __name__ == "__main__":
    unittest.main()