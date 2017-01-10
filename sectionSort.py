somelist = [1,7,4,2,8,9,2,4,6]


def seclectionSort(li):
	for i in range (0, len(li)-1):
		minIndex = i
		for x in xrange(i+1, len(li)):
			if li[x] < li[minIndex]:
				minIndex = x
		if minIndex != i:
			li[i], li[minIndex] = li[minIndex], li[i]
	return li

print(seclectionSort(somelist))
