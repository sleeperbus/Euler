i = 1
j = 2
j_bak = 0
total = 2
while j < 4000000:
	j_bak = j
	j = i + j
	i = j_bak
	print "J: %d\n" % (j)
	if j % 2 == 0 and j < 4000000:
		total = total + j

print total
