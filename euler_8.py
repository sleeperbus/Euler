def readFile(fileName):
	number = ""
	f = open(fileName)
	while 1:
		line = f.readline()
#		print "length: %d" % len(line.strip())
		if not line: break
#		print line 
		number = number + line.strip()
	f.close()
	return number



#print number
#print number[0:5]

def numberSlices(num, unitLen):
	numbers = []
	i = 0
	j = unitLen 
	numLen = len(num) 

	while numLen >= j:
		sliceNum = num[i:j]
		numbers.append(sliceNum)
		i = i + 1
		j = j + 1

	return numbers





number = readFile("number.txt")
numbers = numberSlices(number, 5)
#numbers = numberSlices("12345678", 3)
max = 0
maxNum1 = 0
maxNum2 = 0
for num1 in numbers:
	for num2 in numbers:
#		print "num1: %d, num2: %d" % (int(num1), int(num2))
		num1 = int(num1)
		num2 = int(num2)
		if num1 == num2:
			continue
				
		numProduct = num1 * num2
		if numProduct > max:
			max = numProduct
			maxNum1 = num1
			maxNum2 = num2
print "num1: %d, num2: %d, max: %d" % (maxNum1, maxNum2, max)


#print numberSlices("123456789", 3)
