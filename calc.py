import sys
m = 0
for  m in range (sys.maxsize):
	print("Press CTRL+C to quit")
	i = input("st number - ")
	j = input("nd number - ")
	k = input("operation - ")

	if str(k) == "*":
		print(int(i) * int(j))
	elif str(k) == '+':
		print(int(i) + int(j))
	elif str(k) == '-':
		print(int(i) - int(j))
	elif str(k) == '/':
		print(float(i) / float(j))	
	else:
		print("only '+' '-' '*' '/' are valid operations")
	m += m
print("Restart program")

