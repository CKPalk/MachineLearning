


rows = [ [-2,-1],[-1,-1],[0.5,-1],[1,1],[2,1]]

while True:
	w = input("w: ")
	b = input("b: ")
	C = input("C: ")

	print( (( 0.5 * (w ** 2) ) + (C *
		sum( [ max( 0, 1 - ( row[-1] * ( w * row[0] + b ) ) ) for row in rows ] ) ) ) )
