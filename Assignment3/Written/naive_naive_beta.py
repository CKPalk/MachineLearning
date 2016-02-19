


def main():
	maximum = 100
	for w in range( maximum ):
		for x in range( maximum ):
			for y in range( maximum ):
				for z in range( maximum ):
					positive_Y = ( (y+z+1)/(w+x+y+z+1) ) * ( (z+1)/(y+z+1) )
					negative_Y = ( (w+x+1)/(w+x+y+z+1) ) * ( (x+1)/(w+x+1) )
					if positive_Y > negative_Y and abs( positive_Y - negative_Y ) > 0.00001:
						positive_Y2 = ( (y+z+2)/(w+x+y+z+2) ) * ( (z+2)/(y+z+2) )
						negative_Y2 = ( (w+x+2)/(w+x+y+z+2) ) * ( (x+2)/(w+x+2) )
						if positive_Y2 < negative_Y2 and abs( positive_Y2 - negative_Y2 ) > 0.00001:
							print( w,x,y,z )
							return
						
						
if __name__=='__main__':
	main()
