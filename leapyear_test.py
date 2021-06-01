import unittest
from leapyear import LeapCalc

class TestLeapYear(unittest.Testcase):
	
	def test_leap_div_4(self):
		self.assertTrue(LeapCalc(4))
		self.assertTrue(LeapCalc(1600))
		self.assertTrue(LeapCalc(2020))

	def test_not_leap_div_100(self):
		self.assertFalse(LeapCalc(1800))
		self.assertFalse(LeapCalc(1900))
		self.assertFalse(LeapCalc(2500))

	def test_leap_div_400(self):
		self.assertTrue(LeapCalc(2000))
		self.assertTrue(LeapCalc(2800))

if __name__ == '__main__':
	unittest.main()
