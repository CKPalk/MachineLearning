''' Work of Cameron Palk and Joel Benner '''

import sys
import time
from math import exp
from math import sqrt
from csv_data import Data
from csv_utilities import readIntegerCSV
from csv_utilities import convertToZeroOne

def magnitude( arr ):
	return sqrt( sum( map( lambda x: x**2, arr ) ) )
#
def dotProduct( arr1, arr2 ):
	return sum( [ arr1[idx] * arr2[idx] for idx in range( len( arr1 ) ) ] )
#

def unit( X, W, b ):
	linear_prediction = ( dotProduct( W, X ) + b )
	return ( exp( linear_prediction ) / ( 1 + exp( linear_prediction ) ) )
#

def trainWithGradientAscent( data, eta, lamda, start_time ):
	W = [ 0.1 ] * data.attributeCount
	b =   0.1
	counter = 0
	print( "{:^10}".format( "Run Time" ), "  {:^8}   {:^19}".format( "#Updates", "Gradient Magnitude" ) )
	while True: # Until the termination condition is met, Do
		del_w = [ 0 for _ in W ] # Initialize each del_w[i] to zero.
		del_b = 0
		for row in data.rows: # For each <X,t> in training_examples, Do
			X = row.X
			t = row.Y
			o = unit( X, W, b ) # Input instance X to unit and compute output o
			for i in range( len( del_w ) ): # For each linear unit weight w[i], Do
				del_w[i] = del_w[i] + ( eta * ( t - o ) * X[i] ) # del_w[i] = del_w[i] + eta*( t - o )*X[i]
			del_b = del_b + ( eta * ( t - o ) * 1 )
		for i in range( len( W ) ): # For each linear unit weight w[i], Do
			W[i] = W[i] + del_w[i] - ( eta * lamda * W[i] )# w[i] = w[i] + del_w[i]
		b = b + del_b - ( eta * lamda * 1 )
		if magnitude( del_w ) < 0.001:
			return W, b
		elif counter % 10 == 0:
			print( "{:^10}".format( str(round( time.time() - start_time, 3 )) + "s" ), "  {:^8}   {:^19}".format( counter, round( magnitude( del_w ), 6 ) ) )
		counter += 1
#
def main( argv ):
	try:
		training_data = Data( argv[ 0 ], readIntegerCSV, convertToZeroOne )
		testing_data  = Data( argv[ 1 ], readIntegerCSV, convertToZeroOne )
		eta   = float( argv[ 2 ] )
		sigma = float( argv[ 3 ] )
		model = argv[ 4 ] # Save model into this file
	except IndexError:
		print( "Error, usage: \"python3 /Users/ckpalk/Documents/UO/now_2016_winter/CIS472/MachineLearning/Assignment3/Logistic_Regression/logistic.py <training_data> <testing_data > <eta> <sigma> <model>\"" )
		return

	lamda = 1 / ( sigma ** 2 )

	start_time = time.time()
	W, b = trainWithGradientAscent( training_data, eta, lamda, start_time )

	correctly_classified = 0
	incorrectly_classified = 0
	for row in testing_data.rows:
		if ( b + dotProduct( W, row.X ) ) > 0:
			if row.Y == 1:
				correctly_classified += 1
			else:
				incorrectly_classified += 1
		else:
			if row.Y == 0:
				correctly_classified += 1
			else:
				incorrectly_classified += 1
	
	print( "\nRuntime:", time.time() - start_time )
	print( "Incorrectly Classified:", incorrectly_classified )
	print( "Correctly   Classified:", correctly_classified   )
	print( "Accuracy:", str((correctly_classified / len( testing_data.rows ))*100) + "%" )

	with open( model, 'w+' ) as model_stream:
		model_stream.write( "{}\n".format( b ) )
		for i, w in enumerate( W ):
			model_stream.write( "{:16}\t{}\n".format( training_data.attributes[ i ], w ) )
	
	print( "\nModel Output:", argv[ 4 ], "\n" )


	return
#
if __name__=='__main__':
	main( sys.argv[ 1: ] )
