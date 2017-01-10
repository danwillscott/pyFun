def insertionSort(li):
	for i in range(1, len(li)):
		curNum = li[i]
		pos = i
		while pos > 0 and li[pos-1] > curNum:
			li[pos] = li[pos-1]
			pos = pos-1
		li[pos]=curNum
	print li
			



aList = [5,2,7,9,2,1,5,7,9,0,4,1]
insertionSort(aList)


# def insSort2(li):
# 	for x in xrange(0, len(li)):
# 		currentNum = li[x]
