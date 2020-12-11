while True:
	a=float(input('Type in your first number --> '))
	b=str(input('Type in your operator --> '))
	c=float(input('Type in your second number --> '))
	d=input('Is this what you want to calculate? '+str(a)+b+str(c)+' --> ')
	
	if d == "YES" or d == "yes" or d == "Yes":
		if b == "+":
			x=a+c
			print("The answer is --> "+str(x))
		elif b == "-":
			x=a-c
			print("The answer is --> "+str(x))
		elif b == "*" or b == ".":
			x=a*c
			print("The answer is --> "+str(x))
		elif b == "/" or b == ":":
			x=a/c
			print("The answer is --> "+str(x))
	else:
		print("Something got wrong! Please, try again!")