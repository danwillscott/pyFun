print "this multiplies each number in an array by a second value"

def multiply(arr, num):
	i = 0
	arr_len = len(arr)
	while(arr_len > i):
		arr[i] = arr[i] * 5
		i += 1
	print arr




somearr = [2, 4, 10, 16]


multiply(somearr, 5)