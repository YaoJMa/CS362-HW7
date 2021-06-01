import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.Testcase):
	
	def test_return_num(self):
		self.assertEqual(FizzBuzz(1), 1)
		self.assertEqual(FizzBuzz(2), 2)
		self.assertEqual(FizzBuzz(3), 4)

	def test_mult_3_return_fizz(self):
		self.assertEqual(FizzBuzz(3), "fizz")
		self.assertEqual(FizzBuzz(6), "fizz")

	def test_mult_5_return_buzz(self):
		self.assertEqual(FizzBuzz(5), "buzz")
		self.assertEqual(FizzBuzz(10), "buzz")

if __name__ == '__main__':
	unittest.main()
