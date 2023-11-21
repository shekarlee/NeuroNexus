#function for taking input from user
def input_num():
	try:
		a=float(input("enter first number: "))
		b=float(input("enter second number: "))
		#calling operation function
		operation(a,b)
	except:
		print("-----invalid numbers-----,try again with correct numeric values")
		print()
		print("****************************************************************")
		input_num()
		
#function for performing specified operation
def operation(a,b):
	print("which operation do you want to do")
	operator=input("enter operator(+,-,*,/): ")
	#for addition
	if(operator=="+"):
		print(a,operator,b, "=",a+b)
		print("___________________________________________________")
		print()
		repeater() #CALLING FUNCTION
	#for subtraction
	elif(operator=="-"):
		print(a,operator,b,"=",a-b)
		print("___________________________________________________")
		print()
		repeater() #CALLING FUNCTION
	#for multiplication
	elif(operator=="*"):
		print(a,operator,b,"=",a*b)
		print("___________________________________________________")
		print()
		repeater()  #CALLING FUNCTION
	#for division
	elif(operator=="/"):
		if(b==0):
			print("-----divided by zero is not possible-----")
			print("-------try again-------")
			print()
			print("********************************************************")
			print() 
			input_num()
		else:
			print(a,operator,b,"=",a/b)
			print("___________________________________________________")
			print()
			repeater()  #CALLING FUNCTION
	else:
		print("-----invalid operator-----,try again with correct operator")
		print("*******************************************")
		operation(a,b)
	       
#function for continue or not the calculation
def repeater():
	repeat=input("do you want to do another calculation(y/n)")
	if(repeat=="y" or repeat=="Y"):
		input_num()
	elif(repeat=="n" or repeat=="N"):
		print("***EXIT***")
		return;
	else:
		print("-----invalid-----,try again")
		print("**********************************************")
		repeater()
#calling the input function(process starts from here)
print("***SIMPLE CALCULATOR***")
input_num()