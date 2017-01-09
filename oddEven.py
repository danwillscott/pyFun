print "returns odd and even numbers with odd or even tag"

def oddEven(startNum, endNum):
	message = "Number is {}. This is an {} number"
	for x in xrange(startNum, endNum+1):
		if x % 2 == 0:
			print  message.format(x, "even")
		else:
			print message.format(x, "odd")


oddEven(1, 2000)