import unittest
import calculator


class TestCalculator(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calculator.add(5, 4), 9)
		self.assertEqual(calculator.add(-5, 4), -1)
		self.assertEqual(calculator.add(-5, -5), -10)


	def test_multiply(self):
		self.assertEqual(calculator.multiply(5, 4), 20)
		self.assertEqual(calculator.multiply(-5, 4), -20)
		self.assertEqual(calculator.multiply(-5, -4), 20)

	def test_modulus(self):
		self.assertIsNot(calculator.modulus(10, 3), 10)
		self.assertIsNot(calculator.modulus(5, 3), 12)
		self.assertIsNot(calculator.modulus(-10, 4), 3)


	if __name__ == '__main__':
		unittest.main()



