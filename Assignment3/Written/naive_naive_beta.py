def main():
	maximum = 20
	for w in range( maximum ):
		for x in range( maximum ):
			for y in range( maximum ):
				for z in range( maximum ):
					#print ( w, x, y, z )
					positive_Y = float( float(y+z+1)/float(w+x+y+z+2)  * ( float(z+1)/float(y+z+2) ) )
					negative_Y = float( float(w+x+1)/float(w+x+y+z+2)  * ( float(x+1)/float(w+x+2) ) ) 
					#print ( positive_Y )
					#print ( negative_Y )
					#print ()
					if positive_Y > negative_Y and abs( positive_Y - negative_Y ) > 0.00001:

						positive_Y2 = float( float(y+z+2)/float(w+x+y+z+4) ) * ( float(z+2)/float(y+z+4) )
						negative_Y2 = float( float(w+x+2)/float(w+x+y+z+4) ) * ( float(x+2)/float(w+x+4) )
						if positive_Y2 < negative_Y2 and abs( positive_Y2 - negative_Y2 ) > 0.00001:
							print( w,x,y,z )
							return
						
						
if __name__=='__main__':
	main()