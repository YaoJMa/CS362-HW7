def FizzBuzz(num=100):
	for i in range(num):
		if(i%3==0):
			print("fizz")
		
		elif(i%5==0):
			print("buzz")
		else: 
			print(i)
FizzBuzz()
