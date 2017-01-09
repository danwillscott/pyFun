
def draw_stars(arr):
	for x in arr:
		print "*" * x

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

def draw_stars_expanded(arr):
	for x in arr:
		typeOf = type(x)
		if typeOf == int:
			print "*" * x
		elif typeOf == str:
			print x[0].lower() * len(x)
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars_expanded(y)