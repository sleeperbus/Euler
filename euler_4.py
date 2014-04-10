import math
def isParindrome(num):
#	print "number: %d" % (num)
	front = num

	i = int(math.log10(num))
	reverse_front = 0
	while i > 0:
		remain = front % 10
#		print "remain: %d" % remain

		front = (front - remain) / 10
#		print "new front: %d" % front

		reverse_front = reverse_front + remain * pow(10, i)
#		print "reverse_front: %d" % reverse_front

		i = i - 1
		if i == 0:
			reverse_front = reverse_front + front

#	print "final reverse: %d" % reverse_front
	if reverse_front == num:
#		print "True"
		return True
	else :
#		print "False"
		return False



def twoNumbers(n):
	i = pow(10,n) - 1
	j = i
	min_num = pow(10, (n-1)*2)
	parindrome_list = []

	while i >= pow(10, n-1):
		while j >= pow(10, n-1):
#			print "(%d, %d)" % (i, j)
			if i * j > min_num:
				if isParindrome(i * j):
#					print "(%d, %d) = %d" %(i, j, i*j)
					parindrome_list.append(i*j)
				j = j - 1
		i = i - 1
		if i != pow(10, n-1):
			j = pow(10,n) - 1
#		print "new i: %d", i


	return parindrome_list


#print isParindrome(3, 100001)
l = twoNumbers(4)
l.sort()
print l.pop()
