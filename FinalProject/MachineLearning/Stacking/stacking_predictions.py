''' Work of Cameron Palk '''

import sys
import pandas as pd
import numpy as np

from datetime import datetime


def getY( filename ):
	train_df = pd.read_csv( filename )
	return train_df.ix[:,-1]

def main( argv ):

	try:

		input_csv_filename 	  = argv[ 1 ]
		output_csv_filename   = argv[ 2 ]

	except IndexError:
		print( "Error, usage: \"python3 {} <CSV> <output_CSV>\"".format( argv[ 0 ] ) ) 
		return


	''' Cross validation parameters '''
	split_count = 3
	
	import crossValidationGenerator as cvg

	cvg.splitData( input_csv_filename, split_count )

	Y_results 		= getY( input_csv_filename )
	RF_predictions  = []
	P_predictions   = []
	KNN_predictions = []

	for set_idx in range( split_count ):

		print( "\n{} Starting split {}:".format( str( datetime.now() ), set_idx + 1 ) )

		train_filename = "train_split_{}.csv".format( set_idx )
		test_filename  =  "test_split_{}.csv".format( set_idx )


		# Read training data
		train_df = pd.read_csv( train_filename )
		
		X = train_df.ix[:,0:-1]
		Y = train_df.ix[:,-1]


		# Read training data
		test_df = pd.read_csv( test_filename )
		
		test_X = test_df.ix[:,0:-1]
		test_Y = test_df.ix[:,-1]



		''' Random Forest '''
		from sklearn.ensemble import RandomForestClassifier
	
		# Hyper Parameters
		n_estimators = 60


		RF_classifier = RandomForestClassifier (
			n_estimators = n_estimators
		)

		print( "{} | Training Random Forest".format( str( datetime.now() ) ) )
		RF_classifier.fit( X, Y )

		RF_pred = RF_classifier.predict( test_X )
		RF_predictions.extend( RF_pred )

		print( "{} > Random forest completed for split {} with accuracy {}%\n".format( str( datetime.now() ), set_idx + 1, 100 * RF_classifier.score( test_X, test_Y ) ) )



		''' Perceptron '''
		from sklearn.linear_model import Perceptron

		# Hyper Parameters
		alpha  = 0.0001
		n_iter = 20

		
		P_classifier = Perceptron (
			alpha = alpha,
			n_iter = n_iter
		)

		print( "{} | Training Perceptron".format( str( datetime.now() ) ) )
		P_classifier.fit( X, Y )

		P_pred = P_classifier.predict( test_X )
		P_predictions.extend( P_pred )

		print( "{} > Perceptron completed for split {} with accuracy {}%\n".format( str( datetime.now() ), set_idx + 1, 100 * P_classifier.score( test_X, test_Y ) ) )



		''' K-NN '''
		from sklearn.neighbors import KNeighborsClassifier

		# Hyper Parameters
		n_neighbors = 20

		KNN_classifier = KNeighborsClassifier (
			n_neighbors = n_neighbors
		)

		print( "{} | Training KNN".format( str( datetime.now() ) ) )
		KNN_classifier.fit( X, Y )

		KNN_pred = KNN_classifier.predict( test_X )
		KNN_predictions.extend( KNN_pred )

		print( "{} > K-NN completed for split {} with accuracy {}%\n".format( str( datetime.now() ), set_idx + 1, 100 * KNN_classifier.score( test_X, test_Y ) ) )


	#


	with open( output_csv_filename, 'w+' ) as output_stream:
		output_stream.write( "Random_Forest,Perceptron,KNN,Label\n" )
	
	Y = [ y for y in Y ]

	'''
	print( "len Y   = {}", len( Y_results ) )
	print( "len RF  = {}", len( RF_predictions  ) )
	print( "len P   = {}", len( P_predictions   ) )
	print( "len KNN = {}", len( KNN_predictions ) )
	'''

	for idx in range( len( RF_predictions ) ):
		with open( output_csv_filename, 'a' ) as output_stream:
			output_stream.write( ','.join( [ RF_predictions[ idx ], P_predictions[ idx ], KNN_predictions[ idx ], Y_results[ idx ] ] ) )
			output_stream.write( '\n' )

	print( "\n\nComplete at {}\n\n".format( str( datetime.now() ) ) )





if __name__=='__main__':
	main( sys.argv )
