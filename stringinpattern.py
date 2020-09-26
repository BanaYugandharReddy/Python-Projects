str = input("Enter the string: ")
for i in range(0,len(str)):
	for j in range(0,i+1):
		print(str[j],end="")
	print()
