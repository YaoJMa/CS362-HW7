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

if __name__ == '__main__':
	unittest.main()
