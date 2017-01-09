print "Looping over odd numbers from 1 to 1000"

def print_rang_1_1000():
	for x in xrange(1,1001):
		if x % 2 <> 0:
			print x

print_rang_1_1000()

print "Now lets loop over multibles of 5 to 1,000,000"
def multibles_5():
	y = 5
	i = 1000001
	while y < i:
		 print y
		 y += 5
		
multibles_5()