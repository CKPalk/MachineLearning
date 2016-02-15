
import sys
import csv_data
import csv_utilities
from math import exp, sqrt


'''
		Logical Regression - Machine Learning
'''

max_iterations = 500
convergence_magnitude = 0.00001

#

def sigmaToLambda( sigma ):
	return 1 / ( 2 * ( sigma ** 2 ) )

def magnitude( vector ):
	return sqrt( sum( [ dim ** 2 for dim in vector ] ) )

def currentPrediction( X, W, bias ):
	return sum( [ X[i] * W[i] for i in range( len( W ) ) ] ) + bias

def biasGradient( Data, W, bias ):
	return -1 * sum( [ row.Y * exp( -1 * row.Y * currentPrediction( row.X, W, bias ) ) for row in Data.rows ] )

def weightGradientNorm( index, Data, W, bias, sigma ):
	for row in Data.rows:
		print( currentPrediction( row.X, W, bias ) )
	return -1 * sum( [ row.Y * row.X[ index ] * exp( -1 * row.Y * currentPrediction( row.X, W, bias ) ) for row in Data.rows ] ) + sigmaToLambda( sigma ) * W[ index ]

#

def findOptimalWeights( Data, max_iterations, eta, sigma ):

	W =  [ 0 ] * Data.attributeCount
	bias = 0 # This is W[0] in notes

	for generation in range( max_iterations ): 
		print( "\n--- generation:", generation + 1, "---" )

		dW = [ eta * weightGradientNorm( index, Data, W, bias, sigma ) for index in range( len( W ) ) ]
		print( [ round( dw, 1 ) for dw in dW ], '\n' )
		
		if magnitude( dW ) < convergence_magnitude: # Check for convergence
			print( "it converged" )
			break
		else:
			print( "Magnitude:", magnitude( dW ) )

		dB = eta * biasGradient( Data, W, bias )

		W = [ W[ i ] - dW[ i ] for i in range( len( W ) ) ]
		bias = bias - dB

		print( [ round( w, 3 ) for w in W ], round( bias, 1 ) )
		print( sum( [ round( w, 3 ) for w in W ] ), round( bias, 1 ) )

#

def main( argv ):

	try:
		Train_Data = csv_data.Data( argv[ 0 ], csv_utilities.readIntegerCSV, csv_utilities.convertToPosNegOne )
		Test_Data  = csv_data.Data( argv[ 1 ], csv_utilities.readIntegerCSV, csv_utilities.convertToPosNegOne )
		eta = 	float( argv[ 2 ] )
		sigma = float( argv[ 3 ] )
	except IndexError:
		print( "ERROR: \"python3 logisitic.py <train> <test> <eta> <sigma> <model>\"" ); return
	except:
		raise


	Weights = findOptimalWeights( Train_Data, max_iterations, eta, sigma )

#

if __name__=='__main__':
	main( sys.argv[ 1: ] )


'''
def logisticRegressionPrediction( y, X, W, bias ):
	if y is 1:
		return 1 / ( 1 + exp( linearClassifier( X, bias, W ) ) )
	else:
		return exp( linearClassifier( X, bias, W ) ) / ( 1 + exp( linearClassifier( X, bias, W ) ) )

def gradientForWeight( index, Data, W, bias ):
	return sum( [ row.X[ index ] * ( row.Y - logisticRegressionPrediction( row.Y, row.X, W, bias ) ) for row in Data.rows ] )

def gradientForBias( Data, W, bias ):
	return sum( [ row.Y - logisticRegressionPrediction( row.Y, row.X, W, bias ) for row in Data.rows ] )

def linearClassifier( X, bias, W ):
	return bias + sum( [ W[i] * X[i] for i in range( len( W ) ) ] )
'''
