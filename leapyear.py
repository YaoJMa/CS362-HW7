def LeapCalc(year):
	if year%4 == 0 and (year%100 != 0 or year%100 == 0):
		return True
	return False 
LeapCalc()
