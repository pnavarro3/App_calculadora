import unittest
from operaciones import suma, resta, multiplicacion, division


class TestOperaciones(unittest.TestCase):
	def test_suma_enteros(self):
		self.assertEqual(suma(2, 3), 5.0)

	def test_suma_strings(self):
		self.assertAlmostEqual(suma('1.5', '2.25'), 3.75)

	def test_resta(self):
		self.assertAlmostEqual(resta('5.5', '2.2'), 3.3, places=6)

	def test_multiplicacion(self):
		self.assertEqual(multiplicacion(3, 4), 12.0)

	def test_division(self):
		self.assertEqual(division(7, 2), 3.5)

	def test_division_por_cero_lanza_error(self):
		with self.assertRaises(ValueError):
			division(1, 0)

	def test_entradas_no_numericas_lanzan_valueerror(self):
		with self.assertRaises(ValueError):
			suma('a', 2)
		with self.assertRaises(ValueError):
			resta(1, 'b')
		with self.assertRaises(ValueError):
			multiplicacion('x', 'y')
		with self.assertRaises(ValueError):
			division('foo', 'bar')


if __name__ == '__main__':
	unittest.main()

