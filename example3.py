# num1
num1 = int(input("Enter a number: "))

while True:
	num2 = int(input("Enter a number to compare: "))
	if num2 > num1:
		break
	else:
		print("number too small")

print("congraturation")