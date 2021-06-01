import unittest
from leapyear import LeapCalc

class TestLeapYear(unittest.Testcase):
	
	def test_leap_div_4(self):
		self.assertTrue(LeapCalc(4))
		self.assertTrue(LeapCalc(2000))
		self.assertTrue(LeapCalc(2020))

if __name__ == '__main__':
	unittest.main()
