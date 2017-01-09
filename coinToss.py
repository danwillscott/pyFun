print "this is a coin toss program"
import random

def coinToss():
	heads = 0
	tails = 0
	headMSG = "It's a head!"
	tailMSG = "It's a tail!"
	message = "Attempt #{}: throwing a coin... {} ... Got {} head(s) so far and {} tail(s) so far"
	for x in xrange(1,5001):
		randomNum = random.random()
		randomNum = int(round(randomNum))
		if randomNum == 0:
			heads += 1
			print message.format(x, headMSG, heads, tails)
		else:
			tails += 1
			print message.format(x, tailMSG, heads, tails)

coinToss()