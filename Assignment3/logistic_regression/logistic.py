
import sys
import csv_data
import csv_utilities
from math import exp, sqrt


'''
		Logical Regression - Machine Learning
'''

max_iterations = 500
convergence_magnitude = 0.00001



def magnitude( vector ):
	return sqrt( sum( [ dim ** 2 for dim in vector ] ) )
#

def dotProduct( vector_one, vector_two ):
	return sum( map( lambda tup: tup[0] * tup[1], zip( vector_one, vector_two ) ) )
#

def updateWeights( W, dW ):
	return [ W[i] + dW[i] for i in range( len( W ) ) ]
#

def getPrediction( X, W ):
	return dotProduct( X, W[1:] ) + W[0]
#

def probabilityOf( y, X, W ):
	if y == +1: return 1 / ( 1 + exp( getPrediction( X, W ) ) )
	if y == -1: return 1 - probabilityOf( +1, X, W )
	else: print( "Found something else in probabilityOf" )
#

def gradientOfWeight( Data, W, i ):
	if i == 0: return sum( [ 					   1 * ( Data.rows[row].Y - probabilityOf( 1, Data.rows[row].X, W ) ) for row in range( len( Data.rows ) ) ] )
	if i >= 1: return sum( [ Data.rows[row].X[i - 1] * ( Data.rows[row].Y - probabilityOf( 1, Data.rows[row].X, W ) ) for row in range( len( Data.rows ) ) ] )
#

def gradientOfWeights( Data, W ):
	return [ gradientOfWeight( Data, W, i ) for i in range( len( W ) ) ]


#
#
#


def findOptimalWeights( Data, max_iterations, eta, sigma ):

	W =  [ 0 ] * ( Data.attributeCount + 1 )

	for generation in range( max_iterations ):
		dW = gradientOfWeights( Data, W )

		print( dW )

		W = updateWeights( W, dW )

		print( [ round( w, 1 ) for w in W ] )
		print( "#W =", sum( W ) )

#

def main( argv ):

	try:
		Train_Data 	= csv_data.Data( argv[ 0 ], csv_utilities.readIntegerCSV, csv_utilities.convertToPosNegOne )
		#Test_Data  	= csv_data.Data( argv[ 1 ], csv_utilities.readIntegerCSV, csv_utilities.convertToPosNegOne )
		eta 		= float( argv[ 2 ] )
		sigma 		= float( argv[ 3 ] )
	except IndexError:
		print( "ERROR: \"python3 logisitic.py <train> <test> <eta> <sigma> <model>\"" ); return
	except:
		raise


	Weights = findOptimalWeights( Train_Data, max_iterations, eta, sigma )
	print( exp( 1000 ) )

#

if __name__=='__main__':
	main( sys.argv[ 1: ] )

