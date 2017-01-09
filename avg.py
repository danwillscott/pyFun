print "This will give you the average of a list!"

def avgOfList(a_list):
	list_len = len(a_list)
	list_sum = 0
	for num in a_list:
		list_sum = list_sum + num
	list_avg = list_sum / list_len
	print list_avg

a = [1, 2, 5, 10, 255, 3]

avgOfList(a)