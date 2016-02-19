


def probY( S, y, beta ):
	return float( float( len( subsetWithY( S, y ) ) + beta ) / float( len( S ) + beta ) )

def probX( S, x, beta ):
	return float( float( len( subsetWithX( S, x ) ) + beta ) / float( len( S ) + beta ) )

def subsetWithY( S, y ):
	return [ s for s in S if s[-1] == y ]

def subsetWithX( S, x ):
	return [ s for s in S if s[0] == x ]

def calcForPosOne( S, x, beta ):
	print( probY( S, 1, beta ), probX( subsetWithY( S, 1 ), x, beta ) )
	return float( probY( S, 1, beta ) * probX( subsetWithY( S, 1 ), x, beta ) )

def calcForNegOne( S, x, beta ):
	print( probY( S, 0, beta ), probX( subsetWithY( S, 0 ), x, beta ) )
	return float( probY( S, 0, beta ) * probX( subsetWithY( S, 0 ), x, beta ) )

def testDataWithBeta( S, beta ):
	return ( +1 if calcForPosOne( S, 1, beta ) > calcForNegOne( S, 1, beta ) and abs( calcForPosOne( S, 1, beta ) - calcForNegOne( S, 1, beta ) ) > 0.00001 else -1 )


scope = 3

for w in range( scope ):
	for x in range( scope ):
		for y in range( scope ):
			for z in range( scope ):
				data = []
				data += [ [0,0] for _ in range( w ) ]
				data += [ [1,0] for _ in range( x ) ]
				data += [ [0,1] for _ in range( y ) ]
				data += [ [1,1] for _ in range( z ) ]
				ans1 = testDataWithBeta( data, 1 )
				ans2 = testDataWithBeta( data, 2 )
				if ans1 == 1 and ans2 == -1:
					print( "gotcha" )
					print( w, x, y, z )
					print( calcForPosOne( data, 1, 1 ) )
					print( calcForNegOne( data, 1, 1 ) )
					print( calcForPosOne( data, 1, 2 ) )
					print( calcForNegOne( data, 1, 2 ) )
					print()
					print()

					
				#print( "Beta<2,2> = {}".format(   ans1 ) )
				#print( "Beta<3,3> = {}\n".format( ans2 ) )

